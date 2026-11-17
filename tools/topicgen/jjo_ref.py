# -*- coding: utf-8 -*-
"""JoJo：參考頁——互動圖鑑與名詞表。"""
from nv_common import LS, NVLIB
import jjo_common as C

GUIDE = {
    "file": "guide.html", "title": u"JoJo 互動圖鑑", "h1": u"JoJo 互動圖鑑", "icon": u"🗺️",
    "description": u"年表、喬斯達家族、替身圖鑑、星塵鬥士旅程地圖",
    "body": [
        ("raw", u"<script>%s</script>" % NVLIB),
        ("h", u"1. 年表（第 1 課）"), C.WORKS,
        ("h", u"2. 喬斯達家族（第 3 課）"), C.FAMILY,
        ("h", u"3. 替身圖鑑（第 33 課）"), C.STANDS,
        ("h", u"4. 星塵鬥士的旅程（第 11 課）"), C.ROUTE,
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"名詞表", "h1": u"JoJo 名詞表", "icon": u"📖",
    "description": u"人物、能力與名詞中日英對照",
    "body": [
        ("t", [u"中文", u"原文／英文", u"說明", u"課"], [
            [u"波紋", u"波紋（Hamon / Ripple）", u"呼吸產生的太陽能量", LS(5)],
            [u"石鬼面", u"石仮面（Stone Mask）", u"把人變成吸血鬼的面具", LS(4)],
            [u"柱之男", u"柱の男（Pillar Men）", u"石鬼面的製造者", LS(8)],
            [u"艾哲紅石", u"エイジャの赤石（Red Stone of Aja）", u"增幅波紋的寶石", LS(9)],
            [u"替身", u"スタンド（Stand）", u"精神能量的具象化", LS(10)],
            [u"弓與箭", u"弓と矢（Bow and Arrow）", u"讓人覺醒替身", LS(15)],
            [u"鎮魂曲", u"レクイエム（Requiem）", u"被箭再刺一次的替身進化", LS(22)],
            [u"天國", u"天国（Heaven）", u"迪奧與普奇的目標", LS(24)],
            [u"宇宙一巡", u"一巡（Universe reset）", u"天堂製造讓宇宙重來", LS(25)],
            [u"旋轉", u"回転（Spin）", u"齊貝林家族的鐵球技術", LS(28)],
            [u"黃金迴轉", u"黄金の回転（Golden Spin）", u"依黃金比例的旋轉", LS(28)],
            [u"聖人遺體", u"聖なる遺体（Saint's Corpse）", u"第七部的核心", LS(29)],
            [u"壁之眼", u"壁の目（Wall Eyes）", u"震災後隆起的岩壁", LS(30)],
            [u"洛卡卡卡", u"ロカカカ（Locacaca）", u"等價交換的果實", LS(31)],
            [u"岩人", u"岩人間（Rock Humans）", u"以岩石為基礎的生命", LS(31)],
            [u"黃金的精神", u"黄金の精神（Golden Spirit）", u"勇氣、正直、犧牲", LS(36)],
            [u"漆黑的意志", u"漆黒の意思（Pitch-Black Will）", u"為目的不擇手段", LS(36)],
            [u"JoJo 立", u"ジョジョ立ち", u"誇張的姿勢", LS(2)],
        ]),
    ],
}

REFERENCES = [GUIDE, GLOSSARY]
