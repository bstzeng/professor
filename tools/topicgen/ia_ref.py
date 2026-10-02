# -*- coding: utf-8 -*-
"""冰與火之歌：參考頁——互動圖鑑、名詞表。"""
from nv_common import LS, NVLIB
import ia_a, ia_e

GUIDE = {
    "file": "guide.html", "title": u"冰與火之歌互動圖鑑", "h1": u"冰與火之歌互動圖鑑", "icon": u"🗺️",
    "description": u"閱讀順序、萬年年表、家族關係圖、維斯特洛地圖、人物卡、五王之戰、書劇差異、改編年表",
    "body": [
        ("raw", u"<script>%s</script>" % NVLIB),
        ("h", u"1. 閱讀順序（第 4 課）"), ia_a._ORDER,
        ("h", u"2. 維斯特洛年表（第 5 課）"), ia_a._HIST,
        ("h", u"3. 家族關係圖（第 11 課）"), ia_a._HOUSES,
        ("h", u"4. 人物卡（第 18 課）"), ia_a._CARDS,
        ("h", u"5. 五王之戰（第 29 課）"), ia_e._WAR,
        ("h", u"6. 改編年表（第 52 課）"), ia_e._ADAPT,
        ("h", u"7. 書與影集的差異（第 52 課）"), ia_e._TV,
        ("h", u"8. 維斯特洛地圖（第 1 課）"), ia_a._MAP,
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"冰與火之歌名詞表", "h1": u"冰與火之歌名詞表", "icon": u"📖",
    "description": u"地名、組織、物品與術語中英對照",
    "body": [
        ("t", [u"中文", u"原文", u"說明", u"課"],
         [[u"維斯特洛", u"Westeros", u"七大王國所在的大陸", LS(1)], [u"厄斯索斯", u"Essos", u"狹海以東的大陸", LS(21)],
          [u"鐵王座", u"Iron Throne", u"以千把劍熔鑄的王座", LS(8)], [u"國王之手", u"Hand of the King", u"國王的首相", LS(24)],
          [u"御林鐵衛", u"Kingsguard", u"國王的七名貼身騎士", LS(12)], [u"守夜人", u"Night's Watch", u"守護長城的黑衣弟兄", LS(19)],
          [u"異鬼", u"the Others", u"北方的冰冷生物", LS(20)], [u"屍鬼", u"wights", u"被異鬼復活的死者", LS(20)],
          [u"森林之子", u"Children of the Forest", u"維斯特洛最早的居民", LS(5)], [u"先民", u"First Men", u"最早的人類移民", LS(5)],
          [u"心樹", u"heart tree", u"刻有人臉的魚梁木", LS(5)], [u"龍晶", u"dragonglass", u"黑曜石，能殺死異鬼", LS(20)],
          [u"瓦雷利亞鋼", u"Valyrian steel", u"魔法鍛造的鋼", LS(7)], [u"野火", u"wildfire", u"綠色、無法撲滅的燃燒劑", LS(32)],
          [u"無垢者", u"Unsullied", u"奴隸士兵", LS(41)], [u"無面者", u"Faceless Men", u"布拉佛斯的刺客", LS(40)],
          [u"鐵金庫", u"Iron Bank", u"布拉佛斯的銀行", LS(21)], [u"卡奧", u"khal", u"多斯拉克的首領", LS(27)],
          [u"易形者", u"skinchanger / warg", u"附身動物的人", LS(23)], [u"綠先知", u"greenseer", u"透過心樹觀看的人", LS(23)],
          [u"賓客權利", u"guest right", u"吃過麵包與鹽的客人受保護", LS(34)], [u"決鬥審判", u"trial by combat", u"以決鬥決定罪名", LS(36)],
          [u"凡人皆須一死", u"Valar Morghulis", u"無面者的問候", LS(40)], [u"被應許的王子", u"the prince that was promised", u"預言中的英雄", LS(47)]]),
    ],
}

REFERENCES = [GUIDE, GLOSSARY]
