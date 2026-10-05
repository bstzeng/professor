# -*- coding: utf-8 -*-
"""執行所有離線範例，把輸出存到 _out/，供課程頁面顯示。"""
import glob
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(HERE, "_out"), exist_ok=True)
for f in sorted(glob.glob(os.path.join(HERE, "[a-h][0-9][0-9]_*.py"))):
    p = subprocess.run([sys.executable, f], cwd=HERE, capture_output=True, text=True, timeout=120,
                       env=dict(os.environ, PYTHONIOENCODING="utf-8"))
    if p.returncode != 0:
        sys.exit("FAILED %s\n%s" % (f, p.stderr))
    open(os.path.join(HERE, "_out", os.path.basename(f)[:-3] + ".txt"), "w", encoding="utf-8").write(p.stdout)
    print("ok", os.path.basename(f))
