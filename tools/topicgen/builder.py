# -*- coding: utf-8 -*-
"""把課程內容的小 DSL 變成和站上手寫頁面一模一樣的 HTML。

散文類的參數（p、li、儲存格、圖說…）收的是**原始 HTML**，
所以可以直接寫 <strong>、<code>；只有 code() 收純文字並自動跳脫。

一個區塊可以是：
    "字串"                      -> <p>字串</p>
    ("h", 標題)                 -> <h2>
    ("p", 段落)                 -> <p>
    ("ul", [...])               -> 項目清單
    ("ol", [...])               -> 編號清單
    ("t", 表頭, 列)             -> 表格
    ("note", 標題, [...])       -> callout（內容一樣吃這個 DSL）
    ("fig", svg, viewBox, 圖說) -> 圖
    ("code", 純文字)            -> 程式碼／純文字區塊（自動跳脫）
    ("raw", 片段)               -> 已經是 HTML，原樣輸出
"""

IND = " " * 6          # <article> 內容的基準縮排


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def attr(s):
    return esc(s).replace('"', "&quot;")


def _ind(text, n):
    pad = " " * n
    return "\n".join(pad + ln if ln.strip() else ln for ln in text.split("\n"))


def p(html, n=6):
    return _ind("<p>\n  %s\n</p>" % html, n)


def h2(html, n=6):
    return " " * n + "<h2>%s</h2>" % html


def h3(html, n=6):
    return " " * n + "<h3>%s</h3>" % html


def ul(items, n=6):
    rows = "\n".join("  <li>%s</li>" % i for i in items)
    return _ind("<ul>\n%s\n</ul>" % rows, n)


def ol(items, n=6):
    rows = "\n".join("  <li>%s</li>" % i for i in items)
    return _ind("<ol>\n%s\n</ol>" % rows, n)


def table(head, rows, n=6):
    th = "".join("<th>%s</th>" % c for c in head)
    body = "\n".join("    <tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r)
                     for r in rows)
    return _ind("<table>\n  <thead>\n    <tr>%s</tr>\n  </thead>\n"
                "  <tbody>\n%s\n  </tbody>\n</table>" % (th, body), n)


def code(text, n=6):
    return " " * n + '<div class="code-block">%s</div>' % esc(text.strip("\n"))


def figure(svg, viewbox, caption, n=6):
    inner = svg.strip("\n")
    out = ['<div class="content-figure">',
           '  <svg class="content-diagram" viewBox="%s" xmlns="http://www.w3.org/2000/svg">' % viewbox,
           inner,
           '  </svg>']
    if caption:
        out.append("  <figcaption>%s</figcaption>" % caption)
    out.append("</div>")
    return _ind("\n".join(out), n)


def callout(title, parts, n=6):
    inner = "\n".join(blk(x, n + 2) for x in parts)
    return (" " * n + '<div class="callout">\n'
            + " " * (n + 2) + "<h3>%s</h3>\n" % title
            + inner + "\n" + " " * n + "</div>")


def selfcheck(items, n=6):
    rows = "\n".join(" " * (n + 4) + "<li>%s</li>" % i for i in items)
    return (" " * n + '<div class="self-check">\n'
            + " " * (n + 2) + "<h3>檢查你的理解</h3>\n"
            + " " * (n + 2) + "<ol>\n" + rows + "\n" + " " * (n + 2) + "</ol>\n"
            + " " * n + "</div>")


def blk(x, n=6):
    if isinstance(x, tuple):
        kind = x[0]
        if kind == "h":
            return h2(x[1], n)
        if kind == "h3":
            return h3(x[1], n)
        if kind == "p":
            return p(x[1], n)
        if kind == "ul":
            return ul(x[1], n)
        if kind == "ol":
            return ol(x[1], n)
        if kind == "t":
            return table(x[1], x[2], n)
        if kind == "code":
            return code(x[1], n)
        if kind == "note":
            return callout(x[1], x[2], n)
        if kind == "fig":
            return figure(x[1], x[2], x[3] if len(x) > 3 else "", n)
        if kind == "raw":
            return _ind(x[1], n)
        raise ValueError("unknown block kind: %r" % (kind,))
    return p(x, n)
