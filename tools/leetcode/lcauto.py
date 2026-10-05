# -*- coding: utf-8 -*-
"""從原題英文敘述（stmts/NNNN.json）自動帶出 en / examples / constraints。

stmts/ 的 JSON 由 fetchstmts.py 一次抓好並放進版本控制，產生頁面時不需要網路。
每題的 cNNN.py 仍然要自己寫中文翻譯、思路與解法；
若自動帶出的範例或限制條件不合適，在 spec 裡直接給同名欄位覆蓋即可。
"""
import html, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SUP = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")


def _sup(s):
    s = re.sub(r"<sup>([0-9\-]+)</sup>", lambda m: m.group(1).translate(SUP), s)
    return s.replace("&lt;=", "≤").replace("&gt;=", "≥").replace("<=", "≤").replace(">=", "≥")


def _text(s):
    s = re.sub(r"<img[^>]*>", "", s)
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s).replace("\xa0", " ")


def _top_blocks(body):
    """切出最外層的 <p>/<ul>/<ol>/<pre>/<div> 區塊（正確處理巢狀清單）。"""
    out, i = [], 0
    pat = re.compile(r"<(p|ul|ol|pre|div)\b[^>]*>")
    while True:
        m = pat.search(body, i)
        gap = body[i:m.start() if m else len(body)].strip()
        if gap and not gap.startswith("<!--"):
            out.append("<p>" + gap + "</p>")       # 沒有被 <p> 包住的散文
        if not m:
            return out
        tag, depth, j = m.group(1), 0, m.start()
        tok = re.compile(r"<(/?)%s\b[^>]*>" % tag)
        for t in tok.finditer(body, m.start()):
            depth += -1 if t.group(1) else 1
            if depth == 0:
                j = t.end()
                break
        out.append(body[m.start():j])
        i = j


def _items(b):
    """清單項目；項目內有巢狀清單時保留原始 HTML。"""
    inner = b[4:-5]
    items, depth, start = [], 0, None
    for t in re.finditer(r"<(/?)(li|ul|ol)\b[^>]*>", inner):
        close, tag = t.group(1), t.group(2)
        if tag == "li" and not close and depth == 0:
            start = t.end()
        if not close:
            depth += 1
        else:
            depth -= 1
        if tag == "li" and close and depth == 0:
            items.append(re.sub(r"\s+", " ", inner[start:t.start()].strip()))
    return items


def parse(md):
    m = re.search(r"<!-- description:start -->(.*?)<!-- description:end -->", md, re.S)
    body = m.group(1)
    body = re.sub(r"<img[^>]*>", "", body)
    body = re.sub(r"<p>\s*(&nbsp;)?\s*</p>", "", body)
    # 依區塊切開
    blocks = _top_blocks(body)
    en, exs, cons, tail = [], [], [], []
    mode = "stmt"
    for b in blocks:
        t = _text(b).strip()
        if re.match(r"<p>\s*<strong[^>]*>\s*Example", b):
            mode = "ex"; continue
        if re.match(r"<p>\s*<strong>\s*Constraints", b):
            mode = "cons"; continue
        if mode == "ex" and b.startswith("<p>") and not b.startswith("<p><strong"):
            # 範例之間偶爾有說明段落，略過
            continue
        if mode == "cons" and b.startswith("<p>"):
            mode = "tail"
        if mode == "stmt":
            if b.startswith("<p>"):
                inner = b[3:-4].strip()
                if inner:
                    en.append(["p", re.sub(r"\s+", " ", inner)])
            elif b.startswith("<pre>"):
                en.append(["c", _text(b[5:-6]).strip("\n")])
            elif b.startswith("<ul>") or b.startswith("<ol>"):
                en.append([b[1:3], _items(b)])
        elif mode == "ex":
            if b.startswith("<pre>"):
                exs.append(_text(b[5:-6]).strip("\n"))
            elif b.startswith("<div"):
                t2 = re.sub(r"\n\s*\n", "\n", _text(b)).strip()
                exs.append(t2)
        elif mode == "cons":
            if b.startswith("<ul>"):
                cons += _items(b)
        elif mode == "tail":
            if b.startswith("<p>"):
                inner = b[3:-4].strip()
                if inner:
                    tail.append(["p", re.sub(r"\s+", " ", inner)])
            elif b.startswith("<ul>") or b.startswith("<ol>"):
                tail.append([b[1:3], _items(b)])
    return {"en": en + tail, "examples": exs, "constraints": cons}


