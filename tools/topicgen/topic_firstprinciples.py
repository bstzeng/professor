# -*- coding: utf-8 -*-
"""馬斯克的第一性原理主題的規格。"""
import fp_a, fp_e, fp_h, fp_ref

TOPIC = {
    "id": "first-principles",
    "category": "tech",
    "title": "馬斯克的第一性原理：從物理思考到改變產業",
    "short": "第一性原理",
    "crumb": "第一性原理",
    "icon": "🧭",
    "description": "第一性原理完整導讀：亞里斯多德到物理學家的思考、類比推理的取捨、馬斯克的原話；拆解、白痴指數、理論極限與五步驟演算法；"
                   "SpaceX 的成本拆解、垂直整合、Falcon 1、可重複使用、Starship 與 Starlink；Tesla 的電池、超級工廠、直營、OTA、壓鑄、生產地獄與純視覺；"
                   "PayPal、SolarCity、Boring、Neuralink、推特；近年的 Starship 入軌、xAI 與 SpaceX 合併上市、Robotaxi、銷量挑戰與 DOGE；"
                   "預測失準、失敗案例、倖存者偏差與方法的極限；以及如何用在生活、工作與學習。附九個互動工具。",
}

MODULES = fp_a.MODULES + fp_e.MODULES + fp_h.MODULES

REFERENCES = fp_ref.REFERENCES
