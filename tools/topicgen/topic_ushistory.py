# -*- coding: utf-8 -*-
"""美國歷史主題的規格。"""
import us_a, us_b, us_c, us_ref

TOPIC = {
    "id": "us-history",
    "category": "history",
    "title": u"美國歷史：從殖民地到超級強權",
    "short": u"美國歷史",
    "crumb": u"美國歷史",
    "icon": u"🇺🇸",
    "description": u"從原住民的北美洲與十三個殖民地講起：獨立革命、制憲與權利法案；西部擴張、血淚之路與美墨戰爭；"
                   u"奴隸制度、南北戰爭與重建；工業化、移民潮與排華法案、進步主義；兩次世界大戰、經濟大恐慌與新政；"
                   u"冷戰、民權運動、越戰與水門案；雷根、九一一、金融海嘯到兩極化的當代政治。並附歷任總統表，"
                   u"以及領土擴張、時間軸、選舉人團模擬器與憲法修正案導覽等互動工具。",
}

MODULES = us_a.MODULES + us_b.MODULES + us_c.MODULES

REFERENCES = us_ref.REFERENCES
