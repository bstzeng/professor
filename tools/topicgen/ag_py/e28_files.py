# -*- coding: utf-8 -*-
"""第 28 課：檔案工具——view / create / str_replace，全部限制在專案根目錄內（防止 ../ 路徑穿越）。"""
import os
import tempfile
from pathlib import Path

ROOT = Path(tempfile.mkdtemp(prefix="agent_ws_")).resolve()

def safe(path):
    p = (ROOT / path).resolve()
    if not p.is_relative_to(ROOT):
        raise PermissionError("拒絕：%s 在專案目錄之外" % path)
    return p

def view(path):
    p = safe(path)
    if p.is_dir():
        return "\n".join(sorted(x.name for x in p.iterdir()))
    return "\n".join("%4d  %s" % (i, l) for i, l in enumerate(p.read_text(encoding="utf-8").splitlines(), 1))

def create(path, file_text):
    p = safe(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(file_text, encoding="utf-8")
    return "已建立 %s（%d 行）" % (path, file_text.count("\n") + 1)

def str_replace(path, old_str, new_str):
    """只取代『剛好出現一次』的字串——出現 0 次或多次都報錯，避免改錯地方。"""
    p = safe(path)
    s = p.read_text(encoding="utf-8")
    n = s.count(old_str)
    if n != 1:
        raise ValueError("old_str 出現 %d 次，必須剛好 1 次；請提供更多上下文" % n)
    p.write_text(s.replace(old_str, new_str), encoding="utf-8")
    return "已修改 %s" % path

print(create("app/config.py", "DEBUG = True\nPORT = 8000\nHOST = 'localhost'"))
print(view("app/config.py"))
print(str_replace("app/config.py", "DEBUG = True", "DEBUG = False"))
for call in [lambda: str_replace("app/config.py", "=", ":"),
             lambda: view("../../etc/passwd")]:
    try:
        call()
    except Exception as e:
        print("✗", type(e).__name__, e)
print(view("app/config.py"))
