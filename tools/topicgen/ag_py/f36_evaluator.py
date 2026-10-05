# -*- coding: utf-8 -*-
"""第 36 課：評估者－優化者（evaluator-optimizer）。一個代理寫、另一個代理依評分標準打分並給建議，反覆到合格。"""
import json
from mockllm import MockClient, text

RUBRIC = ["有具體數字", "不超過 40 字", "有行動呼籲"]
DRAFTS = ["我們的新咖啡很好喝，歡迎大家來試試看，真的非常好喝喔，保證你會喜歡！",
          "新品冷萃咖啡，口感滑順，第二杯半價，歡迎嘗鮮。",
          "新品冷萃咖啡，12 小時低溫萃取，第二杯半價——今天就來店嘗鮮！"]

writer = MockClient(lambda ctx: text(DRAFTS[min(ctx.turn, 2)]))

def judge(draft):
    checks = {"有具體數字": any(ch.isdigit() for ch in draft), "不超過 40 字": len(draft) <= 40,
              "有行動呼籲": any(w in draft for w in ("今天就", "立即", "馬上"))}
    j = MockClient(lambda ctx: text(json.dumps({"pass": all(checks.values()), "failed": [k for k, v in checks.items() if not v]},
                                               ensure_ascii=False)))
    return json.loads(j.messages.create(model="mock", max_tokens=200, system="依評分標準評分，輸出 JSON",
                                        messages=[{"role": "user", "content": draft}]).content[0].text)

msgs = [{"role": "user", "content": "寫一句新品咖啡的廣告文案"}]
for i in range(1, 5):
    draft = writer.messages.create(model="mock", max_tokens=200, messages=msgs).content[0].text
    v = judge(draft)
    print("第 %d 稿（%d 字）：%s\n   評審：%s" % (i, len(draft), draft, "✓ 合格" if v["pass"] else "✗ 未達 " + "、".join(v["failed"])))
    if v["pass"]:
        break
    msgs += [{"role": "assistant", "content": draft}, {"role": "user", "content": "請修改：未達 " + "、".join(v["failed"])}]
