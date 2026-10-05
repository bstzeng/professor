# -*- coding: utf-8 -*-
"""第 38 課：結構化輸出——讓模型的回答變成程式能直接用的資料（JSON），而且要驗證。
沒有約束時，模型可能多講廢話、漏欄位、用錯型別；約束解碼（constrained decoding）則保證符合 schema。"""
import json
import re
from mockllm import MockClient, text

SCHEMA_KEYS = {"name": str, "email": str, "plan": str, "demo": bool}
EMAIL = "我是王小美（mei@example.com），想試用企業方案，可以安排展示嗎？"

loose = MockClient(lambda ctx: text('好的！以下是擷取結果：\n```json\n{"name": "王小美", "email": "mei@example.com", "plan": "企業", "demo": "要"}\n```\n希望有幫助！'))
strict = MockClient(lambda ctx: text('{"name": "王小美", "email": "mei@example.com", "plan": "enterprise", "demo": true}'))

def parse_and_check(raw):
    m = re.search(r"\{.*\}", raw, re.S)                # 從一堆文字中挖出 JSON（脆弱的做法）
    data = json.loads(m.group(0))
    errs = ["%s 應為 %s" % (k, t.__name__) for k, t in SCHEMA_KEYS.items() if not isinstance(data.get(k), t)]
    return data, errs

for name, c in [("沒約束", loose), ("有約束", strict)]:
    raw = c.messages.create(model="mock", max_tokens=300, messages=[{"role": "user", "content": EMAIL}]).content[0].text
    data, errs = parse_and_check(raw)
    print("【%s】原始輸出：%s" % (name, raw.replace("\n", "⏎")))
    print("        驗證：%s" % ("通過 ✓ → " + str(data) if not errs else "失敗 ✗ " + "；".join(errs)))
