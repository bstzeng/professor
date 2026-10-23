/* 魔術方塊核心：狀態、轉動、公式解析、展開圖。瀏覽器與 Node 共用（掛在 RBCore）。
 * 座標：x 往右（R）、y 往上（U）、z 往前（F）。配色採白底黃頂、綠色朝前：
 *   U 黃、R 橘、F 綠、D 白、L 紅、B 藍。
 * 貼紙位置 0–53 依 URFDLB 順序，每面 9 格，由左上到右下（Kociemba 的 facelet 慣例）。
 * 狀態 state[位置] = 目前在該位置的貼紙編號（復原時 state[i] = i），貼紙顏色 = floor(編號 / 9)。
 */
(function (root) {
  "use strict";
  var FACES = "URFDLB";
  var COLORS = ["#ffd500", "#ff6a00", "#13a34a", "#f4f4f4", "#d7192c", "#1565d8"];   // U R F D L B
  var COLOR_NAMES = ["黃", "橘", "綠", "白", "紅", "藍"];

  // 每個面的法向量與格子座標（列 r、行 c 從左上開始）
  function stickerPos(f, r, c) {
    switch (f) {
      case 0: return [c - 1, 1.5, r - 1];          // U：從上方看，B 在上
      case 1: return [1.5, 1 - r, 1 - c];          // R：U 在上，左邊是 F
      case 2: return [c - 1, 1 - r, 1.5];          // F
      case 3: return [c - 1, -1.5, 1 - r];         // D：從下方看，F 在上
      case 4: return [-1.5, 1 - r, c - 1];         // L：U 在上，左邊是 B
      default: return [1 - c, 1 - r, -1.5];        // B：U 在上，左邊是 R
    }
  }
  var NORMALS = [[0, 1, 0], [1, 0, 0], [0, 0, 1], [0, -1, 0], [-1, 0, 0], [0, 0, -1]];
  var POS = [], NRM = [];
  for (var f = 0; f < 6; f++) for (var r = 0; r < 3; r++) for (var c = 0; c < 3; c++) { POS.push(stickerPos(f, r, c)); NRM.push(NORMALS[f]); }
  function rot(v, axis, q) {          // 繞座標軸轉 q × 90°（右手定則）
    var x = v[0], y = v[1], z = v[2];
    q = ((q % 4) + 4) % 4;
    for (var i = 0; i < q; i++) {
      if (axis === 0) { var t = y; y = -z; z = t; }
      else if (axis === 1) { var t2 = x; x = z; z = -t2; }
      else { var t3 = x; x = -y; y = t3; }
    }
    return [x, y, z];
  }
  function keyOf(p, n) { return p.map(function (v) { return Math.round(v * 2); }).join(",") + "|" + n.join(","); }
  var INDEX = {};
  for (var i = 0; i < 54; i++) INDEX[keyOf(POS[i], NRM[i])] = i;

  // 基本轉動：[軸, 層, 方向]（方向 −1 = 從該軸正方向看順時針）
  var ALL = [-1, 0, 1];
  var BASE = {
    U: [1, [1], -1], D: [1, [-1], 1], R: [0, [1], -1], L: [0, [-1], 1], F: [2, [1], -1], B: [2, [-1], 1],
    M: [0, [0], 1], E: [1, [0], 1], S: [2, [0], -1],
    x: [0, ALL, -1], y: [1, ALL, -1], z: [2, ALL, -1],
    u: [1, [1, 0], -1], d: [1, [-1, 0], 1], r: [0, [1, 0], -1], l: [0, [-1, 0], 1], f: [2, [1, 0], -1], b: [2, [-1, 0], 1],
  };
  var PERM = {};   // PERM[名稱][i] = 位置 i 的貼紙轉完後到哪個位置
  Object.keys(BASE).forEach(function (k) {
    var a = BASE[k][0], layers = BASE[k][1], dir = BASE[k][2], perm = new Array(54);
    for (var i = 0; i < 54; i++) {
      var cub = cubieOf(i);
      if (layers.indexOf(cub[a]) < 0) { perm[i] = i; continue; }
      perm[i] = INDEX[keyOf(rot(POS[i], a, dir), rot(NRM[i], a, dir))];
    }
    PERM[k] = perm;
  });
  function cubieOf(i) { return POS[i].map(function (v) { return Math.abs(v) === 1.5 ? (v > 0 ? 1 : -1) : v; }); }

  // ---- 公式解析 ----
  // 支援 R R' R2 R2'、小寫或 Rw 寬層、M E S、x y z，括號與 (…)3 重複
  function parse(str) {
    if (Array.isArray(str)) return str.slice();
    str = String(str || "").replace(/[’′‘`]/g, "'").replace(/[\[\]]/g, function (m) { return m === "[" ? "(" : ")"; });
    var out = [], stack = [[]], i = 0, s = str;
    while (i < s.length) {
      var ch = s[i];
      if (/\s/.test(ch)) { i++; continue; }
      if (ch === "(") { stack.push([]); i++; continue; }
      if (ch === ")") {
        var grp = stack.pop(); i++;
        var m = /^\d+/.exec(s.slice(i)), n = 1;
        if (m) { n = +m[0]; i += m[0].length; }
        for (var k = 0; k < n; k++) Array.prototype.push.apply(stack[stack.length - 1], grp);
        continue;
      }
      var mm = /^([URFDLBMESxyzurfdlb])(w?)(2|3)?('?)/.exec(s.slice(i));
      if (!mm) { i++; continue; }
      var base = mm[1];
      if (mm[2] === "w") base = base.toLowerCase();
      var amt = mm[3] === "2" ? 2 : mm[3] === "3" ? 3 : 1;
      if (mm[4]) amt = (4 - amt) % 4 || 4;
      if (amt === 4) amt = 0;
      if (amt) stack[stack.length - 1].push(base + (amt === 1 ? "" : amt === 2 ? "2" : "'"));
      i += mm[0].length;
    }
    while (stack.length > 1) { var g2 = stack.pop(); Array.prototype.push.apply(stack[stack.length - 1], g2); }
    return stack[0];
  }
  function amountOf(mv) { return mv.slice(-1) === "2" ? 2 : mv.slice(-1) === "'" ? 3 : 1; }
  function baseOf(mv) { return mv[0]; }
  function invertMove(mv) { var a = amountOf(mv); return baseOf(mv) + (a === 1 ? "'" : a === 2 ? "2" : ""); }
  function invert(moves) { return parse(moves).slice().reverse().map(invertMove); }
  function format(moves) { return parse(moves).join(" "); }

  function solved() { var s = new Array(54); for (var i = 0; i < 54; i++) s[i] = i; return s; }
  function applyMove(state, mv) {
    var perm = PERM[baseOf(mv)], n = amountOf(mv), s = state;
    for (var k = 0; k < n; k++) { var t = new Array(54); for (var i = 0; i < 54; i++) t[perm[i]] = s[i]; s = t; }
    return s;
  }
  function apply(state, moves) { var s = state.slice(); parse(moves).forEach(function (m) { s = applyMove(s, m); }); return s; }
  function colorOf(id) { return Math.floor(id / 9); }
  function isSolved(state) {
    for (var f = 0; f < 6; f++) { var c = colorOf(state[f * 9 + 4]); for (var k = 0; k < 9; k++) if (colorOf(state[f * 9 + k]) !== c) return false; }
    return true;
  }
  // 給求解器的 54 字元字串（依中心顏色命名各面，所以整顆轉過也沒關係）
  function toFacelets(state) {
    var centerFace = {};
    for (var f = 0; f < 6; f++) centerFace[colorOf(state[f * 9 + 4])] = FACES[f];
    return state.map(function (id) { return centerFace[colorOf(id)]; }).join("");
  }
  // 由「每格顏色」（0–5）建立狀態；同色的貼紙編號挑該色的中心
  function fromColors(cols) { return cols.map(function (c) { return c * 9 + 4; }); }
  function scramble(n, rnd) {
    rnd = rnd || Math.random; n = n || 20; var out = [], last = -1, prev = -1;
    while (out.length < n) {
      var f = Math.floor(rnd() * 6);
      if (f === last) continue;
      if (f % 3 === last % 3 && f % 3 === prev % 3) continue;     // 避免 U D U 這種可合併的序列
      out.push(FACES[f] + ["", "2", "'"][Math.floor(rnd() * 3)]); prev = last; last = f;
    }
    return out;
  }

  // ---- 展開圖（SVG 字串）----
  // 版面：      U
  //         L  F  R  B
  //            D
  function netSVG(state, opt) {
    opt = opt || {}; var s = opt.size || 10, g = opt.gap || 1, mask = opt.mask, hl = opt.highlight;
    var off = { U: [3, 0], L: [0, 3], F: [3, 3], R: [6, 3], B: [9, 3], D: [3, 6] }, out = [];
    var W = 12 * s + 2 * g, H = 9 * s + 2 * g;
    for (var f = 0; f < 6; f++) {
      var o = off[FACES[f]];
      for (var k = 0; k < 9; k++) {
        var id = state[f * 9 + k], col = (mask && !mask(id)) ? "#5a5f68" : COLORS[colorOf(id)];
        var x = g + (o[0] + k % 3) * s, y = g + (o[1] + Math.floor(k / 3)) * s;
        out.push('<rect x="' + (x + 0.6) + '" y="' + (y + 0.6) + '" width="' + (s - 1.2) + '" height="' + (s - 1.2) + '" rx="' + (s * 0.15) +
          '" fill="' + col + '" stroke="' + (hl && hl.indexOf(f * 9 + k) >= 0 ? "#ff3df2" : "#111") + '" stroke-width="' + (hl && hl.indexOf(f * 9 + k) >= 0 ? 2 : 0.8) + '"/>');
      }
    }
    return '<svg viewBox="0 0 ' + W + ' ' + H + '" style="width:100%;display:block">' + out.join("") + "</svg>";
  }

  var RBCore = { FACES: FACES, COLORS: COLORS, COLOR_NAMES: COLOR_NAMES, POS: POS, NRM: NRM, BASE: BASE, PERM: PERM,
    cubieOf: cubieOf, rot: rot, parse: parse, invert: invert, invertMove: invertMove, format: format, amountOf: amountOf, baseOf: baseOf,
    solved: solved, applyMove: applyMove, apply: apply, colorOf: colorOf, isSolved: isSolved, toFacelets: toFacelets, fromColors: fromColors,
    scramble: scramble, netSVG: netSVG };
  root.RBCore = RBCore;
  if (typeof module !== "undefined" && module.exports) module.exports = RBCore;
})(typeof window !== "undefined" ? window : globalThis);
