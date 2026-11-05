# -*- coding: utf-8 -*-
"""基因與 DNA 主題的規格。"""
import dna_a, dna_c, dna_e, dna_ref

TOPIC = {
    "id": "genetics-dna",
    "category": "science",
    "title": u"基因與 DNA：從孟德爾到 CRISPR",
    "short": u"基因與 DNA",
    "crumb": u"基因與 DNA",
    "icon": u"🧬",
    "description": u"孟德爾、染色體、摩根的果蠅、DNA 是遺傳物質、雙股螺旋；核苷酸、複製、中心法則、剪接與遺傳密碼、蛋白質、基因調控、人類基因體與非編碼 DNA；"
                   u"發育的程式、同源基因、多基因遺傳與遺傳率、同卵雙胞胎、表觀遺傳、複製貓 CC 與 X 染色體去活化、複製動物、突變；地中海貧血、蠶豆症、癌症基因、台灣的新生兒與產前篩檢、消費型檢測、藥物基因學與 HLA-B*1502、粒線體與 Y 染色體；"
                   u"基因工程、PCR、基改作物、CRISPR、基因治療、賀建奎事件、DNA 鑑識、分子演化、尼安德塔人與澎湖的丹尼索瓦人。含遺傳格子、中心法則轉譯器與多基因模擬。",
}

MODULES = dna_a.MODULES + dna_c.MODULES + dna_e.MODULES
REFERENCES = dna_ref.REFERENCES
