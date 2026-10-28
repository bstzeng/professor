# -*- coding: utf-8 -*-
"""國際太空站：參考頁——互動圖鑑、艙段速查、名詞中英對照。"""
from iss_common import ISSLIB, LS, iw, MAP, MODS, DAY

PN = {"US": u"美國", "RU": u"俄羅斯", "ESA": u"歐洲", "JAXA": u"日本", "CSA": u"加拿大"}

GUIDE = {
    "file": "guide.html", "title": u"ISS 互動圖鑑", "h1": u"ISS 互動圖鑑", "icon": u"🛰️",
    "description": u"可點選的太空站示意圖、組裝時間軸、軌道與地面軌跡、一天作息、水與氧氣回收、軌道衰減",
    "body": [
        ("raw", u"<script>%s</script>" % ISSLIB),
        ("h", u"1. 太空站示意圖（第 5 課）"), MAP(),
        ("h", u"2. 組裝時間軸（第 4 課）"), MAP(u"拉動年份或按播放：", year=True),
        ("h", u"3. 軌道與地面軌跡（第 1、33 課）"), iw("orbit"),
        ("h", u"4. 一天作息（第 20 課）"), DAY,
        ("h", u"5. 水與氧氣回收（第 16、17 課）"), iw("loop"),
        ("h", u"6. 軌道衰減與抬升（第 18、49 課）"), iw("decay"),
    ],
}

MODTABLE = {
    "file": "modules.html", "title": u"ISS 艙段速查", "h1": u"ISS 艙段速查", "icon": u"🧩",
    "description": u"各艙段的中英文名稱、負責國家、升空年份與功能",
    "body": [
        ("t", [u"艙段", u"英文", u"國家", u"年份", u"功能", u"課"],
         [[m[1], m[2], PN[m[3]], (u"%d～%d" % (m[4], m[5])) if m[5] else str(m[4]), m[10], LS(m[11])] for m in MODS]),
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"ISS 名詞中英對照", "h1": u"ISS 名詞中英對照", "icon": u"📖",
    "description": u"太空站、維生系統、太空船與太空生活的中英名詞",
    "body": [
        ("t", [u"中文", u"英文", u"課"], [
            [u"國際太空站", u"International Space Station（ISS）", LS(1)], [u"微重力", u"Microgravity", LS(1)], [u"軌道傾角", u"Orbital Inclination", LS(3)],
            [u"政府間協定", u"Intergovernmental Agreement（IGA）", LS(3)], [u"長期考察", u"Expedition", LS(46)], [u"俄羅斯軌道段", u"Russian Orbital Segment（ROS）", LS(5)],
            [u"美國軌道段", u"US Orbital Segment（USOS）", LS(5)], [u"節點艙", u"Node", LS(7)], [u"國際對接轉接器", u"International Docking Adapter（IDA）", LS(7)],
            [u"對接／停靠", u"Docking／Berthing", LS(7)], [u"國際標準酬載機架", u"International Standard Payload Rack（ISPR）", LS(8)], [u"氣閘艙", u"Airlock", LS(8)],
            [u"穹頂觀測艙", u"Cupola", LS(11)], [u"可擴展艙段", u"Expandable Module（BEAM）", LS(11)], [u"整合桁架", u"Integrated Truss Structure", LS(12)],
            [u"捲展式太陽能板", u"iROSA", LS(12)], [u"加拿大臂 2 號", u"Canadarm2", LS(13)], [u"維生系統", u"ECLSS", LS(16)],
            [u"薩巴捷反應", u"Sabatier Reaction", LS(16)], [u"水回收系統", u"Water Recovery System", LS(17)], [u"控制力矩陀螺", u"Control Moment Gyroscope（CMG）", LS(18)],
            [u"軌道抬升", u"Reboost", LS(18)], [u"碎片迴避機動", u"Debris Avoidance Maneuver", LS(18)], [u"惠普爾防護罩", u"Whipple Shield", LS(18)],
            [u"中繼衛星", u"TDRS", LS(19)], [u"太空艙通訊員", u"CAPCOM", LS(19)], [u"通用廢棄物管理系統", u"UWMS", LS(23)],
            [u"先進阻力訓練裝置", u"ARED", LS(24)], [u"太空飛行相關神經眼科症候群", u"SANS", LS(25)], [u"南大西洋異常區", u"South Atlantic Anomaly", LS(26)],
            [u"總觀效應", u"Overview Effect", LS(27)], [u"艙外活動（太空漫步）", u"Extravehicular Activity（EVA）", LS(28)], [u"減壓症", u"Decompression Sickness", LS(28)],
            [u"聯盟號", u"Soyuz", LS(30)], [u"進步號", u"Progress", LS(31)], [u"天鵝座號", u"Cygnus", LS(31)], [u"龍飛船", u"Dragon", LS(31)],
            [u"商業補給服務", u"Commercial Resupply Services", LS(31)], [u"商業載人計畫", u"Commercial Crew Program", LS(32)], [u"星際客機", u"Starliner", LS(32)],
            [u"發射窗口", u"Launch Window", LS(33)], [u"國家實驗室", u"ISS National Lab", LS(34)], [u"玻色－愛因斯坦凝聚", u"Bose–Einstein Condensate", LS(38)],
            [u"阿爾法磁譜儀", u"Alpha Magnetic Spectrometer（AMS-02）", LS(39)], [u"凱斯勒症候群", u"Kessler Syndrome", LS(45)], [u"反衛星試驗", u"Anti-satellite Test（ASAT）", LS(45)],
            [u"美國離軌載具", u"US Deorbit Vehicle（USDV）", LS(49)], [u"尼莫點", u"Point Nemo", LS(49)], [u"商業低軌道目的地", u"Commercial LEO Destinations（CLD）", LS(50)],
            [u"天宮太空站", u"Tiangong Space Station", LS(51)], [u"門戶月球軌道站", u"Lunar Gateway", LS(52)]]),
    ],
}

REFERENCES = [GUIDE, MODTABLE, GLOSSARY]
