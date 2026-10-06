# -*- coding: utf-8 -*-
"""依序執行課程範例，把輸出存到 _out/（train.txt、train_modern.txt 由 train.py 另外產生）。"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = [("prepare_data", None), ("s01_tensor", None), ("s02_module", None), ("s03_data", None), ("s04_char_tok", None), ("s05_bpe", None),
        ("s06_bigram", None), ("s07_attention", None), ("s08_params", None), ("sample", None), ("s10_sampling", None), ("s11_kvcache", None),
        ("chat", "月\n孤帆遠影\n\n"), ("s12_modern", None), ("s13_instruct_data", None), ("lora", None), ("s14_eval", None), ("x_dump", None), ("x_lens", None),
        ("s09_experiments", None)]
only = set(sys.argv[1:])
for name, stdin in RUNS:
    if only and name not in only:
        continue
    p = subprocess.run([sys.executable, name + ".py"], cwd=HERE, input=stdin, capture_output=True, text=True,
                       env=dict(os.environ, PYTHONIOENCODING="utf-8"))
    if p.returncode != 0:
        sys.exit("FAILED %s\n%s" % (name, p.stderr))
    out = p.stdout
    open(os.path.join(HERE, "_out", name + ".txt"), "w", encoding="utf-8").write(out)
    print("ok", name)
