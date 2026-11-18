# -*- coding: utf-8 -*-
"""編譯器的規格。"""
import cmp_a, cmp_f, cmp_ref

TOPIC = {
    "id": "compilers",
    "category": "tech",
    "title": u"編譯器：程式碼怎麼變成機器碼",
    "short": u"編譯器",
    "crumb": u"編譯器",
    "icon": u"🛠️",
    "description": u"葛麗絲・霍普與 FORTRAN、直譯與 JIT、編譯的流程；詞法分析、正規表示式與有限自動機、BNF 文法與歧義、遞迴下降剖析、優先順序與結合性、抽象語法樹；符號表與閉包、型別檢查、型別推論、錯誤訊息；"
                   u"三位址碼與控制流程圖、SSA、常數摺疊與死碼消除、迴圈最佳化與向量化、內聯與 PGO、LLVM；指令選擇、暫存器配置與圖著色、呼叫慣例與緩衝區溢位、連結器；垃圾回收、V8 與推測式最佳化、動手做迷你編譯器。附詞法分析、語法樹、最佳化與暫存器配置四個互動工具。",
}

MODULES = cmp_a.MODULES + cmp_f.MODULES
REFERENCES = cmp_ref.REFERENCES
