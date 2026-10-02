# -*- coding: utf-8 -*-
"""基地：參考頁——互動圖鑑、名詞表。"""
from nv_common import LS, NVLIB
import fd_a, fd_e

GUIDE = {
    "file": "guide.html", "title": u"基地互動圖鑑", "h1": u"基地互動圖鑑", "icon": u"🗺️",
    "description": u"閱讀順序、謝頓計畫時間表、心理史學模擬、人物卡、艾西莫夫大宇宙、影集差異",
    "body": [
        ("raw", u"<script>%s</script>" % NVLIB),
        ("h", u"1. 閱讀順序（第 4 課）"), fd_a._ORDER,
        ("h", u"2. 心理史學模擬（第 6 課）"), fd_a._CROWD,
        ("h", u"3. 謝頓計畫時間表（第 9 課）"), fd_a._PLAN,
        ("h", u"4. 〈騾〉篇人物（第 18 課）"), fd_a._MULE_CARDS,
        ("h", u"5. 全系列人物卡（第 32 課）"), fd_e._CARDS,
        ("h", u"6. 艾西莫夫大宇宙（第 36 課）"), fd_e._UNIVERSE,
        ("h", u"7. 原著與影集差異（第 41 課）"), fd_e._TV,
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"基地名詞表", "h1": u"基地名詞表", "icon": u"📖",
    "description": u"概念、地名與組織中英對照",
    "body": [
        ("t", [u"中文", u"原文", u"說明", u"課"],
         [[u"心理史學", u"psychohistory", u"以統計預測群體行為的科學", LS(6)], [u"謝頓計畫", u"Seldon Plan", u"把黑暗時代縮短為一千年的計畫", LS(7)],
          [u"謝頓危機", u"Seldon Crisis", u"歷史只留下一條出路的關鍵時刻", LS(8)], [u"時光穹窿", u"Time Vault", u"播放謝頓影像的地方", LS(7)],
          [u"銀河紀元／基地紀元", u"GE / FE", u"兩種紀年", LS(9)], [u"川陀", u"Trantor", u"帝國首都；第二基地所在", LS(5)],
          [u"端點星", u"Terminus", u"第一基地所在", LS(7)], [u"銀河百科全書", u"Encyclopedia Galactica", u"基地的表面任務", LS(11)],
          [u"科學宗教", u"Church of Science", u"哈定的統治工具", LS(12)], [u"行商", u"Traders", u"半獨立的商人兼間諜", LS(13)],
          [u"商業王侯", u"Merchant Princes", u"馬洛之後的富商統治", LS(14)], [u"騾", u"The Mule", u"能控制情緒的突變種", LS(18)],
          [u"第二基地", u"Second Foundation", u"守護計畫的心靈科學家", LS(23)], [u"發言者", u"Speaker", u"第二基地成員", LS(23)],
          [u"元光體", u"Prime Radiant", u"謝頓計畫的方程式", LS(23)], [u"星際盡頭", u"Star's End", u"第二基地的暗號", LS(25)],
          [u"蓋婭", u"Gaia", u"有集體意識的星球", LS(27)], [u"銀河人", u"Galaxia", u"整個銀河成為一個意識", LS(27)],
          [u"太空族", u"Spacers", u"最早殖民的五十顆星球上的人", LS(34)], [u"機器人三定律", u"Three Laws of Robotics", u"機器人的行為準則", LS(33)],
          [u"第零法則", u"Zeroth Law", u"保護人類整體", LS(35)], [u"正子腦", u"positronic brain", u"機器人的大腦", LS(29)]]),
    ],
}

REFERENCES = [GUIDE, GLOSSARY]
