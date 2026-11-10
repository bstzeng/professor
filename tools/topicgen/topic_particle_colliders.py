# -*- coding: utf-8 -*-
"""大型對撞機主題的規格。"""
import col_a, col_c, col_e, col_g, col_ref

TOPIC = {
    "id": "particle-colliders",
    "category": "science",
    "title": u"大型對撞機：從迴旋加速器到 LHC，以及怎麼從資料中找到新粒子",
    "short": u"大型對撞機",
    "crumb": u"大型對撞機",
    "icon": u"💥",
    "description": u"德布羅意波長、質心能量、截面與亮度；迴旋加速器、Bevatron 與反質子、AdA 與 ISR、J/ψ 與十一月革命、SppS 與 W/Z、Tevatron 與頂夸克、LEP 與三代微中子、SSC、LHC 與 2008 年事故；"
                   u"射頻腔、超導磁鐵、聚焦、注入鏈、堆疊；粒子與物質作用、矽徑跡與動量、量能器、緲子系統、ATLAS 與 CMS、LHCb 與 ALICE、觸發系統、全球運算網格；"
                   u"卡爾曼濾波、頂點、粒子流、anti-kt 噴流、b 標記、消失的橫向能量、標記—探測法；卜瓦松與 p 值、不變質量、背景估計與 ABCD、輪廓似然、漸近公式與阿西莫夫、5σ、別處效應、CLs 與巴西圖、盲分析；"
                   u"事件產生器、Geant4、BDT 與深度學習、異常偵測；H→γγ 與 H→4ℓ 的完整分析、2012 年發現論文、希格斯性質；750 GeV、超對稱與 B 介子異常、高亮度 LHC 與 FCC。附六個互動模擬與論文清單。",
}

MODULES = col_a.MODULES + col_c.MODULES + col_e.MODULES + col_g.MODULES
REFERENCES = col_ref.REFERENCES
