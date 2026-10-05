# -*- coding: utf-8 -*-
"""第 25 課：提示快取（prompt caching）——代理每一輪都重送相同的開頭（system、工具、舊歷史），
伺服器若把這段「前綴」的計算結果存起來，下一輪就只需要算新增的部分。
這裡模擬快取的計費：前綴完全相同才命中；改到任何一個字，後面全部失效。"""
import hashlib

PRICE_IN, WRITE_X, READ_X = 4.0, 1.25, 0.1        # 每百萬 token 美元；寫入 1.25 倍、讀取約 0.1 倍（實際以官方價目表為準）
cache = {}

def call(prefix_blocks, new_tokens):
    """prefix_blocks: [(文字, tokens)]；回傳 (費用, 命中 tokens)。"""
    h, hit, cost, hit_tok = hashlib.sha256(), True, 0.0, 0
    for txt, tok in prefix_blocks:
        h.update(txt.encode())
        key = h.hexdigest()                          # 前綴的雜湊：前面任何一處不同，雜湊就不同
        if hit and key in cache:
            cost += tok * PRICE_IN * READ_X / 1e6
            hit_tok += tok
        else:
            hit = False
            cache[key] = True
            cost += tok * PRICE_IN * WRITE_X / 1e6
    return cost + new_tokens * PRICE_IN / 1e6, hit_tok

system, tools = ("你是程式代理……" * 100, 20000), ("[工具定義×12]", 8000)
history = []
total_c = total_n = 0.0
for turn in range(1, 11):
    prefix = [system, tools] + history
    c, hit = call(prefix, 3000)
    n = (sum(t for _, t in prefix) + 3000) * PRICE_IN / 1e6       # 沒有快取的費用
    total_c, total_n = total_c + c, total_n + n
    print("第 %2d 輪：前綴 %6d tokens，命中 %6d｜有快取 $%.4f vs 無快取 $%.4f" % (turn, sum(t for _, t in prefix), hit, c, n))
    history.append(("第 %d 輪的對話與工具結果" % turn, 3000))
print("10 輪合計：有快取 $%.3f，無快取 $%.3f，省下 %.0f%%" % (total_c, total_n, 100 * (1 - total_c / total_n)))

c, hit = call([("你是程式代理…… 今天是 2026-10-05", 20000), tools], 3000)
print("\n陷阱：在 system 開頭放『今天日期』這種會變的東西 → 命中 %d tokens（全部失效）" % hit)
