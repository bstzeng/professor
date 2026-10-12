# -*- coding: utf-8 -*-
"""菲爾茲獎：參考頁——互動工具箱與得主速查。"""
from fm_common import *

GUIDE = {
    "file": "guide.html", "title": u"菲爾茲獎工具箱", "h1": u"菲爾茲獎工具箱", "icon": u"🧰",
    "description": u"歷屆得主時間軸、得主速查卡、年齡分布，以及滲流、質數間隔、掛谷針三個數學小實驗",
    "body": [
        ("raw", u"<script>%s</script><script>%s</script>" % (NVLIB, FMLIB)),
        ("p", u"本頁集中課程中的互動工具。得主資料以國際數學聯盟公布為準，獲獎年齡以「屆別年份 − 出生年」估算。"),
        ("h", u"1. 歷屆得主時間軸（第 3、84 課）"), timeline_all(),
        ("h", u"2. 得主速查卡（第 2 課）"), cards_all(),
        ("h", u"3. 獲獎年齡分布（第 2 課）"), age_chart(),
        ("h", u"4. 滲流實驗（維爾納、斯米爾諾夫、杜明尼爾-科潘）"), PERC,
        ("h", u"5. 質數與質數間隔（塞爾伯格、邦別里、陶哲軒、梅納德）"), PRIMES,
        ("h", u"6. 掛谷針問題（費弗曼、布爾甘、王虹）"), KAKEYA,
    ],
}

_rows = []
for k in ORDER:
    y, zh, en, b, d, c, f, cit = MED[k]
    _rows.append([str(y), u"%s（%s）" % (zh, en), u"%s–%s" % (b, d or u"") if b else u"—", c, FIELDS[f], cit])

GLOSSARY = {
    "file": "glossary.html", "title": u"歷屆得主總表", "h1": u"歷屆得主總表", "icon": u"📖",
    "description": u"1936–2026 年 68 位得主與懷爾斯特別獎",
    "body": [
        ("p", u"表彰重點為中文意譯；1982 年得主於 1983 年華沙大會頒發。1998 年另頒特別銀質紀念牌給懷爾斯（Andrew Wiles）。"),
        ("t", [u"屆", u"得主", u"生卒", u"國籍", u"領域", u"表彰重點"], _rows),
        ("h", u"名詞"),
        ("t", [u"名詞", u"說明"],
         [[u"ICM", u"國際數學家大會，每四年一次，菲爾茲獎在開幕式公布"], [u"IMU", u"國際數學聯盟，負責選出菲爾茲獎得主"], [u"年齡限制", u"大會當年 1 月 1 日前未滿 40 歲"],
          [u"表彰（citation）", u"官方對得主貢獻的簡短說明"], [u"laudatio", u"大會中介紹得主工作的頌詞演講"]]),
    ],
}

REFERENCES = [GUIDE, GLOSSARY]
