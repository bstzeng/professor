/* 魔術方塊介面：canvas 3D 方塊（可拖曳旋轉、動畫轉層）、公式播放器、記號練習、自由轉。
 * 依賴 RBCore（rb_core.js）。頁面上 class="rb-w" 的元素依 data-cfg 自動初始化。
 */
(function () {
  "use strict";
  if (window.RBUI) return;
  var RC = window.RBCore;

  // ---- 遮罩：只顯示這一步相關的塊（依貼紙的「原本位置」判斷）----
  function pieceOf(id) { return RC.cubieOf(id); }
  function nz(c) { return (c[0] ? 1 : 0) + (c[1] ? 1 : 0) + (c[2] ? 1 : 0); }
  var MASKS = {
    all: null,
    cross: function (id) { var c = pieceOf(id); return nz(c) === 1 || (c[1] === -1 && nz(c) === 2); },
    f1: function (id) { var c = pieceOf(id); return nz(c) === 1 || c[1] === -1; },
    f2l: function (id) { var c = pieceOf(id); return nz(c) === 1 || c[1] <= 0; },
    oll: function (id) { var c = pieceOf(id); return nz(c) === 1 || c[1] <= 0 || id < 9; },
    ycross: function (id) { var c = pieceOf(id); return nz(c) === 1 || c[1] <= 0 || (id < 9 && nz(c) === 2); },
    centers: function (id) { return nz(pieceOf(id)) === 1; },
  };

  var FACE_ZH = { U: "上", R: "右", F: "前", D: "下", L: "左", B: "後", M: "中間層（跟 L 同向）", E: "水平中層（跟 D 同向）", S: "前後中層（跟 F 同向）",
    x: "整顆往前翻（跟 R 同向）", y: "整顆水平轉（跟 U 同向）", z: "整顆側轉（跟 F 同向）",
    u: "上兩層", r: "右兩層", f: "前兩層", d: "下兩層", l: "左兩層", b: "後兩層" };
  function describe(mv) {
    var b = RC.baseOf(mv), a = RC.amountOf(mv);
    var who = FACE_ZH[b] || b;
    if ("URFDLBurfdlb".indexOf(b) >= 0) who += (b === b.toUpperCase() ? "面" : "");
    return mv + "：" + who + (a === 2 ? "轉半圈" : a === 3 ? "逆時針轉 90°" : "順時針轉 90°");
  }

  // ---- 3D 繪圖 ----
  function mat3(axis, ang) {
    var c = Math.cos(ang), s = Math.sin(ang);
    if (axis === 0) return [1, 0, 0, 0, c, -s, 0, s, c];
    if (axis === 1) return [c, 0, s, 0, 1, 0, -s, 0, c];
    return [c, -s, 0, s, c, 0, 0, 0, 1];
  }
  function mv3(m, v) { return [m[0] * v[0] + m[1] * v[1] + m[2] * v[2], m[3] * v[0] + m[4] * v[1] + m[5] * v[2], m[6] * v[0] + m[7] * v[1] + m[8] * v[2]]; }
  function mm3(a, b) { var r = []; for (var i = 0; i < 3; i++) for (var j = 0; j < 3; j++) r.push(a[i * 3] * b[j] + a[i * 3 + 1] * b[3 + j] + a[i * 3 + 2] * b[6 + j]); return r; }

  // 每個小方塊（位置）與其 6 個面；外側的面對應到哪個貼紙
  var CUBIES = [];
  (function () {
    var lookup = {};
    for (var i = 0; i < 54; i++) { var c = RC.cubieOf(i), n = RC.NRM[i]; lookup[c.join(",") + "|" + n.join(",")] = i; }
    for (var x = -1; x <= 1; x++) for (var y = -1; y <= 1; y++) for (var z = -1; z <= 1; z++) {
      if (!x && !y && !z) continue;
      var faces = [];
      [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]].forEach(function (n) {
        var k = [x, y, z].join(",") + "|" + n.join(",");
        faces.push({ n: n, sticker: lookup[k] === undefined ? -1 : lookup[k] });
      });
      CUBIES.push({ c: [x, y, z], faces: faces });
    }
  })();
  function quad(center, n, size) {     // 以 center 為中心、法向 n 的正方形四個頂點
    var u = n[0] ? [0, 1, 0] : [1, 0, 0], v = n[2] ? [0, 1, 0] : [0, 0, 1];
    var h = size / 2, pts = [];
    [[-1, -1], [1, -1], [1, 1], [-1, 1]].forEach(function (s) { pts.push([center[0] + (u[0] * s[0] + v[0] * s[1]) * h, center[1] + (u[1] * s[0] + v[1] * s[1]) * h, center[2] + (u[2] * s[0] + v[2] * s[1]) * h]); });
    return pts;
  }

  function Cube3D(canvas, opt) {
    opt = opt || {};
    var self = this, ctx = canvas.getContext("2d");
    this.canvas = canvas; this.state = RC.solved(); this.mask = null; this.anim = null;
    this.yaw = opt.yaw === undefined ? -0.62 : opt.yaw; this.pitch = opt.pitch === undefined ? 0.5 : opt.pitch;
    this.highlight = null;
    function resize() {
      var w = canvas.clientWidth || 300, dpr = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = Math.round(w * dpr); canvas.height = Math.round(w * dpr); self.draw();
    }
    this.resize = resize;
    this.draw = function () {
      var W = canvas.width, H = canvas.height; if (!W) return;
      ctx.clearRect(0, 0, W, H);
      var view = mm3(mat3(0, self.pitch), mat3(1, self.yaw)), dist = 9.5, sc = W * 0.3;
      function proj(p) { var q = mv3(view, p), zz = dist - q[2]; return [W / 2 + q[0] * sc * dist / zz / 2.2 * 1.0, H / 2 - q[1] * sc * dist / zz / 2.2, q[2]]; }
      var a = self.anim, rotM = null;
      if (a) rotM = mat3(a.axis, a.angle);
      var items = CUBIES.map(function (cb) {
        var moving = a && a.layers.indexOf(cb.c[a.axis]) >= 0;
        var M = moving ? rotM : null;
        var center = M ? mv3(M, cb.c) : cb.c;
        return { cb: cb, M: M, depth: mv3(view, center)[2] };
      }).sort(function (p, q) { return p.depth - q.depth; });
      items.forEach(function (it) {
        it.cb.faces.forEach(function (fc) {
          var n = it.M ? mv3(it.M, fc.n) : fc.n, vn = mv3(view, n);
          // 背面剔除（考慮透視：用面中心到相機的方向）
          var ctr = [it.cb.c[0] + fc.n[0] * 0.5, it.cb.c[1] + fc.n[1] * 0.5, it.cb.c[2] + fc.n[2] * 0.5];
          if (it.M) ctr = mv3(it.M, ctr);
          var vc = mv3(view, ctr), toCam = [-vc[0], -vc[1], dist - vc[2]];
          if (vn[0] * toCam[0] + vn[1] * toCam[1] + vn[2] * toCam[2] <= 0) return;
          var body = quad([it.cb.c[0] + fc.n[0] * 0.5, it.cb.c[1] + fc.n[1] * 0.5, it.cb.c[2] + fc.n[2] * 0.5], fc.n, 1.0);
          poly(body.map(function (p) { return proj(it.M ? mv3(it.M, p) : p); }), "#15171c", "#000");
          if (fc.sticker >= 0) {
            var id = self.state[fc.sticker], col = (self.mask && !self.mask(id)) ? "#4b5059" : RC.COLORS[RC.colorOf(id)];
            var st = quad([it.cb.c[0] + fc.n[0] * 0.505, it.cb.c[1] + fc.n[1] * 0.505, it.cb.c[2] + fc.n[2] * 0.505], fc.n, 0.84);
            var hl = self.highlight && self.highlight.indexOf(fc.sticker) >= 0;
            poly(st.map(function (p) { return proj(it.M ? mv3(it.M, p) : p); }), col, hl ? "#ff3df2" : "rgba(0,0,0,0.35)", hl ? 3 : 1);
          }
        });
      });
    };
    function poly(pts, fill, stroke, lw) {
      ctx.beginPath(); pts.forEach(function (p, i) { if (i) ctx.lineTo(p[0], p[1]); else ctx.moveTo(p[0], p[1]); }); ctx.closePath();
      ctx.fillStyle = fill; ctx.fill(); ctx.lineWidth = (lw || 1) * (canvas.width / 300); ctx.strokeStyle = stroke; ctx.stroke();
    }
    // 拖曳旋轉視角
    var drag = null;
    canvas.style.touchAction = "none"; canvas.style.cursor = "grab";
    canvas.addEventListener("pointerdown", function (e) { drag = [e.clientX, e.clientY, self.yaw, self.pitch]; canvas.setPointerCapture(e.pointerId); });
    canvas.addEventListener("pointermove", function (e) {
      if (!drag) return;
      self.yaw = drag[2] + (e.clientX - drag[0]) * 0.012;
      self.pitch = Math.max(-1.4, Math.min(1.4, drag[3] + (e.clientY - drag[1]) * 0.012));
      self.draw();
    });
    canvas.addEventListener("pointerup", function () { drag = null; });
    canvas.addEventListener("dblclick", function () { self.yaw = opt.yaw === undefined ? -0.62 : opt.yaw; self.pitch = opt.pitch === undefined ? 0.5 : opt.pitch; self.draw(); });
    if (window.ResizeObserver) new ResizeObserver(resize).observe(canvas);
    setTimeout(resize, 0);
  }
  // 動畫轉一步；回傳 Promise
  Cube3D.prototype.animateMove = function (mv, ms) {
    var self = this, b = RC.BASE[RC.baseOf(mv)], amt = RC.amountOf(mv);
    var total = b[2] * Math.PI / 2 * (amt === 3 ? -1 : amt), dur = (ms || 350) * (amt === 2 ? 1.5 : 1);
    return new Promise(function (res) {
      var t0 = null;
      function step(ts) {
        if (t0 === null) t0 = ts;
        var u = Math.min(1, (ts - t0) / dur), e = u < 0.5 ? 2 * u * u : 1 - Math.pow(-2 * u + 2, 2) / 2;
        self.anim = { axis: b[0], layers: b[1], angle: total * e };
        self.draw();
        if (u < 1) requestAnimationFrame(step);
        else { self.anim = null; self.state = RC.applyMove(self.state, mv); self.draw(); res(); }
      }
      requestAnimationFrame(step);
    });
  };

  // ---- 共用小元件 ----
  function el(tag, css, html) { var e = document.createElement(tag); if (css) e.style.cssText = css; if (html !== undefined) e.innerHTML = html; return e; }
  function btn(t, title) { var b = el("button", "padding:5px 11px;margin:3px 4px 0 0;border-radius:8px;border:1px solid var(--border);background:var(--surface);color:var(--text);cursor:pointer;font:inherit;font-size:0.92em", t); b.type = "button"; if (title) b.title = title; return b; }
  function head(root, q) { if (q) root.appendChild(el("p", "margin:0 0 8px", q)); }
  function canvasBox(root, maxw) {
    var wrap = el("div", "display:flex;gap:12px;flex-wrap:wrap;align-items:flex-start"), cv = el("canvas", "width:100%;max-width:" + (maxw || 320) + "px;aspect-ratio:1;display:block;border-radius:12px;background:radial-gradient(circle at 50% 40%,rgba(120,140,170,0.18),rgba(0,0,0,0) 70%)");
    var left = el("div", "flex:1 1 260px;max-width:" + (maxw || 320) + "px"), right = el("div", "flex:1 1 220px;min-width:0");
    left.appendChild(cv); wrap.appendChild(left); wrap.appendChild(right); root.appendChild(wrap);
    left.appendChild(el("div", "font-size:0.78em;color:var(--text-muted);text-align:center;margin-top:2px", "拖曳可旋轉視角，雙擊恢復"));
    return { cv: cv, right: right, left: left };
  }

  // ---- 公式播放器 ----
  function mountPlayer(root, cfg) {
    head(root, cfg.q);
    var moves = RC.parse(cfg.alg), setup = cfg.setup !== undefined ? RC.parse(cfg.setup) : RC.invert(moves);
    var box = canvasBox(root, cfg.maxw), cube = new Cube3D(box.cv, cfg.view || {});
    cube.mask = cfg.mask ? MASKS[cfg.mask] : null;
    var start = cfg.state ? cfg.state.slice() : RC.apply(RC.solved(), setup);
    if (cfg.pre) start = RC.apply(start, cfg.pre);
    cube.state = start.slice();
    var algLine = el("div", "display:flex;flex-wrap:wrap;gap:4px;margin-bottom:8px"), chips = [];
    moves.forEach(function (m, i) {
      var c = el("span", "font-family:ui-monospace,Menlo,monospace;font-weight:700;padding:3px 8px;border-radius:7px;border:1px solid var(--border);cursor:pointer;min-width:22px;text-align:center", m);
      c.onclick = function () { jump(i + 1); }; chips.push(c); algLine.appendChild(c);
    });
    var info = el("div", "min-height:2.6em;font-size:0.92em;line-height:1.5;margin-bottom:6px"), bar = el("div"), net = el("div", "max-width:230px;margin-top:8px");
    var bReset = btn("⏮", "回到開始"), bPrev = btn("◀", "上一步"), bPlay = btn("▶ 播放"), bNext = btn("▶|", "下一步");
    bar.appendChild(bReset); bar.appendChild(bPrev); bar.appendChild(bPlay); bar.appendChild(bNext);
    var spdL = el("label", "display:block;font-size:0.85em;margin-top:6px", "速度 "), spd = el("input"); spd.type = "range"; spd.min = 0.4; spd.max = 2.5; spd.step = 0.1; spd.value = 1; spd.style.verticalAlign = "middle"; spdL.appendChild(spd);
    box.right.appendChild(algLine); box.right.appendChild(info); box.right.appendChild(bar); box.right.appendChild(spdL);
    if (cfg.net !== false) box.right.appendChild(net);
    if (cfg.note) box.right.appendChild(el("div", "font-size:0.88em;color:var(--text-muted);margin-top:6px", cfg.note));
    var k = 0, playing = false, busy = false;
    function refresh() {
      chips.forEach(function (c, i) { c.style.background = i < k ? "var(--accent-soft)" : i === k && playing ? "rgba(255,61,242,0.18)" : "transparent"; c.style.opacity = i < k ? 0.75 : 1; });
      info.innerHTML = k === 0 ? (cfg.start || "起始狀態。按「播放」或點公式裡的任一步。") : "第 " + k + " / " + moves.length + " 步　" + describe(moves[k - 1]) +
        (k === moves.length ? "<br><b>" + (cfg.done || "完成！") + "</b>" : "");
      bPlay.textContent = playing ? "⏸ 暫停" : "▶ 播放";
      if (cfg.net !== false) net.innerHTML = RC.netSVG(cube.state, { size: 18, mask: cube.mask });
    }
    function stateAt(n) { return RC.apply(start, moves.slice(0, n)); }
    function jump(n) { if (busy) return; playing = false; k = n; cube.state = stateAt(n); cube.draw(); refresh(); }
    function next() {
      if (busy || k >= moves.length) return Promise.resolve(false);
      busy = true; var mv = moves[k];
      return cube.animateMove(mv, 380 / (+spd.value)).then(function () { k++; busy = false; refresh(); return true; });
    }
    function loop() { if (!playing) return; next().then(function (ok) { if (!ok || k >= moves.length) { playing = false; refresh(); return; } setTimeout(loop, 90 / (+spd.value)); }); }
    bPlay.onclick = function () { if (playing) { playing = false; refresh(); return; } if (k >= moves.length) jump(0); playing = true; refresh(); setTimeout(loop, 150); };
    bNext.onclick = function () { playing = false; next(); };
    bPrev.onclick = function () { if (k > 0) jump(k - 1); };
    bReset.onclick = function () { jump(0); };
    refresh();
  }

  // ---- 記號練習：按按鈕轉 ----
  function mountNotation(root, cfg) {
    head(root, cfg.q);
    var box = canvasBox(root, cfg.maxw), cube = new Cube3D(box.cv, cfg.view || {});
    var groups = cfg.groups || [["U", "U'", "U2", "D", "D'", "D2"], ["R", "R'", "R2", "L", "L'", "L2"], ["F", "F'", "F2", "B", "B'", "B2"]];
    var info = el("div", "min-height:2.6em;font-size:0.92em;margin-bottom:6px", "點按鈕看看每個記號怎麼轉。"), hist = el("div", "font-family:ui-monospace,monospace;font-size:0.9em;word-break:break-all;margin-top:6px;color:var(--text-muted)");
    box.right.appendChild(info);
    var queue = Promise.resolve(), done = [];
    groups.forEach(function (g) {
      var row = el("div");
      g.forEach(function (m) {
        var b = btn(m); b.style.fontFamily = "ui-monospace,monospace"; b.style.minWidth = "44px";
        b.onclick = function () { queue = queue.then(function () { info.textContent = describe(m); done.push(m); hist.textContent = "已轉：" + done.join(" "); return cube.animateMove(m, 330); }); };
        row.appendChild(b);
      });
      box.right.appendChild(row);
    });
    var rst = btn("↺ 復原"); rst.onclick = function () { queue = queue.then(function () { cube.state = RC.solved(); done = []; hist.textContent = ""; info.textContent = "已復原。"; cube.draw(); }); };
    box.right.appendChild(rst); box.right.appendChild(hist);
  }

  // ---- 自由轉＋打亂＋（有求解器時）求解 ----
  function mountFree(root, cfg) {
    head(root, cfg.q);
    var box = canvasBox(root, cfg.maxw), cube = new Cube3D(box.cv, cfg.view || {});
    var info = el("div", "min-height:2.6em;font-size:0.92em;margin-bottom:6px", "可以打亂、自己轉，或讓電腦算出解法並播放。"), sol = el("div", "font-family:ui-monospace,monospace;word-break:break-word;margin-top:6px");
    box.right.appendChild(info);
    var row = el("div"), busy = false;
    "U U' R R' F F' D D' L L' B B'".split(" ").forEach(function (m) {
      var b = btn(m); b.style.fontFamily = "ui-monospace,monospace"; b.style.minWidth = "38px";
      b.onclick = function () { if (busy) return; busy = true; cube.animateMove(m, 260).then(function () { busy = false; }); }; row.appendChild(b);
    });
    box.right.appendChild(row);
    var bS = btn("🔀 打亂"), bSolve = btn("🧠 電腦求解"), bReset = btn("↺ 復原");
    box.right.appendChild(bS); if (window.RBSolver) box.right.appendChild(bSolve); box.right.appendChild(bReset); box.right.appendChild(sol);
    bS.onclick = function () { if (busy) return; var s = RC.scramble(20); cube.state = RC.apply(RC.solved(), s); cube.draw(); info.innerHTML = "打亂：<code>" + s.join(" ") + "</code>"; sol.textContent = ""; };
    bReset.onclick = function () { if (busy) return; cube.state = RC.solved(); cube.draw(); info.textContent = "已復原。"; sol.textContent = ""; };
    bSolve.onclick = function () {
      if (busy) return;
      if (RC.isSolved(cube.state)) { info.textContent = "已經是復原狀態。"; return; }
      busy = true; info.textContent = window.RBSolver.ready() ? "計算中…" : "第一次使用要先建立查找表（約 1–3 秒）…";
      setTimeout(function () {
        var t0 = Date.now(), moves = window.RBSolver.solve(RC.toFacelets(cube.state), { timeLimit: 1200 });
        info.innerHTML = "找到 <b>" + moves.length + " 步</b>的解（" + (Date.now() - t0) + " ms），播放中…";
        sol.textContent = moves.join(" ");
        var i = 0;
        (function go() { if (i >= moves.length) { busy = false; info.innerHTML += " 完成！"; return; } cube.animateMove(moves[i++], 260).then(go); })();
      }, 30);
    };
  }

  // ---- 靜態展開圖：顯示公式作用後的樣子 ----
  function mountNet(root, cfg) {
    head(root, cfg.q);
    var wrap = el("div", "display:flex;flex-wrap:wrap;gap:14px");
    (cfg.items || []).forEach(function (it) {
      var s = RC.apply(RC.solved(), it.setup || RC.invert(it.alg || ""));
      var c = el("div", "flex:1 1 150px;max-width:200px;text-align:center;font-size:0.88em");
      c.innerHTML = RC.netSVG(s, { size: 14, mask: it.mask ? MASKS[it.mask] : null }) + '<div style="margin-top:4px">' + (it.label || "") + "</div>" + (it.alg ? '<code style="font-size:0.85em">' + it.alg + "</code>" : "");
      wrap.appendChild(c);
    });
    root.appendChild(wrap);
  }

  var INIT = { player: mountPlayer, notation: mountNotation, free: mountFree, net: mountNet };
  function boot() {
    document.querySelectorAll(".rb-w").forEach(function (root) {
      if (root.__done) return; root.__done = 1;
      var cfg = JSON.parse(root.getAttribute("data-cfg")), f = INIT[cfg.t];
      if (f) f(root, cfg);
    });
  }
  window.RBUI = { Cube3D: Cube3D, MASKS: MASKS, describe: describe, mountPlayer: mountPlayer, boot: boot, el: el, btn: btn };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
