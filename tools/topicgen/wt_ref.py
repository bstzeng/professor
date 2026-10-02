# -*- coding: utf-8 -*-
"""時光之輪：參考頁——互動圖鑑、名詞表。"""
from nv_common import LS, NVLIB
import wt_a, wt_e

GUIDE = {
    "file": "guide.html", "title": u"時光之輪互動圖鑑", "h1": u"時光之輪互動圖鑑", "icon": u"🗺️",
    "description": u"閱讀順序、世界年表、勢力卡、兩河人物圖、大陸地圖、影集差異、與冰與火之歌比較",
    "body": [
        ("raw", u"<script>%s</script>" % NVLIB),
        ("h", u"1. 十五本書與閱讀策略（第 4 課）"), wt_a._ORDER,
        ("h", u"2. 世界年表（第 8 課）"), wt_a._TL,
        ("h", u"3. 主要勢力（第 12 課）"), wt_a._FACT,
        ("h", u"4. 兩河的主角們（第 19 課）"), wt_a._FIVE,
        ("h", u"5. 大陸地圖（第 30 課）"), wt_e._MAP,
        ("h", u"6. 影集與原著差異（第 47 課）"), wt_e._TV,
        ("h", u"7. 與冰與火之歌比較（第 49 課）"), wt_e._COMP,
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"時光之輪名詞表", "h1": u"時光之輪名詞表", "icon": u"📖",
    "description": u"世界觀、組織與術語中英對照",
    "body": [
        ("t", [u"中文", u"原文", u"說明", u"課"],
         [[u"紋路", u"the Pattern", u"時光之輪編織的命運掛毯", LS(5)], [u"時軸人", u"ta'veren", u"紋路圍繞其編織的人", LS(5)],
          [u"至上力", u"the One Power", u"魔法的總稱", LS(7)], [u"陽極力／陰極力", u"saidin / saidar", u"男性與女性的力量", LS(7)],
          [u"導引", u"channeling", u"使用至上力", LS(7)], [u"炎火", u"balefire", u"把目標從紋路中抹去的編織", LS(7)],
          [u"暗帝", u"the Dark One / Shai'tan", u"被囚禁的邪惡存在", LS(8)], [u"鑽孔", u"the Bore", u"暗帝牢獄上的洞", LS(8)],
          [u"世界崩毀", u"the Breaking", u"男性導引者發瘋造成的災難", LS(8)], [u"被棄者", u"the Forsaken", u"投靠暗帝的十三位兩儀師", LS(9)],
          [u"轉生真龍", u"the Dragon Reborn", u"轉世的盧斯·瑟林", LS(10)], [u"夢境世界", u"Tel'aran'rhiod", u"與現實平行的夢之國度", LS(11)],
          [u"兩儀師", u"Aes Sedai", u"女性導引者組織", LS(12)], [u"玉座", u"the Amyrlin Seat", u"白塔的領袖", LS(12)],
          [u"宗", u"Ajah", u"白塔的派系", LS(13)], [u"護法", u"Warder", u"與兩儀師羈絆的戰士", LS(14)],
          [u"節義", u"ji'e'toh", u"艾伊爾人的榮譽規範", LS(15)], [u"達曼／蘇達姆", u"damane / sul'dam", u"被拴住者與拴住者", LS(17)],
          [u"獸魔人", u"Trollocs", u"暗影的怪物大軍", LS(18)], [u"魔達奧", u"Myrddraal", u"無眼的「半人」", LS(18)],
          [u"阿沙曼", u"Asha'man", u"男性導引者組織", LS(31)], [u"最後之戰", u"Tarmon Gai'don", u"光明與暗影的決戰", LS(41)]]),
    ],
}

REFERENCES = [GUIDE, GLOSSARY]
