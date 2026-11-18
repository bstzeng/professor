# -*- coding: utf-8 -*-
"""異塵餘生 Fallout 全紀錄：參考頁——作品與名詞、互動圖鑑。"""
from nv_common import LS, NVLIB
import flo_common as C

TERMS = {
    "file": "terms.html", "title": u"作品與名詞", "h1": u"Fallout 作品與名詞對照", "icon": u"📚",
    "description": u"歷代作品與常見名詞的中英對照",
    "body": [
        ("h", u"歷代作品"),
        ("t", [u"作品", u"年份", u"開發", u"舞台", u"課"], [
            [u"Fallout（異塵餘生）", u"1997", u"Interplay", u"南加州，2161", LS(8)], [u"Fallout 2", u"1998", u"黑島工作室", u"北加州，2241", LS(9)],
            [u"Fallout Tactics", u"2001", u"Micro Forté", u"美國中西部", LS(10)], [u"Fallout: Brotherhood of Steel", u"2004", u"Interplay", u"美國西南部", LS(10)],
            [u"Fallout 3", u"2008", u"Bethesda Game Studios", u"華盛頓特區，2277", LS(11)], [u"Fallout: New Vegas（新維加斯）", u"2010", u"黑曜石娛樂", u"莫哈維，2281", LS(12)],
            [u"Fallout Shelter", u"2015", u"Bethesda／Behaviour", u"避難所", LS(13)], [u"Fallout 4", u"2015", u"Bethesda Game Studios", u"波士頓，2287", LS(13)],
            [u"Fallout 76", u"2018", u"Bethesda Game Studios", u"西維吉尼亞，2102", LS(14)], [u"影集 Fallout", u"2024～", u"Amazon Prime Video", u"洛杉磯、新維加斯，2296", LS(15)],
        ]),
        ("h", u"常見名詞"),
        ("t", [u"中文", u"英文", u"說明", u"課"], [
            [u"大戰", u"the Great War", u"2077 年 10 月 23 日的核戰", LS(3)], [u"避難所", u"Vault", u"Vault-Tec 建造的地下避難所", LS(4)],
            [u"監督者", u"Overseer", u"避難所的管理者", LS(4)], [u"屍鬼", u"Ghoul", u"受輻射而變異、壽命極長的人", LS(5)],
            [u"超級變種人", u"Super Mutant", u"FEV 造成的變種人", LS(5)], [u"強制進化病毒", u"FEV", u"Forced Evolutionary Virus", LS(5)],
            [u"嗶嗶小子", u"Pip-Boy", u"手腕上的個人電腦", LS(6)], [u"伊甸園創造套件", u"G.E.C.K.", u"Garden of Eden Creation Kit", LS(6)],
            [u"死亡爪", u"Deathclaw", u"廢土上最危險的生物之一", LS(5)], [u"婆羅門", u"Brahmin", u"雙頭牛", LS(5)],
            [u"合成人", u"Synth", u"學院製造的人造人", LS(21)], [u"Vault-Tec 輔助瞄準系統", u"V.A.T.S.", u"Vault-Tec Assisted Targeting System", LS(28)],
        ]),
        ("p", u"中文名稱以台灣常見的譯名為主；部分名詞沒有通用的官方譯名，不同版本或社群的譯法可能不同。"),
    ],
}

GUIDE = {
    "file": "guide.html", "title": u"廢土互動圖鑑", "h1": u"Fallout 互動圖鑑", "icon": u"🗺️",
    "description": u"發行年表、世界歷史、避難所、地圖、勢力與 S.P.E.C.I.A.L. 配點器",
    "body": [
        ("raw", u"<script>%s</script>" % NVLIB),
        ("h", u"1. 發行年表（第 1 課）"), C.GAMES,
        ("h", u"2. 世界的歷史（第 3 課）"), C.LORE,
        ("h", u"3. 避難所實驗（第 4 課）"), C.VAULTS,
        ("h", u"4. 各代的舞台（第 16 課）"), C.MAP,
        ("h", u"5. 主要勢力（第 21 課）"), C.FACTIONS,
        ("h", u"6. S.P.E.C.I.A.L. 配點器（第 27 課）"), C.SPECIAL,
    ],
}

REFERENCES = [TERMS, GUIDE]
