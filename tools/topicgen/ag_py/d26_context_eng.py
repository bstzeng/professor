# -*- coding: utf-8 -*-
"""第 26 課：上下文工程——在有限的視窗裡，決定「放什麼、放多少、什麼時候放」。
技巧：① 只放索引、需要時再載入（just-in-time） ② 工具結果截斷  ③ 依優先順序裝箱  ④ 重要指示放在固定位置"""
from mockllm import count_tokens

REPO = {"src/auth.py": "def login(user, pw):\n    ...\n" * 300,
        "src/db.py": "class DB:\n    ...\n" * 500,
        "src/ui.py": "def render():\n    ...\n" * 800,
        "README.md": "# 專案說明\n安裝步驟……\n" * 50}

# ❌ 天真做法：把整個專案塞進去
naive = "\n".join("=== %s ===\n%s" % kv for kv in REPO.items())
print("天真做法：%d tokens" % count_tokens(naive))

# ✓ 只放檔案索引（路徑＋大小），讓代理用 read_file 工具按需讀取
index = "\n".join("%s（%d 行）" % (p, c.count("\n")) for p, c in REPO.items())
print("只放索引：%d tokens →\n%s" % (count_tokens(index), index))

def truncate(output, limit=200):
    """工具結果太長時保留頭尾，並告訴模型被截斷了、怎麼看更多。"""
    if count_tokens(output) <= limit:
        return output
    lines = output.splitlines()
    return "\n".join(lines[:5] + ["…（省略 %d 行，可用 read_file(path, start, end) 讀指定範圍）…" % (len(lines) - 10)] + lines[-5:])

print("\n讀取 src/db.py 的結果（截斷後）：%d tokens" % count_tokens(truncate(REPO["src/db.py"])))

def pack(items, budget):
    """依優先順序裝箱：先放最重要的，放不下就跳過。"""
    out, used = [], 0
    for prio, name, content in sorted(items):
        t = count_tokens(content)
        if used + t <= budget:
            out.append(name)
            used += t
    return out, used

items = [(0, "系統指示", "你是程式代理" * 50), (1, "任務說明", "修好登入錯誤" * 20),
         (2, "auth.py", REPO["src/auth.py"]), (3, "相關測試失敗訊息", "AssertionError" * 30),
         (4, "db.py", REPO["src/db.py"]), (5, "ui.py", REPO["src/ui.py"])]
print("在 4000 tokens 預算內放入：%s（%d tokens）" % pack(items, 4000))
