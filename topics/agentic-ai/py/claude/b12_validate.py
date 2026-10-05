# -*- coding: utf-8 -*-
"""第 12 課（Claude API 版）：strict: true 讓 Claude 產生的工具參數「保證」符合 schema。
schema 需要 additionalProperties: false 與 required。仍建議在伺服器端再驗證一次商業規則。"""
import anthropic

client = anthropic.Anthropic()
r = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=16000,
    messages=[{"role": "user", "content": "幫我訂兩張下週五飛東京的商務艙機票"}],
    tools=[{
        "name": "book_flight",
        "description": "預訂機票",
        "strict": True,
        "input_schema": {
            "type": "object",
            "properties": {
                "destination": {"type": "string"},
                "date": {"type": "string", "format": "date"},
                "passengers": {"type": "integer", "enum": [1, 2, 3, 4, 5, 6, 7, 8]},
                "cabin": {"type": "string", "enum": ["economy", "business"]},
            },
            "required": ["destination", "date", "passengers", "cabin"],
            "additionalProperties": False,
        },
    }],
)
for b in r.content:
    if b.type == "tool_use":
        print("符合 schema 的參數：", b.input)
