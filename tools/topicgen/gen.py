# -*- coding: utf-8 -*-
"""依主題規格產生 topics/<id>/ 底下的索引頁與所有課程頁，並同步 data/topics.js。

用法：
    python3 gen.py topic_re
    python3 gen.py topic_sh

規格模組要提供：
    TOPIC = {"id","category","title","short","description","icon","crumb"}
    MODULES = [(模組標題, [Lesson, ...]), ...]
"""
import io, os, sys, json, importlib
import builder as B

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))


class Lesson(object):
    """一課的內容。body 吃 builder 的 DSL；goals/check 是純 HTML 字串清單。"""

    def __init__(self, title, desc, goals, body, check, nxt=None):
        self.title = title
        self.desc = desc
        self.goals = goals
        self.body = body
        self.check = check
        self.nxt = nxt          # 下一課預告；None 代表用預設語句


PAGE = u"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="../../css/style.css">
</head>
<body{bodyattr}>

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
{body}
  </div>
</main>

<footer class="site-footer">
  <div class="container">
    <p>&copy; <span id="year"></span> 博雅書院</p>
  </div>
</footer>

{scripts}
</body>
</html>
"""

INDEX_BODY = u"""    <nav class="breadcrumb">
      <a href="../../index.html">首頁</a>
      <span class="sep">/</span>
      <span>{crumb}</span>
    </nav>

    <section class="topic-hero">
      <h1 id="topic-title">{title}</h1>
      <p id="topic-description"></p>
    </section>

    <section id="modules-container">
      <!-- 由 js/topic.js 依據 data/topics.js 動態產生模組與課程列表 -->
    </section>"""

INDEX_SCRIPTS = u"""<script>window.SITE_BASE = "../../";</script>
<script src="../../data/topics.js"></script>
<script src="../../js/topic.js"></script>
<script>document.getElementById("year").textContent = new Date().getFullYear();</script>"""

LESSON_SCRIPTS = u"""<script>
  document.getElementById("year").textContent = new Date().getFullYear();
</script>"""


def lesson_html(spec, mod_title, num, lesson, prev_l, next_l):
    parts = [B.callout(u"這一課的目標", [(u"ul", lesson.goals)])]
    parts += [B.blk(x) for x in lesson.body]
    parts.append(B.selfcheck(lesson.check))
    if lesson.nxt is not False:
        parts.append(B.h2(u"下一課預告"))
        if lesson.nxt:
            parts.append(B.p(lesson.nxt))
        elif next_l:
            parts.append(B.p(u"下一課：<strong>%s</strong>。" % next_l[1].title))
        else:
            parts.append(B.p(u"這是這門課的最後一課。"))

    prev_html = (u'<a href="lesson-%02d.html">← 上一課：%s</a>' % (prev_l[0], prev_l[1].title)
                 if prev_l else u'<span class="disabled">← 上一課</span>')
    next_html = (u'<a href="lesson-%02d.html">下一課：%s →</a>' % (next_l[0], next_l[1].title)
                 if next_l else u'<span class="disabled">下一課 →</span>')

    body = u"""    <nav class="breadcrumb">
      <a href="../../index.html">首頁</a>
      <span class="sep">/</span>
      <a href="index.html">{crumb}</a>
      <span class="sep">/</span>
      <span>第 {num} 課</span>
    </nav>

    <header class="lesson-header">
      <div class="eyebrow">{mod} · 第 {num} 課</div>
      <h1>{title}</h1>
    </header>

    <article class="lesson-content">

