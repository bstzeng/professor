# -*- coding: utf-8 -*-
"""克蘇魯神話主題的規格。"""
import cth_a, cth_c, cth_e, cth_ref

TOPIC = {
    "id": "cthulhu-mythos",
    "category": "fantasy",
    "title": u"克蘇魯神話：洛夫克拉夫特與宇宙恐怖",
    "short": u"克蘇魯神話",
    "crumb": u"克蘇魯神話",
    "icon": u"🐙",
    "description": u"洛夫克拉夫特的生平、宇宙恐怖與「不可名狀」、德雷斯與共享宇宙的形成；〈大袞〉〈克蘇魯的呼喚〉〈異域之色〉〈敦威治恐怖事件〉〈暗夜呢喃〉〈瘋狂山脈〉〈印斯茅斯疑雲〉〈魔女屋之夢〉〈查爾斯・德克斯特・沃德事件〉〈超越時間之影〉〈獵黑行者〉與夢境系列導讀（完整劇透）；"
                   u"外神、克蘇魯與舊日支配者、深潛者、古老者與修格斯、米・戈、伊斯之偉大種族；《死靈之書》與禁書、洛夫克拉夫特之國、拉萊耶與夢境；TRPG 與理智值、電玩、電影、動漫、文學繼承者、新世代的再詮釋與中文圈的克系熱；科學時代的恐懼、種族主義爭議與開源神話。",
}

MODULES = cth_a.MODULES + cth_c.MODULES + cth_e.MODULES
REFERENCES = cth_ref.REFERENCES
