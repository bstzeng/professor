# -*- coding: utf-8 -*-
"""最終幻想：參考頁——互動工具箱與人物速查。"""
from gm_common import *
from gm_common import GMLIB
import ff_a, ff_e

_CARDS = nvw({"t": "cards", "q": u"歷代主要人物（可依作品篩選或搜尋）：",
  "groups": [["c", u"FF1～3", CK], ["s", u"FF4～6", CO], ["7", u"FF7", CB], ["p", u"FF8～9", CP], ["x", u"FF10", CT], ["i", u"FF12／戰略版", CY], ["n", u"FF13", CG], ["m", u"FF15～16", CR]],
  "cards": [card(u"光之戰士", "c", u"FF1 的四位主角。"), card(u"加蘭德", "c", u"FF1 的騎士，即混沌。"), card(u"弗利奧尼爾", "c", u"FF2 的主角，野玫瑰反抗軍。"),
            card(u"塞西爾", "s", u"FF4 的暗黑騎士，成為聖騎士。"), card(u"凱因", "s", u"FF4 的龍騎士，塞西爾的摯友。"), card(u"巴茲", "s", u"FF5 的旅人。"), card(u"艾克斯迪斯", "s", u"FF5 的反派，樹木化身的魔導士。"),
            card(u"蒂娜", "s", u"FF6 半人半幻獸的少女。"), card(u"洛克", "s", u"FF6 自稱寶藏獵人的青年。"), card(u"凱夫卡", "s", u"FF6 的小丑魔導士，毀滅世界。"),
            card(u"克勞德", "7", u"FF7 的前神羅士兵（自稱）。"), card(u"蒂法", "7", u"克勞德的青梅竹馬。"), card(u"艾莉絲", "7", u"古代種的最後血脈。"), card(u"薩菲羅斯", "7", u"英雄化身的反派。"), card(u"扎克斯", "7", u"危機核心的主角。"),
            card(u"斯寇爾", "p", u"FF8 的 SeeD 學員。"), card(u"莉諾雅", "p", u"FF8 的反抗組織少女，繼承魔女之力。"), card(u"魔女阿爾提米希亞", "p", u"FF8 的未來魔女。"),
            card(u"吉坦", "p", u"FF9 的盜賊，加蘭德所造。"), card(u"比比", "p", u"FF9 的黑魔導士。"), card(u"庫加", "p", u"FF9 的反派。"),
            card(u"提達", "x", u"FF10 來自夢之薩納爾罕的球員。"), card(u"尤娜", "x", u"FF10 的召喚士。"), card(u"傑克特", "x", u"提達的父親，成為「辛」。"),
            card(u"梵", "i", u"FF12 的少年。"), card(u"艾希", "i", u"FF12 達爾馬斯卡的公主。"), card(u"巴爾弗雷亞", "i", u"FF12 的天空海盜。"), card(u"芙蘭", "i", u"FF12 維埃拉族的夥伴。"),
            card(u"拉姆薩", "i", u"戰略版的主角，被歷史抹去的英雄。"), card(u"迪利塔", "i", u"拉姆薩的摯友，成為國王。"),
            card(u"雷光", "n", u"FF13 的前士兵。"), card(u"斯諾", "n", u"FF13 的反抗組織領袖。"), card(u"霍普", "n", u"FF13 的少年。"), card(u"瑟拉", "n", u"雷光的妹妹。"),
            card(u"諾克提斯", "m", u"FF15 的王子。"), card(u"露娜", "m", u"FF15 的神巫。"), card(u"阿汀", "m", u"FF15 的反派。"), card(u"伊格尼斯", "m", u"FF15 的軍師。"), card(u"格拉迪歐拉斯", "m", u"FF15 的護衛。"), card(u"普羅恩普特", "m", u"FF15 的好友。"),
            card(u"克萊夫", "m", u"FF16 的主角。"), card(u"吉兒", "m", u"FF16 克萊夫的青梅竹馬。"), card(u"約夏", "m", u"FF16 克萊夫的弟弟。"), card(u"究極", "m", u"FF16 的神。")]})

GUIDE = {
    "file": "guide.html", "title": u"FF 互動工具箱", "h1": u"FF 互動工具箱", "icon": u"🧭",
    "description": u"發行年表、共通元素、FF7 年表、召喚獸、席德、人物關係、全系列結局",
    "body": [
        ("raw", u"<script>%s</script><script>%s</script>" % (NVLIB, GMLIB)),
        ("p", u"本頁集中課程中的互動工具。內容有完整劇情暴雷。"),
        ("h", u"1. 發行年表（第 1 課）"), ff_a._REL,
        ("h", u"2. 共通元素（第 2 課）"), ff_a._COMMON,
        ("h", u"3. FF7 的宇宙（第 16～23 課）"), ff_a._FF7,
        ("h", u"4. 人物關係（第 8、24 課）"), ff_a._P4, ff_a._P8,
        ("h", u"5. 召喚獸與席德（第 52、54 課）"), ff_e._SUM, ff_e._CID,
        ("h", u"6. 全系列結局對照（第 53 課）"), ff_e._ALL,
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"人物與名詞速查", "h1": u"人物與名詞速查", "icon": u"📖",
    "description": u"歷代主要人物、世界與名詞",
    "body": [
        ("raw", u"<script>%s</script>" % NVLIB),
        _CARDS,
        ("h", u"歷代世界速查"),
        ("t", [u"作品", u"年份", u"世界", u"課"],
         [[u"FF1", u"1987", u"四顆水晶的世界", LS(4)], [u"FF4", u"1991", u"巴隆王國與月亮", LS(8)], [u"FF6", u"1994", u"魔導與帝國", LS(12)], [u"FF7", u"1997", u"星球與神羅", LS(16)],
          [u"FF8", u"1999", u"花園與魔女", LS(24)], [u"FF9", u"2000", u"蓋亞", LS(27)], [u"FF10", u"2001", u"斯匹拉", LS(30)], [u"FF12", u"2006", u"伊瓦利斯", LS(35)],
          [u"FF13", u"2009", u"繭與脈衝", LS(40)], [u"FF15", u"2016", u"伊歐斯", LS(44)], [u"FF16", u"2023", u"瓦利斯傑亞", LS(47)]]),
        ("h", u"名詞"),
        ("t", [u"名詞", u"說明", u"課"],
         [[u"水晶", u"系列的核心象徵", LS(2)], [u"ATB", u"即時戰鬥系統", LS(8)], [u"魔晄", u"FF7 星球的生命能量", LS(16)], [u"SeeD", u"FF8 的傭兵", LS(24)],
          [u"祈子", u"FF10 的夢之存在", LS(32)], [u"露希", u"FF13 被神賦予使命的人", LS(40)], [u"顯化者", u"FF16 召喚獸的宿主", LS(47)]]),
    ],
}

REFERENCES = [GUIDE, GLOSSARY]
