# -*- coding: utf-8 -*-
"""美國政府怎麼運作主題的規格。"""
import usg_a, usg_c, usg_e, usg_ref

TOPIC = {
    "id": "us-government",
    "category": "history",
    "title": u"美國政府怎麼運作：三權、兩院與台灣比較",
    "short": u"美國政府怎麼運作",
    "crumb": u"美國政府",
    "icon": u"🦅",
    "description": u"共和、聯邦與分權制衡；制憲會議與康乃狄克妥協、憲法與修憲、聯邦主義、兩黨制；國會的列舉權力、眾議院與參議院、兩院權力分界、議長與多數黨領袖、委員會、立法流程、冗長辯論與 60 票、撥款與政府關門、監督與 CBO／GAO；"
                   u"總統權力與行政命令、選舉人團、白宮與總統行政辦公室、十五個部、獨立機構、文官、戰爭權、彈劾與繼任；聯邦法院、最高法院、司法審查與重要判例、法官任命、州法院；選舉、遊說、州與地方、媒體與改革；"
                   u"每課附「台灣怎麼做」，並以八課完整比較中華民國五權憲法、總統與行政院、立法院、監察考試司法三院、單一制、覆議罷免與公投。",
}

MODULES = usg_a.MODULES + usg_c.MODULES + usg_e.MODULES
REFERENCES = usg_ref.REFERENCES
