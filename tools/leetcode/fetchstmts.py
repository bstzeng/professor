# -*- coding: utf-8 -*-
"""一次性工具：把 doocs/leetcode 的原題敘述轉成 stmts/NNNN.json。

用法：python3 fetchstmts.py <doocs 原始 README_EN.md 所在目錄> <sel.json>
"""
import json, os, re, sys
from lcauto import parse, HERE

src, sel = sys.argv[1], json.load(open(sys.argv[2], encoding="utf-8"))
for r in sel:
    num, title, path = r[0], r[1], r[2]
    d = parse(open(os.path.join(src, "%d.md" % num), encoding="utf-8").read())
    m = re.search(r"leetcode\.com/problems/([a-z0-9\-]+)", open(os.path.join(src, "%d.md" % num), encoding="utf-8").read())
    d["slug"] = m.group(1)
    d["title"] = title
    d["difficulty"] = r[4]
    d["tags"] = [t.strip("` ") for t in r[3].split(",")]
    json.dump(d, open(os.path.join(HERE, "stmts", "%04d.json" % num), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(sel), "written")
