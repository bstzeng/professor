# -*- coding: utf-8 -*-
"""提示工程主題的規格。"""
import pe_a, pe_b, pe_c, pe_ref

TOPIC = {
    "id": "prompt-engineering",
    "category": "ai",
    "title": u"提示工程：從一句指令到可上線的 AI 系統",
    "short": u"提示工程",
    "crumb": u"提示工程",
    "icon": u"✍️",
    "description": u"從模型怎麼讀提示開始：指令、說明理由、具體化、結構化、Few-shot、輸出格式與結構化輸出、思考與拆解；"
                   u"上下文工程、長文件、RAG、記憶、工具說明、提示快取與上下文污染；"
                   u"代理的系統提示、規劃者與執行者、狀態、錯誤恢復、模型路由、子代理與自主程度；"
                   u"需求、測試集、評分、失敗分類、提示注入與縱深防禦、優化、版本管理、模型遷移與成本。以改寫前後對照為主，附六個互動工具。",
}

MODULES = pe_a.MODULES + pe_b.MODULES + pe_c.MODULES

REFERENCES = pe_ref.REFERENCES
