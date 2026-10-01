# -*- coding: utf-8 -*-
"""人體使用手冊主題的規格：把 um_a、um_c、um_d、um_e、um_g 的模組與速查表串起來。"""
import um_a, um_c, um_d, um_e, um_g, um_ref

TOPIC = {
    "id": "body-manual",
    "category": "biomed",
    "title": "人體使用手冊：吃、睡、動、休息的日常操作指南",
    "short": "人體使用手冊",
    "crumb": "人體使用手冊",
    "icon": "🩺",
    "description": "把身體機制落到每天的生活：怎麼睡飽、一餐怎麼配、外食怎麼選、從零開始運動與肌力訓練、"
                   "日常保養與健康檢查、壓力與心理照顧，以及不同年齡的重點；"
                   "每課最後一個「本週就做這一件事」，搭配睡眠計算器、蛋白質與喝水計算器、運動課表產生器和習慣檢核表。",
}

MODULES = um_a.MODULES + um_c.MODULES + um_d.MODULES + um_e.MODULES + um_g.MODULES

REFERENCES = um_ref.REFERENCES
