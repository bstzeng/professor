# -*- coding: utf-8 -*-
"""計算理論主題的規格。"""
import tc_a, tc_e, tc_h, tc_ref

TOPIC = {
    "id": "computability",
    "category": "math",
    "title": "計算理論：從圖靈機到停機問題",
    "short": "計算理論",
    "crumb": "計算理論",
    "icon": "🧮",
    "description": "計算理論完整導讀：希爾伯特的夢想、1936 年的丘奇與圖靈；有限自動機、NFA、正規表達式與抽水引理；上下文無關文法、下推自動機與喬姆斯基階層；"
                   "圖靈機、萬能圖靈機、丘奇－圖靈論題、λ 演算與圖靈完備；對角線論證、停機問題的證明、歸約、萊斯定理與其他不可判定問題；"
                   "哥德爾數與不完備定理、忙碌海狸與考拉茲猜想；時間複雜度、P、NP、NP 完全與 P vs NP。附十四個互動模擬器。",
}

MODULES = tc_a.MODULES + tc_e.MODULES + tc_h.MODULES

REFERENCES = tc_ref.REFERENCES
