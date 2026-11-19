# -*- coding: utf-8 -*-
"""手機裡的感測器的規格。"""
import sns_a, sns_ref

TOPIC = {
    "id": "phone-sensors", "category": "tech",
    "title": u"手機裡的感測器：從加速度計到 Face ID 與 GPS",
    "short": u"手機感測器", "crumb": u"手機感測器", "icon": u"📱",
    "description": u"感測器的共同架構與誤差、MEMS；加速度計、陀螺儀與科氏力、磁力計與校正、感測器融合與卡爾曼濾波、計步與跌倒偵測、氣壓計；環境光、近接感測、飛時測距與 LiDAR、Face ID 的結構光；電容式、光學式與超音波指紋、生物辨識的安全；"
                   u"MEMS 麥克風與波束成形、線性馬達與觸覺回饋；GPS 與相對論、多系統與雙頻定位、Wi-Fi 與藍牙定位、UWB 與室內定位；穿戴裝置的心率血氧與心電圖、感測器與隱私。附加速度計、陀螺儀漂移、感測器融合、指紋電容、GPS 定位五個互動模擬。",
}
MODULES = sns_a.MODULES
REFERENCES = sns_ref.REFERENCES