def _ex_zh(exs):
    out = []
    for i, e in enumerate(exs, 1):
        lines = []
        for ln in e.split("\n"):
            s = ln.strip()
            if not s:
                continue
            if re.match(r"(Explanation|Note)\b", s) or (lines and lines[-1] == "  說明"):
                # 原文說明略過（中文說明由各題自行補充）
                if lines and lines[-1] != "  說明":
                    lines.append("  說明")
                continue
            s = re.sub(r"^Input\s*:?\s*", "輸入：", s)
            s = re.sub(r"^Output\s*:?\s*", "輸出：", s)
            s = re.sub(r"：$", "", s)
            lines.append("  " + s)
        lines = [l for l in lines if l != "  說明"]
        out.append(("範例 %d\n" % i if len(exs) > 1 else "範例\n") + "\n".join(lines))
    return "\n\n".join(out)


_C = r"((?:<code>.*?</code>)(?:,? (?:and )?<code>.*?</code>)*)"
_TR = [
    (r"^The number of (?:the )?nodes in (?:the )?(?:tree|list|both trees)(?: will be| is)? in the range " + _C + r"\.?$", r"節點數在 \1 範圍內"),
    (r"^The number of nodes in the " + _C + r" tree is in the range " + _C + r"\.?$", r"\1 樹的節點數在 \2 範圍內"),
    (r"^The total number of nodes is in the range " + _C + r"\.?$", r"節點總數在 \1 範圍內"),
    (r"^" + _C + r" (?:consists?|consist) of (?:only )?(?:lowercase|lower-case|lower case) (?:English )?letters(?: only)?\.?$", r"\1 只含小寫英文字母"),
    (r"^" + _C + r" (?:consists only|consist only) of (?:lowercase|lower-case) (?:English )?letters\.?$", r"\1 只含小寫英文字母"),
    (r"^" + _C + r" is (?:either )?" + r"(.*)\.$", None),
    (r"^At most " + _C + r" calls will be made to " + r"(.*?)\.?$", r"最多呼叫 \1 次（\2）"),
    (r"^All the (?:values|elements|integers|strings|words|characters) (?:of|in) " + _C + r" are <strong>(?:unique|distinct)</strong>\.?$", r"\1 中的元素互不相同"),
    (r"^All the values in the tree are <strong>unique</strong>\.?$", r"樹中所有節點值互不相同"),
    (r"^" + _C + r" is guaranteed to be a (?:<strong>)?valid(?:</strong>)? binary search tree\.?$", r"\1 保證是合法的二元搜尋樹"),
    (r"^" + _C + r" is sorted in (?:<strong>)?(?:non-decreasing|ascending)(?: order)?(?:</strong>)?(?: order)?\.?$", r"\1 已依非遞減順序排序"),
    (r"^" + _C + r" (?:does not contain any|does not have) leading or trailing spaces\.?$", r"\1 開頭與結尾沒有空白"),
    (r"^" + _C + r" consists of only digits\.?$", r"\1 只含數字"),
    (r"^" + _C + r" (?:consists?|consist) of (?:only )?English letters\.?$", r"\1 只含英文字母"),
    (r"^" + _C + r" consists of printable (?:<strong>)?ASCII(?:</strong>)? characters\.?$", r"\1 由可列印的 ASCII 字元組成"),
    (r"^The depth of the (?:n-ary )?tree (?:is less than or equal to|will not exceed) " + _C + r"\.?$", r"樹的深度不超過 \1"),
    (r"^The height of the n-ary tree is less than or equal to " + _C + r"\.?$", r"樹高不超過 \1"),
    (r"^The depth of the tree (?:will be |is )?in the range " + _C + r"\.?$", r"樹的深度在 \1 範圍內"),
    (r"^Each value " + _C + r" is <strong>unique</strong>\.?$", r"每個 \1 互不相同"),
    (r"^" + _C + r" is a lowercase English letter\.?$", r"\1 是小寫英文字母"),
    (r"^" + _C + r" is an uppercase English letter\.?$", r"\1 是大寫英文字母"),
    (r"^The answer is guaranteed to fit (?:inside|in) a (?:<strong>)?32-bit(?:</strong>)? integer\.?$", r"答案保證在 32 位元整數範圍內"),
]


