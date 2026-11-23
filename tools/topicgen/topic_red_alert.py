# -*- coding: utf-8 -*-
import rea_a
from nv_common import NVLIB

ATLAS = {"file": "atlas.html", "title": u"紅色警戒圖鑑", "h1": u"紅色警戒圖鑑", "icon": u"📜",
         "description": u"時間線與人物關係圖",
         "body": [("raw", u"<script>%s</script>" % NVLIB), ("h", u"1. 時間線"), rea_a.STORY, ("h", u"2. 人物關係圖"), rea_a.PEOPLE]}

TOPIC = {
    "id": "red-alert-saga", "category": "games",
    "title": u"紅色警戒全劇情：一代、二代、三代與資料片",
    "short": u"紅色警戒", "crumb": u"紅色警戒", "icon": u"☭",
    "description": u"終極動員令的兩條世界線、愛因斯坦刪除希特勒；紅警 1 盟軍與蘇聯戰役、史達林之死與凱恩現身、反擊戰、餘波、巨蟻任務、Retaliation 與重製版；紅警 2 的蘇聯入侵美國、心靈信標、超時空傳送莫斯科、艾菲爾鐵塔線圈與尤里的背叛；尤里的復仇兩條時光機戰役；紅警 3 刪除愛因斯坦、旭日帝國與三方結局；起義時刻的未來科技與百合子；真人過場影片的文化（含完整劇透）。附時間線與人物關係圖。",
}
MODULES = rea_a.MODULES
REFERENCES = [ATLAS]
