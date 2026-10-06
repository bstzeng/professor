# -*- coding: utf-8 -*-
"""AI 的內心與邊界主題的規格。"""
import xai_a, xai_e, xai_ref

TOPIC = {
    "id": "ai-inside-limits",
    "category": "ai",
    "title": u"AI 的內心與邊界：可解釋性、幻覺、安全與社會",
    "short": u"AI 的內心與邊界",
    "crumb": u"AI 的內心與邊界",
    "icon": u"🔍",
    "description": u"打開 AI 的黑盒子，也看清它的邊界：幻覺的成因、校準、諂媚與減少幻覺的方法；探針、logit lens、殘差流、induction head、疊加、稀疏自編碼器、"
                   u"金門大橋 Claude 與電路追蹤；思維鏈的忠實性與測試時運算；對齊、RLHF 的極限、憲法式 AI、獎勵駭客、欺騙研究與可擴展監督；越獄、提示注入、紅隊、"
                   u"資料投毒與隱私；偏見與公平；著作權、各國法規（含台灣）、工作、能源、深偽與選舉、AGI 的各方觀點。附真實小模型的 logit lens 與注意力等互動工具。",
}

MODULES = xai_a.MODULES + xai_e.MODULES

REFERENCES = xai_ref.REFERENCES
