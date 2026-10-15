# -*- coding: utf-8 -*-
"""〈論語〉（ly_）共用：章句區塊、課程包裝與 LYLIB 互動元件。

章句：Z(篇名, 原文, 白話) 產生原文＋白話的區塊，並登記到 ALL 供名句搜尋使用。
LYLIB 元件（class="ly-w"）：
  tog     原文／白話切換（有章句的課自動插入）
  pian    二十篇索引
  views   一章多解
  quiz    成語與名句測驗
  search  名句搜尋
"""
from cc_common import make_lesson, wdg, LS
from qt_common import BASEJS
from nv_common import NVLIB, nvw, ev, card, CB, CG, CO, CR, CP, CT, CY, CK

LY_NOTE = (u"原文以通行的朱熹《四書章句集注》本為準，白話為本站的意譯；《論語》許多章句歷來有不同的解讀，課文會盡量說明主要的分歧。"
           u"章句只標篇名，不標章次，因為各家分章不同。")

ALL = []
_CUR = [0]


def Z(pian, text, bh, note=None):
    """一則章句：原文、白話、出處。"""
    ALL.append([pian, text, bh, 0])
    h = (u'<div class="ly-z" style="border-left:4px solid #b8862b;padding:8px 12px;margin:12px 0;background:var(--accent-soft);border-radius:6px">'
         u'<div style="font-size:1.08em;line-height:1.95;letter-spacing:0.02em">%s</div>'
         u'<div class="ly-bh" style="margin-top:6px;line-height:1.75"><span style="color:var(--text-muted);font-size:0.88em">白話　</span>%s</div>'
         % (text, bh))
    if note:
        h += u'<div class="ly-bh" style="margin-top:4px;font-size:0.9em;color:var(--text-muted)">%s</div>' % note
    h += u'<div style="font-size:0.8em;color:var(--text-muted);text-align:right">——〈%s〉</div></div>' % pian
    return ("raw", h)


def W(rows):
    """字詞表：[[字詞, 讀音, 解釋], ...]"""
    return ("t", [u"字詞", u"讀音", u"解釋"], rows)


