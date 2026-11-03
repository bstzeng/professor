# -*- coding: utf-8 -*-
"""日本戰國時代主題的規格。"""
import sgk_a, sgk_c, sgk_e, sgk_ref

TOPIC = {
    "id": "sengoku-japan",
    "category": "history",
    "title": u"日本戰國時代：從應仁之亂到天下統一",
    "short": u"日本戰國時代",
    "crumb": u"日本戰國時代",
    "icon": u"🏯",
    "description": u"室町幕府與應仁之亂、下剋上與戰國大名、足輕與鐵砲、戰國的經濟；北條、武田、上杉、川中島、今川、毛利、齋藤道三、九州三強與伊達政宗；"
                   u"織田信長（桶狹間、天下布武、信長包圍網、比叡山、長篠、石山合戰、安土城、本能寺）、豐臣秀吉（中國大返還、賤岳、小牧長久手、關白、太閤檢地與刀狩、朝鮮出兵）、德川家康（三方原、關原、江戶幕府、大坂之陣、幕藩體制與鎖國）；城、茶道與千利休、南蠻貿易、忍者、戰國與台灣、大河劇與遊戲。含 1560～1615 年勢力版圖互動地圖。",
}

MODULES = sgk_a.MODULES + sgk_c.MODULES + sgk_e.MODULES
REFERENCES = sgk_ref.REFERENCES
