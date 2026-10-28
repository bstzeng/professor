# -*- coding: utf-8 -*-
"""LLM Skill 專區：參考頁——Skill 收藏庫、產生器與互動工具、欄位速查、名詞對照。"""
from skl_common import SKLLIB, LS, kw, GALLERY, TRIGGER

LIBRARY = {
    "file": "library.html", "title": u"Skill 收藏庫", "h1": u"Skill 收藏庫", "icon": u"📚",
    "description": u"多工、自主完成、實用工具、治理四類 Skill：自製範本可一鍵複製 SKILL.md，官方與社群 Skill 附來源與安裝方式",
    "body": [
        ("raw", u"<script>%s</script>" % SKLLIB),
        ("p", u"自製範本採 Agent Skills 開放格式，只使用 <code>name</code> 與 <code>description</code> 兩個欄位，可直接放進 Claude Code（<code>.claude/skills/&lt;name&gt;/SKILL.md</code>）或 Codex（<code>.agents/skills/&lt;name&gt;/SKILL.md</code>）。使用前請依自己的專案調整。"),
        ("p", u"官方與社群 Skill 只附說明、來源與安裝方式；安裝前請到原始碼庫閱讀完整內容並做安全審核（第 40 課）。"),
        GALLERY,
    ],
}

TOOLS = {
    "file": "tools.html", "title": u"Skill 工具箱", "h1": u"Skill 工具箱", "icon": u"🧰",
    "description": u"Skill 產生器、觸發模擬、依序與平行比較、自主迴圈模擬、漸進式載入計算",
    "body": [
        ("raw", u"<script>%s</script>" % SKLLIB),
        ("h", u"1. Skill 產生器（第 2、41 課）"), kw("gen", u""),
        ("h", u"2. 觸發模擬（第 5 課）"), TRIGGER,
        ("h", u"3. 依序 vs 平行（第 15、23 課）"), kw("orch", u""),
        ("h", u"4. 自主迴圈（第 13、30 課）"), kw("loop", u""),
        ("h", u"5. 漸進式載入（第 3 課）"), kw("disc", u""),
    ],
}

