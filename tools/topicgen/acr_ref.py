# -*- coding: utf-8 -*-
"""空難全紀錄：參考頁——事故總表、名詞、互動圖鑑。"""
from nv_common import LS, NVLIB
import acr_common as C

_G = dict((g[0], g[1]) for g in C.GROUPS)

TABLE = {
    "file": "table.html", "title": u"事故總表", "h1": u"70 起事故總表", "icon": u"📋",
    "description": u"依年份排列的事故、類別與一句話摘要",
    "body": [
        ("t", [u"年份", u"事故", u"類別", u"一句話", u"課"], [[c[0], c[1], _G[c[2]], c[3], LS(c[4])] for c in C._sorted]),
        ("p", u"死傷人數與原因請見各課；調查尚未結案的事故，以各課開頭的「調查進度」為準。"),
    ],
}

TERMS = {
    "file": "terms.html", "title": u"飛安名詞", "h1": u"飛安名詞對照", "icon": u"📚",
    "description": u"本課程常見的飛安名詞",
    "body": [
        ("t", [u"中文", u"英文", u"說明"], [
            [u"組員資源管理", u"CRM", u"善用所有組員與資源做決策的訓練"], [u"空中防撞系統", u"TCAS", u"偵測附近航機並發出避讓指示"],
            [u"強化型近地警告系統", u"EGPWS / TAWS", u"結合地形資料庫，警告前方地形"], [u"飛航資料記錄器", u"FDR", u"記錄飛行參數的黑盒子"],
            [u"座艙語音記錄器", u"CVR", u"記錄駕駛艙聲音的黑盒子"], [u"空速管", u"Pitot tube", u"測量空速的感測器"],
            [u"靜壓孔", u"Static port", u"測量外界氣壓的開口"], [u"攻角", u"Angle of attack", u"機翼與相對氣流的夾角"],
            [u"失速", u"Stall", u"攻角過大，機翼失去升力"], [u"重飛", u"Go-around", u"放棄進場，重新爬升"],
            [u"最低下降高度", u"MDA", u"非精確進場時，沒看到跑道就不能低於的高度"], [u"跑道入侵", u"Runway incursion", u"未經許可進入使用中的跑道"],
            [u"微爆氣流", u"Microburst", u"雷雨下方強烈的下沉氣流"], [u"順槳", u"Feather", u"把螺旋槳葉片轉到與氣流平行，減少阻力，不產生推力"],
            [u"金屬疲勞", u"Metal fatigue", u"反覆受力下逐漸成長的裂紋"], [u"油箱惰化", u"Fuel tank inerting", u"以氮氣降低油箱可燃性"],
        ]),
    ],
}

GUIDE = {
    "file": "guide.html", "title": u"互動圖鑑", "h1": u"空難互動圖鑑", "icon": u"🗺️",
    "description": u"年表、事故圖鑑、瑞士乳酪模型與改進關係圖",
    "body": [
        ("raw", u"<script>%s</script>" % NVLIB),
        ("h", u"1. 年表（第 1 課）"), C.TIMELINE,
        ("h", u"2. 事故圖鑑"), C.CARDS,
        ("h", u"3. 瑞士乳酪模型（第 2 課）"), C.SWISS,
        ("h", u"4. 每一條規則背後的事故（第 73 課）"), C.GRAPH,
    ],
}

REFERENCES = [TABLE, TERMS, GUIDE]
