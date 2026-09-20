# -*- coding: utf-8 -*-
"""題解內容的產生輔助工具。

用途：bodies/NNNN.html 是塞進 <article> 的 HTML 片段，裡面有大量程式碼。
手寫 HTML 很容易忘記跳脫 < > &，這個模組把 code() 的跳脫自動化，
其餘 helper 只是把常用結構包起來，保持排版一致。

散文類的參數（p、li、儲存格…）收的是**原始 HTML**，
所以可以直接寫 <strong>、<code>；只有 code() 收的是純文字並自動跳脫。
"""
import io, os

IND = " " * 8   # 片段會被塞進 <article> 裡，統一縮排 8 格


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def code(text):
    """程式碼／純文字區塊。內容會自動跳脫。"""
    return IND + '<div class="code-block">%s</div>' % esc(text.strip("\n"))


def _stmt_inner(paras):
    """paras 裡的元素可以是一段散文（原始 HTML，會被包成 <p>），
    或是 ("blk", html) —— 已經由 authoring 的 DSL 產生好的完整區塊。"""
    out = []
    for x in paras:
        if isinstance(x, tuple) and x and x[0] == "blk":
            h = x[1]
            out.append("\n" + (h if h.startswith(IND) else IND + "  " + h))
        else:
            out.append("\n%s  <p>%s</p>" % (IND, x))
    return "".join(out)


def stmt_en(*paras):
    return (IND + '<div class="lc-statement is-en">\n'
            + IND + '  <h3>Problem</h3>' + _stmt_inner(paras) + "\n" + IND + "</div>")


def stmt_zh(*paras):
    return (IND + '<div class="lc-statement">\n'
            + IND + '  <h3>中文翻譯</h3>' + _stmt_inner(paras) + "\n" + IND + "</div>")


def h2(t):
    return IND + "<h2>%s</h2>" % t


def h3(t):
    return IND + "<h3>%s</h3>" % t


def p(html):
    return IND + "<p>%s</p>" % html


def ul(items):
    return (IND + "<ul>\n"
            + "\n".join(IND + "  <li>%s</li>" % i for i in items)
            + "\n" + IND + "</ul>")


def ol(items):
    return (IND + "<ol>\n"
            + "\n".join(IND + "  <li>%s</li>" % i for i in items)
            + "\n" + IND + "</ol>")


def callout(title, *parts):
    """parts 可以是 HTML 字串，或已經由其他 helper 產生的區塊。"""
    inner = "\n".join(x if x.lstrip().startswith("<") and x.startswith(IND)
                      else IND + "  " + x for x in parts)
    return (IND + '<div class="callout">\n'
            + IND + "  <h3>%s</h3>\n" % title
            + inner + "\n" + IND + "</div>")


def selfcheck(items):
    return (IND + '<div class="self-check">\n'
            + IND + "  <h3>檢查你的理解</h3>\n"
            + IND + "  <ol>\n"
            + "\n".join(IND + "    <li>%s</li>" % i for i in items)
            + "\n" + IND + "  </ol>\n" + IND + "</div>")


def table(headers, rows):
    head = "".join("<th>%s</th>" % h for h in headers)
    body = "\n".join(
        IND + "    <tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>"
        for r in rows)
    return (IND + "<table>\n"
            + IND + "  <thead><tr>%s</tr></thead>\n" % head
            + IND + "  <tbody>\n" + body + "\n" + IND + "  </tbody>\n"
            + IND + "</table>")


def complexity(time, space, tnote="", snote=""):
    return table(["", "複雜度", "說明"],
                 [["時間", time, tnote], ["空間", space, snote]])


def approach(tag, title, parts, optimal=False):
    cls = "lc-approach is-optimal" if optimal else "lc-approach"
    inner = "\n".join(parts)
    return (IND + '<div class="%s">\n' % cls
            + IND + '  <span class="lc-approach-tag">%s</span>\n' % tag
            + IND + "  <h3>%s</h3>\n" % title
            + inner + "\n" + IND + "</div>")


def figure(svg_inner, viewbox):
    return (IND + '<div class="content-figure">\n'
            + IND + '  <svg class="content-diagram" viewBox="%s" '
                    'xmlns="http://www.w3.org/2000/svg">\n' % viewbox
            + svg_inner + "\n"
            + IND + "  </svg>\n" + IND + "</div>")


def link(num, slug):
    return IND + ('<p><a href="https://leetcode.com/problems/%s/" '
                  'target="_blank" rel="noopener">LeetCode 原題</a></p>' % slug)


def write(num, parts):
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "bodies", "%04d.html" % num)
    io.open(out, "w", encoding="utf-8").write("\n\n".join(parts) + "\n")
    return out
