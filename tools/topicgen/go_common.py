# -*- coding: utf-8 -*-
"""圍棋入門課程：共用工具。

- Board：Python 版棋盤（提子、自殺、打劫），用來驗證所有例題與練習題。
- dia()：把一個局面畫成靜態 SVG 棋盤圖。
- problem() / replay() / sandbox() / counting()：產生互動元件的 HTML，由 GOLIB（JS）在瀏覽器中執行。
- can_kill()：小範圍死活搜尋，用來驗證死活題的正解與錯解。
- lesson()：每課結尾加上「下棋時記得」；有互動元件的課會自動帶入 GOLIB。

座標用 SGF 慣例：兩個字母，第一個是欄（a = 最左），第二個是列（a = 最上）。
顯示時轉為 A–T（跳過 I）與 1–19（由下往上）。
"""
import json
from gen import Lesson

LETTERS = "ABCDEFGHJKLMNOPQRST"


def P(s):
    """'cd' -> (2, 3)。"""
    return (ord(s[0]) - 97, ord(s[1]) - 97)


def PTS(s):
    return [P(t) for t in s.split()] if s else []


def opp(c):
    return "w" if c == "b" else "b"


class Illegal(Exception):
    pass


class Board(object):
    def __init__(self, n, b="", w=""):
        self.n = n
        self.g = {}
        self.prev = None
        for p in PTS(b):
            self.g[p] = "b"
        for p in PTS(w):
            self.g[p] = "w"

    def copy(self):
        o = Board(self.n)
        o.g = dict(self.g)
        o.prev = self.prev
        return o

    def key(self):
        return frozenset(self.g.items())

    def nb(self, p):
        x, y = p
        for q in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= q[0] < self.n and 0 <= q[1] < self.n:
                yield q

    def group(self, p):
        c = self.g[p]
        seen, libs, st = {p}, set(), [p]
        while st:
            q = st.pop()
            for r in self.nb(q):
                v = self.g.get(r)
                if v is None:
                    libs.add(r)
                elif v == c and r not in seen:
                    seen.add(r)
                    st.append(r)
        return seen, libs

    def libs(self, p):
        return len(self.group(p)[1])

    def play(self, p, c):
        if p in self.g:
            raise Illegal("occupied %s" % (p,))
        before = self.key()
        self.g[p] = c
        cap = []
        for q in self.nb(p):
            if self.g.get(q) == opp(c):
                s, l = self.group(q)
                if not l:
                    cap.extend(s)
                    for r in s:
                        del self.g[r]
        if not self.group(p)[1]:
            del self.g[p]
            for r in cap:
                self.g[r] = opp(c)
            raise Illegal("suicide %s" % (p,))
        if self.prev is not None and self.key() == self.prev:
            del self.g[p]
            for r in cap:
                self.g[r] = opp(c)
            raise Illegal("ko %s" % (p,))
        self.prev = before
        return cap

    def run(self, seq, first="b"):
        """seq = 'cd de ef' 或 [(pt, color)]；交替落子。回傳所有被提的子。"""
        caps = []
        c = first
        items = seq.split() if isinstance(seq, str) else seq
        for m in items:
            if isinstance(m, tuple):
                p, col = m
            else:
                p, col = m, c
            if p not in ("pass", "tt"):
                caps.extend(self.play(P(p) if isinstance(p, str) else p, col))
            c = opp(col)
        return caps

    def area(self):
        """數子法：棋子 + 只被單一顏色包圍的空點。"""
        sc = {"b": 0, "w": 0}
        for v in self.g.values():
            sc[v] += 1
        seen = set()
        for x in range(self.n):
            for y in range(self.n):
                p = (x, y)
                if p in self.g or p in seen:
                    continue
                reg, border, st = {p}, set(), [p]
                while st:
                    q = st.pop()
                    for r in self.nb(q):
                        v = self.g.get(r)
                        if v is None and r not in reg:
                            reg.add(r)
                            st.append(r)
                        elif v:
                            border.add(v)
                seen |= reg
                if len(border) == 1:
                    sc[border.pop()] += len(reg)
        return sc


def can_kill(board, region, target, to_move, depth, memo=None, passed=False):
    """攻方（target 的對手）能否在 depth 手內提掉 target 所在的棋塊。
    雙方只能下在 region 內或虛手；守方撐到 depth 用完或雙方連續虛手即算活。"""
    if memo is None:
        memo = {}
    tc = board.g.get(target)
    if tc is None:
        return True
    attacker = opp(tc)
    if depth == 0:
        return False
    k = (board.key(), board.prev, to_move, depth, passed)
    if k in memo:
        return memo[k]
    results = []
    moves = [p for p in region if p not in board.g] + [None]
    res = (to_move != attacker)
    for m in moves:
        b2 = board.copy()
        if m is None:
            if passed:
                r = False
            else:
                b2.prev = None
                r = can_kill(b2, region, target, opp(to_move), depth - 1, memo, True)
        else:
            try:
                b2.play(m, to_move)
            except Illegal:
                continue
            r = can_kill(b2, region, target, opp(to_move), depth - 1, memo, False)
        if to_move == attacker and r:
            res = True
            break
        if to_move != attacker and not r:
            res = False
            break
    memo[k] = res
    return res