def _con(c):
    c = _sup(c).replace("&nbsp;", " ")
    for pat, rep in _TR:
        if rep is None:
            continue
        m = re.match(pat, c)
        if m:
            return re.sub(pat, rep, c)
    return c


def load(num):
    return json.load(open(os.path.join(HERE, "stmts", "%04d.json" % num), encoding="utf-8"))


def en_items(d):
    out = []
    for kind, v in d["en"]:
        if kind == "p":
            out.append(v)
        elif kind == "c":
            out.append(("c", v))
        else:
            out.append((kind, v))
    return out


def auto(num, **spec):
    """回傳一個可以直接交給 emit() 的 spec：缺的欄位由原題補上。"""
    d = load(num)
    base = {"num": num, "slug": d["slug"], "en": en_items(d),
            "examples": _ex_zh(d["examples"]),
            "constraints": [_con(c) for c in d["constraints"]]}
    base.update(spec)
    return base


TAGS = {
    "Array": "陣列", "String": "字串", "Hash Table": "雜湊表", "Depth-First Search": "深度優先搜尋", "Math": "數學",
    "Dynamic Programming": "動態規劃", "Tree": "樹", "Sorting": "排序", "Breadth-First Search": "廣度優先搜尋",
    "Binary Tree": "二元樹", "Greedy": "貪心", "Two Pointers": "雙指標", "Binary Search": "二分搜尋", "Stack": "堆疊",
    "Design": "設計", "Heap (Priority Queue)": "堆積（優先佇列）", "Matrix": "矩陣", "Bit Manipulation": "位元運算",
    "Binary Search Tree": "二元搜尋樹", "Prefix Sum": "前綴和", "Simulation": "模擬", "Sliding Window": "滑動視窗",
    "Backtracking": "回溯", "Union Find": "聯合查找", "Monotonic Stack": "單調堆疊", "Memoization": "記憶化搜尋",
    "Graph": "圖", "Linked List": "鏈結串列", "Trie": "字典樹", "Segment Tree": "線段樹", "Hash Function": "雜湊函數",
    "Ordered Set": "有序集合", "Recursion": "遞迴", "Bitmask": "位元遮罩", "Counting": "計數", "Randomized": "隨機化",
    "Divide and Conquer": "分治", "Queue": "佇列", "String Matching": "字串匹配", "Geometry": "幾何",
    "Reservoir Sampling": "水塘抽樣", "Counting Sort": "計數排序", "Binary Indexed Tree": "樹狀陣列",
    "Bucket Sort": "桶排序", "Data Stream": "資料流", "Rolling Hash": "滾動雜湊", "Shortest Path": "最短路徑",
    "Eulerian Circuit": "歐拉迴路", "Number Theory": "數論", "Combinatorics": "組合數學", "Game Theory": "博弈",
    "Topological Sort": "拓撲排序", "Enumeration": "列舉", "Brainteaser": "腦筋急轉彎", "Probability and Statistics": "機率與統計",
    "Rejection Sampling": "拒絕抽樣", "Doubly-Linked List": "雙向鏈結串列", "Quickselect": "快速選擇",
    "Merge Sort": "合併排序", "Line Sweep": "掃描線", "Monotonic Queue": "單調佇列", "Iterator": "迭代器",
}


def em(spec):
    """emit() 並記下這題要寫進 meta.py 的資料（_meta/NNNN.json）。"""
    from authoring import emit
    num = spec["num"]
    d = load(num)
    tags = spec.pop("tags", None) or [TAGS[t] for t in d["tags"] if t in TAGS][:4]
    m = {"num": num, "en": d["title"], "zh": spec.pop("title"), "difficulty": d["difficulty"],
         "tags": tags, "desc": spec.pop("desc")}
    os.makedirs(os.path.join(HERE, "stmts", "_meta"), exist_ok=True)
    json.dump(m, open(os.path.join(HERE, "stmts", "_meta", "%04d.json" % num), "w", encoding="utf-8"), ensure_ascii=False)
    spec.pop("num")
    return emit(auto(num, **spec))
