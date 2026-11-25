# -*- coding: utf-8 -*-
"""工程與理科十二門課（kca、kcg、kcv、kds、kmt、kdc、kth、kwt、kmd、kop、kol、kpb）共用的工具。
每門課用 lib(cls, js, names) 建立自己的互動元件庫。"""
from cc_common import make_lesson, wdg, LS, M, D  # noqa: F401
from qt_common import BASEJS

KX_NOTE = u"本課的數字多為教學用的簡化例子；互動元件是示意模型，實際的設計與計算請以專業文件與標準為準。"

HELP = r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5', TL = '#2a9d8f', YL = '#c9a227';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }
  function small(s) { return '<br><span style="font-size:0.88em;color:var(--text-muted)">' + s + '</span>'; }
  function presets(root, list, cb, k0) { var b = bar(root); list.forEach(function (o, i) { var x = btn(o, i); x.onclick = function () { mark(b, i); cb(i); }; b.appendChild(x); }); mark(b, k0 === undefined ? 0 : k0); return b; }
  function setS(root, k, v) { var s = root.querySelector('input[data-k="' + k + '"]'); if (s) s.value = v; }
  function rc(x, y, w, h, f, st, rx) { return '<rect x="' + n1(x) + '" y="' + n1(y) + '" width="' + n1(Math.max(w, 0)) + '" height="' + n1(Math.max(h, 0)) + '" rx="' + (rx === undefined ? 4 : rx) + '" fill="' + f + '"' + (st ? ' stroke="' + st + '"' : '') + '/>'; }
  function ci(x, y, r, f, st, sw) { return '<circle cx="' + n1(x) + '" cy="' + n1(y) + '" r="' + n1(r) + '" fill="' + f + '"' + (st ? ' stroke="' + st + '" stroke-width="' + (sw || 1.5) + '"' : '') + '/>'; }
  function pa(d, c, w, f, ex) { return '<path d="' + d + '" fill="' + (f || 'none') + '" stroke="' + c + '" stroke-width="' + (w || 1.5) + '" ' + (ex || '') + '/>'; }
  function poly(pts) { return pts.map(function (p, i) { return (i ? 'L' : 'M') + n1(p[0]) + ' ' + n1(p[1]); }).join(' '); }
  function tbl(h, rows) { var s = '<table style="border-collapse:collapse;width:100%;font-size:0.86em;margin-top:6px"><tr>' + h.map(function (x) { return '<th style="border:1px solid var(--border);padding:3px 5px;background:var(--accent-soft)">' + x + '</th>'; }).join('') + '</tr>';
    rows.forEach(function (r) { s += '<tr>' + r.map(function (c, j) { return '<td style="border:1px solid var(--border);padding:3px 5px;text-align:' + (j ? 'center' : 'left') + '">' + c + '</td>'; }).join('') + '</tr>'; }); return s + '</table>'; }
  function rng(seed) { var s = seed || 1; return function () { s = (s * 1103515245 + 12345) % 2147483648; return s / 2147483648; }; }
  function gauss(r) { var u = Math.max(r(), 1e-9), v = r(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); }
  function pct(v) { return f1(v * 100) + '%'; }
  function clamp(v, a, b) { return Math.max(a, Math.min(b, v)); }
"""


def lib(cls, flag, js, names):
    """組出元件庫：js 內定義 init 函式；names 為 {型別: 函式名}。"""
    reg = u", ".join(u"%s: %s" % (k, v) for k, v in names.items())
    return (u"\n(function () {\n  if (window.%s) return; window.%s = 1;\n" % (flag, flag) + BASEJS + HELP + js +
            u"\n  function initAll() { document.querySelectorAll('.%s').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));\n"
            u"    ({ %s })[cfg.t](w, cfg); }); }\n"
            u"  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();\n})();\n" % (cls, reg))


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def kit(icon, cls, js, note=None):
    """回傳 (lesson, widget)。"""
    lesson = make_lesson(icon, note or KX_NOTE, js, cls)

    def w(cfg, maxw=680):
        return wdg(cls, cfg, maxw)
    return lesson, w


def guide(title, h1, items, js, desc):
    body = [("raw", u"<script>%s</script>" % js)]
    for i, (h, w) in enumerate(items):
        body += [("h", u"%d. %s" % (i + 1, h)), w]
    return {"file": "guide.html", "title": title, "h1": h1, "icon": u"🧪", "description": desc, "body": body}


def table(title, h1, desc, sections):
    body = []
    for h, head_, rows in sections:
        body += [("h", h), ("t", head_, rows)]
    return {"file": "table.html", "title": title, "h1": h1, "icon": u"📋", "description": desc, "body": body}
