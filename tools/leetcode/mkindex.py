# -*- coding: utf-8 -*-
# 產生 topics/leetcode/index.html，並把主題項目寫進 data/topics.js。
# 這支腳本可以重複執行：data/topics.js 裡已存在的 leetcode 項目會被整個取代，
# 所以之後新增題目時直接再跑一次即可。
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))   # tools/leetcode -> repo 根目錄
sys.path.insert(0, HERE)
import meta

TITLE = u"LeetCode 題解：思路、圖解與 Python 實作"
DESC = (u"一題一頁、持續累積的 LeetCode 解題筆記。每一題都附英文題目敘述與中文翻譯、"
        u"完整的範例與限制條件，再把所有值得知道的解法一個一個拆開講："
        u"從暴力法開始，說明它為什麼慢，再一步步優化到最佳解，需要的地方補上圖解。"
        u"全部用 Python，附複雜度對照表與邊界條件檢查清單。")
TOPICS_JS = os.path.join(REPO, "data", "topics.js")
OUT_DIR = os.path.join(REPO, "topics", "leetcode")

INDEX_BODY = u"""        <header class="lesson-header">
          <div class="eyebrow">LeetCode 題解</div>
          <h1>思路、圖解與 Python 實作</h1>
        </header>

        <div class="callout">
          <h3>這個主題怎麼用</h3>
          <ul>
            <li><strong>左邊是題目列表</strong>，點任何一題就會在這一欄打開完整題解；手機上列表會收到上方。</li>
            <li>每一題的結構固定：英文題目敘述 → 中文翻譯 → 範例與限制 → 所有解法（由慢到快）→ 邊界條件 → 延伸。</li>
            <li>程式碼一律是 Python，可以直接貼進 LeetCode 送出。</li>
            <li>題目依題號累積，之後會持續新增。</li>
          </ul>
        </div>

        <h2>為什麼有些題號跳過了</h2>
        <p>
          LeetCode 的題號裡混了三種不是「Python 演算法題」的題目，這個主題不收：
        </p>
        <ul>
          <li><strong>資料庫題（SQL）</strong>——例如 175–178、180–185、196–197。答案是 SQL 查詢，不是 Python。</li>
          <li><strong>Shell 題</strong>——192–195。答案是 Bash 指令稿。</li>
          <li><strong>付費鎖定題</strong>——例如 156–159、161、163、170、186。沒有訂閱看不到原題，這裡也就無法附上可對照的題目敘述。</li>
        </ul>
        <p>
          除此之外的題目都會依題號補齊。
        </p>

        <h2>關於題目敘述</h2>
        <p>
          每一題的英文敘述是<strong>依照原題規格重寫的版本</strong>，不是從 LeetCode 複製的原文——
          規格、範例與限制條件完全一致，但文字是這裡自己寫的。
          中文則是對照這份英文的翻譯。
          想看官方原文的話，每一題都附了原題連結。
        </p>

        <h2>複雜度速查</h2>
        <p>
          題解裡的複雜度都用這套符號。<code>n</code> 通常是輸入規模（陣列長度、字串長度、節點數）。
        </p>
        <table>
          <thead><tr><th>符號</th><th>意思</th><th>n = 10⁵ 時的量級感</th></tr></thead>
          <tbody>
            <tr><td>O(1)</td><td>常數</td><td>瞬間</td></tr>
            <tr><td>O(log n)</td><td>對數（每次砍一半）</td><td>約 17 步</td></tr>
            <tr><td>O(n)</td><td>線性（掃一遍）</td><td>10 萬步</td></tr>
            <tr><td>O(n log n)</td><td>排序的典型複雜度</td><td>約 170 萬步</td></tr>
            <tr><td>O(n²)</td><td>雙層迴圈</td><td><strong>100 億步 —— 會逾時</strong></td></tr>
            <tr><td>O(2ⁿ)</td><td>指數（枚舉所有子集）</td><td>天文數字</td></tr>
          </tbody>
        </table>
        <p>
          LeetCode 的評測機大約每秒能跑 10⁷ 到 10⁸ 個基本運算。
          看到 <code>n ≤ 10⁵</code> 這種限制，就知道 O(n²) 一定過不了，
          要往 O(n log n) 或 O(n) 想。
        </p>

        <h2>Python 解題的幾個前提</h2>
        <ul>
          <li>LeetCode 的 Python 環境是 CPython 3，可以使用標準函式庫，<code>collections</code>、<code>heapq</code>、<code>bisect</code>、<code>functools</code> 都能直接 import。</li>
          <li>Python 的整數沒有上限，所以在 C++／Java 會溢位的題目在 Python 常常「不小心就過了」——但題解裡會特別指出哪些地方是這樣，因為那通常代表你沒有真的解決題目要考的東西。</li>
          <li>Python 比較慢，同樣的演算法可能在邊界上逾時。題解會標出哪些寫法在 Python 下特別吃虧（例如字串相加、<code>list.pop(0)</code>）。</li>
        </ul>
"""

