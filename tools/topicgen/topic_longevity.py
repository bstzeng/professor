# -*- coding: utf-8 -*-
"""老化與長壽科學的規格。"""
import lng_a, lng_f, lng_ref

TOPIC = {
    "id": "longevity",
    "category": "biomed",
    "title": u"老化與長壽科學",
    "short": u"老化與長壽",
    "crumb": u"老化與長壽",
    "icon": u"⏳",
    "description": u"健康壽命、岡珀茲定律、老化的演化理論；老化的十二個特徵：DNA 損傷、端粒、表觀遺傳時鐘、蛋白質恆定與自噬、粒線體與營養感知、細胞衰老、幹細胞與發炎老化；"
                   u"熱量限制與猴子實驗、裸鼴鼠與格陵蘭鯊、daf-2、雷帕黴素、二甲雙胍與白藜蘆醇、清除衰老細胞、山中因子與重新編程；百歲人瑞與藍區爭議、運動、飲食睡眠與社交、失智與肌少症；抗老產業的炒作、延壽的倫理、台灣的超高齡社會。附岡珀茲存活曲線、端粒與動物壽命三個互動圖。",
}

MODULES = lng_a.MODULES + lng_f.MODULES
REFERENCES = lng_ref.REFERENCES
