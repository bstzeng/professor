# -*- coding: utf-8 -*-
"""第 31 課：改層數、寬度、上下文長度，各訓練 300 步，比較驗證損失。"""
import re
import subprocess
import sys

RUNS = [("基準：2 層、128 維、上下文 80", []),
        ("加深：4 層", ["--n_layer", "4"]),
        ("加寬：256 維", ["--n_embd", "256"]),
        ("上下文縮短為 16", ["--block", "16"])]
for name, extra in RUNS:
    cmd = [sys.executable, "train.py", "--steps", "300", "--eval_every", "299", "--n_layer", "2", "--n_embd", "128",
           "--out", "exp.pt", "--warmup", "30"] + extra
    out = subprocess.run(cmd, capture_output=True, text=True).stdout
    last = [l for l in out.splitlines() if l.startswith("step")][-1]
    params = re.search(r"參數 ([\d.]+)M", out).group(1)
    print("%-22s 參數 %sM  →  驗證損失 %s" % (name, params, re.search(r"val loss ([\d.]+)", last).group(1)))
