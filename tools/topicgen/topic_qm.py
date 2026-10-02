# -*- coding: utf-8 -*-
"""量子力學主題的規格。"""
import qm_a, qm_e, qm_ref

TOPIC = {
    "id": "quantum-mechanics",
    "category": "science",
    "title": "量子力學：從黑體輻射到薛丁格方程式與糾纏",
    "short": "量子力學",
    "crumb": "量子力學",
    "icon": "⚛️",
    "description": "古典物理的危機：黑體輻射、光電效應、康普頓散射；波耳模型與原子光譜；物質波與一次一顆的雙縫實驗；"
                   "複數、波函數、狄拉克符號與算符；薛丁格方程式、位能井、量子穿隧、簡諧振子；測不準原理與量測問題；"
                   "氫原子軌域、自旋與週期表；EPR、糾纏與貝爾不等式；各種詮釋、應用與通往量子場論。附九個互動實驗。",
}

MODULES = qm_a.MODULES + qm_e.MODULES

REFERENCES = qm_ref.REFERENCES