def check_life(n, b, w, region, target, to_move, good, depth=14):
    """驗證死活題：只有 good 裡的第一手能達成目標。
    to_move 若是攻方：good 必須殺得掉，其他手（含虛手）殺不掉。
    to_move 若是守方：good 必須活得了，其他手活不了。"""
    bd = Board(n, b, w)
    R = PTS(region)
    tgt = P(target)
    attacker = opp(bd.g[tgt])
    goods = set(PTS(good))
    for m in R + [None]:
        b2 = bd.copy()
        if m is not None:
            if m in b2.g:
                continue
            try:
                b2.play(m, to_move)
            except Illegal:
                continue
        killed = can_kill(b2, R, tgt, opp(to_move), depth)
        ok = killed if to_move == attacker else not killed
        expect = (m in goods)
        if ok != expect:
            raise AssertionError("life check failed at move %s: ok=%s expect=%s (%s)" % (m, ok, expect, target))
    return True


# ---------------- 靜態棋盤圖 ----------------

WOOD = "#dcb35c"
LINEC = "#3a2a10"
STAR = {9: [2, 4, 6], 13: [3, 6, 9], 19: [3, 9, 15]}


def _view(n, view):
    if view is None:
        return (0, 0, n - 1, n - 1)
    if isinstance(view, str):
        a, b = view.split()
        (x0, y0), (x1, y1) = P(a), P(b)
        return (x0, y0, x1, y1)
    return view


def board_svg(n, b="", w="", view=None, marks=None, seq=None, first="b", coords=True, cell=30, tri="", sq="", cir="",
              xmark=""):
    """回傳 (svg 內容, 寬, 高)。seq：依序落子並在棋子上標手數（被提的子不顯示）。
    marks：{'cd': 'A'} 在點上標字母；tri/sq/cir/xmark：標記。"""
    bd = Board(n, b, w)
    nums = {}
    if seq:
        c = first
        for i, m in enumerate(seq.split()):
            if m == "pass":
                c = opp(c)
                continue
            p = P(m)
            for q in bd.play(p, c):
                nums.pop(q, None)
            nums[p] = i + 1
            c = opp(c)
    x0, y0, x1, y1 = _view(n, view)
    m = 30 if coords else 14
    W = (x1 - x0) * cell + 2 * m
    H = (y1 - y0) * cell + 2 * m
    o = ['<rect x="0" y="0" width="%d" height="%d" rx="6" fill="%s"/>' % (W, H, WOOD)]

    def X(x):
        return m + (x - x0) * cell

    def Y(y):
        return m + (y - y0) * cell

    ext = cell * 0.3
    for x in range(x0, x1 + 1):
        ya = Y(y0) - (ext if y0 > 0 else 0)
        yb = Y(y1) + (ext if y1 < n - 1 else 0)
        sw = 1.6 if x in (0, n - 1) else 0.9
        o.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="%g"/>' % (X(x), ya, X(x), yb, LINEC, sw))
    for y in range(y0, y1 + 1):
        xa = X(x0) - (ext if x0 > 0 else 0)
        xb = X(x1) + (ext if x1 < n - 1 else 0)
        sw = 1.6 if y in (0, n - 1) else 0.9
        o.append('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="%g"/>' % (xa, Y(y), xb, Y(y), LINEC, sw))
    for sx in STAR.get(n, []):
        for sy in STAR.get(n, []):
            if n == 9 and (sx, sy) not in ((2, 2), (6, 2), (2, 6), (6, 6), (4, 4)):
                continue
            if x0 <= sx <= x1 and y0 <= sy <= y1:
                o.append('<circle cx="%g" cy="%g" r="3" fill="%s"/>' % (X(sx), Y(sy), LINEC))
    if coords:
        for x in range(x0, x1 + 1):
            o.append('<text x="%g" y="%g" font-size="10" text-anchor="middle" fill="%s">%s</text>' % (X(x), m - 12, LINEC, LETTERS[x]))
            o.append('<text x="%g" y="%g" font-size="10" text-anchor="middle" fill="%s">%s</text>' % (X(x), H - 6, LINEC, LETTERS[x]))
        for y in range(y0, y1 + 1):
            o.append('<text x="%g" y="%g" font-size="10" text-anchor="middle" fill="%s">%d</text>' % (m - 19, Y(y) + 3.5, LINEC, n - y))
            o.append('<text x="%g" y="%g" font-size="10" text-anchor="middle" fill="%s">%d</text>' % (W - 11, Y(y) + 3.5, LINEC, n - y))
    r = cell * 0.47
    for (x, y), c in sorted(bd.g.items()):
        if not (x0 <= x <= x1 and y0 <= y <= y1):
            continue
        if c == "b":
            o.append('<circle cx="%g" cy="%g" r="%g" fill="#1d1d1d" stroke="#000" stroke-width="0.8"/>' % (X(x), Y(y), r))
        else:
            o.append('<circle cx="%g" cy="%g" r="%g" fill="#f8f8f4" stroke="#444" stroke-width="0.9"/>' % (X(x), Y(y), r))
    marks = dict(marks or {})
    for p, num in nums.items():
        marks.setdefault("%s%s" % (chr(p[0] + 97), chr(p[1] + 97)), str(num))
    for k, lab in marks.items():
        p = P(k)
        x, y = p
        if not (x0 <= x <= x1 and y0 <= y <= y1):
            continue
        c = bd.g.get(p)
        col = "#fff" if c == "b" else ("#111" if c == "w" else "#b3261e")
        if c is None:
            o.append('<rect x="%g" y="%g" width="%g" height="%g" fill="%s"/>' % (X(x) - 8, Y(y) - 8, 16, 16, WOOD))
        fs = (12 if n < 19 else 15) if len(lab) < 3 else 10
        o.append('<text x="%g" y="%g" font-size="%d" font-weight="bold" text-anchor="middle" fill="%s">%s</text>' % (X(x), Y(y) + fs / 2.8, fs, col, lab))
    for k in PTS(tri):
        x, y = k
        c = bd.g.get(k)
        col = "#fff" if c == "b" else "#b3261e"
        s = cell * 0.22
        o.append('<polygon points="%g,%g %g,%g %g,%g" fill="none" stroke="%s" stroke-width="1.8"/>' % (
            X(x), Y(y) - s, X(x) - s * 0.95, Y(y) + s * 0.65, X(x) + s * 0.95, Y(y) + s * 0.65, col))
    for k in PTS(sq):
        x, y = k
        c = bd.g.get(k)
        col = "#fff" if c == "b" else "#1f6fb5"
        s = cell * 0.2
        o.append('<rect x="%g" y="%g" width="%g" height="%g" fill="none" stroke="%s" stroke-width="1.8"/>' % (X(x) - s, Y(y) - s, 2 * s, 2 * s, col))
    for k in PTS(cir):
        x, y = k
        c = bd.g.get(k)
        col = "#fff" if c == "b" else "#1f8a4c"
        o.append('<circle cx="%g" cy="%g" r="%g" fill="none" stroke="%s" stroke-width="1.8"/>' % (X(x), Y(y), cell * 0.2, col))
    for k in PTS(xmark):
        x, y = k
        s = cell * 0.18
        o.append('<path d="M%g %g L%g %g M%g %g L%g %g" stroke="#b3261e" stroke-width="2"/>' % (
            X(x) - s, Y(y) - s, X(x) + s, Y(y) + s, X(x) - s, Y(y) + s, X(x) + s, Y(y) - s))
    return "\n".join(o), W, H


