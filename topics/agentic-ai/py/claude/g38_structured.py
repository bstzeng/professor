# -*- coding: utf-8 -*-
"""第 38 課（Claude API 版）：用 Pydantic 定義格式，messages.parse() 自動驗證並回傳物件。"""
from typing import Literal
from pydantic import BaseModel
import anthropic


class Lead(BaseModel):
    name: str
    email: str
    plan: Literal["free", "pro", "enterprise"]
    demo: bool


client = anthropic.Anthropic()
r = client.messages.parse(
    model="claude-opus-5-5",
    max_tokens=16000,
    messages=[{"role": "user", "content": "擷取資料：我是王小美（mei@example.com），想試用企業方案，可以安排展示嗎？"}],
    output_format=Lead,
)
lead = r.parsed_output          # 已驗證的 Lead 物件
print(lead.name, lead.email, lead.plan, lead.demo)
