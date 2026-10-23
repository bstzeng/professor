/* 魔術方塊求解器：Kociemba 兩階段演算法（自行實作）。
 * 第一階段：把方塊帶進子群 G1 = <U, D, R2, L2, F2, B2>（角塊方向、邊塊方向、中層邊塊位置都歸位）。
 * 第二階段：只用 G1 的轉動把方塊復原。
 * 用法：RBSolver.init(); RBSolver.solve("UUUUUUUUURRR…", { timeLimit: 1500 }) → "R U2 F' …"
 * facelet 字串依 URFDLB 各 9 格（Kociemba 慣例）。瀏覽器、Web Worker、Node 共用。
 */
(function (root) {
  "use strict";
  var URF = 0, UFL = 1, ULB = 2, UBR = 3, DFR = 4, DLF = 5, DBL = 6, DRB = 7;
  var UR = 0, UF = 1, UL = 2, UB = 3, DR = 4, DF = 5, DL = 6, DB = 7, FR = 8, FL = 9, BL = 10, BR = 11;
  // ---- 角塊與邊塊在 facelet 上的位置 ----
  var U = 0, R = 1, F = 2, D = 3, L = 4, B = 5;
  var cornerFacelet = [[8, 9, 20], [6, 18, 38], [0, 36, 47], [2, 45, 11], [29, 26, 15], [27, 44, 24], [33, 53, 42], [35, 17, 51]];
  var edgeFacelet = [[5, 10], [7, 19], [3, 37], [1, 46], [32, 16], [28, 25], [30, 43], [34, 52], [23, 12], [21, 41], [50, 39], [48, 14]];
  var cornerColor = [[U, R, F], [U, F, L], [U, L, B], [U, B, R], [D, F, R], [D, L, F], [D, B, L], [D, R, B]];
  var edgeColor = [[U, R], [U, F], [U, L], [U, B], [D, R], [D, F], [D, L], [D, B], [F, R], [F, L], [B, L], [B, R]];

  function Cube(cp, co, ep, eo) {
    this.cp = cp || [0, 1, 2, 3, 4, 5, 6, 7]; this.co = co || [0, 0, 0, 0, 0, 0, 0, 0];
    this.ep = ep || [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]; this.eo = eo || [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  }
  Cube.prototype.clone = function () { return new Cube(this.cp.slice(), this.co.slice(), this.ep.slice(), this.eo.slice()); };
  Cube.prototype.mul = function (b) {   // this * b（先做 this 再做 b）
    var c = new Cube();
    for (var i = 0; i < 8; i++) { c.cp[i] = this.cp[b.cp[i]]; c.co[i] = (this.co[b.cp[i]] + b.co[i]) % 3; }
    for (var j = 0; j < 12; j++) { c.ep[j] = this.ep[b.ep[j]]; c.eo[j] = (this.eo[b.ep[j]] + b.eo[j]) % 2; }
    return c;
  };
  var BASIC = [
    new Cube([UBR, URF, UFL, ULB, DFR, DLF, DBL, DRB], [0, 0, 0, 0, 0, 0, 0, 0], [UB, UR, UF, UL, DR, DF, DL, DB, FR, FL, BL, BR], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    new Cube([DFR, UFL, ULB, URF, DRB, DLF, DBL, UBR], [2, 0, 0, 1, 1, 0, 0, 2], [FR, UF, UL, UB, BR, DF, DL, DB, DR, FL, BL, UR], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    new Cube([UFL, DLF, ULB, UBR, URF, DFR, DBL, DRB], [1, 2, 0, 0, 2, 1, 0, 0], [UR, FL, UL, UB, DR, FR, DL, DB, UF, DF, BL, BR], [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0]),
    new Cube([URF, UFL, ULB, UBR, DLF, DBL, DRB, DFR], [0, 0, 0, 0, 0, 0, 0, 0], [UR, UF, UL, UB, DF, DL, DB, DR, FR, FL, BL, BR], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    new Cube([URF, ULB, DBL, UBR, DFR, UFL, DLF, DRB], [0, 1, 2, 0, 0, 2, 1, 0], [UR, UF, BL, UB, DR, DF, FL, DB, FR, UL, DL, BR], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    new Cube([URF, UFL, UBR, DRB, DFR, DLF, ULB, DBL], [0, 0, 1, 2, 0, 0, 2, 1], [UR, UF, UL, BR, DR, DF, DL, BL, FR, FL, UB, DB], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1]),
  ];
  var MOVES = [];   // 18 種轉動：面 × 3 + (次數 − 1)
  for (var f = 0; f < 6; f++) { var m = new Cube(); for (var k = 0; k < 3; k++) { m = m.mul(BASIC[f]); MOVES.push(m.clone()); } }
  var MOVE_NAMES = []; "URFDLB".split("").forEach(function (fc) { MOVE_NAMES.push(fc, fc + "2", fc + "'"); });

  // ---- facelet ↔ cubie ----
  function fromFacelets(str) {
    if (typeof str !== "string" || str.length !== 54) throw new Error("需要 54 格");
    var col = [], map = {};
    for (var f = 0; f < 6; f++) map[str[f * 9 + 4]] = f;
    if (Object.keys(map).length !== 6) throw new Error("六個中心的顏色必須都不同");
    for (var i = 0; i < 54; i++) { if (!(str[i] in map)) throw new Error("出現了不是中心顏色的格子"); col.push(map[str[i]]); }
    var cnt = [0, 0, 0, 0, 0, 0]; col.forEach(function (c) { cnt[c]++; });
    if (cnt.some(function (n) { return n !== 9; })) throw new Error("每種顏色都必須剛好 9 格");
    var c = new Cube(), seenC = [], seenE = [];
    for (var p = 0; p < 8; p++) {
      var ori = -1; for (ori = 0; ori < 3; ori++) if (col[cornerFacelet[p][ori]] === U || col[cornerFacelet[p][ori]] === D) break;
      if (ori === 3) throw new Error("有一個角塊沒有上下色（黃或白）");
      var c1 = col[cornerFacelet[p][(ori + 1) % 3]], c2 = col[cornerFacelet[p][(ori + 2) % 3]], found = -1;
      for (var j = 0; j < 8; j++) if (c1 === cornerColor[j][1] && c2 === cornerColor[j][2] && col[cornerFacelet[p][ori]] === cornerColor[j][0]) found = j;
      if (found < 0) throw new Error("有一個角塊的顏色組合不存在");
      c.cp[p] = found; c.co[p] = ori % 3; seenC.push(found);
    }
    for (var q = 0; q < 12; q++) {
      var a = col[edgeFacelet[q][0]], b2 = col[edgeFacelet[q][1]], fe = -1;
      for (var j2 = 0; j2 < 12; j2++) {
        if (a === edgeColor[j2][0] && b2 === edgeColor[j2][1]) { fe = j2; c.eo[q] = 0; }
        if (a === edgeColor[j2][1] && b2 === edgeColor[j2][0]) { fe = j2; c.eo[q] = 1; }
      }
      if (fe < 0) throw new Error("有一個邊塊的顏色組合不存在");
      c.ep[q] = fe; seenE.push(fe);
    }
    if (new Set(seenC).size !== 8) throw new Error("角塊重複出現（可能有顏色辨識錯誤）");
    if (new Set(seenE).size !== 12) throw new Error("邊塊重複出現（可能有顏色辨識錯誤）");
    if (c.co.reduce(function (s, v) { return s + v; }, 0) % 3) throw new Error("有一個角塊被扭轉了（物理上轉不出來）");
    if (c.eo.reduce(function (s, v) { return s + v; }, 0) % 2) throw new Error("有一個邊塊被翻面了（物理上轉不出來）");
    if (parity(c.cp) !== parity(c.ep)) throw new Error("有兩個塊被對調了（物理上轉不出來）");
    return c;
  }
  function parity(p) { var s = 0; for (var i = 0; i < p.length; i++) for (var j = i + 1; j < p.length; j++) if (p[i] > p[j]) s++; return s % 2; }

  // ---- 座標 ----
  var Cnk = []; for (var n = 0; n < 13; n++) { Cnk[n] = []; for (var kk = 0; kk < 13; kk++) Cnk[n][kk] = kk > n ? 0 : kk === 0 ? 1 : Cnk[n - 1][kk - 1] + Cnk[n - 1][kk]; }
  function getTwist(c) { var t = 0; for (var i = 0; i < 7; i++) t = 3 * t + c.co[i]; return t; }
  function setTwist(c, t) { var s = 0; for (var i = 6; i >= 0; i--) { c.co[i] = t % 3; s += c.co[i]; t = Math.floor(t / 3); } c.co[7] = (3 - s % 3) % 3; }
  function getFlip(c) { var t = 0; for (var i = 0; i < 11; i++) t = 2 * t + c.eo[i]; return t; }
  function setFlip(c, t) { var s = 0; for (var i = 10; i >= 0; i--) { c.eo[i] = t & 1; s += c.eo[i]; t >>= 1; } c.eo[11] = s % 2; }
  function getSlice(c) { var s = 0, k = 0; for (var j = 0; j < 12; j++) if (c.ep[j] >= 8) { k++; s += Cnk[j][k]; } return s; }
  function setSlice(c, s) {
    var pos = [], k = 4;
    for (var j = 11; j >= 0 && k > 0; j--) if (Cnk[j][k] <= s) { s -= Cnk[j][k]; pos.push(j); k--; }
    var other = 0, sl = 8; for (var q = 0; q < 12; q++) c.ep[q] = -1;
    pos.forEach(function (p) { c.ep[p] = sl++; });
    for (var q2 = 0; q2 < 12; q2++) if (c.ep[q2] < 0) c.ep[q2] = other++;
  }
  function rank(arr, n) { var r = 0; for (var i = 0; i < n; i++) { var s = 0; for (var j = i + 1; j < n; j++) if (arr[j] < arr[i]) s++; r = r * (n - i) + s; } return r; }
  function unrank(r, n) {
    var d = new Array(n), out = new Array(n), used = new Array(n).fill(false);
    for (var i = n - 1; i >= 0; i--) { d[i] = r % (n - i); r = Math.floor(r / (n - i)); }
    for (var k = 0; k < n; k++) { var c = d[k]; for (var v = 0; v < n; v++) if (!used[v]) { if (c === 0) { out[k] = v; used[v] = true; break; } c--; } }
    return out;
  }
  var N_TWIST = 2187, N_FLIP = 2048, N_SLICE = 495, N_PERM8 = 40320, N_SLICEP = 24;
  var P2MOVES = [0, 1, 2, 4, 7, 9, 10, 11, 13, 16];   // U U2 U' R2 F2 D D2 D' L2 B2
  var tables = null;

  function init() {
    if (tables) return tables;
    var t0 = Date.now(), i, m;
    var twistMove = new Uint16Array(N_TWIST * 18), flipMove = new Uint16Array(N_FLIP * 18), sliceMove = new Uint16Array(N_SLICE * 18);
    for (i = 0; i < N_TWIST; i++) { var a = new Cube(); setTwist(a, i); for (m = 0; m < 18; m++) twistMove[i * 18 + m] = getTwist(a.mul(MOVES[m])); }
    for (i = 0; i < N_FLIP; i++) { var b = new Cube(); setFlip(b, i); for (m = 0; m < 18; m++) flipMove[i * 18 + m] = getFlip(b.mul(MOVES[m])); }
    for (i = 0; i < N_SLICE; i++) { var c = new Cube(); setSlice(c, i); for (m = 0; m < 18; m++) sliceMove[i * 18 + m] = getSlice(c.mul(MOVES[m])); }
    var cpMove = new Uint16Array(N_PERM8 * 10), udMove = new Uint16Array(N_PERM8 * 10), spMove = new Uint8Array(N_SLICEP * 10);
    for (i = 0; i < N_PERM8; i++) {
      var p = unrank(i, 8), cc = new Cube(); cc.cp = p.slice();
      var ec = new Cube(); ec.ep = p.concat([8, 9, 10, 11]);
      for (m = 0; m < 10; m++) {
        var mv = MOVES[P2MOVES[m]];
        cpMove[i * 10 + m] = rank(cc.mul(mv).cp, 8);
        udMove[i * 10 + m] = rank(ec.mul(mv).ep, 8);
      }
    }
    for (i = 0; i < N_SLICEP; i++) {
      var q = unrank(i, 4), sc = new Cube(); sc.ep = [0, 1, 2, 3, 4, 5, 6, 7].concat(q.map(function (v) { return v + 8; }));
      for (m = 0; m < 10; m++) spMove[i * 10 + m] = rank(sc.mul(MOVES[P2MOVES[m]]).ep.slice(8).map(function (v) { return v - 8; }), 4);
    }
    var SLICE_GOAL = getSlice(new Cube());
    function bfs(size, start, step, nm) {
      var dist = new Int8Array(size).fill(-1), frontier = [start], d = 0; dist[start] = 0;
      while (frontier.length) {
        var next = [];
        for (var x = 0; x < frontier.length; x++) for (var mm = 0; mm < nm; mm++) { var y = step(frontier[x], mm); if (dist[y] < 0) { dist[y] = d + 1; next.push(y); } }
        frontier = next; d++;
      }
      return dist;
    }
    var pSliceTwist = bfs(N_SLICE * N_TWIST, SLICE_GOAL * N_TWIST, function (s, mm) { var sl = (s / N_TWIST) | 0, tw = s % N_TWIST; return sliceMove[sl * 18 + mm] * N_TWIST + twistMove[tw * 18 + mm]; }, 18);
    var pSliceFlip = bfs(N_SLICE * N_FLIP, SLICE_GOAL * N_FLIP, function (s, mm) { var sl = (s / N_FLIP) | 0, fl = s % N_FLIP; return sliceMove[sl * 18 + mm] * N_FLIP + flipMove[fl * 18 + mm]; }, 18);
    var pCp = bfs(N_SLICEP * N_PERM8, 0, function (s, mm) { var sp = (s / N_PERM8) | 0, c2 = s % N_PERM8; return spMove[sp * 10 + mm] * N_PERM8 + cpMove[c2 * 10 + mm]; }, 10);
    var pUd = bfs(N_SLICEP * N_PERM8, 0, function (s, mm) { var sp = (s / N_PERM8) | 0, c2 = s % N_PERM8; return spMove[sp * 10 + mm] * N_PERM8 + udMove[c2 * 10 + mm]; }, 10);
    tables = { twistMove: twistMove, flipMove: flipMove, sliceMove: sliceMove, cpMove: cpMove, udMove: udMove, spMove: spMove,
      pSliceTwist: pSliceTwist, pSliceFlip: pSliceFlip, pCp: pCp, pUd: pUd, SLICE_GOAL: SLICE_GOAL, ms: Date.now() - t0 };
    return tables;
  }

  // 同一面不連續轉；相對面只允許一種順序（U 後可接 D，D 後不可接 U）
  function allowed(f, last) { return last < 0 || (f !== last && f !== last - 3); }

  function solveCube(cube, opt) {
    opt = opt || {};
    var T = init(), tLimit = opt.timeLimit === undefined ? 1500 : opt.timeLimit, maxLen = opt.maxLength || 30, t0 = Date.now();
    var best = null, bestLen = maxLen + 1, path1 = [], path2 = [], timeUp = false, nodes = 0;
    var tw0 = getTwist(cube), fl0 = getFlip(cube), sl0 = getSlice(cube);
    if (tw0 === 0 && fl0 === 0 && sl0 === T.SLICE_GOAL && isSolvedCube(cube)) return [];

    function h1(sl, tw, fl) { return Math.max(T.pSliceTwist[sl * N_TWIST + tw], T.pSliceFlip[sl * N_FLIP + fl]); }
    function phase1(sl, tw, fl, depth, last) {
      if ((++nodes & 4095) === 0 && best && Date.now() - t0 > tLimit) timeUp = true;
      if (timeUp) return;
      if (depth === 0) {
        if (sl === T.SLICE_GOAL && tw === 0 && fl === 0 && (path1.length === 0 || P2MOVES.indexOf(path1[path1.length - 1]) < 0)) startPhase2();
        return;
      }
      if (h1(sl, tw, fl) > depth) return;
      for (var f = 0; f < 6; f++) {
        if (!allowed(f, last)) continue;
        for (var k = 0; k < 3; k++) {
          var mv = f * 3 + k;
          path1.push(mv);
          phase1(T.sliceMove[sl * 18 + mv], T.twistMove[tw * 18 + mv], T.flipMove[fl * 18 + mv], depth - 1, f);
          path1.pop();
          if (timeUp) return;
        }
      }
    }
    function startPhase2() {
      var c = cube; for (var i = 0; i < path1.length; i++) c = c.mul(MOVES[path1[i]]);
      var cp = rank(c.cp, 8), ud = rank(c.ep.slice(0, 8), 8), sp = rank(c.ep.slice(8).map(function (v) { return v - 8; }), 4);
      var room = bestLen - 1 - path1.length;
      if (room < 0) return;
      var last = path1.length ? Math.floor(path1[path1.length - 1] / 3) : -1;
      for (var d2 = Math.max(T.pCp[sp * N_PERM8 + cp], T.pUd[sp * N_PERM8 + ud]); d2 <= room; d2++) {
        path2.length = 0;
        if (phase2(cp, ud, sp, d2, last)) {
          best = path1.concat(path2); bestLen = best.length;
          return;
        }
      }
    }
    function phase2(cp, ud, sp, depth, last) {
      if (depth === 0) return cp === 0 && ud === 0 && sp === 0;
      if (Math.max(T.pCp[sp * N_PERM8 + cp], T.pUd[sp * N_PERM8 + ud]) > depth) return false;
      for (var j = 0; j < 10; j++) {
        var mv = P2MOVES[j], f = Math.floor(mv / 3);
        if (!allowed(f, last)) continue;
        path2.push(mv);
        if (phase2(T.cpMove[cp * 10 + j], T.udMove[ud * 10 + j], T.spMove[sp * 10 + j], depth - 1, f)) return true;
        path2.pop();
      }
      return false;
    }
    for (var d1 = h1(sl0, tw0, fl0); d1 < bestLen && d1 <= 20; d1++) {
      phase1(sl0, tw0, fl0, d1, -1);
      if (timeUp) break;
      if (best && Date.now() - t0 > tLimit) break;
    }
    return best ? best.map(function (m) { return MOVE_NAMES[m]; }) : null;
  }
  function isSolvedCube(c) {
    for (var i = 0; i < 8; i++) if (c.cp[i] !== i || c.co[i]) return false;
    for (var j = 0; j < 12; j++) if (c.ep[j] !== j || c.eo[j]) return false;
    return true;
  }
  function solve(facelets, opt) { return solveCube(fromFacelets(facelets), opt); }
  function applyMoves(cube, moves) {
    moves.forEach(function (n) { cube = cube.mul(MOVES[MOVE_NAMES.indexOf(n)]); }); return cube;
  }

  var RBSolver = { init: init, solve: solve, solveCube: solveCube, fromFacelets: fromFacelets, Cube: Cube, MOVES: MOVES, MOVE_NAMES: MOVE_NAMES,
    applyMoves: applyMoves, isSolvedCube: isSolvedCube, ready: function () { return !!tables; } };
  root.RBSolver = RBSolver;
  if (typeof module !== "undefined" && module.exports) module.exports = RBSolver;
  // 當成 Web Worker 執行時：收到 {facelets, timeLimit} 就回傳解法
  if (typeof self !== "undefined" && typeof window === "undefined" && typeof self.postMessage === "function" && typeof module === "undefined") {
    self.onmessage = function (e) {
      try {
        if (e.data && e.data.init) { var tt = init(); self.postMessage({ ready: true, ms: tt.ms }); return; }
        var t1 = Date.now(), sol = solve(e.data.facelets, { timeLimit: e.data.timeLimit || 1500 });
        self.postMessage({ ok: true, moves: sol, ms: Date.now() - t1 });
      } catch (err) { self.postMessage({ ok: false, error: String(err.message || err) }); }
    };
  }
})(typeof self !== "undefined" ? self : typeof window !== "undefined" ? window : globalThis);
