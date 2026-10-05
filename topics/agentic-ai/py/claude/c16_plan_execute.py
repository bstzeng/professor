# -*- coding: utf-8 -*-
"""第 16 課（Claude API 版）：用結構化輸出（output_config.format）讓規劃者回傳保證合法的 JSON 計畫。"""
import json
import anthropic

client = anthropic.Anthropic()
PLAN_SCHEMA = {
    "type": "object",
    "properties": {"steps": {"type": "array", "items": {"type": "string"}}},
    "required": ["steps"],
    "additionalProperties": False,
}


def plan(goal, feedback=""):
    r = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=16000,
        system="你是規劃者。把目標拆成 3～6 個具體、可執行的步驟。",
        messages=[{"role": "user", "content": goal + feedback}],
        output_config={"format": {"type": "json_schema", "schema": PLAN_SCHEMA}},
    )
    return json.loads(next(b.text for b in r.content if b.type == "text"))["steps"]


steps = plan("做一份上個月營收的分析報告")
for i, s in enumerate(steps, 1):
    print(i, s)
# 執行失敗時：plan(goal, "\n已完成：...\n失敗：...（原因）") 讓 Claude 重新規劃