def dia(n, b="", w="", cap=u"", **kw):
    """靜態棋盤圖 → raw 區塊（寬度依棋盤大小限制，避免小棋盤被放得太大）。"""
    s, W, H = board_svg(n, b, w, **kw)
    mw = min(440, int(W * 1.35))
    html = (u'<div class="content-figure"><svg class="content-diagram go-dia" viewBox="0 0 %d %d" '
            u'xmlns="http://www.w3.org/2000/svg" style="max-width:%dpx;width:100%%;margin:0 auto;display:block">%s</svg>'
            % (W, H, mw, s))
    if cap:
        html += u"<figcaption>%s</figcaption>" % cap
    html += u"</div>"
    return ("raw", html)


def dias(items):
    """並排兩三張小圖：items = [(n, b, w, cap, kw)]。"""
    parts = []
    for n, b, w, cap, kw in items:
        s, W, H = board_svg(n, b, w, **kw)
        parts.append(u'<figure style="margin:0;flex:1 1 180px;max-width:%dpx"><svg viewBox="0 0 %d %d" '
                     u'xmlns="http://www.w3.org/2000/svg" style="width:100%%;display:block">%s</svg>'
                     u'<figcaption style="text-align:center">%s</figcaption></figure>' % (min(300, int(W * 1.3)), W, H, s, cap))
    return ("raw", u'<div class="content-figure" style="display:flex;flex-wrap:wrap;gap:12px;justify-content:center">%s</div>'
            % u"".join(parts))


# ---------------- 互動元件 ----------------

def _verify_seq(n, b, w, seq, first):
    bd = Board(n, b, w)
    bd.run(seq, first)
    return bd


def problem(n, b, w, to_play, correct, wrong=None, view=None, prompt=u"", other=u"這一手不是最好的。再想想看！",
            verify=None):
    """correct / wrong = {'cd': ('後續手順', '說明')}；後續手順從對手的回應開始交替。
    verify：可選的驗證函式 verify(Board after correct line) -> bool。"""
    wrong = wrong or {}
    for d, good in ((correct, True), (wrong, False)):
        for mv, (seq, msg) in d.items():
            full = (mv + " " + seq).strip()
            bd = _verify_seq(n, b, w, full, to_play)
            if good and verify is not None and not verify(bd):
                raise AssertionError("verify failed for %s" % mv)
    cfg = {"t": "prob", "n": n, "b": b, "w": w, "p": to_play, "v": list(_view(n, view)), "q": prompt,
           "ok": {k: [v[0], v[1]] for k, v in correct.items()}, "ng": {k: [v[0], v[1]] for k, v in wrong.items()},
           "other": other}
    return ("raw", u'<div class="go-w content-figure" data-cfg="%s"></div>' % _attr(cfg))


