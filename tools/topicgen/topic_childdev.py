# -*- coding: utf-8 -*-
"""兒童成長心理學主題的規格。"""
import cd_a, cd_e, cd_ref

TOPIC = {
    "id": "child-development",
    "category": "edu",
    "title": u"兒童成長心理學：0～18 歲",
    "short": u"兒童成長心理學",
    "crumb": u"兒童成長心理學",
    "icon": u"🌱",
    "description": u"從大腦發育、五大發展理論出發，依年齡走過 0～2 歲（依附、物體恆存、語言萌芽）、2～6 歲（心智理論、遊戲、執行功能）、6～12 歲（具體運思、友誼、霸凌、道德推理）與 12～18 歲（青春期、青少年大腦、自我認同、社群媒體）；"
                   u"再談發展遲緩與早療、ADHD、自閉症、學習障礙、焦慮憂鬱與何時求助，納入台灣的兒童預防保健與早療制度。附發展里程碑、發展地圖與求助決策樹等互動工具。",
}

MODULES = cd_a.MODULES + cd_e.MODULES

REFERENCES = cd_ref.REFERENCES
