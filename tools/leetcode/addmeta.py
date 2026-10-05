# -*- coding: utf-8 -*-
"""把 stmts/_meta/*.json 併入 meta.py 的 PROBLEMS（已存在的題號會被取代）。"""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "meta.py"), encoding="utf-8").read()
import meta
have = {p["num"] for p in meta.PROBLEMS}
d = os.path.join(HERE, "stmts", "_meta")
new = [json.load(open(os.path.join(d, f), encoding="utf-8")) for f in sorted(os.listdir(d))]
new = [m for m in new if m["num"] not in have]
def fmt(m):
    return ('    {\n        "num": %d,\n        "en": %s,\n        "zh": %s,\n        "difficulty": "%s",\n        "tags": %s,\n        "desc": %s,\n    },\n'
            % (m["num"], json.dumps(m["en"], ensure_ascii=False), json.dumps(m["zh"], ensure_ascii=False), m["difficulty"],
               json.dumps(m["tags"], ensure_ascii=False), json.dumps(m["desc"], ensure_ascii=False)))
i = src.index("]\n\nDIFFICULTY_ZH")
src = src[:i] + "".join(fmt(m) for m in new) + src[i:]
open(os.path.join(HERE, "meta.py"), "w", encoding="utf-8").write(src)
print("added", len(new))