def replay(n, moves, b="", w="", first="b", view=None, title=u""):
    """moves = [('cd', '說明'), ...]；交替落子（'pass' 表示虛手）。"""
    seq = " ".join(m for m, _ in moves)
    _verify_seq(n, b, w, seq, first)
    cfg = {"t": "replay", "n": n, "b": b, "w": w, "f": first, "v": list(_view(n, view)), "m": [[m, c] for m, c in moves],
           "q": title}
    return ("raw", u'<div class="go-w content-figure" data-cfg="%s"></div>' % _attr(cfg))


def sandbox(n=9, b="", w="", title=u"自由擺棋"):
    cfg = {"t": "sand", "n": n, "b": b, "w": w, "q": title}
    return ("raw", u'<div class="go-w content-figure" data-cfg="%s"></div>' % _attr(cfg))


def counting(n, b, w, komi=7.0, title=u""):
    bd = Board(n, b, w)
    sc = bd.area()
    cfg = {"t": "count", "n": n, "b": b, "w": w, "k": komi, "q": title, "a": [sc["b"], sc["w"]]}
    return ("raw", u'<div class="go-w content-figure" data-cfg="%s"></div>' % _attr(cfg))


def _attr(cfg):
    s = json.dumps(cfg, ensure_ascii=False)
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")


