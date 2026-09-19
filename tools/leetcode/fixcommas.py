# -*- coding: utf-8 -*-
"""補上 authoring DSL 清單裡忘記的逗號。

兩種常見的手滑，Python 都會報成「'str'/'tuple' object is not callable」，
而且錯誤行號指向「下一行」，很不好找：

    ("h", "標題")          <- 漏逗號
    "接下來的段落"

    "某個段落"             <- 漏逗號
    ("ul", [...])

這支工具直接把它們補好。
"""
import io, re, sys

TUP = r'\("(?:h|c|ul|ol|t|note|fig|raw)",'
total = 0
for path in sys.argv[1:]:
    src = io.open(path, encoding="utf-8").read()
    out = src
    # 1) tuple 行（單行寫完）後面接字串或 tuple
    out = re.sub(r'(\n( +)' + TUP + r'.*\))\n(?=\2(?:"|\())', r'\1,\n', out)
    # 2) 字串行後面接 tuple 行（字串接字串是合法的隱式串接，不能動）
    out = re.sub(r'(\n( +)".*")\n(?=\2' + TUP + r')', r'\1,\n', out)
    # 3) 多行 tuple 的收尾 ]) 後面接字串或 tuple
    out = re.sub(r'(\n( +)\]\))\n(?=\2(?:"|\())', r'\1,\n', out)
    if out != src:
        n = sum(1 for a, b in zip(src.split("\n"), out.split("\n")) if a != b)
        print("%s: 補了 %d 個逗號" % (path, n))
        io.open(path, "w", encoding="utf-8").write(out)
        total += n
print("total %d" % total)
