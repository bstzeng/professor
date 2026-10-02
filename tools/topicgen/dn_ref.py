# -*- coding: utf-8 -*-
"""沙丘：參考頁——人物與勢力速查、名詞表。"""
from nv_common import LS, NVLIB
import dn_a, dn_e

GUIDE = {
    "file": "guide.html", "title": u"沙丘互動圖鑑", "h1": u"沙丘互動圖鑑", "icon": u"🗺️",
    "description": u"閱讀路線、宇宙年表、帝國權力圖、厄拉科斯地圖、人物卡、亞崔迪家族圖、改編年表",
    "body": [
        ("raw", u"<script>%s</script>" % NVLIB),
        ("h", u"1. 閱讀路線（第 4 課）"), dn_a._ORDER,
        ("h", u"2. 宇宙年表（第 5 課）"), dn_a._TL,
        ("h", u"3. 帝國的權力平衡（第 7 課）"), dn_a._POWER,
        ("h", u"4. 厄拉科斯地圖（第 14 課）"), dn_a._MAP,
        ("h", u"5. 人物卡（第 26 課）"), dn_a._CARDS,
        ("h", u"6. 亞崔迪家族四代（第 27 課）"), dn_e._FAMILY,
        ("h", u"7. 改編年表（第 44 課）"), dn_e._ADAPT,
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"沙丘名詞表", "h1": u"沙丘名詞表", "icon": u"📖",
    "description": u"勢力、地名、物品與術語中英對照",
    "body": [
        ("h", u"1. 勢力與組織"),
        ("t", [u"中文", u"原文", u"說明", u"課"],
         [[u"亞崔迪家族", u"House Atreides", u"保羅的家族，以榮譽著稱", LS(18)], [u"哈肯能家族", u"House Harkonnen", u"亞崔迪的世仇", LS(20)],
          [u"柯瑞諾家族", u"House Corrino", u"皇室", LS(7)], [u"大家族議會", u"Landsraad", u"貴族聯合體", LS(7)],
          [u"宇航公會", u"Spacing Guild", u"壟斷星際航行", LS(8)], [u"貝尼·傑瑟里特", u"Bene Gesserit", u"女修會", LS(9)],
          [u"薩督卡", u"Sardaukar", u"皇帝的軍團", LS(7)], [u"弗瑞曼人", u"Fremen", u"厄拉科斯的原住民", LS(14)],
          [u"特雷亞拉克斯人", u"Tleilaxu", u"生物技術專家", LS(12)], [u"魚語者", u"Fish Speakers", u"神帝的女性軍隊", LS(31)],
          [u"尊母", u"Honored Matres", u"離散後歸來的女性組織", LS(33)]]),
        ("h", u"2. 術語"),
        ("t", [u"中文", u"原文", u"說明", u"課"],
         [[u"香料", u"melange / spice", u"延壽、預知、成癮", LS(11)], [u"沙蟲／沙胡羅", u"sandworm / Shai-Hulud", u"沙漠之王", LS(13)],
          [u"沙鱒", u"sandtrout", u"沙蟲的幼體", LS(13)], [u"生命之水", u"Water of Life", u"沙蟲的毒液", LS(13)],
          [u"蒸餾服", u"stillsuit", u"回收體內水分的服裝", LS(15)], [u"穴地", u"sietch", u"弗瑞曼人的洞穴聚落", LS(14)],
          [u"晶牙匕", u"crysknife", u"沙蟲牙齒做的匕首", LS(14)], [u"門塔特", u"Mentat", u"人腦電腦", LS(10)],
          [u"魁薩茲·哈德拉赫", u"Kwisatz Haderach", u"修會育種計畫的目標", LS(9)], [u"音聲", u"the Voice", u"以聲音控制他人", LS(9)],
          [u"毒針", u"gom jabbar", u"痛苦之盒測試的毒針", LS(18)], [u"再生人", u"ghola", u"由死者細胞培養的複製人", LS(12)],
          [u"臉舞者", u"Face Dancer", u"變形間諜", LS(12)], [u"巴特勒聖戰", u"Butlerian Jihad", u"推翻思考機器的戰爭", LS(6)],
          [u"金色通道", u"Golden Path", u"雷托二世的計畫", LS(32)], [u"憎惡", u"Abomination", u"被祖先人格吞噬的預生者", LS(29)],
          [u"焚石", u"stone burner", u"讓保羅失明的武器", LS(28)], [u"無形船", u"no-ship", u"無法被偵測或預知的太空船", LS(34)]]),
    ],
}

REFERENCES = [GUIDE, GLOSSARY]
