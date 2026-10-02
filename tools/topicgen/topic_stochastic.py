# -*- coding: utf-8 -*-
"""隨機過程與馬可夫鏈主題的規格。"""
import rp_a, rp_e, rp_ref

TOPIC = {
    "id": "stochastic-processes",
    "category": "math",
    "title": "隨機過程與馬可夫鏈：會隨時間變化的機率",
    "short": "隨機過程與馬可夫鏈",
    "crumb": "隨機過程",
    "icon": "🎲",
    "description": "樣本路徑與四種隨機過程；隨機漫步、賭徒破產、反射原理、波利亞定理、中央極限定理；馬可夫鏈、轉移矩陣、狀態分類、吸收與首次步分析；"
                   "平穩分布、遍歷、七次洗牌、細緻平衡、PageRank；卜瓦松、生死與分支過程、檢查站悖論；布朗運動、伊藤引理、幾何布朗運動、"
                   "布萊克—修斯；隱馬可夫、強化學習、語言模型、鞅與常見誤解。附九個互動模擬。",
}

MODULES = rp_a.MODULES + rp_e.MODULES

REFERENCES = rp_ref.REFERENCES
