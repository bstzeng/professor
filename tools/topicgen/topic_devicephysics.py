# -*- coding: utf-8 -*-
"""半導體元件物理主題的規格。"""
import dp_a, dp_e, dp_ref

TOPIC = {
    "id": "device-physics",
    "category": "tech",
    "title": u"半導體元件物理：從能帶到 3 奈米電晶體",
    "short": u"半導體元件物理",
    "crumb": u"元件物理",
    "icon": u"🔬",
    "description": u"大學部程度的元件物理，附推導：晶格、量子力學速成、能帶、有效質量、電洞、狀態密度與費米分布；本質與摻雜、漂移擴散、SRH 復合、連續方程式；"
                   u"PN 接面的空乏區、二極體方程式、非理想效應、崩潰與暫態；蕭特基與異質接面、量子井；BJT 與 HBT；MOS 電容、C–V、臨界電壓、MOSFET、次臨界擺幅、短通道效應、"
                   u"微縮、high-k 金屬閘極、CMOS；應變矽、SOI、FinFET、GAA 與未來元件；太陽能電池、LED、影像感測器；DRAM、快閃記憶體、功率元件與可靠度。附能帶圖、PN 接面、MOS C–V、MOSFET 等九個互動工具。",
}

MODULES = dp_a.MODULES + dp_e.MODULES

REFERENCES = dp_ref.REFERENCES
