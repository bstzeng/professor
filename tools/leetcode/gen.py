# -*- coding: utf-8 -*-
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))   # tools/leetcode -> repo 根目錄
sys.path.insert(0, HERE)
import meta

OUT = os.path.join(REPO, "topics", "leetcode")
BODY = os.path.join(HERE, "bodies")

TPL = u"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{num}. {en} {zh} ｜ LeetCode 題解 ｜ 博雅書院</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="../../css/style.css">
</head>
<body data-topic-id="leetcode" data-problem="{num}">

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
      <a href="index.html">LeetCode 題解</a>
      <span class="sep">/</span>
      <span>第 {num} 題</span>
    </nav>

    <div class="lc-layout">
      <aside class="lc-sidebar" id="lc-sidebar"></aside>

      <article class="lc-content lesson-content">
        <header class="lesson-header">
          <div class="eyebrow">LeetCode {num}</div>
          <h1>{en}<br>{zh}</h1>
        </header>

        <div class="lc-meta">
          <span class="lc-badge {diffclass}">{diff_en} · {diff_zh}</span>
{tagspans}
        </div>

{body}

        <nav class="lesson-nav">
{nav}
        </nav>
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


def main():
    if not os.path.isdir(OUT):
        os.makedirs(OUT)
    ps = sorted(meta.PROBLEMS, key=lambda x: x["num"])
    for i, p in enumerate(ps):
        src = os.path.join(BODY, "%04d.html" % p["num"])
        body = io.open(src, encoding="utf-8").read().rstrip("\n")

        nav = []
        if i > 0:
            prev = ps[i - 1]
            nav.append(u'          <a href="%s.html">← 上一題：%d. %s</a>'
                       % (meta.slug(prev), prev["num"], prev["zh"]))
        else:
            nav.append(u'          <a href="index.html">回題目總覽</a>')
        if i < len(ps) - 1:
            nxt = ps[i + 1]
            nav.append(u'          <a href="%s.html">下一題：%d. %s →</a>'
                       % (meta.slug(nxt), nxt["num"], nxt["zh"]))
        else:
            nav.append(u'          <a href="index.html">回題目總覽</a>')

        tagspans = u"\n".join(
            u'          <span class="lc-badge">%s</span>' % t for t in p["tags"]
        )

        html = TPL.format(
            num=p["num"], en=p["en"], zh=p["zh"],
            desc=p["desc"].replace(u'"', u"&quot;"),
            diff_en=p["difficulty"],
            diff_zh=meta.DIFFICULTY_ZH[p["difficulty"]],
            diffclass=p["difficulty"].lower(),
            tagspans=tagspans,
            body=body,
            nav=u"\n".join(nav),
        )
        io.open(os.path.join(OUT, meta.slug(p) + ".html"), "w",
                encoding="utf-8").write(html)
    print("generated %d problems" % len(ps))


main()
