# -*- coding: utf-8 -*-
"""駕駛艙儀表全圖解：參考頁——速查表、儀表模擬器。"""
from ck_common import LS, XL, CKLIB, inst, nd, fig
from ck_a import cockpit_map

CHEATSHEET = {
    "file": "cheatsheet.html",
    "title": u"駕駛艙速查表",
    "h1": u"駕駛艙儀表速查表",
    "icon": u"🗂️",
    "description": u"縮寫中英對照、顏色規則、重要語音警告與每塊面板的位置，一頁查完",
    "body": [
        ("h", u"1. 駕駛艙地圖"),
        ("fig", cockpit_map(), "0 0 640 420", u"點擊區塊跳到對應課程。"),
        ("h", u"2. 常見縮寫"),
        ("t", [u"縮寫", u"英文", u"中文", u"課"],
         [[u"PFD", u"Primary Flight Display", u"主飛行顯示器", LS(12)], [u"ND", u"Navigation Display", u"導航顯示器", LS(18)],
          [u"ECAM／EICAS", u"Electronic Centralised Aircraft Monitor／Engine Indicating and Crew Alerting System", u"中央警告與系統顯示", LS(24)],
          [u"FMA", u"Flight Mode Annunciator", u"飛行模式顯示", LS(17)], [u"FD", u"Flight Director", u"飛行導引指示", LS(14)],
          [u"FCU／MCP", u"Flight Control Unit／Mode Control Panel", u"自動駕駛面板", LS(29)], [u"AP／A/THR", u"Autopilot／Autothrust", u"自動駕駛／自動油門", LS(30)],
          [u"EFIS", u"Electronic Flight Instrument System", u"電子飛行儀表（控制面板）", LS(31)], [u"MCDU／CDU", u"(Multipurpose) Control Display Unit", u"飛航管理電腦操作單元", LS(36)],
          [u"FMS", u"Flight Management System", u"飛航管理系統", LS(36)], [u"RMP", u"Radio Management Panel", u"無線電管理面板", LS(37)],
          [u"TCAS", u"Traffic Collision Avoidance System", u"空中防撞系統", LS(21)], [u"EGPWS", u"Enhanced Ground Proximity Warning System", u"增強型近地警告系統", LS(22)],
          [u"ILS", u"Instrument Landing System", u"儀器降落系統", LS(16)], [u"N1／N2／EGT／FF", u"Fan speed／Core speed／Exhaust Gas Temp／Fuel Flow", u"風扇轉速／核心轉速／排氣溫度／燃油流量", LS(23)],
          [u"APU", u"Auxiliary Power Unit", u"輔助動力單元", LS(46)], [u"PTU", u"Power Transfer Unit", u"動力轉換單元", LS(42)],
          [u"RAT", u"Ram Air Turbine", u"衝壓空氣渦輪", LS(41)], [u"ISIS／ISFD", u"Integrated Standby Instrument System／Integrated Standby Flight Display", u"整合式備用儀表", LS(48)]]),
        ("h", u"3. 顏色規則（常見原則）"),
        ("t", [u"顏色", u"燈號", u"螢幕"],
         [[u"紅", u"警告，立即處理", u"警告、限制"], [u"琥珀", u"注意，需要處理", u"注意"], [u"綠", u"正常運作", u"啟用中的模式、正常值"],
          [u"藍（青）", u"暫時使用、待命", u"預備模式、可選擇的值、處置步驟"], [u"白", u"開關不在正常位置", u"刻度、標示"], [u"洋紅", u"—", u"目標值、航路（依機型）"]]),
        ("h", u"4. 重要語音警告"),
        ("t", [u"語音", u"來源", u"意思", u"課"],
         [[u"Traffic, traffic", u"TCAS", u"附近有飛機（提示）", LS(21)], [u"Climb, climb／Descend, descend", u"TCAS", u"立即照做", LS(21)],
          [u"Terrain, pull up", u"EGPWS", u"立即拉升", LS(22)], [u"Sink rate", u"EGPWS", u"下降率過大", LS(22)],
          [u"Windshear", u"風切警告", u"遇到風切", LS(28)], [u"Stall", u"失速警告", u"接近失速", LS(13)],
          [u"Retard", u"自動報讀（Airbus）", u"落地時收油門", LS(34)], [u"Five hundred…Ten", u"無線電高度報讀", u"離地高度", LS(15)]]),
        ("p", u"這些儀表在一趟航班中的使用，見 " + XL("fo") + u"。"),
    ],
}

SIM = {
    "file": "simulator.html",
    "title": u"儀表模擬器",
    "h1": u"駕駛艙儀表模擬器",
    "icon": u"🕹️",
    "description": u"六大儀表、主飛行顯示器、導航顯示器、引擎警告顯示與自動駕駛面板，全部可以操作",
    "body": [
        ("raw", u"<script>%s</script>" % CKLIB),
        ("p", u"所有模擬器都是<strong>簡化示意</strong>，用來理解儀表怎麼讀，不是真實的飛行模型。"),
        ("h", u"1. 六大儀表"),
        inst({"t": "six", "sl": True, "pre": [[u"平飛", {"pitch": 2, "roll": 0, "vs": 0, "ias": 250}], [u"爬升", {"pitch": 10, "roll": 0, "vs": 2500}],
                                               [u"下降", {"pitch": -3, "roll": 0, "vs": -1800}], [u"右轉", {"pitch": 3, "roll": 25, "vs": 0, "ias": 220}]]}),
        ("h", u"2. 主飛行顯示器"),
        inst({"t": "pfd", "sl": True, "v": {"ils": 1, "ra": 2600}}, 480),
        ("h", u"3. 導航顯示器"),
        nd(v={"mode": "ARC"}, ctl=["mode", "range", "wx", "terr", "tcas", "hdg"]),
        ("h", u"4. 引擎與警告顯示"),
        inst({"t": "ecam", "ctl": 1, "scn": 1, "thr": 30}, 480),
        ("h", u"5. 自動駕駛面板"),
        inst({"t": "fcu"}, 520),
    ],
}

REFERENCES = [CHEATSHEET, SIM]
