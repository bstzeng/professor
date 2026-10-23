# -*- coding: utf-8 -*-
"""魔術方塊：參考頁——相機解方塊工具、公式速查。"""
from rb_common import *
from rb_c import _OLLC, _PLL

GUIDE = {
    "file": "guide.html", "title": u"相機解方塊", "h1": u"📷 相機解方塊", "icon": u"📷",
    "description": u"拍照六面、校正顏色、自動辨識，算出最短解並用 3D 動畫與逐步示意圖帶你轉",
    "body": [
        ("raw", u"<script>%s</script>" % RBLIB),
        ("raw", u"<script>%s</script>" % RBSOLVE),
        ("p", u"用手機後鏡頭或電腦相機拍下方塊的六個面，工具會辨識顏色、檢查方塊是否合法，再用科先巴兩階段演算法算出解法（通常 18～21 步）。"
              u"所有處理都在你的瀏覽器裡完成，不會上傳任何影像。拍攝順序與原理見" + LS(22) + u"。"),
        ("t", [u"順序", u"朝向鏡頭的中心", u"朝上的中心"],
         [[u"1", u"黃", u"藍"], [u"2", u"橘", u"黃"], [u"3", u"綠", u"黃"], [u"4", u"白", u"綠"], [u"5", u"紅", u"黃"], [u"6", u"藍", u"黃"]]),
        SCAN,
        ("h", u"沒有實體方塊？用虛擬方塊試試"),
        rbw({"t": "free", "q": u"打亂、自己轉，或讓電腦求解並播放："}),
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"魔術方塊公式速查", "h1": u"魔術方塊公式速查", "icon": u"📖",
    "description": u"記號、層先法七步、兩步 OLL／PLL 公式一覽",
    "body": [
        ("raw", u"<script>%s</script>" % RBLIB),
        ("h", u"1. 記號"),
        ("t", [u"記號", u"意思", u"課"],
         [[alg("R L U D F B"), u"右、左、上、下、前、後面，正對該面順時針 90°", LS(2)], [alg("R'"), u"逆時針 90°", LS(2)], [alg("R2"), u"180°", LS(2)],
          [alg("M E S"), u"中層（M 同 L、E 同 D、S 同 F）", LS(2)], [alg("x y z"), u"整顆轉（同 R、U、F）", LS(2)], [alg("r f u"), u"寬層（兩層一起）", LS(2)]]),
        ("h", u"2. 層先法"),
        ("t", [u"步驟", u"公式", u"課"],
         [[u"白十字", u"直覺（F2、U' R' F R、F）", LS(4)],
          [u"白色角塊", alg("R U R' U'") + u" 重複 1／3／5 次", LS(5)],
          [u"第二層（往右／往左）", alg("U R U' R' U' F' U F") + u"<br>" + alg("U' L' U L U F U' F'"), LS(6)],
          [u"黃十字", alg("F R U R' U' F'"), LS(7)],
          [u"黃邊對齊", alg("R U R' U R U2 R' U"), LS(8)],
          [u"黃角歸位", alg("U R U' L' U R' U' L"), LS(9)],
          [u"黃角翻轉", alg("R' D' R D") + u" 重複 2／4 次，只轉 U 換角", LS(10)]]),
        ("h", u"3. 兩步 OLL"),
        ("t", [u"情況", u"公式", u"課"],
         [[u"一字", alg("F R U R' U' F'"), LS(15)], [u"L 形", alg("F U R U' R' F'"), LS(15)], [u"點", alg("F R U R' U' F' f R U R' U' f'"), LS(15)]] +
         [[n, alg(a), LS(16)] for n, a, _ in _OLLC]),
        rbw({"t": "net", "q": u"翻角七種情況：", "items": [{"alg": a, "mask": "oll", "label": n} for n, a, _ in _OLLC]}),
        ("h", u"4. 兩步 PLL"),
        ("t", [u"情況", u"辨認", u"公式", u"課"], [[n, d, alg(a), LS(17 if i < 2 else 18)] for i, (n, a, d) in enumerate(_PLL)]),
        ("h", u"5. 數字"),
        ("t", [u"項目", u"數值", u"課"],
         [[u"可轉到的狀態數", u"43,252,003,274,489,856,000", LS(19)], [u"上帝之數（半轉計步）", u"20（2010 年證明）", LS(20)],
          [u"上帝之數（四分之一轉計步）", u"26（2014 年證明）", LS(20)], [u"任何十字最多", u"8 步", LS(4)], [u"sexy move 的週期", u"6", LS(3)]]),
    ],
}

REFERENCES = [GUIDE, GLOSSARY]