INDEX_TPL = u"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} ｜ 博雅書院</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="../../css/style.css">
</head>
<body data-topic-id="leetcode">

<header class="site-header">
  <div class="container header-inner">
    <a href="../../index.html" class="brand">🏛 博雅書院</a>
    <nav class="site-nav">
      <a href="../../index.html">首頁</a>
      <a href="../../index.html#topics">主題</a>
    </nav>
  </div>
</header>

<main>
  <div class="container">
    <nav class="breadcrumb">
      <a href="../../index.html">首頁</a>
      <span class="sep">/</span>
      <span>LeetCode 題解</span>
    </nav>

    <div class="lc-layout">
      <aside class="lc-sidebar" id="lc-sidebar"></aside>

      <article class="lc-content lesson-content">
{body}
      </article>
    </div>
  </div>
</main>

<footer class="site-footer">
  <div class="container">
    <p>&copy; <span id="year"></span> 博雅書院</p>
  </div>
</footer>

<script>window.SITE_BASE = "../../";</script>
<script src="../../data/topics.js"></script>
<script src="../../js/leetcode-nav.js"></script>
<script>
  document.getElementById("year").textContent = new Date().getFullYear();
</script>
</body>
</html>
"""


def build_entry():
    L = []
    L.append(u'    {')
    L.append(u'      id: "leetcode",')
    L.append(u'      category: "tech",')
    L.append(u'      title: "%s",' % TITLE)
    L.append(u'      description:')
    L.append(u'        "%s",' % DESC)
    L.append(u'      icon: "\U0001F9E9",')
    L.append(u'      url: "topics/leetcode/index.html",')
    L.append(u'      modules: [')
    mods = []
    for label, ps in meta.grouped():
        b = [u'        {', u'          title: "%s",' % label, u'          courses: [']
        b.append(u',\n'.join(
            u'            { title: "%s", url: "topics/leetcode/%s.html" }'
            % (meta.course_title(p), meta.slug(p)) for p in ps))
        b += [u'          ]', u'        }']
        mods.append(u'\n'.join(b))
    L.append(u',\n'.join(mods))
    L += [u'      ]', u'    }']
    return u'\n'.join(L)


def find_existing(s):
    """找出 data/topics.js 裡既有 leetcode 項目的 [start, end) 範圍；找不到回傳 None。"""
    marker = u'id: "leetcode",'
    i = s.find(marker)
    if i < 0:
        return None
    start = s.rindex(u'    {', 0, i)
    depth = 0
    j = start
    while j < len(s):
        if s[j] == u'{':
            depth += 1
        elif s[j] == u'}':
            depth -= 1
            if depth == 0:
                return (start, j + 1)
        j += 1
    raise RuntimeError("unbalanced braces while locating leetcode entry")


def main():
    if not os.path.isdir(OUT_DIR):
        os.makedirs(OUT_DIR)
    io.open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8").write(
        INDEX_TPL.format(title=TITLE, desc=DESC.replace(u'"', u"&quot;"),
                         body=INDEX_BODY.rstrip("\n")))

    entry = build_entry()
    s = io.open(TOPICS_JS, encoding="utf-8").read()
    span = find_existing(s)
    if span:
        s = s[:span[0]] + entry + s[span[1]:]
        print("topics.js: replaced existing leetcode entry")
    else:
        marker = u"\n  ]\n};"
        assert marker in s
        i = s.rindex(marker)
        s = s[:i] + u",\n" + entry + s[i:]
        print("topics.js: appended leetcode entry")
    io.open(TOPICS_JS, "w", encoding="utf-8").write(s)


main()
