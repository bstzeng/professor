# -*- coding: utf-8 -*-
"""傅立葉分析與訊號處理主題的規格。"""
import fou_a, fou_f, fou_ref

TOPIC = {
    "id": "fourier-signal",
    "category": "math",
    "title": u"傅立葉分析與訊號處理：從聲音到 MRI",
    "short": u"傅立葉分析",
    "crumb": u"傅立葉分析",
    "icon": u"🎵",
    "description": u"傅立葉級數、正交性、吉布斯現象；傅立葉轉換、卷積定理、測不準關係、帕塞瓦爾；取樣定理、混疊、量化、DFT 與 CD 的 44.1 kHz；"
                   u"FFT 的推導與冷戰起源、視窗函數、頻譜圖；FIR/IIR 濾波器與 Z 轉換；音色、音高偵測、MP3 心理聲學、梅爾頻譜；"
                   u"二維轉換、JPEG 與 DCT、CNN；MRI 的 k 空間、CT 切片定理、DNA 的 51 號照片、FTIR、LIGO 匹配濾波；小波、壓縮感知、OFDM。附五個互動模擬。",
}

MODULES = fou_a.MODULES + fou_f.MODULES
REFERENCES = fou_ref.REFERENCES
