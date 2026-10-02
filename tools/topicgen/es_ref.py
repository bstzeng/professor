# -*- coding: utf-8 -*-
"""地海：參考頁——互動圖鑑、名詞表。"""
from nv_common import LS, NVLIB
import es_a, es_e

GUIDE = {
    "file": "guide.html", "title": u"地海互動圖鑑", "h1": u"地海互動圖鑑", "icon": u"🗺️",
    "description": u"閱讀順序、群島地圖、柔克九師傅、人物卡、地海歷史年表",
    "body": [
        ("raw", u"<script>%s</script>" % NVLIB),
        ("h", u"1. 六部作品（第 4 課）"), es_a._ORDER,
        ("h", u"2. 地海群島地圖（第 3 課）"), es_a._MAP,
        ("h", u"3. 柔克學院九師傅（第 7 課）"), es_a._MASTERS,
        ("h", u"4. 人物卡（第 23 課）"), es_e._CARDS,
        ("h", u"5. 地海歷史（第 27 課）"), es_e._HIST,
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"地海名詞表", "h1": u"地海名詞表", "icon": u"📖",
    "description": u"人物、地名與術語中英對照",
    "body": [
        ("t", [u"中文", u"原文", u"說明", u"課"],
         [[u"地海", u"Earthsea", u"由群島組成的世界", LS(1)], [u"真名", u"true name", u"萬物在太古語中的名字", LS(5)],
          [u"太古語", u"the Old Speech", u"創世的語言、龍的語言", LS(9)], [u"平衡", u"Equilibrium", u"魔法的核心原則", LS(6)],
          [u"柔克學院", u"the School on Roke", u"巫師學院", LS(7)], [u"大法師", u"Archmage", u"柔克學院的領袖", LS(7)],
          [u"弓忒島", u"Gont", u"格得與歐吉安的故鄉", LS(10)], [u"黑弗諾", u"Havnor", u"國王的首都", LS(3)],
          [u"卡耳格帝國", u"the Kargad Lands", u"東北方的帝國", LS(3)], [u"峨團", u"Atuan", u"陵墓所在的島", LS(15)],
          [u"無名者", u"the Nameless Ones", u"陵墓中的黑暗力量", LS(15)], [u"厄瑞亞拜之環", u"Ring of Erreth-Akbe", u"刻有和平符文的手環", LS(17)],
          [u"旱域", u"the Dry Land", u"死者之地", LS(21)], [u"偕勒多", u"Selidor", u"最西邊的島嶼", LS(22)],
          [u"兮果乙", u"Segoy", u"創世者", LS(9)], [u"韋德瑙", u"Verw nadan / Vedurnan", u"龍與人的分歧", LS(29)],
          [u"死者之牆", u"the wall of stones", u"古代巫師所建，把死者困在旱域", LS(28)], [u"女巫", u"witch", u"只會「低等」魔法的女性", LS(8)]]),
    ],
}

REFERENCES = [GUIDE, GLOSSARY]
