# -*- coding: utf-8 -*-
"""納尼亞傳奇：參考頁——互動圖鑑、名詞表。"""
from nv_common import LS, NVLIB
import nr_a, nr_e

GUIDE = {
    "file": "guide.html", "title": u"納尼亞互動圖鑑", "h1": u"納尼亞互動圖鑑", "icon": u"🗺️",
    "description": u"閱讀順序、納尼亞年表、地圖、人物卡、七行星理論、改編年表",
    "body": [
        ("raw", u"<script>%s</script>" % NVLIB),
        ("h", u"1. 兩種閱讀順序（第 4 課）"), nr_a._ORDER,
        ("h", u"2. 納尼亞地圖（第 5 課）"), nr_a._MAP,
        ("h", u"3. 納尼亞年表（第 5 課）"), nr_a._TL,
        ("h", u"4. 人物卡（第 1 課）"), nr_a._CARDS,
        ("h", u"5. 七行星理論（第 35 課）"), nr_e._PLANETS,
        ("h", u"6. 改編年表（第 39 課）"), nr_e._ADAPT,
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"納尼亞名詞表", "h1": u"納尼亞名詞表", "icon": u"📖",
    "description": u"人物、地名與物品中英對照",
    "body": [
        ("t", [u"中文", u"原文", u"說明", u"課"],
         [[u"納尼亞", u"Narnia", u"亞斯蘭創造的國度", LS(1)], [u"亞斯蘭", u"Aslan", u"偉大的獅子", LS(8)],
          [u"凱爾帕拉維爾", u"Cair Paravel", u"納尼亞國王的城堡", LS(9)], [u"石桌", u"Stone Table", u"亞斯蘭犧牲的地方", LS(8)],
          [u"更深的魔法", u"Deep Magic", u"石桌上的律法", LS(8)], [u"路燈柱", u"lamp-post", u"由鐵條長成", LS(28)],
          [u"台爾馬人", u"Telmarines", u"征服納尼亞的人類", LS(10)], [u"卡羅門", u"Calormen", u"南方的帝國", LS(22)],
          [u"亞欽蘭", u"Archenland", u"納尼亞南邊的小國", LS(25)], [u"塔胥", u"Tash", u"卡羅門的神", LS(30)],
          [u"恰恩", u"Charn", u"潔蒂絲毀滅的世界", LS(27)], [u"毀滅之詞", u"the Deplorable Word", u"殺死恰恩所有生命的咒語", LS(27)],
          [u"世界之間的森林", u"Wood between the Worlds", u"通往各個世界的水池", LS(27)], [u"黎明行者號", u"Dawn Treader", u"賈思潘的船", LS(14)],
          [u"銀椅", u"the Silver Chair", u"束縛瑞里安的魔法椅", LS(20)], [u"沼澤怪", u"Marsh-wiggle", u"普德格倫的種族", LS(19)],
          [u"墨水會", u"the Inklings", u"牛津的作家聚會", LS(3)], [u"假想", u"supposal", u"路易斯對納尼亞性質的說明", LS(34)]]),
    ],
}

REFERENCES = [GUIDE, GLOSSARY]