_H = [u"欄位", u"開放規格", u"Claude Code", u"Claude 應用程式／API", u"Codex"]
FIELDS = {
    "file": "fields.html", "title": u"SKILL.md 欄位與路徑速查", "h1": u"SKILL.md 欄位與路徑速查", "icon": u"🗂️",
    "description": u"開放規格、Claude Code、Claude 應用程式與 API、Codex 的欄位、存放位置與呼叫方式對照",
    "body": [
        ("p", u"依撰寫時（2026 年）的官方文件整理，各工具更新頻繁，請以最新文件為準。"),
        ("h", u"1. 欄位"),
        ("t", _H, [
            [u"<code>name</code>", u"必填；≤ 64 字元，小寫字母、數字、連字號", u"選填，預設為資料夾名稱", u"支援", u"必填"],
            [u"<code>description</code>", u"必填；≤ 1,024 字元", u"建議填；與 when_to_use 合計在清單中截到 1,536 字元", u"支援", u"必填"],
            [u"<code>license</code>／<code>compatibility</code>／<code>metadata</code>", u"選填", u"保留但不作用", u"支援", u"—"],
            [u"<code>allowed-tools</code>", u"選填", u"執行時免確認的工具", u"支援", u"—"],
            [u"<code>when_to_use</code>、<code>argument-hint</code>、<code>arguments</code>", u"—", u"支援", u"不允許", u"—"],
            [u"<code>disable-model-invocation</code>、<code>user-invocable</code>", u"—", u"控制誰能呼叫", u"不允許", u"可用 agents/openai.yaml 設定呼叫政策"],
            [u"<code>context: fork</code>、<code>agent</code>、<code>background</code>", u"—", u"在子代理中執行", u"不允許", u"—"],
            [u"<code>model</code>、<code>effort</code>、<code>paths</code>、<code>hooks</code>、<code>disallowed-tools</code>、<code>shell</code>", u"—", u"支援", u"不允許", u"—"]]),
        ("h", u"2. 存放位置"),
        ("t", [u"範圍", u"Claude Code", u"Codex"], [
            [u"專案", u"<code>.claude/skills/&lt;name&gt;/SKILL.md</code>（子資料夾的 .claude/skills 也會載入）", u"<code>.agents/skills/&lt;name&gt;/SKILL.md</code>（工作目錄、上一層、repo 根）"],
            [u"個人", u"<code>~/.claude/skills/&lt;name&gt;/SKILL.md</code>", u"<code>$HOME/.agents/skills/&lt;name&gt;/SKILL.md</code>（舊路徑 ~/.codex/skills）"],
            [u"組織／管理員", u"管理設定目錄下的 .claude/skills", u"<code>/etc/codex/skills</code>"],
            [u"內建", u"隨版本提供，見 / 選單", u"SYSTEM 範圍（如 skill-creator）"],
            [u"外掛", u"<code>&lt;plugin&gt;/skills/&lt;name&gt;/SKILL.md</code>，呼叫為 /外掛:名稱", u"透過外掛安裝"]]),
        ("h", u"3. 呼叫與管理"),
        ("t", [u"項目", u"Claude Code", u"Codex"], [
            [u"自動觸發", u"依描述", u"依描述"],
            [u"手動呼叫", u"<code>/名稱 參數</code>（$ARGUMENTS、$0、$1）", u"<code>$名稱</code>"],
            [u"安裝", u"放進目錄，或 <code>/plugin marketplace add</code>＋<code>/plugin install</code>", u"放進目錄，或 <code>$skill-installer</code>（安裝後重啟）"],
            [u"停用", u"權限規則 <code>Skill(名稱)</code>、設定 <code>skillOverrides</code>", u"<code>~/.codex/config.toml</code> 的 <code>[[skills.config]]</code>"],
            [u"專案長期規則", u"<code>CLAUDE.md</code>", u"<code>AGENTS.md</code>"],
            [u"子代理", u"<code>.claude/agents/&lt;name&gt;.md</code>、內建 Explore／Plan 等", u"多代理（撰寫時為實驗性功能）"],
            [u"非互動執行", u"<code>claude -p \"...\"</code>", u"<code>codex exec \"...\"</code>"]]),
        ("h", u"4. 相關課程"),
        ("ul", [LS(10, u"第 10 課：Claude Code 的 Skill"), LS(11, u"第 11 課：Claude 應用程式與 API"), LS(12, u"第 12 課：Codex 與開放規格"), LS(37, u"第 37 課：權限與沙箱")]),
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"Skill 與代理名詞對照", "h1": u"Skill 與代理名詞對照", "icon": u"📖",
    "description": u"Skill、代理、多工與安全的中英名詞",
    "body": [
        ("t", [u"中文", u"英文", u"課"], [
            [u"技能", u"Agent Skill", LS(1)], [u"開放規格", u"Agent Skills open standard（agentskills.io）", LS(1)], [u"開頭設定區塊", u"YAML frontmatter", LS(2)],
            [u"漸進式載入", u"Progressive disclosure", LS(3)], [u"上下文視窗", u"Context window", LS(3)], [u"專案說明檔", u"CLAUDE.md／AGENTS.md", LS(4)],
            [u"模型上下文協定", u"Model Context Protocol（MCP）", LS(4)], [u"鉤子", u"Hooks", LS(4)], [u"外掛", u"Plugin", LS(9)], [u"外掛市集", u"Plugin marketplace", LS(9)],
            [u"觸發", u"Invocation／Triggering", LS(5)], [u"動態背景", u"Dynamic context injection", LS(7)], [u"評估", u"Evaluation（eval）", LS(8)],
            [u"代理迴圈", u"Agent loop", LS(13)], [u"子代理", u"Subagent", LS(14)], [u"分派與彙整", u"Fan-out / Fan-in", LS(15)], [u"工作樹", u"git worktree", LS(16)],
            [u"編排", u"Orchestration", LS(17)], [u"評估者－優化者", u"Evaluator–optimizer", LS(17)], [u"紅－綠－重構", u"Red–green–refactor", LS(25)],
            [u"根本原因", u"Root cause", LS(26)], [u"進度檔", u"Progress / checkpoint file", LS(27)], [u"交接筆記", u"Handoff note", LS(27)],
            [u"非互動模式", u"Headless mode", LS(28)], [u"持續整合", u"Continuous Integration（CI）", LS(29)], [u"完成的定義", u"Definition of done", LS(30)],
            [u"升級求助", u"Escalation", LS(31)], [u"最小權限", u"Least privilege", LS(37)], [u"沙箱", u"Sandbox", LS(37)], [u"提示注入", u"Prompt injection", LS(38)],
            [u"人在迴圈中", u"Human in the loop", LS(39)], [u"供應鏈風險", u"Supply-chain risk", LS(40)]]),
    ],
}

REFERENCES = [LIBRARY, TOOLS, FIELDS, GLOSSARY]
