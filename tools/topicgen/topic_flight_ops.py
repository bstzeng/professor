# -*- coding: utf-8 -*-
"""一趟航班的幕後主題的規格。"""
import fo_a, fo_d, fo_g, fo_ref

TOPIC = {
    "id": "flight-ops",
    "category": "tech",
    "title": "一趟航班的幕後：機師、塔台與空服的工作",
    "short": "一趟航班的幕後",
    "crumb": "航班幕後",
    "icon": "✈️",
    "description": "跟著一班從桃園飛往成田的航班，從機師報到、簽派簡報、駕駛艙準備、推出滑行、起飛、巡航、下降進場、"
                   "落地到下機講評，逐一看機師的每一個動作；再看塔台與航管各單位如何接力指揮天空，以及空服員在客艙的安全與服務工作。"
                   "附無線電對話、檢查單、V1 決斷與三方時間軸等互動元件。",
}

MODULES = fo_a.MODULES + fo_d.MODULES + fo_g.MODULES

REFERENCES = fo_ref.REFERENCES
