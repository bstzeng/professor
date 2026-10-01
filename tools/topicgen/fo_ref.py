# -*- coding: utf-8 -*-
"""一趟航班的幕後：參考頁——速查表、三方時間軸。"""
from fo_common import LS, XL, FOLIB, widget
from fo_g import _TL

CHEATSHEET = {
    "file": "cheatsheet.html",
    "title": u"航班速查表",
    "h1": u"一趟航班的幕後：速查表",
    "icon": u"🗂️",
    "description": u"音標字母、常用無線電用語、特殊應答機代碼、航管單位與飛行階段，一頁查完",
    "body": [
        ("h", u"1. 音標字母"),
        ("t", [u"A–I", u"J–R", u"S–Z"],
         [[u"A Alfa", u"J Juliett", u"S Sierra"], [u"B Bravo", u"K Kilo", u"T Tango"], [u"C Charlie", u"L Lima", u"U Uniform"],
          [u"D Delta", u"M Mike", u"V Victor"], [u"E Echo", u"N November", u"W Whiskey"], [u"F Foxtrot", u"O Oscar", u"X X-ray"],
          [u"G Golf", u"P Papa", u"Y Yankee"], [u"H Hotel", u"Q Quebec", u"Z Zulu"], [u"I India", u"R Romeo", u"數字 3 Tree、5 Fife、9 Niner"]]),
        ("h", u"2. 常用無線電用語"),
        ("t", [u"用語", u"意思", u"課"],
         [[u"Roger / Wilco", u"收到／收到會照做", LS(3)], [u"Say again", u"請重複", LS(3)],
          [u"Hold short", u"在跑道（或指定點）外停下等候", LS(12)],
          [u"Line up and wait", u"進跑道等候（不是起飛許可）", LS(13)],
          [u"Cleared for takeoff / to land", u"可以起飛／可以落地", LS(13)],
          [u"Go around", u"重飛", LS(26)], [u"MAYDAY / PAN-PAN", u"遇險／緊急", LS(21)]]),
        ("h", u"3. 特殊應答機代碼"),
        ("t", [u"代碼", u"意思"], [[u"7500", u"非法干擾（劫機）"], [u"7600", u"無線電通訊失效"], [u"7700", u"一般緊急"]]),
        ("h", u"4. 航管單位"),
        ("t", [u"單位", u"負責", u"課"],
         [[u"許可頒發", u"發航管許可", LS(31)], [u"地面管制", u"機坪與滑行道", LS(32)], [u"塔台", u"跑道與機場附近", LS(33)],
          [u"近場／離場", u"機場周邊數十海里", LS(35)], [u"區域管制", u"高空航路", LS(36)]]),
        ("h", u"5. 起飛與降落的關鍵詞"),
        ("t", [u"詞", u"意思", u"課"],
         [[u"V1", u"決斷速度：之後不再中止起飛", LS(7)], [u"VR", u"抬頭速度", LS(7)], [u"V2", u"起飛安全速度", LS(7)],
          [u"轉換高度", u"切換高度表撥定（QNH ↔ 1013.25）", LS(17)],
          [u"穩定進場", u"1000 呎（儀器）／500 呎（目視）前要穩定", LS(25)],
          [u"決斷高度", u"看不到跑道就重飛", LS(25)]]),
        ("h", u"6. 客艙"),
        ("t", [u"詞", u"意思", u"課"],
         [[u"滑梯預位（Armed）", u"開門時滑梯自動彈出", LS(43)], [u"互相檢查（Cross-check）", u"另一位空服員再確認", LS(43)],
          [u"無菌駕駛艙", u"關鍵階段只談安全", LS(5)], [u"90 秒撤離", u"認證時的撤離時間標準", LS(45)]]),
        ("p", u"駕駛艙的面板與儀表，見 " + XL("ck") + u"。"),
    ],
}

TIMELINE = {
    "file": "timeline.html",
    "title": u"三方時間軸",
    "h1": u"三方同步時間軸：機師、航管、空服",
    "icon": u"⏱️",
    "description": u"同一時刻，駕駛艙、航管與客艙各在做什麼",
    "body": [
        ("raw", u"<script>%s</script>" % FOLIB),
        ("p", u"拉動滑桿，或看下方的完整表格（以短程國際線為例，時間為大約值；各航空公司與機場不同）。"),
        widget({"t": "tl", "q": u"<b>時間軸：</b>", "s": _TL}),
        ("t", [u"時間", u"✈️ 機師", u"📡 航管", u"🧳 空服"], [list(r) for r in _TL]),
        ("p", u"詳細說明見 " + LS(47) + u"。"),
    ],
}

REFERENCES = [CHEATSHEET, TIMELINE]
