# -*- coding: utf-8 -*-
"""第 34 課（Claude API 版）：協調者用 Claude Opus 5.5 拆任務與整合；工作者用較便宜的 Claude Sonnet 5.5 平行執行。"""
import json
from concurrent.futures import ThreadPoolExecutor
import anthropic

client = anthropic.Anthropic()
ORCH, WORKER = "claude-opus-5-5", "claude-sonnet-5-5"
SCHEMA = {"type": "object", "properties": {"subtasks": {"type": "array", "items": {"type": "string"}}},
          "required": ["subtasks"], "additionalProperties": False}


def ask(model, system, prompt, **kw):
    r = client.messages.create(model=model, max_tokens=16000, system=system,
                               messages=[{"role": "user", "content": prompt}], **kw)
    return next(b.text for b in r.content if b.type == "text")


goal = "我們要不要進軍日本電動機車市場？"
plan = json.loads(ask(ORCH, "把目標拆成 3～5 個彼此獨立、可平行研究的子任務。", goal,
                      output_config={"format": {"type": "json_schema", "schema": SCHEMA}}))["subtasks"]
with ThreadPoolExecutor(max_workers=len(plan)) as pool:
    findings = list(pool.map(lambda t: ask(WORKER, "你是研究員，只負責這一個子任務，用 150 字內回報重點與不確定之處。", t), plan))
report = ask(ORCH, "整合各研究員的發現，給出建議與主要風險。",
             goal + "\n\n" + "\n\n".join("【%s】\n%s" % tf for tf in zip(plan, findings)))
print(report)
