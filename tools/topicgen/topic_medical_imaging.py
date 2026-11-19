# -*- coding: utf-8 -*-
"""醫學影像原理的規格。"""
import mim_a, mim_ref

TOPIC = {
    "id": "medical-imaging", "category": "biomed",
    "title": u"醫學影像原理：X 光、CT、MRI、超音波、PET",
    "short": u"醫學影像", "crumb": u"醫學影像", "icon": u"🩻",
    "description": u"電磁波譜與游離輻射、對比與顯影劑、解析度雜訊與偽影；倫琴與 X 光管、光電效應與康普頓散射、胸部 X 光、乳房攝影、骨密度、透視與血管攝影、介入性放射學、輻射劑量與背景輻射；CT 的發明、濾波反投影與迭代重建、CT 值與窗寬窗位、顯影劑時相、心臟 CT 與台灣的低劑量肺癌篩檢；"
                   u"MRI 的自旋與拉莫頻率、共振與訊號、T1 與 T2、梯度與 k 空間、擴散、功能性 MRI、MR 血管攝影與安全；超音波的回波、都卜勒與臨床用途；示蹤劑、PET 與 SPECT、PET-CT 與癌症分期；AI 判讀與檢查比較。附 CT 重建、窗寬窗位、T1／T2、超音波、劑量五個互動模擬。",
}
MODULES = mim_a.MODULES
REFERENCES = mim_ref.REFERENCES
