# -*- coding: utf-8 -*-
"""Agentic AI：參考頁——互動實驗室（含範例下載）、名詞速查。"""
import os
from ag_common import LS, AGLIB, agw, PYDIR

_names = sorted(f[:-3] for f in os.listdir(PYDIR) if f[:1] in "abcdefgh" and f[1:3].isdigit() and f.endswith(".py"))
_claude = set(f[:-3] for f in os.listdir(os.path.join(PYDIR, "claude")) if f.endswith(".py"))
_rows = [[LS(int(n[1:3])), u'<a href="py/%s.py" download>%s.py</a>' % (n, n),
          u'<a href="py/claude/%s.py" download>Claude 版</a>' % n if n in _claude else u"—"] for n in _names]

GUIDE = {
    "file": "guide.html", "title": u"Agentic AI 實驗室", "h1": u"Agentic AI 實驗室", "icon": u"🧪",
    "description": u"代理迴圈、工具定義、向量相似度、上下文視窗、提示注入攻防、成本估算，以及全部 Python 範例下載",
    "body": [
        ("raw", u"<script>%s</script>" % AGLIB),
        ("h", u"下載全部範例"),
        ("p", u'<a href="py/agentic-ai-examples.zip" download><strong>📦 agentic-ai-examples.zip</strong></a>：包含 %d 個離線範例、%d 個 Claude API 版範例與 mockllm.py。'
              u"解壓縮後，離線範例直接 <code>python a01_chat_vs_agent.py</code> 即可執行（Python 3.9 以上，不需安裝任何套件）；"
              u"Claude 版在 <code>claude/</code> 資料夾，需要 <code>pip install anthropic</code> 並設定 <code>ANTHROPIC_API_KEY</code>。" % (len(_names), len(_claude))),
        ("p", u'核心模組：<a href="py/mockllm.py" download>mockllm.py</a>——一個介面模仿 Anthropic SDK 的離線「假 LLM」，讓你不花一毛錢就能把代理的每一個動作跑一遍。'),
        ("t", [u"課", u"離線範例", u"Claude API 版"], _rows),
        ("h", u"1. 代理迴圈（第 5 課）"), agw({"t": "loop"}),
        ("h", u"2. 工具定義產生器（第 6 課）"), agw({"t": "tool"}),
        ("h", u"3. 上下文視窗計算機（第 20 課）"), agw({"t": "ctx"}),
        ("h", u"4. 向量相似度與檢索（第 22 課）"), agw({"t": "vec"}),
        ("h", u"5. 提示注入攻防（第 42 課）"), agw({"t": "inject"}),
        ("h", u"6. 成本估算器（第 45 課）"), agw({"t": "cost"}),
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"Agentic AI 名詞速查", "h1": u"Agentic AI 名詞速查", "icon": u"📖",
    "description": u"代理、工具、記憶、多代理與安全的名詞",
    "body": [
        ("h", u"1. 代理與工具"),
        ("t", [u"名詞", u"說明", u"課"],
         [[u"代理（agent）", u"在迴圈中根據環境回饋自己使用工具的 LLM", LS(1)], [u"token", u"模型處理文字的單位", LS(2)],
          [u"system／user／assistant", u"訊息的三種角色", LS(3)], [u"工作流（workflow）", u"由程式決定步驟、LLM 填空的流程", LS(4)],
          [u"代理迴圈", u"感知、思考、行動、觀察的循環", LS(5)], [u"stop_reason", u"回應停止的原因：tool_use、end_turn、max_tokens、refusal 等", LS(5)],
          [u"工具定義", u"name、description、input_schema", LS(6)], [u"tool_use／tool_result", u"模型要求工具／程式回傳結果，以 id 配對", LS(7)],
          [u"平行工具呼叫", u"一則回應中有多個 tool_use，結果放同一則訊息", LS(9)], [u"is_error", u"標記工具結果為錯誤，讓模型修正", LS(10)],
          [u"strict 模式", u"保證工具參數符合 schema", LS(12)], [u"Tool Runner", u"SDK 內建的代理迴圈", LS(13)]]),
        ("h", u"2. 推理與記憶"),
        ("t", [u"名詞", u"說明", u"課"],
         [[u"adaptive thinking", u"模型自行決定思考深度", LS(14)], [u"effort", u"控制思考深度與 token 花費的參數", LS(14)],
          [u"ReAct", u"推理與行動交錯的代理模式", LS(15)], [u"Plan-and-Execute", u"先產生計畫再逐步執行", LS(16)],
          [u"反思（reflection）", u"產生、檢查、修改的循環", LS(18)], [u"task budget", u"讓模型知道整個任務的 token 預算", LS(19)],
          [u"上下文視窗", u"模型一次能看的 token 上限，代理的工作記憶", LS(20)], [u"compaction", u"伺服器端自動摘要較早的對話", LS(21)],
          [u"嵌入（embedding）", u"把文字轉成向量，意思相近則方向相近", LS(22)], [u"RAG", u"檢索增強生成：先找資料再回答", LS(23)],
          [u"長期記憶", u"寫入檔案或資料庫、跨對話保存的資訊", LS(24)], [u"提示快取", u"重用相同前綴的計算結果以降低成本", LS(25)],
          [u"上下文工程", u"決定每輪讓模型看到什麼資訊", LS(26)]]),
        ("h", u"3. 與世界互動、多代理"),
        ("t", [u"名詞", u"說明", u"課"],
         [[u"沙箱", u"隔離執行環境，限制傷害範圍", LS(27)], [u"str_replace", u"以「原文剛好出現一次」為條件的精確修改", LS(28)],
          [u"路徑穿越", u"用 ../ 存取專案外檔案的攻擊", LS(28)], [u"MCP", u"模型上下文協定，工具的通用介面（JSON-RPC 2.0）", LS(30)],
          [u"computer use", u"以截圖與滑鼠鍵盤操作電腦", LS(31)], [u"子代理", u"在獨立上下文中處理子任務、只回傳結論的代理", LS(33)],
          [u"協調者－工作者", u"拆解、平行執行、整合的多代理模式", LS(34)], [u"路由／交接", u"把請求分派給專門代理／代理之間轉手", LS(35)],
          [u"評估者－優化者", u"一個產生、一個依標準評分的循環", LS(36)]]),
        ("h", u"4. 可靠性、安全與實務"),
        ("t", [u"名詞", u"說明", u"課"],
         [[u"結構化輸出", u"以 JSON Schema 約束模型輸出格式", LS(38)], [u"防護欄", u"在輸入、工具、輸出設下的程式檢查", LS(39)],
          [u"人在迴路", u"危險動作執行前由人核准", LS(40)], [u"允許清單", u"只准列出的項目，其他一律拒絕", LS(41)],
          [u"提示注入", u"藏在外部內容中、誘導代理的指令", LS(42)], [u"evals", u"用固定案例與自動評分衡量代理", LS(43)],
          [u"追蹤（trace）", u"記錄代理每一步的輸入、輸出、耗時與關係", LS(44)], [u"冪等性", u"重做不會產生重複的副作用", LS(49)],
          [u"檢查點", u"保存進度以便中斷後恢復", LS(49)], [u"CLAUDE.md／AGENTS.md", u"Claude Code／Codex 讀取的專案說明檔", LS(48)]]),
    ],
}

REFERENCES = [GUIDE, GLOSSARY]