LYLIB = r"""
(function () {
  if (window.__lyLib) return; window.__lyLib = 1;
""" + BASEJS + r"""
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div'); root.appendChild(b); return b; }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;'); }

  function initTog(root, cfg) { var bb = bar(root), on = true;
    var b1 = btn('原文＋白話', 'a'), b2 = btn('只看原文（自己先試著讀懂）', 'b');
    function set(v) { on = v; mark(bb, v ? 'a' : 'b'); document.querySelectorAll('.ly-bh').forEach(function (e) { e.style.display = v ? '' : 'none'; }); }
    b1.addEventListener('click', function () { set(true); }); b2.addEventListener('click', function () { set(false); }); bb.appendChild(b1); bb.appendChild(b2); set(true); }

  function initPian(root, cfg) { head(root, cfg.q); var P = cfg.p, cur = 0, bb = bar(root), out = el('div', 'margin-top:8px');
    P.forEach(function (x, i) { var b = btn((i + 1) + '.' + x[0], 'p' + i); b.addEventListener('click', function () { cur = i; mark(bb, 'p' + i); draw(); }); bb.appendChild(b); });
    root.appendChild(out);
    function draw() { var x = P[cur]; out.innerHTML = '<div style="padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.8"><b style="font-size:1.1em">第 ' + (cur + 1) + ' 篇〈' + x[0] + '〉</b>　<span style="color:var(--text-muted);font-size:0.9em">' + x[1] + '</span><br>' + x[2] +
      '<ul style="margin:6px 0 0;padding-left:20px">' + x[3].map(function (q) { return '<li>' + q + '</li>'; }).join('') + '</ul></div>'; }
    mark(bb, 'p0'); draw(); }

  function initViews(root, cfg) { head(root, cfg.q); var V = cfg.v, cur = 0, top = el('div', 'font-size:1.15em;line-height:1.9;padding:8px 12px;border-left:4px solid #b8862b;margin:6px 0', cfg.text), bb, p;
    root.appendChild(top); bb = bar(root); p = info(root);
    V.forEach(function (v, i) { var b = btn(v[0], 'v' + i); b.addEventListener('click', function () { cur = i; mark(bb, 'v' + i); draw(); }); bb.appendChild(b); });
    function draw() { var v = V[cur]; p.innerHTML = '<b>' + v[0] + '</b><br>讀法：' + v[1] + '<br><span style="color:var(--text-muted)">' + v[2] + '</span>'; }
    mark(bb, 'v0'); draw(); }

  function initQuiz(root, cfg) { head(root, cfg.q); var Q = cfg.items, i = 0, score = 0, done = false, box = el('div', 'margin-top:6px'), p;
    root.appendChild(box); p = info(root);
    function draw() { var q0 = Q[i], ord = q0[1].map(function (_, k) { return k; }); done = false;
      for (var s = ord.length - 1; s > 0; s--) { var r = Math.floor(Math.random() * (s + 1)), t = ord[s]; ord[s] = ord[r]; ord[r] = t; }
      var q = [q0[0], ord.map(function (k) { return q0[1][k]; }), ord.indexOf(q0[2]), q0[3]];
      box.innerHTML = '<div style="font-size:0.85em;color:var(--text-muted)">第 ' + (i + 1) + ' / ' + Q.length + ' 題　答對 ' + score + ' 題</div><div style="font-weight:bold;margin:6px 0">' + q[0] + '</div>';
      q[1].forEach(function (o, k) { var b = btn(o, 'o' + k); b.style.display = 'block'; b.style.width = '100%'; b.style.textAlign = 'left';
        b.addEventListener('click', function () { if (done) return; done = true; var ok = k === q[2]; if (ok) score++;
          box.querySelectorAll('button').forEach(function (x, j) { if (j === q[2]) x.style.background = '#cfe8d0'; else if (j === k) x.style.background = '#f4cccc'; });
          p.innerHTML = (ok ? '✅ 答對了！' : '❌ 正確答案是：' + esc(q[1][q[2]])) + '<br>' + q[3];
          var n = btn(i + 1 < Q.length ? '下一題 →' : '重新開始', 'n'); n.addEventListener('click', function () { if (i + 1 < Q.length) i++; else { i = 0; score = 0; } p.innerHTML = '選一個答案。'; draw(); }); p.appendChild(el('div', 'margin-top:6px')).appendChild(n); });
        box.appendChild(b); }); }
    p.innerHTML = '選一個答案。'; draw(); }

  function initSearch(root, cfg) { head(root, cfg.q); var A = cfg.a, inp = document.createElement('input'), out = el('div', 'margin-top:8px;max-height:520px;overflow-y:auto');
    inp.type = 'search'; inp.placeholder = '輸入關鍵字，例如：學、仁、君子、朋友、孝'; inp.style.cssText = 'width:100%;box-sizing:border-box;padding:8px 10px;border-radius:8px;border:1px solid var(--border);background:var(--surface);color:var(--text);font:inherit';
    root.appendChild(inp); root.appendChild(out);
    function draw() { var k = inp.value.trim(), r = A.filter(function (a) { return !k || a[1].indexOf(k) >= 0 || a[2].indexOf(k) >= 0 || a[0].indexOf(k) >= 0; });
      out.innerHTML = '<div style="font-size:0.85em;color:var(--text-muted)">共 ' + r.length + ' 則' + (k ? '（關鍵字「' + esc(k) + '」）' : '') + '</div>' + r.slice(0, 120).map(function (a) {
        var t = esc(a[1]); if (k) t = t.split(esc(k)).join('<mark>' + esc(k) + '</mark>');
        return '<div style="border-bottom:1px solid var(--border);padding:6px 2px;line-height:1.7">' + t + '<div style="font-size:0.82em;color:var(--text-muted)">〈' + a[0] + '〉　<a href="lesson-' + (a[3] < 10 ? '0' : '') + a[3] + '.html">第 ' + a[3] + ' 課</a></div></div>'; }).join('') + (r.length > 120 ? '<div style="color:var(--text-muted)">……只顯示前 120 則，請再縮小關鍵字</div>' : ''); }
    inp.addEventListener('input', draw); draw(); }

  function initAll() { document.querySelectorAll('.ly-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ tog: initTog, pian: initPian, views: initViews, quiz: initQuiz, search: initSearch })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def lyw(cfg, maxw=720):
    return wdg("ly-w", cfg, maxw)


TOG = lyw({"t": "tog"})


def VIEWS(q, text, views):
    return lyw({"t": "views", "q": q, "text": text, "v": views})


def QUIZ(q, items):
    return lyw({"t": "quiz", "q": q, "items": items})


def make(icon, note):
    base = make_lesson(icon, note, LYLIB, "ly-w")

    def lesson(title_, desc, goals, body, point, check, nxt=None):
        _CUR[0] += 1
        for a in ALL:
            if a[3] == 0:
                a[3] = _CUR[0]
        body = list(body)
        if any(isinstance(b, tuple) and b[0] == "raw" and 'class="ly-z' in b[1] for b in body):
            body.insert(0, TOG)
        L = base(title_, desc, goals, body, point, check, nxt)
        if any(isinstance(b, tuple) and b[0] == "raw" and 'class="nv-w' in b[1] for b in L.body):
            L.body.insert(0, ("raw", u"<script>%s</script>" % NVLIB))
        return L
    return lesson
