# -*- coding: utf-8 -*-
"""機場是怎麼運作的 的規格。"""
import apt_a, apt_ref

TOPIC = {
    "id": "airports", "category": "tech",
    "title": u"機場是怎麼運作的：從報到、行李到跑道",
    "short": u"機場的運作", "crumb": u"機場", "icon": u"🛫",
    "description": u"機場是一座城市、空側與陸側、跑道的編號與容量；報到、行李處理系統、安檢與液體規定、證照查驗與自動通關、登機門與空橋、轉機、免稅與非航空收入；過站作業與要徑、停機位分配、航空貨運站、機場消防救援；"
                   u"塔台與地面管制、時刻帶、延誤與流量管理、天氣、鳥擊防制；機場的收入、樞紐與航空聯盟、桃園機場第三航廈與第三跑道、聯外交通、噪音與松山機場；大規模延誤、CrowdStrike 當機、蓋威克無人機事件；世界著名機場比較。附過站甘特圖、跑道容量計算器與行李流程動畫。",
}
MODULES = apt_a.MODULES
REFERENCES = apt_ref.REFERENCES
