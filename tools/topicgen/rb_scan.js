/* 相機解方塊：開相機（或上傳照片、手動輸入）→ 校正顏色 → 拍六面 → 辨識顏色 → 檢查 → 兩階段演算法求解 → 3D 動畫與逐步示意圖。
 * 依賴 RBCore、RBUI、RBSolver（以及 window.__rbSolverSrc：在 Web Worker 中建表、求解）。
 * 元素：<div class="rb-scan"></div>
 */
(function () {
  "use strict";
  var RC = window.RBCore, UI = window.RBUI, el = UI.el, btn = UI.btn;
  // 掃描順序與拿法（配色：U 黃、R 橘、F 綠、D 白、L 紅、B 藍）
  var ORDER = [
    { f: 0, name: "上（黃）", tip: "黃色中心朝向鏡頭，藍色中心朝上" },
    { f: 1, name: "右（橘）", tip: "橘色中心朝向鏡頭，黃色中心朝上" },
    { f: 2, name: "前（綠）", tip: "綠色中心朝向鏡頭，黃色中心朝上" },
    { f: 3, name: "下（白）", tip: "白色中心朝向鏡頭，綠色中心朝上" },
    { f: 4, name: "左（紅）", tip: "紅色中心朝向鏡頭，黃色中心朝上" },
    { f: 5, name: "後（藍）", tip: "藍色中心朝向鏡頭，黃色中心朝上" },
  ];
  var UNKNOWN = -1;

  // ---- 色彩：sRGB → Lab ----
  function lab(rgb) {
    var c = rgb.map(function (v) { v /= 255; return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); });
    var X = (c[0] * 0.4124 + c[1] * 0.3576 + c[2] * 0.1805) / 0.95047, Y = c[0] * 0.2126 + c[1] * 0.7152 + c[2] * 0.0722, Z = (c[0] * 0.0193 + c[1] * 0.1192 + c[2] * 0.9505) / 1.08883;
    function g(t) { return t > 0.008856 ? Math.cbrt(t) : 7.787 * t + 16 / 116; }
    var fx = g(X), fy = g(Y), fz = g(Z);
    var sum = rgb[0] + rgb[1] + rgb[2] + 1;
    // 後兩項是色度（R、G 佔總和的比例），不受明暗影響，用來分辨陰影下的紅與橘
    return [116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz), rgb[0] / sum, rgb[1] / sum];
  }
  function dist(a, b) {
    var dl = (a[0] - b[0]) * 0.35, lab2 = dl * dl + (a[1] - b[1]) * (a[1] - b[1]) + (a[2] - b[2]) * (a[2] - b[2]);
    var cr = (a[3] - b[3]) * 160, cg = (a[4] - b[4]) * 160;
    return Math.sqrt(lab2 + cr * cr + cg * cg);
  }

  // ---- 匈牙利演算法：n×n 成本矩陣的最小指派 ----
  function hungarian(cost) {
    var n = cost.length, INF = 1e18, u = new Array(n + 1).fill(0), v = new Array(n + 1).fill(0), p = new Array(n + 1).fill(0), way = new Array(n + 1).fill(0);
    for (var i = 1; i <= n; i++) {
      p[0] = i; var j0 = 0, minv = new Array(n + 1).fill(INF), used = new Array(n + 1).fill(false);
      do {
        used[j0] = true; var i0 = p[j0], delta = INF, j1 = 0;
        for (var j = 1; j <= n; j++) if (!used[j]) {
          var cur = cost[i0 - 1][j - 1] - u[i0] - v[j];
          if (cur < minv[j]) { minv[j] = cur; way[j] = j0; }
          if (minv[j] < delta) { delta = minv[j]; j1 = j; }
        }
        for (var jj = 0; jj <= n; jj++) { if (used[jj]) { u[p[jj]] += delta; v[jj] -= delta; } else minv[jj] -= delta; }
        j0 = j1;
      } while (p[j0] !== 0);
      do { var jn = way[j0]; p[j0] = p[jn]; j0 = jn; } while (j0);
    }
    var ans = new Array(n); for (var k = 1; k <= n; k++) ans[p[k] - 1] = k - 1; return ans;
  }
  // 54 格依顏色樣本分成 6 色、每色 9 格；中心固定
  function classify(samples, refs) {
    var L = samples.map(function (s) { return s ? lab(s) : null; }), R = refs.map(lab), cost = [];
    for (var i = 0; i < 54; i++) {
      var row = [];
      for (var slot = 0; slot < 54; slot++) {
        var col = Math.floor(slot / 9), c;
        if (i % 9 === 4) c = (col === Math.floor(i / 9)) ? 0 : 1e9;
        else c = L[i] ? dist(L[i], R[col]) : 0;
        row.push(c);
      }
      cost.push(row);
    }
    var a = hungarian(cost);
    return a.map(function (slot) { return Math.floor(slot / 9); });
  }
  function nearest(sample, refs) { var L = lab(sample), best = 0, bd = 1e9; refs.forEach(function (r, k) { var d = dist(L, lab(r)); if (d < bd) { bd = d; best = k; } }); return best; }

  // 在 canvas 影像上取 3×3 格的中位數顏色；box = {cx, cy, size}（以像素計）
  function sampleGrid(ctx, box) {
    var out = [], cell = box.size / 3;
    for (var r = 0; r < 3; r++) for (var c = 0; c < 3; c++) {
      var x0 = Math.round(box.cx - box.size / 2 + (c + 0.28) * cell), y0 = Math.round(box.cy - box.size / 2 + (r + 0.28) * cell), w = Math.max(2, Math.round(cell * 0.44));
      var d = ctx.getImageData(x0, y0, w, w).data, R = [], G = [], B = [];
      for (var i = 0; i < d.length; i += 4 * 3) { R.push(d[i]); G.push(d[i + 1]); B.push(d[i + 2]); }
      out.push([med(R), med(G), med(B)]);
    }
    return out;
  }
  function med(a) { a.sort(function (x, y) { return x - y; }); return a[Math.floor(a.length / 2)]; }
  function rgbCss(c) { return "rgb(" + c.map(Math.round).join(",") + ")"; }

  // ---- 求解器：優先用 Web Worker ----
  var worker = null, workerReady = false, pending = null;
  function startWorker() {
    if (worker || !window.__rbSolverSrc) return;
    try {
      worker = new Worker(URL.createObjectURL(new Blob([window.__rbSolverSrc], { type: "text/javascript" })));
      worker.onmessage = function (e) { if (e.data.ready) { workerReady = true; return; } if (pending) { var p = pending; pending = null; p(e.data); } };
      worker.onerror = function () { worker = null; if (pending) { var p = pending; pending = null; solveAsync(lastFacelets, p); } };
      worker.postMessage({ init: true });
    } catch (err) { worker = null; }
  }
  var lastFacelets = null;
  function solveAsync(facelets, cb) {
    lastFacelets = facelets;
    if (worker) { pending = cb; worker.postMessage({ facelets: facelets, timeLimit: 1800 }); return; }
    setTimeout(function () {
      try { var t0 = Date.now(), m = window.RBSolver.solve(facelets, { timeLimit: 1500 }); cb({ ok: true, moves: m, ms: Date.now() - t0 }); }
      catch (err) { cb({ ok: false, error: String(err.message || err) }); }
    }, 30);
  }

  function mount(root) {
    startWorker();
    var faces = [null, null, null, null, null, null];   // 每面 9 個樣本 RGB
    var colors = new Array(54).fill(UNKNOWN);            // 最後的顏色（0–5）
    var calib = [null, null, null, null, null, null];    // 校正樣本
    var current = 0, stream = null, video = null, live = null, src = "none", img = null, boxScale = 0.62, offset = [0, 0], paint = 0;
    for (var f = 0; f < 6; f++) colors[f * 9 + 4] = f;

    var sec = function (title) { var d = el("div", "border:1px solid var(--border);border-radius:12px;padding:12px 14px;margin:12px 0;background:var(--surface)"); d.appendChild(el("div", "font-weight:700;margin-bottom:8px", title)); root.appendChild(d); return d; };

    // ① 來源
    var s1 = sec("① 選擇輸入方式");
    var bCam = btn("📷 開啟相機"), bUp = btn("🖼 上傳照片"), bMan = btn("✍️ 手動輸入（不用相機）");
    var file = el("input"); file.type = "file"; file.accept = "image/*"; file.style.display = "none";
    s1.appendChild(bCam); s1.appendChild(bUp); s1.appendChild(bMan); s1.appendChild(file);
    var srcInfo = el("div", "font-size:0.88em;color:var(--text-muted);margin-top:6px", "相機需要在 https 網頁上、並允許瀏覽器使用相機；不行的話可以拍照後上傳，或直接手動輸入顏色。");
    s1.appendChild(srcInfo);

    // ② 取景與拍攝
    var s2 = sec("② 對準方塊，逐面拍攝");
    var stageWrap = el("div", "position:relative;max-width:480px;margin:auto;touch-action:none"), view = el("canvas", "width:100%;display:block;border-radius:10px;background:#111");
    stageWrap.appendChild(view); s2.appendChild(stageWrap);
    var tip = el("div", "text-align:center;margin:8px 0;font-size:1.02em"), faceBar = el("div", "display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin:6px 0");
    s2.appendChild(tip); s2.appendChild(faceBar);
    var bShot = btn("📸 拍這一面"), bPrevF = btn("◀ 上一面"), bNextF = btn("下一面 ▶");
    var ctrl = el("div", "text-align:center"); ctrl.appendChild(bPrevF); ctrl.appendChild(bShot); ctrl.appendChild(bNextF); s2.appendChild(ctrl);
    var szL = el("label", "display:block;font-size:0.85em;margin-top:6px;text-align:center", "格線大小 "), sz = el("input"); sz.type = "range"; sz.min = 0.3; sz.max = 0.95; sz.step = 0.01; sz.value = boxScale; sz.style.verticalAlign = "middle"; szL.appendChild(sz); s2.appendChild(szL);
    s2.appendChild(el("div", "font-size:0.85em;color:var(--text-muted);text-align:center", "讓方塊的一面剛好填滿格線（照片可以拖曳格線對位）。光線均勻、避免反光，效果最好。"));

    // ③ 校正顏色
    var s3 = sec("③ 校正顏色（建議）");
    s3.appendChild(el("div", "font-size:0.88em;margin-bottom:6px", "把指定顏色的貼紙對準畫面<b>正中央那一格</b>，按下該顏色。沒校正時，會用六面中心塊的顏色當基準。"));
    var calRow = el("div", "display:flex;flex-wrap:wrap;gap:8px"); s3.appendChild(calRow);
    var calBtns = RC.COLOR_NAMES.map(function (nm, k) {
      var b = btn(""); b.style.minWidth = "84px"; calRow.appendChild(b);
      b.onclick = function () { var s = currentSamples(); if (!s) { msg3.textContent = "請先開啟相機或上傳照片。"; return; } calib[k] = s[4]; drawCal(); reclassify(); };
      return b;
    });
    var msg3 = el("div", "font-size:0.85em;color:var(--text-muted);margin-top:6px"); s3.appendChild(msg3);
    var bClrCal = btn("清除校正"); bClrCal.onclick = function () { calib = [null, null, null, null, null, null]; drawCal(); reclassify(); }; s3.appendChild(bClrCal);
    function refs() { return calib.map(function (c, k) { return c || (faces[k] ? faces[k][4] : hexRgb(RC.COLORS[k])); }); }
    function hexRgb(h) { return [parseInt(h.slice(1, 3), 16), parseInt(h.slice(3, 5), 16), parseInt(h.slice(5, 7), 16)]; }
    function drawCal() {
      var R = refs();
      calBtns.forEach(function (b, k) { b.innerHTML = '<span style="display:inline-block;width:14px;height:14px;border-radius:3px;vertical-align:-2px;border:1px solid #0006;background:' + rgbCss(R[k]) + '"></span> ' + RC.COLOR_NAMES[k] + (calib[k] ? " ✓" : ""); });
    }

    // ④ 檢查與修正
    var s4 = sec("④ 檢查顏色，點格子可以修正");
    var palette = el("div", "display:flex;flex-wrap:wrap;gap:6px;margin-bottom:8px"), netBox = el("div", "max-width:420px;margin:auto"), check = el("div", "margin-top:8px;font-size:0.92em");
    s4.appendChild(palette); s4.appendChild(netBox); s4.appendChild(check);
    RC.COLORS.forEach(function (c, k) {
      var b = btn('<span style="display:inline-block;width:16px;height:16px;border-radius:4px;vertical-align:-3px;background:' + c + ';border:1px solid #0006"></span> ' + RC.COLOR_NAMES[k]);
      b.onclick = function () { paint = k; markPal(); }; b.dataset.k = k; palette.appendChild(b);
    });
    function markPal() { palette.querySelectorAll("button").forEach(function (b) { b.style.outline = +b.dataset.k === paint ? "2px solid var(--accent)" : "none"; }); }
    var bClear = btn("全部清空（手動輸入用）"), bDemo = btn("填入一個隨機打亂（試用）");
    s4.appendChild(bClear); s4.appendChild(bDemo);

    // ⑤ 求解
    var s5 = sec("⑤ 求解");
    var bSolve = btn("🧠 算出最短解"), out = el("div", "margin-top:10px"), steps = el("div", "display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px;margin-top:12px");
    s5.appendChild(bSolve); s5.appendChild(el("div", "font-size:0.85em;color:var(--text-muted);margin-top:4px", "用 Kociemba 兩階段演算法搜尋，通常 1–2 秒內找到 18–21 步的解（最少步數的理論上限是 20 步）。解法以「黃色朝上、綠色朝前」的拿法表示。")); s5.appendChild(out); s5.appendChild(steps);

    // ---- 畫面 ----
    var vctx = view.getContext("2d");
    function frameSize() { if (src === "cam" && video && video.videoWidth) return [video.videoWidth, video.videoHeight]; if (src === "img" && img) return [img.naturalWidth, img.naturalHeight]; return [640, 480]; }
    function box() { var s = frameSize(), m = Math.min(s[0], s[1]) * boxScale; return { cx: s[0] / 2 + offset[0], cy: s[1] / 2 + offset[1], size: m }; }
    function drawFrame() {
      var s = frameSize(); if (view.width !== s[0]) { view.width = s[0]; view.height = s[1]; }
      vctx.fillStyle = "#111"; vctx.fillRect(0, 0, view.width, view.height);
      if (src === "cam" && video && video.videoWidth) vctx.drawImage(video, 0, 0);
      else if (src === "img" && img) vctx.drawImage(img, 0, 0);
      else { vctx.fillStyle = "#888"; vctx.font = Math.round(view.width / 24) + "px sans-serif"; vctx.textAlign = "center"; vctx.fillText("先在 ① 開啟相機或上傳照片", view.width / 2, view.height / 2); return null; }
      var b = box(), samples = sampleGrid(vctx, b), R = refs(), cell = b.size / 3, lw = Math.max(2, view.width / 300);
      for (var k = 0; k < 9; k++) {
        var x = b.cx - b.size / 2 + (k % 3) * cell, y = b.cy - b.size / 2 + Math.floor(k / 3) * cell, guess = nearest(samples[k], R);
        vctx.lineWidth = lw * 2; vctx.strokeStyle = "rgba(0,0,0,0.6)"; vctx.strokeRect(x + cell * 0.08, y + cell * 0.08, cell * 0.84, cell * 0.84);
        vctx.lineWidth = lw; vctx.strokeStyle = RC.COLORS[guess]; vctx.strokeRect(x + cell * 0.08, y + cell * 0.08, cell * 0.84, cell * 0.84);
        vctx.fillStyle = rgbCss(samples[k]); vctx.fillRect(x + cell * 0.4, y + cell * 0.4, cell * 0.2, cell * 0.2);
      }
      vctx.lineWidth = lw * 1.5; vctx.strokeStyle = "#fff"; vctx.strokeRect(b.cx - b.size / 2, b.cy - b.size / 2, b.size, b.size);
      return samples;
    }
    function currentSamples() { return src === "none" ? null : drawFrame(); }
    function tick() { if (src === "cam") { drawFrame(); live = requestAnimationFrame(function () { setTimeout(tick, 120); }); } }
    // 拖曳格線（照片用）
    var drag = null;
    view.addEventListener("pointerdown", function (e) { drag = [e.clientX, e.clientY, offset[0], offset[1]]; view.setPointerCapture(e.pointerId); });
    view.addEventListener("pointermove", function (e) { if (!drag) return; var k = view.width / view.clientWidth; offset = [drag[2] + (e.clientX - drag[0]) * k, drag[3] + (e.clientY - drag[1]) * k]; if (src !== "cam") drawFrame(); });
    view.addEventListener("pointerup", function () { drag = null; });
    sz.oninput = function () { boxScale = +sz.value; if (src !== "cam") drawFrame(); };

    bCam.onclick = function () {
      if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) { srcInfo.textContent = "這個瀏覽器不支援網頁相機，請改用「上傳照片」或手動輸入。"; return; }
      navigator.mediaDevices.getUserMedia({ video: { facingMode: { ideal: "environment" }, width: { ideal: 1280 }, height: { ideal: 960 } }, audio: false }).then(function (st) {
        stream = st; video = el("video"); video.playsInline = true; video.muted = true;
        video.onloadedmetadata = function () { tick(); };
        video.srcObject = st; video.play();
        src = "cam"; offset = [0, 0]; srcInfo.textContent = "相機已開啟。";
      }).catch(function (err) { srcInfo.textContent = "無法開啟相機（" + err.name + "）。請確認已允許使用相機，或改用「上傳照片」。"; });
    };
    bUp.onclick = function () { file.click(); };
    file.onchange = function () {
      if (!file.files[0]) return;
      var r = new FileReader();
      r.onload = function () { var im = new Image(); im.onload = function () { img = im; if (stream) { stream.getTracks().forEach(function (t) { t.stop(); }); stream = null; } src = "img"; offset = [0, 0]; drawFrame(); srcInfo.textContent = "已載入照片：" + ORDER[current].name + "。拖曳格線對位後按「拍這一面」。"; }; im.src = r.result; };
      r.readAsDataURL(file.files[0]); file.value = "";
    };
    bMan.onclick = function () { s4.scrollIntoView({ behavior: "smooth" }); };

    function showFace() {
      tip.innerHTML = "第 " + (current + 1) + " / 6 面：<b>" + ORDER[current].name + "</b>　" + ORDER[current].tip;
      faceBar.innerHTML = "";
      ORDER.forEach(function (o, k) {
        var d = el("div", "cursor:pointer;text-align:center;font-size:0.8em;padding:4px;border-radius:8px;border:2px solid " + (k === current ? "var(--accent)" : "transparent"));
        var g = "";
        for (var i = 0; i < 9; i++) { var c = colors[o.f * 9 + i]; g += '<span style="display:inline-block;width:12px;height:12px;margin:1px;border-radius:2px;background:' + (c < 0 ? "#555" : RC.COLORS[c]) + '"></span>' + (i % 3 === 2 ? "<br>" : ""); }
        d.innerHTML = '<div style="line-height:0">' + g + "</div>" + o.name + (faces[o.f] ? " ✓" : "");
        d.onclick = function () { current = k; showFace(); };
        faceBar.appendChild(d);
      });
    }
    bShot.onclick = function () {
      var s = currentSamples(); if (!s) { tip.innerHTML = "請先在 ① 開啟相機或上傳照片。"; return; }
      faces[ORDER[current].f] = s; reclassify();
      if (current < 5) current++;
      showFace();
      if (src === "img") srcInfo.textContent = "請上傳下一面：" + ORDER[current].name + "。";
    };
    bPrevF.onclick = function () { current = (current + 5) % 6; showFace(); };
    bNextF.onclick = function () { current = (current + 1) % 6; showFace(); };

    function reclassify() {
      drawCal();
      var samples = [];
      for (var f = 0; f < 6; f++) for (var k = 0; k < 9; k++) samples.push(faces[f] ? faces[f][k] : null);
      if (faces.every(function (x) { return x; })) colors = classify(samples, refs());
      else { var R = refs(); for (var f2 = 0; f2 < 6; f2++) if (faces[f2]) for (var k2 = 0; k2 < 9; k2++) colors[f2 * 9 + k2] = k2 === 4 ? f2 : nearest(faces[f2][k2], R); }
      renderNet(); showFace();
    }
    function renderNet() {
      var off = [[3, 0], [6, 3], [3, 3], [3, 6], [0, 3], [9, 3]], s = 30, svg = ['<svg viewBox="0 0 ' + (12 * s + 2) + " " + (9 * s + 2) + '" style="width:100%;display:block;touch-action:manipulation">'];
      for (var f = 0; f < 6; f++) for (var k = 0; k < 9; k++) {
        var i = f * 9 + k, x = 1 + (off[f][0] + k % 3) * s, y = 1 + (off[f][1] + Math.floor(k / 3)) * s, c = colors[i];
        svg.push('<rect data-i="' + i + '" x="' + (x + 1) + '" y="' + (y + 1) + '" width="' + (s - 2) + '" height="' + (s - 2) + '" rx="4" fill="' + (c < 0 ? "#555" : RC.COLORS[c]) + '" stroke="#111" stroke-width="1.2" style="cursor:' + (k === 4 ? "default" : "pointer") + '"/>');
        if (k === 4) svg.push('<text x="' + (x + s / 2) + '" y="' + (y + s / 2 + 4) + '" font-size="10" text-anchor="middle" fill="#0008">' + "URFDLB"[f] + "</text>");
      }
      netBox.innerHTML = svg.join("") + "</svg>";
      netBox.querySelectorAll("rect").forEach(function (r) {
        r.addEventListener("click", function () { var i = +r.getAttribute("data-i"); if (i % 9 === 4) return; colors[i] = paint; renderNet(); });
      });
      validate();
    }
    function validate() {
      var cnt = [0, 0, 0, 0, 0, 0], unk = 0;
      colors.forEach(function (c) { if (c < 0) unk++; else cnt[c]++; });
      var parts = cnt.map(function (n, k) { return '<span style="color:' + (n === 9 ? "inherit" : "#e0605a") + '">' + RC.COLOR_NAMES[k] + " " + n + "</span>"; }).join("　");
      var okMsg = "";
      if (!unk && cnt.every(function (n) { return n === 9; })) {
        try { window.RBSolver.fromFacelets(colors.map(function (c) { return "URFDLB"[c]; }).join("")); okMsg = '<div style="color:#4caf50;margin-top:4px">✓ 這是一個合法、轉得出來的狀態。</div>'; }
        catch (err) { okMsg = '<div style="color:#e0605a;margin-top:4px">✗ ' + err.message + "。請檢查拍攝的方向，或點格子修正。</div>"; }
      } else okMsg = '<div style="color:var(--text-muted);margin-top:4px">' + (unk ? "還有 " + unk + " 格未填。" : "每種顏色都要剛好 9 格。") + "</div>";
      check.innerHTML = "各色數量：" + parts + okMsg;
    }
    bClear.onclick = function () { for (var i = 0; i < 54; i++) colors[i] = i % 9 === 4 ? Math.floor(i / 9) : UNKNOWN; faces = [null, null, null, null, null, null]; renderNet(); showFace(); };
    bDemo.onclick = function () { var st = RC.apply(RC.solved(), RC.scramble(22)); colors = st.map(RC.colorOf); renderNet(); showFace(); };

    bSolve.onclick = function () {
      out.innerHTML = ""; steps.innerHTML = "";
      if (colors.some(function (c) { return c < 0; })) { out.textContent = "還有格子沒有顏色。"; return; }
      var fl = colors.map(function (c) { return "URFDLB"[c]; }).join(""), state = RC.fromColors(colors);
      if (RC.isSolved(state)) { out.textContent = "已經是復原狀態了！"; return; }
      out.textContent = (worker && !workerReady) || (!worker && !window.RBSolver.ready()) ? "第一次求解要先建立查找表（約 1–3 秒）…" : "搜尋中…";
      bSolve.disabled = true;
      solveAsync(fl, function (res) {
        bSolve.disabled = false;
        if (!res.ok) { out.innerHTML = '<span style="color:#e0605a">無法求解：' + res.error + "</span>"; return; }
        var moves = res.moves;
        if (!moves) { out.innerHTML = '<span style="color:#e0605a">這次沒有在時限內找到解，請再按一次。</span>'; return; }
        out.innerHTML = "<div>找到 <b>" + moves.length + " 步</b>的解（" + res.ms + " ms）：</div>";
        var pl = el("div", "margin-top:8px"); out.appendChild(pl);
        UI.mountPlayer(pl, { alg: moves.join(" "), state: state, start: "掃描到的狀態。拿好方塊：黃色朝上、綠色朝前，照著一步一步轉。", done: "方塊復原了！", maxw: 340 });
        // 逐步示意圖：每一步轉之前的狀態，標出要轉的那一層
        var st = state;
        moves.forEach(function (mv, k) {
          var b = RC.BASE[RC.baseOf(mv)], hl = [];
          for (var i = 0; i < 54; i++) if (b[1].indexOf(RC.cubieOf(i)[b[0]]) >= 0) hl.push(i);
          var card = el("div", "border:1px solid var(--border);border-radius:10px;padding:6px;text-align:center;font-size:0.85em");
          card.innerHTML = RC.netSVG(st, { size: 12, highlight: hl }) + '<div style="margin-top:4px"><b>第 ' + (k + 1) + " 步　" + mv + "</b><br>" + UI.describe(mv).split("：")[1] + "</div>";
          steps.appendChild(card); st = RC.applyMove(st, mv);
        });
        var fin = el("div", "border:1px solid var(--border);border-radius:10px;padding:6px;text-align:center;font-size:0.85em");
        fin.innerHTML = RC.netSVG(st, { size: 12 }) + "<div><b>完成</b></div>"; steps.appendChild(fin);
      });
    };

    drawCal(); renderNet(); showFace(); markPal(); drawFrame();
  }
  function boot() { document.querySelectorAll(".rb-scan").forEach(function (r) { if (!r.__done) { r.__done = 1; mount(r); } }); }
  window.RBScan = { classify: classify, lab: lab, hungarian: hungarian, sampleGrid: sampleGrid };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
