# -*- coding: utf-8 -*-
"""印度教主題的規格。"""
import hi_a, hi_b, hi_ref

TOPIC = {
    "id": "hinduism",
    "category": "religion",
    "title": u"印度教：歷史與教義",
    "short": u"印度教",
    "crumb": u"印度教",
    "icon": u"🕉️",
    "description": u"一個沒有創始人的宗教：從印度河文明、吠陀、梵書到奧義書；梵與我、業與輪迴、解脫、法、人生四目標與四階段、種姓制度；"
                   u"天啟與傳承、《摩訶婆羅多》、《薄伽梵歌》、《羅摩衍那》、往世書與《摩奴法典》；三相神、毗濕奴十化身、黑天、濕婆與女神；"
                   u"六派哲學、吠檀多、虔信運動與密教；與佛教的互動、南印度神廟、伊斯蘭時代與錫克教、殖民改革、甘地與現代印度；"
                   u"普迦、節日與人生禮儀。以理解為目的，並列不同觀點。附十化身、人生階段與歷史時間軸互動工具。",
}

MODULES = hi_a.MODULES + hi_b.MODULES

REFERENCES = hi_ref.REFERENCES
