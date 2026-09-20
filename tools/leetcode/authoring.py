# -*- coding: utf-8 -*-
"""bodies/NNNN.html 的高階組裝層。

builder.py 負責「一個區塊怎麼變成 HTML」，
authoring.py 負責「一篇題解由哪些區塊、依什麼順序組成」，
讓每一題的原始碼只描述內容，不重複排版。

內容用一個小 DSL 表示，每個元素可以是：
    "字串"                -> <p>字串</p>（收原始 HTML）
    ("c", 純文字)          -> 程式碼區塊（自動跳脫）
    ("h", 標題)            -> <h3>
    ("ul", [...])          -> 項目清單（收原始 HTML）
    ("ol", [...])          -> 編號清單
    ("t", 表頭, 列)        -> 表格
    ("fig", svg, viewBox)  -> 圖
    ("note", 標題, [...])  -> callout（內容一樣吃這個 DSL）
    ("raw", 片段)          -> 已經是 HTML 的區塊，原樣輸出
"""
import builder as B


def blk(x):
    if isinstance(x, tuple):
        kind = x[0]
        if kind == "c":
            return B.code(x[1])
        if kind == "h":
            return B.h3(x[1])
        if kind == "ul":
            return B.ul(x[1])
        if kind == "ol":
            return B.ol(x[1])
        if kind == "t":
            return B.table(x[1], x[2])
        if kind == "fig":
            return B.figure(x[1], x[2])
        if kind == "note":
            return B.callout(x[1], *[blk(i) for i in x[2]])
        if kind == "raw":
            return x[1]
        raise ValueError("unknown block kind: %r" % (kind,))
    return B.p(x)


def blocks(items):
    return [blk(i) for i in items]


def ap(tag, title, items, time=None, space=None,
       tnote="", snote="", optimal=False):
    """一個解法區塊；有給複雜度就自動補上複雜度小表。"""
    parts = blocks(items)
    if time is not None:
        parts.append(B.complexity(time, space, tnote, snote))
    return B.approach(tag, title, parts, optimal)


def emit(spec):
    """把一題的 spec 寫成 bodies/NNNN.html。"""
    P = []
    P.append(B.stmt_en(*spec["en"]))
    P.append(B.stmt_zh(*spec["zh"]))
    P += blocks(spec.get("pre", []))

    P.append(B.h2("範例"))
    P.append(B.code(spec["examples"]))

    P.append(B.h2("限制條件"))
    P.append(B.ul(spec["constraints"]))
    P.append(B.link(spec["num"], spec["slug"]))

    P += blocks(spec.get("mid", []))

    P.append(B.h2("解題思路"))
    P += blocks(spec.get("idea", []))
    P += spec["approaches"]

    if spec.get("compare"):
        P.append(B.h2("解法對照"))
        P.append(B.table(spec["compare"][0], spec["compare"][1]))

    P += blocks(spec.get("post", []))

    P.append(B.h2("邊界條件檢查清單"))
    P.append(B.ul(spec["edges"]))

    P.append(B.h2("常見追問"))
    P += blocks(spec["follow"])

    if spec.get("related"):
        P.append(B.h2("延伸題目"))
        P.append(B.ul(spec["related"]))

    P.append(B.selfcheck(spec["check"]))
    return B.write(spec["num"], P)