GOLIB = r"""
(function () {
  if (window.__goLib) return; window.__goLib = 1;
  var L = 'ABCDEFGHJKLMNOPQRST', WOOD = '#dcb35c', LC = '#3a2a10';
  function P(s) { return [s.charCodeAt(0) - 97, s.charCodeAt(1) - 97]; }
  function K(x, y) { return x + ',' + y; }
  function opp(c) { return c === 'b' ? 'w' : 'b'; }
  function Board(n) { this.n = n; this.g = {}; this.prev = null; }
  Board.prototype.copy = function () { var o = new Board(this.n); for (var k in this.g) o.g[k] = this.g[k]; o.prev = this.prev; return o; };
  Board.prototype.key = function () { return Object.keys(this.g).sort().map(function (k) { return k + this.g[k]; }, this).join(';'); };
  Board.prototype.nb = function (x, y) { var r = [], n = this.n; [[x-1,y],[x+1,y],[x,y-1],[x,y+1]].forEach(function (q) { if (q[0] >= 0 && q[0] < n && q[1] >= 0 && q[1] < n) r.push(q); }); return r; };
  Board.prototype.group = function (x, y) {
    var c = this.g[K(x, y)], seen = {}, libs = {}, st = [[x, y]], self = this; seen[K(x, y)] = 1;
    while (st.length) { var q = st.pop(); self.nb(q[0], q[1]).forEach(function (r) { var k = K(r[0], r[1]), v = self.g[k];
      if (!v) libs[k] = 1; else if (v === c && !seen[k]) { seen[k] = 1; st.push(r); } }); }
    return { s: Object.keys(seen), l: Object.keys(libs).length };
  };
  Board.prototype.play = function (x, y, c) {
    var k = K(x, y); if (this.g[k]) return null;
    var before = this.key(), self = this, cap = [];
    this.g[k] = c;
    this.nb(x, y).forEach(function (q) { var kk = K(q[0], q[1]);
      if (self.g[kk] === opp(c)) { var gr = self.group(q[0], q[1]); if (!gr.l) gr.s.forEach(function (s) { if (self.g[s]) { cap.push(s); delete self.g[s]; } }); } });
    if (!this.group(x, y).l || (this.prev !== null && this.key() === this.prev)) {
      delete this.g[k]; cap.forEach(function (s) { self.g[s] = opp(c); }); return null; }
    this.prev = before; return cap;
  };
  Board.prototype.load = function (b, w) { var self = this;
    (b || '').split(' ').forEach(function (s) { if (s) { var p = P(s); self.g[K(p[0], p[1])] = 'b'; } });
    (w || '').split(' ').forEach(function (s) { if (s) { var p = P(s); self.g[K(p[0], p[1])] = 'w'; } }); return this; };
  Board.prototype.area = function () {
    var sc = { b: 0, w: 0 }, seen = {}, self = this, n = this.n;
    for (var k in this.g) sc[this.g[k]]++;
    for (var x = 0; x < n; x++) for (var y = 0; y < n; y++) { var kk = K(x, y); if (this.g[kk] || seen[kk]) continue;
      var reg = [kk], bor = {}, st = [[x, y]]; seen[kk] = 1;
      while (st.length) { var q = st.pop(); self.nb(q[0], q[1]).forEach(function (r) { var k2 = K(r[0], r[1]), v = self.g[k2];
        if (!v && !seen[k2]) { seen[k2] = 1; reg.push(k2); st.push(r); } else if (v) bor[v] = 1; }); }
      var bs = Object.keys(bor); if (bs.length === 1) sc[bs[0]] += reg.length; }
    return sc;
  };
  var NS = 'http://www.w3.org/2000/svg';
  function el(tag, at, txt) { var e = document.createElementNS(NS, tag); for (var a in at) e.setAttribute(a, at[a]); if (txt !== undefined) e.textContent = txt; return e; }
  function draw(svg, bd, v, opt) {
    opt = opt || {}; var n = bd.n, cell = 30, m = 30, x0 = v[0], y0 = v[1], x1 = v[2], y1 = v[3];
    var W = (x1 - x0) * cell + 2 * m, H = (y1 - y0) * cell + 2 * m;
    svg.setAttribute('viewBox', '0 0 ' + W + ' ' + H); while (svg.firstChild) svg.removeChild(svg.firstChild);
    function X(x) { return m + (x - x0) * cell; } function Y(y) { return m + (y - y0) * cell; }
    svg.appendChild(el('rect', { x: 0, y: 0, width: W, height: H, rx: 6, fill: WOOD }));
    var ext = cell * 0.3;
    for (var x = x0; x <= x1; x++) svg.appendChild(el('line', { x1: X(x), x2: X(x), y1: Y(y0) - (y0 > 0 ? ext : 0), y2: Y(y1) + (y1 < n - 1 ? ext : 0), stroke: LC, 'stroke-width': (x === 0 || x === n - 1) ? 1.6 : 0.9 }));
    for (var y = y0; y <= y1; y++) svg.appendChild(el('line', { y1: Y(y), y2: Y(y), x1: X(x0) - (x0 > 0 ? ext : 0), x2: X(x1) + (x1 < n - 1 ? ext : 0), stroke: LC, 'stroke-width': (y === 0 || y === n - 1) ? 1.6 : 0.9 }));
    var st = { 9: [[2,2],[6,2],[2,6],[6,6],[4,4]], 13: [3,6,9], 19: [3,9,15] }[n] || [];
    if (n !== 9) { var t = []; st.forEach(function (a) { st.forEach(function (b) { t.push([a, b]); }); }); st = t; }
    st.forEach(function (s) { if (s[0] >= x0 && s[0] <= x1 && s[1] >= y0 && s[1] <= y1) svg.appendChild(el('circle', { cx: X(s[0]), cy: Y(s[1]), r: 3, fill: LC })); });
    for (x = x0; x <= x1; x++) { svg.appendChild(el('text', { x: X(x), y: m - 12, 'font-size': 10, 'text-anchor': 'middle', fill: LC }, L[x])); }
    for (y = y0; y <= y1; y++) { svg.appendChild(el('text', { x: m - 19, y: Y(y) + 3.5, 'font-size': 10, 'text-anchor': 'middle', fill: LC }, String(n - y))); }
    for (var k in bd.g) { var p = k.split(',').map(Number); if (p[0] < x0 || p[0] > x1 || p[1] < y0 || p[1] > y1) continue;
      var b = bd.g[k] === 'b';
      svg.appendChild(el('circle', { cx: X(p[0]), cy: Y(p[1]), r: cell * 0.47, fill: b ? '#1d1d1d' : '#f8f8f4', stroke: b ? '#000' : '#444', 'stroke-width': 0.9 }));
      var lab = opt.nums && opt.nums[k];
      if (lab) svg.appendChild(el('text', { x: X(p[0]), y: Y(p[1]) + 4.3, 'font-size': 12, 'font-weight': 'bold', 'text-anchor': 'middle', fill: b ? '#fff' : '#111' }, String(lab)));
      if (opt.last === k) svg.appendChild(el('circle', { cx: X(p[0]), cy: Y(p[1]), r: cell * 0.18, fill: 'none', stroke: b ? '#fff' : '#b3261e', 'stroke-width': 2 })); }
    (opt.marks || []).forEach(function (mk) { svg.appendChild(el('text', { x: X(mk[0]), y: Y(mk[1]) + 4.3, 'font-size': 13, 'font-weight': 'bold', 'text-anchor': 'middle', fill: mk[3] || '#b3261e' }, mk[2])); });
    if (opt.click) { var hit = el('rect', { x: 0, y: 0, width: W, height: H, fill: 'transparent', style: 'cursor:pointer' });
      hit.addEventListener('click', function (ev) { var r = svg.getBoundingClientRect(), sx = W / r.width;
        var gx = Math.round(((ev.clientX - r.left) * sx - m) / cell) + x0, gy = Math.round(((ev.clientY - r.top) * sx - m) / cell) + y0;
        if (gx >= x0 && gx <= x1 && gy >= y0 && gy <= y1) opt.click(gx, gy); });
      svg.appendChild(hit); }
    return [W, H];
  }
  function btn(t) { var b = document.createElement('button'); b.type = 'button'; b.textContent = t;
    b.style.cssText = 'padding:4px 12px;margin:4px 6px 0 0;border-radius:8px;border:1px solid var(--border);background:var(--surface);color:var(--text);cursor:pointer;font:inherit'; return b; }
  function frame(root, cfg, maxw) {
    if (cfg.q) { var h = document.createElement('p'); h.style.margin = '0 0 8px'; h.innerHTML = cfg.q; root.appendChild(h); }
    var svg = el('svg', { xmlns: NS }); svg.setAttribute('style', 'width:100%;max-width:' + maxw + 'px;display:block;margin:0 auto;touch-action:manipulation');
    root.appendChild(svg); var msg = document.createElement('p'); msg.style.cssText = 'margin:8px 0 0;min-height:1.6em;line-height:1.7';
    var bar = document.createElement('div'); bar.style.textAlign = 'center'; root.appendChild(bar); root.appendChild(msg);
    return { svg: svg, msg: msg, bar: bar };
  }
  function maxw(v) { return Math.min(460, Math.round(((v[2] - v[0]) * 30 + 60) * 1.35)); }
  function initProb(root, cfg) {
    root.style.textAlign = 'left'; var f = frame(root, cfg, maxw(cfg.v)), bd, done, nums, timer;
    var who = cfg.p === 'b' ? '黑' : '白';
    function reset() { clearTimeout(timer); bd = new Board(cfg.n).load(cfg.b, cfg.w); done = false; nums = {}; f.msg.innerHTML = '<span style="color:var(--text-muted)">輪到' + who + '下，請點選棋盤。</span>'; render(); }
    function render(last) { draw(f.svg, bd, cfg.v, { nums: nums, last: last, click: done ? null : click }); }
    function playSeq(seq, c, i, after) { var mv = seq.split(' ').filter(Boolean); var j = 0;
      function step() { if (j >= mv.length) { after(); return; } var p = P(mv[j]); var k = K(p[0], p[1]);
        if (mv[j] !== 'pass') { bd.play(p[0], p[1], c); nums[k] = i + j + 1; render(k); } c = opp(c); j++; timer = setTimeout(step, 550); }
      timer = setTimeout(step, 450); }
    function click(x, y) { if (done) return; var k = K(x, y), s = String.fromCharCode(97 + x) + String.fromCharCode(97 + y);
      var test = bd.copy(); if (test.play(x, y, cfg.p) === null) { f.msg.textContent = '這裡不能下（已有棋子、自殺或打劫禁著）。'; return; }
      done = true; bd.play(x, y, cfg.p); nums[k] = 1; render(k);
      var hit = cfg.ok[s] || cfg.ng[s], good = !!cfg.ok[s];
      if (!hit) { f.msg.innerHTML = '❌ ' + cfg.other; return; }
      f.msg.innerHTML = good ? '✅ 正確！<span style="color:var(--text-muted)">（看看後續變化）</span>' : '❌ 不對喔，看看對方怎麼應⋯⋯';
      playSeq(hit[0], opp(cfg.p), 1, function () { f.msg.innerHTML = (good ? '✅ 正確！' : '❌ ') + hit[1]; render(); });
    }
    var r = btn('重來'); r.addEventListener('click', reset); f.bar.appendChild(r);
    var a = btn('看答案'); a.addEventListener('click', function () { reset(); var s = Object.keys(cfg.ok)[0], p = P(s); click(p[0], p[1]); }); f.bar.appendChild(a);
    reset();
  }
  function initReplay(root, cfg) {
    root.style.textAlign = 'left'; var f = frame(root, cfg, maxw(cfg.v)), i = 0;
    function show() { var bd = new Board(cfg.n).load(cfg.b, cfg.w), c = cfg.f, nums = {}, last = null;
      for (var j = 0; j < i; j++) { var mv = cfg.m[j][0]; if (mv !== 'pass') { var p = P(mv), k = K(p[0], p[1]); bd.play(p[0], p[1], c); nums[k] = j + 1; last = k; } c = opp(c); }
      for (var kk in nums) if (!bd.g[kk]) delete nums[kk];
      draw(f.svg, bd, cfg.v, { nums: nums, last: last });
      f.msg.innerHTML = '<b>' + i + ' / ' + cfg.m.length + '</b>　' + (i ? cfg.m[i - 1][1] : '按「下一手」開始。'); }
    var b0 = btn('⏮'), b1 = btn('◀ 上一手'), b2 = btn('下一手 ▶'), b3 = btn('⏭');
    b0.addEventListener('click', function () { i = 0; show(); }); b1.addEventListener('click', function () { if (i > 0) i--; show(); });
    b2.addEventListener('click', function () { if (i < cfg.m.length) i++; show(); }); b3.addEventListener('click', function () { i = cfg.m.length; show(); });
    [b0, b1, b2, b3].forEach(function (b) { f.bar.appendChild(b); }); show();
  }
  function initSand(root, cfg) {
    root.style.textAlign = 'left'; var n = cfg.n, v = [0, 0, n - 1, n - 1], f = frame(root, cfg, maxw(v)), hist, bd, c, caps;
    function reset() { bd = new Board(n).load(cfg.b, cfg.w); c = 'b'; hist = []; caps = { b: 0, w: 0 }; render(); }
    function render(last) { draw(f.svg, bd, v, { last: last, click: click });
      var sc = bd.area();
      f.msg.innerHTML = '輪到：<b>' + (c === 'b' ? '黑' : '白') + '</b>　提子：黑 ' + caps.b + '、白 ' + caps.w +
        '<br><span style="color:var(--text-muted);font-size:0.9em">目前數子（假設盤上沒有死子）：黑 ' + sc.b + '、白 ' + sc.w + '</span>'; }
    function click(x, y) { var snap = bd.copy(), r = bd.play(x, y, c);
      if (r === null) { f.msg.innerHTML += '<br>這裡不能下（已有棋子、自殺或打劫禁著）。'; return; }
      hist.push([snap, c, { b: caps.b, w: caps.w }]); caps[c] += r.length; c = opp(c); render(K(x, y)); }
    var u = btn('悔棋'); u.addEventListener('click', function () { if (!hist.length) return; var h = hist.pop(); bd = h[0]; c = h[1]; caps = h[2]; render(); });
    var p = btn('虛手（pass）'); p.addEventListener('click', function () { hist.push([bd.copy(), c, { b: caps.b, w: caps.w }]); bd.prev = null; c = opp(c); render(); });
    var r = btn('清空'); r.addEventListener('click', reset);
    [u, p, r].forEach(function (b) { f.bar.appendChild(b); }); reset();
  }
  function initCount(root, cfg) {
    root.style.textAlign = 'left'; var n = cfg.n, v = [0, 0, n - 1, n - 1], f = frame(root, cfg, maxw(v));
    var bd = new Board(n).load(cfg.b, cfg.w); draw(f.svg, bd, v, {});
    var box = document.createElement('div'); box.style.cssText = 'text-align:center;margin-top:6px';
    box.innerHTML = '你算黑棋有幾點？ <input type="number" style="width:5em;font:inherit;padding:3px 6px;border-radius:6px;border:1px solid var(--border);background:var(--surface);color:var(--text)">';
    var b = btn('對答案'); box.appendChild(b); f.bar.appendChild(box);
    b.addEventListener('click', function () { var g = parseInt(box.querySelector('input').value, 10), sc = bd.area(), marks = [];
      var seen = {}; for (var x = 0; x < n; x++) for (var y = 0; y < n; y++) { var k = K(x, y); if (bd.g[k]) continue;
        var bor = {}; bd.nb(x, y).forEach(function (q) { var vv = bd.g[K(q[0], q[1])]; if (vv) bor[vv] = 1; }); }
      var tot = n * n, diff = sc.b - (tot / 2), res = sc.b - sc.w - cfg.k;
      f.msg.innerHTML = (g === sc.b ? '✅ 答對了！' : '答案是 <b>' + sc.b + '</b>。') + '黑 ' + sc.b + ' 點、白 ' + sc.w + ' 點（共 ' + tot + ' 點）。' +
        '<br>白貼 ' + cfg.k + ' 目（數子法相當於貼 ' + (cfg.k / 2) + ' 子）：' + (res > 0 ? '黑勝 ' + res + ' 目' : '白勝 ' + (-res) + ' 目') + '。'; });
  }
  function initAll() { var ws = document.querySelectorAll('.go-w'); for (var i = 0; i < ws.length; i++) { var w = ws[i]; if (w.__done) continue; w.__done = 1;
    var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ prob: initProb, replay: initReplay, sand: initSand, count: initCount })[cfg.t](w, cfg); } }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def lesson(title_, desc, goals, body, tip, check, nxt=None):
    blocks = list(body)
    blocks.append(("note", u"💡 下棋時記得", [("p", tip)]))
    if any(isinstance(b, tuple) and b[0] == "raw" and 'class="go-w' in b[1] for b in blocks):
        blocks.insert(0, ("raw", u"<script>%s</script>" % GOLIB))
    return Lesson(title_, desc, goals, blocks, check, nxt)


def LS(n, text=None):
    return u'<a href="lesson-%02d.html">%s</a>' % (n, text or u"第 %d 課" % n)


def C(s, n=19):
    """SGF 座標 → 顯示座標，例如 C('dd') = 'D16'。"""
    x, y = P(s)
    return u"%s%d" % (LETTERS[x], n - y)


def ladder(bd, target, attacker_to_move=True, depth=40):
    """征子讀法：攻方只下在目標的氣上叫吃，守方只長出氣或提掉叫吃自己的子。回傳攻方能否提掉目標。"""
    if bd.g.get(target) is None:
        return True
    tc = bd.g[target]
    att = opp(tc)
    s, libs = bd.group(target)
    if depth == 0:
        return False
    if attacker_to_move:
        if len(libs) == 1:
            return True
        if len(libs) > 2:
            return False
        for m in libs:
            b2 = bd.copy()
            try:
                b2.play(m, att)
            except Illegal:
                continue
            if b2.g.get(target) is None:
                return True
            if b2.libs(target) == 1 and not ladder(b2, target, False, depth - 1):
                continue
            if b2.libs(target) == 1:
                return True
        return False
    # 守方
    cands = list(libs)
    for q in s:
        for r in bd.nb(q):
            if bd.g.get(r) == att and bd.libs(r) == 1:
                cands.extend(bd.group(r)[1])
    for m in set(cands):
        b2 = bd.copy()
        try:
            b2.play(m, tc)
        except Illegal:
            continue
        if b2.g.get(target) is None:
            continue
        n = b2.libs(target)
        if n >= 3:
            return False
        if n == 2 and not ladder(b2, target, True, depth - 1):
            return False
    return True


def ladder_pv(bd, target, maxlen=60):
    """回傳征子的主要變化（SGF 座標字串列表），從攻方先手開始，直到提子或失敗。"""
    seq = []
    b = bd.copy()
    tc = b.g[target]
    att = opp(tc)
    for _ in range(maxlen):
        s, libs = b.group(target)
        mv = None
        for m in sorted(libs):
            b2 = b.copy()
            try:
                b2.play(m, att)
            except Illegal:
                continue
            if b2.g.get(target) is None or (b2.libs(target) == 1 and ladder(b2, target, False)):
                mv = m
                break
        if mv is None:
            break
        b.play(mv, att)
        seq.append(mv)
        if b.g.get(target) is None:
            break
        ext = list(b.group(target)[1])[0]
        b.play(ext, tc)
        seq.append(ext)
    return ["%s%s" % (chr(p[0] + 97), chr(p[1] + 97)) for p in seq]


def enclose(n, eye, extra_b="", extra_w=""):
    """給定眼位（SGF 座標字串），自動產生黑棋外牆（含斜角，保證相連）與白棋包圍。回傳 (b, w)。"""
    E = set(PTS(eye))
    B = set()
    for (x, y) in E:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                q = (x + dx, y + dy)
                if 0 <= q[0] < n and 0 <= q[1] < n and q not in E:
                    B.add(q)
    W = set()
    for (x, y) in B:
        for q in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= q[0] < n and 0 <= q[1] < n and q not in E and q not in B:
                W.add(q)
    f = lambda S: " ".join("%s%s" % (chr(p[0] + 97), chr(p[1] + 97)) for p in sorted(S))
    b = (f(B) + " " + extra_b).strip()
    w = (f(W) + " " + extra_w).strip()
    return b, w


def tac_kill(bd, target, to_move, depth, memo=None):
    """戰術讀法（吃子題用）：攻方候選點＝目標的氣與「氣的氣」；守方候選點＝自己的氣與可提的對方子。
    目標氣數達 4 口以上視為逃出。"""
    if memo is None:
        memo = {}
    tc = bd.g.get(target)
    if tc is None:
        return True
    att = opp(tc)
    s, libs = bd.group(target)
    if len(libs) >= 4:
        return False
    if depth == 0:
        return False
    k = (bd.key(), bd.prev, to_move, depth)
    if k in memo:
        return memo[k]
    if to_move == att:
        if len(libs) == 1:
            memo[k] = True
            return True
        cands = set(libs)
        if len(libs) == 2:
            for l in libs:
                for r in bd.nb(l):
                    if r not in bd.g:
                        cands.add(r)
        res = False
        for m in cands:
            b2 = bd.copy()
            try:
                b2.play(m, att)
            except Illegal:
                continue
            if tac_kill(b2, target, tc, depth - 1, memo):
                res = True
                break
    else:
        cands = set(libs)
        for q in s:
            for r in bd.nb(q):
                if bd.g.get(r) == att and bd.libs(r) == 1:
                    cands |= bd.group(r)[1]
        res = True
        for m in list(cands) + [None]:
            b2 = bd.copy()
            if m is not None:
                try:
                    b2.play(m, tc)
                except Illegal:
                    continue
            if not tac_kill(b2, target, att, depth - 1, memo):
                res = False
                break
    memo[k] = res
    return res


def tac_winners(n, b, w, target, to_move, depth=9, region=None):
    """列出能「提掉 target」（攻方）或「救活 target」（守方）的第一手。"""
    bd = Board(n, b, w)
    t = P(target)
    tc = bd.g[t]
    att = opp(tc)
    if region is None:
        s, libs = bd.group(t)
        region = set(libs)
        for l in libs:
            for r in bd.nb(l):
                if r not in bd.g:
                    region.add(r)
    out = []
    for m in sorted(region):
        b2 = bd.copy()
        try:
            b2.play(m, to_move)
        except Illegal:
            continue
        k = tac_kill(b2, t, opp(to_move), depth)
        if (to_move == att and k) or (to_move != att and not k):
            out.append("%s%s" % (chr(m[0] + 97), chr(m[1] + 97)))
    return out


def _s(p):
    return "%s%s" % (chr(p[0] + 97), chr(p[1] + 97))


def life_problem(n, b, w, region, target, to_move, good, prompt, ok_msg, ng_msg=None, view=None, depth=30):
    """死活題：用 check_life 驗證 good 是唯一（或全部）正解，並自動產生錯解的回應（對方下在第一個正解點）。"""
    check_life(n, b, w, region, target, to_move, good, depth=depth)
    goods = good.split()
    bd = Board(n, b, w)
    correct = {g: ("", ok_msg) for g in goods}
    wrong = {}
    key = goods[0]
    for m in PTS(region):
        sm = _s(m)
        if sm in goods or m in bd.g:
            continue
        b2 = bd.copy()
        try:
            b2.play(m, to_move)
        except Illegal:
            continue
        reply = ""
        b3 = b2.copy()
        try:
            b3.play(P(key), opp(to_move))
            reply = key
        except Illegal:
            pass
        wrong[sm] = (reply, ng_msg or (u"對方搶到要點 %s，結果就反過來了。" % C(key, n)))
    other = u"這一手離開了要緊的地方。死活的關鍵在眼位裡面或旁邊。"
    return problem(n, b, w, to_move, correct, wrong, view=view, prompt=prompt, other=other)