{parts}

    </article>

    <nav class="lesson-nav">
      {prev}
      <a href="index.html">回主題頁</a>
      {next}
    </nav>""".format(crumb=spec.TOPIC["crumb"], num=num, mod=B.esc(mod_title),
                     title=B.esc(lesson.title), parts="\n\n".join(parts),
                     prev=prev_html, next=next_html)

    return PAGE.format(
        title=u"第 %d 課：%s ｜ %s ｜ 博雅書院" % (num, B.esc(lesson.title), spec.TOPIC["short"]),
        desc=B.attr(lesson.desc), bodyattr="", body=body, scripts=LESSON_SCRIPTS)


def topics_entry(spec, flat):
    """產生 data/topics.js 裡的主題物件（字串），格式比照檔案既有風格。"""
    t = spec.TOPIC
    L = [u"    {",
         u'      id: "%s",' % t["id"],
         u'      category: "%s",' % t["category"],
         u'      title: "%s",' % t["title"],
         u"      description:",
         u"        %s," % json.dumps(t["description"], ensure_ascii=False),
         u'      icon: "%s",' % t["icon"],
         u'      url: "topics/%s/index.html",' % t["id"],
         u"      modules: ["]
    n = 0
    mods = []
    for mod_title, lessons in spec.MODULES:
        rows = []
        for ls in lessons:
            n += 1
            rows.append(u'            { title: %s, url: "topics/%s/lesson-%02d.html" },'
                        % (json.dumps(ls.title, ensure_ascii=False), t["id"], n))
        mods.append(u"        {\n          title: %s,\n          courses: [\n%s\n          ],\n        },"
                    % (json.dumps(mod_title, ensure_ascii=False), "\n".join(rows)))
    L.append("\n".join(mods))
    L += [u"      ],", u"    }"]
    return "\n".join(L)


def _block_end(src, start):
    """從 src[start] 的 '{' 開始做大括號配對，回傳對應 '}' 的索引（含）。
    會跳過字串常值裡的括號。"""
    depth, i, n = 0, start, len(src)
    while i < n:
        c = src[i]
        if c == '"':
            i += 1
            while i < n and src[i] != '"':
                i += 2 if src[i] == "\\" else 1
        elif c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    raise ValueError("unbalanced braces from %d" % start)


def inject_topics_js(entry, topic_id):
    """entry 結尾不帶逗號（'    }'）。取代既有條目，或附加到 topics 陣列最後。"""
    path = os.path.join(REPO, "data", "topics.js")
    src = io.open(path, encoding="utf-8").read()
    marker = u'      id: "%s",' % topic_id
    if marker in src:
        i = src.index(marker)
        start = src.rindex(u"\n    {", 0, i) + 1
        end = _block_end(src, start)
        tail = src[end + 1:]
        if tail.startswith(","):            # 保留原本有沒有逗號
            end += 1
            entry += ","
        src = src[:start] + entry + src[end + 1:]
        note = "replaced"
    else:
        anchor = u"\n  ]\n};"
        idx = src.rindex(anchor)
        head = src[:idx].rstrip()
        if head.endswith("}"):              # 前一個條目要補上逗號
            head += ","
        src = head + "\n" + entry + src[idx:]
        note = "appended"
    io.open(path, "w", encoding="utf-8").write(src)
    return note


def build(modname):
    spec = importlib.import_module(modname)
    t = spec.TOPIC
    out = os.path.join(REPO, "topics", t["id"])
    if not os.path.isdir(out):
        os.makedirs(out)

    flat = []
    for mod_title, lessons in spec.MODULES:
        for ls in lessons:
            flat.append((mod_title, ls))

    for i, (mod_title, ls) in enumerate(flat):
        num = i + 1
        prev_l = (i, flat[i - 1][1]) if i > 0 else None
        next_l = (num + 1, flat[i + 1][1]) if i + 1 < len(flat) else None
        html = lesson_html(spec, mod_title, num, ls, prev_l, next_l)
        io.open(os.path.join(out, "lesson-%02d.html" % num), "w", encoding="utf-8").write(html)

    idx = PAGE.format(title=u"%s ｜ 博雅書院" % B.esc(t["title"]),
                      desc=B.attr(t["description"]),
                      bodyattr=u' data-topic-id="%s"' % t["id"],
                      body=INDEX_BODY.format(crumb=t["crumb"], title=B.esc(t["title"])),
                      scripts=INDEX_SCRIPTS)
    io.open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(idx)

    note = inject_topics_js(topics_entry(spec, flat), t["id"])
    print("%s: %d lessons written, topics.js %s" % (t["id"], len(flat), note))


if __name__ == "__main__":
    build(sys.argv[1])
