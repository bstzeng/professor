# -*- coding: utf-8 -*-
"""開公司主題的規格。"""
import inc_a, inc_e, inc_ref

TOPIC = {
    "id": "start-a-company",
    "category": "finance",
    "title": u"開公司：好處、代價與紅線",
    "short": u"開公司：好處、代價與紅線",
    "crumb": u"開公司",
    "icon": u"🏢",
    "description": u"依台灣現行法規，從公司是什麼、五種組織型態開始，講清楚開公司的好處（有限責任、營所稅與盈餘保留、費用列支、信用、募資、傳承）、代價（設立與每年成本、兩層課稅、未分配盈餘、清算）、"
                   u"設立流程，以及公司不能做的事：公私不分、抽逃資本、違法貸與與保證、吸金、作假帳與假發票、逃漏稅、人頭負責人、勞動、個資、公平交易與洗錢防制。附稅負試算器、組織型態比較、紅線測驗、檢查清單與年度行事曆。",
}

MODULES = inc_a.MODULES + inc_e.MODULES

REFERENCES = inc_ref.REFERENCES
