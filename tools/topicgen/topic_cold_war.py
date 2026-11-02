# -*- coding: utf-8 -*-
"""冷戰史（cw_）。"""
import cw_a, cw_c, cw_e, cw_ref

TOPIC = {
    "id": "cold-war",
    "category": "history",
    "title": u"冷戰史：從鐵幕到蘇聯解體",
    "short": u"冷戰史",
    "crumb": u"冷戰史",
    "icon": u"🧊",
    "description": u"雅爾達與波茨坦、長電報與圍堵、杜魯門主義與馬歇爾計畫、柏林封鎖與北約；國共內戰、韓戰、第七艦隊與中美共同防禦條約、台海危機與八二三砲戰、奠邊府、中蘇分裂；"
                   u"核武競賽、太空競賽、相互保證毀滅、U-2 與黑貓中隊、柏林圍牆、古巴飛彈危機、情報機構；去殖民化、越戰、中東與石油危機、拉丁美洲、非洲、阿富汗；"
                   u"布拉格之春、低盪、尼克森訪華與 2758 號決議、台灣關係法、改革開放、台灣的冷戰經濟；雷根、團結工聯、戈巴契夫、車諾比、1989、德國統一、蘇聯解體；冷戰文化、科技遺產、戒嚴與解嚴、俄烏戰爭與美中競爭。",
}

MODULES = cw_a.MODULES + cw_c.MODULES + cw_e.MODULES
REFERENCES = cw_ref.REFERENCES
