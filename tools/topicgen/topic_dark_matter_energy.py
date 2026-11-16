# -*- coding: utf-8 -*-
"""暗物質與暗能量主題的規格。"""
import dkm_a, dkm_f, dkm_ref

TOPIC = {
    "id": "dark-matter-energy",
    "category": "science",
    "title": u"暗物質與暗能量：怎麼尋找看不見的東西",
    "short": u"暗物質與暗能量",
    "crumb": u"暗物質與暗能量",
    "icon": u"🌑",
    "description": u"宇宙的帳本、茲威基、薇拉・魯賓的自轉曲線；重力透鏡、子彈星系團、宇宙微波背景的聲學峰、大尺度結構、大爆炸核合成；"
                   u"WIMP 奇蹟、軸子、惰性微中子、原始黑洞、MOND；直接偵測與液態氙、微中子霧、DAMA 年度調制、ADMX；銀河中心超出、AMS-02 正電子、LHC 單噴流；"
                   u"加速膨脹與 Ia 型超新星、宇宙常數問題、第五元素；重子聲學振盪、弱透鏡、哈伯張力、DESI；MCMC、系統誤差、盲分析；歐幾里得與魯賓天文台。附三個互動模擬。",
}

MODULES = dkm_a.MODULES + dkm_f.MODULES
REFERENCES = dkm_ref.REFERENCES
