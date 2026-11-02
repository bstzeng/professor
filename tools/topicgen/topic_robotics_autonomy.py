# -*- coding: utf-8 -*-
"""機器人與自動駕駛：原理、硬體需求與產業分析（rbt_）。"""
import rbt_a, rbt_c, rbt_e, rbt_g, rbt_h, rbt_ref

TOPIC = {
    "id": "robotics-autonomy",
    "category": "tech",
    "title": u"機器人與自動駕駛：從 PID、卡爾曼濾波到人形機器人，硬體需求與產業分析",
    "short": u"機器人與自動駕駛",
    "crumb": u"機器人與自駕",
    "icon": u"🤖",
    "description": u"感知、規劃、控制：自駕分級、機器人種類、運動學與動力學、PID、LQR、MPC、全身控制；感測器、卡爾曼與粒子濾波、感測器融合、SLAM、BEV；"
                   u"路徑規劃、抓取、模仿與強化學習、端到端自駕、VLA 模型與世界模型。深入硬體需求：BOM 拆解、算力與記憶體頻寬推算、感測器資料量、致動器與減速器、電池、功能安全、雲端訓練、成本曲線與全球需求推算；"
                   u"產業分析：Waymo、百度、特斯拉、Figure、宇樹、工業與物流機器人、美中競爭、台灣供應鏈、市場預測與泡沫、法規與就業、5／10／15 年展望。附 11 個互動工具。",
}

MODULES = rbt_a.MODULES + rbt_c.MODULES + rbt_e.MODULES + rbt_g.MODULES + rbt_h.MODULES
REFERENCES = rbt_ref.REFERENCES
