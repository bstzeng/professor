# -*- coding: utf-8 -*-
"""一次 LLM 推論到底發生什麼主題的規格。"""
import lf_a, lf_e, lf_ref

TOPIC = {
    "id": "llm-inference",
    "category": "tech",
    "title": "一次 LLM 推論到底發生什麼：Prefill 與 Decode",
    "short": "LLM 推論",
    "crumb": "LLM 推論",
    "icon": "⚡",
    "description": "從按下 Enter 到看到文字：tokenizer、chat template、embedding、RoPE 與 Transformer 層；Q、K、V、因果遮罩、KV Cache 的大小與 GQA／MLA；"
                   "prefill 的 FLOPs、算力受限與 FlashAttention；decode 的頻寬受限、roofline、速度上限與抽樣；batching、continuous batching、PagedAttention、"
                   "prefix cache、量化、推測解碼、分離部署與 MoE；GPU、記憶體階層、多卡平行與互連；排程、成本、benchmark 與本地推論。附九個互動計算器。",
}

MODULES = lf_a.MODULES + lf_e.MODULES

REFERENCES = lf_ref.REFERENCES
