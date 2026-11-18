# -*- coding: utf-8 -*-
"""流體力學與飛行的規格。"""
import fld_a, fld_f, fld_ref

TOPIC = {
    "id": "fluid-dynamics",
    "category": "science",
    "title": u"流體力學與飛行：從白努利到音障",
    "short": u"流體力學",
    "crumb": u"流體力學",
    "icon": u"🌊",
    "description": u"壓力、浮力與帕斯卡原理、黏滯性與非牛頓流體、連續方程式；白努利定律與「等時間」迷思、雷諾數與亂流、普朗特的邊界層與流動分離、阻力、納維–斯托克斯與千禧年難題；"
                   u"升力的來源、翼型與攻角、失速、襟翼、翼尖渦流與誘導阻力；馬赫數、音障與震波、協和號與 X-59、高超音速與重返大氣層；風洞與 CFD；鳥與昆蟲、曲球與高爾夫球、血流、天氣與洋流。附文氏管、雷諾數、機翼升力與馬赫錐四個互動模擬。",
}

MODULES = fld_a.MODULES + fld_f.MODULES
REFERENCES = fld_ref.REFERENCES
