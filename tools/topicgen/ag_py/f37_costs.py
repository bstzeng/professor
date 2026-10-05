# -*- coding: utf-8 -*-
"""第 37 課：多代理的代價——token 用量會倍增，協調也會出錯。先算清楚再決定。"""

PRICE = {"claude-opus-5-5": (4.0, 20.0), "claude-sonnet-5-5": (2.0, 10.0), "claude-haiku-4-5": (1.0, 5.0)}   # 美元／百萬 tokens

def cost(model, inp, out):
    pi, po = PRICE[model]
    return (inp * pi + out * po) / 1e6

def agent_run(model, turns, base_ctx, growth, out_per_turn):
    """一個代理跑 turns 輪：每輪重送整段上下文，上下文每輪增加 growth。"""
    inp = sum(base_ctx + growth * t for t in range(turns))
    return cost(model, inp, out_per_turn * turns), inp + out_per_turn * turns

single, st = agent_run("claude-opus-5-5", 30, 8000, 3000, 800)
print("單一代理（Opus 5.5，30 輪）：%7.2f 美元，%9d tokens" % (single, st))

orch, ot = agent_run("claude-opus-5-5", 10, 8000, 2000, 800)
# 每個工作者都要重新讀背景資料、自己探索，所以各自的上下文也會長大
workers = [agent_run("claude-sonnet-5-5", 20, 8000, 3000, 800) for _ in range(6)]
multi = orch + sum(c for c, _ in workers)
mt = ot + sum(t for _, t in workers)
print("多代理（Opus 協調 + 6 個 Sonnet 工作者）：%5.2f 美元，%9d tokens" % (multi, mt))
print("\ntoken 是單一代理的 %.1f 倍；工作者改用較便宜的模型，成本只是 %.1f 倍。值得嗎？看任務：" % (mt / st, multi / single))
for k, v in [("✓ 適合", "可平行、彼此獨立、資訊量大（研究、大量檔案審查）"),
             ("✗ 不適合", "步驟緊密相依、需要共享大量上下文（例如：多人同時改同一段程式碼）")]:
    print("  %s：%s" % (k, v))
