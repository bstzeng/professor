# -*- coding: utf-8 -*-
"""LLM Skill 專區：模組 A 認識 Skill（1～4）、B 怎麼寫好 Skill（5～9）、C 平台與安裝（10～12）。"""
from skl_common import *

C = lambda s: ("code", s.strip("\n"))

MODULES = [
(u"模組 A｜認識 Skill", [

lesson(u"Skill 是什麼",
  u"把「怎麼做某件事」打包成資料夾，讓 AI 需要時自己去拿",
  [u"說出 Skill 解決了什麼問題", u"理解 Skill 與一般提示詞的差別", u"知道哪些工具支援 Skill"],
  [("p", u"每次請 AI 代理寫週報、做程式審查、跑發布流程，你都得重新解釋一遍：「先看這些資料、照這個格式、不要忘了這一步……」。<strong>Skill（技能）</strong>就是把這些說明寫成檔案，存在固定的地方。AI 判斷「現在需要這個技能」時，自己去讀那份說明，照著做。"),
   ("h", u"一句話定義"),
   ("p", u"Skill 是一個<strong>資料夾</strong>，裡面至少有一個 <code>SKILL.md</code>：開頭幾行寫名稱和「什麼時候該用我」，後面寫具體做法；需要的話再附上腳本、參考文件、範本。"),
   C(u"""
weekly-report/
├── SKILL.md          ← 必要：名稱、描述、做法
├── scripts/
│   └── collect.sh    ← 選用：交給程式做的步驟
└── references/
    └── format.md     ← 選用：需要時才讀的參考資料
"""),
   ("h", u"它解決的三個問題"),
   ("ul", [u"<strong>重複解釋</strong>：一次寫好，之後每次都能用，團隊也能共用。", u"<strong>上下文有限</strong>：說明平常不佔空間，用到才載入（第 3 課）。", u"<strong>做法不穩定</strong>：把容易出錯的步驟寫成檢查清單或腳本，讓結果更一致。"]),
   ("h", u"誰支援 Skill"),
   ("p", u"Anthropic 在 2025 年推出 Agent Skills，後來把格式公開成<strong>開放規格</strong>（agentskills.io）。撰寫時，Claude Code、Claude 網頁版與 API、OpenAI Codex 等多種 AI 工具都支援這種 <code>SKILL.md</code> 格式。這門課以 <strong>Claude Code</strong> 與 <strong>Codex</strong> 為主（第 10～12 課）。"),
   ("note", u"這門課的重點", [("p", u"Skill 可以用來做任何事，但這門課特別著重三類：讓代理<strong>同時處理很多事</strong>（多工）、<strong>自己把事情做完並驗證</strong>（自主完成），以及<strong>知道什麼時候該停下來問人</strong>（安全）。所有範本都收在「Skill 收藏庫」參考頁，可以直接複製。")]),
   GALLERY,
  ],
  u"Skill 是一個資料夾，核心是 SKILL.md（名稱、描述、做法），可附腳本、參考文件與範本。它解決重複解釋、上下文有限與做法不穩定三個問題。Agent Skills 已公開為開放規格，Claude Code、Claude 網頁版與 API、Codex 等工具都支援。",
  [u"Skill 和每次貼一段提示詞有什麼不同？", u"一個 Skill 資料夾最少需要什麼檔案？", u"為什麼說 Skill 能節省上下文空間？"]),

lesson(u"一個 Skill 的構造",
  u"YAML 開頭、Markdown 內文、選用的 scripts、references、assets",
  [u"看懂 SKILL.md 的格式", u"知道 name 與 description 的規則", u"了解選用資料夾的用途"],
  [("h", u"SKILL.md 的兩個部分"),
   C(u"""
---
name: commit-message
description: Write a commit message for the staged changes that follows the
  repository's conventions. Use when the user asks for a commit message.
---

# Commit message

1. Read the staged diff with `git diff --cached`.
2. Look at the last 10 commit messages to learn the style.
3. Write a subject line of at most 72 characters ...
"""),
   ("ul", [u"<strong>開頭的 YAML 區塊</strong>（frontmatter）：夾在兩行 <code>---</code> 之間，必須在檔案第一行開始。", u"<strong>內文</strong>：一般的 Markdown，寫步驟、規則、範例。"]),
   ("h", u"兩個核心欄位"),
   ("t", [u"欄位", u"規則（開放規格）", u"用途"],
    [[u"<code>name</code>", u"最多 64 個字元；只能用小寫英文字母、數字與連字號；不能以連字號開頭或結尾；通常和資料夾同名", u"識別名稱，也是手動呼叫時用的名字"],
     [u"<code>description</code>", u"最多 1,024 個字元", u"寫「做什麼」和「什麼時候用」：AI 靠它決定要不要載入這個 Skill"]]),
   ("p", u"開放規格另外定義了 <code>license</code>、<code>compatibility</code>、<code>metadata</code>、<code>allowed-tools</code> 等選用欄位。各工具還有自己的擴充欄位，例如 Claude Code 的 <code>disable-model-invocation</code>、<code>context</code>（第 10 課）。"),
   ("h", u"選用的資料夾"),
   ("t", [u"資料夾", u"放什麼", u"什麼時候被讀"],
    [[u"<code>scripts/</code>", u"可執行的腳本（Python、Shell……）", u"被<strong>執行</strong>，而不是被讀進上下文"],
     [u"<code>references/</code>", u"詳細文件、API 說明、範例", u"內文提到「需要時請讀 references/xxx.md」時才讀"],
     [u"<code>assets/</code>", u"範本、圖片、設定檔", u"產出時使用"]]),
   ("note", u"為什麼通用的範本只用 name 與 description", [("p", u"本課程收藏庫裡的自製 Skill 都只用這兩個欄位，所以同一個檔案放進 Claude Code 或 Codex 都能直接用。需要特定工具的進階功能時，再另外加欄位。")]),
   kw("gen", u"試試看：填表產生一份 SKILL.md（第 41 課與參考頁也有）："),
  ],
  u"SKILL.md 以兩行 --- 包住的 YAML 開頭（必須在第一行），後接 Markdown 內文。name 最多 64 字元、只用小寫字母數字與連字號，description 最多 1,024 字元，寫做什麼與何時用。選用資料夾有 scripts（被執行）、references（需要時才讀）、assets（範本與資源）。只用 name 與 description 的 Skill 可跨工具使用。",
  [u"name 欄位有哪些格式限制？", u"scripts 裡的檔案和 references 裡的檔案，被使用的方式有什麼不同？", u"為什麼通用範本只寫 name 與 description？"]),

lesson(u"漸進式載入",
  u"平常只看名片，需要時才翻開說明書",
  [u"理解漸進式載入的三個層次", u"知道 Skill 數量多時的上下文成本", u"學會控制 SKILL.md 的長度"],
  [("p", u"假設你裝了 50 個 Skill，每個說明 3,000 字。如果全部塞進對話，AI 還沒開始工作，上下文就滿了。Skill 的設計是<strong>漸進式載入</strong>（progressive disclosure）："),
   ("ol", [u"<strong>第一層：名稱與描述</strong>。啟動時只載入每個 Skill 的名稱和描述，每個大約幾十到一百多個 token。", u"<strong>第二層：SKILL.md 全文</strong>。AI 判斷這次任務需要某個 Skill 時，才讀進它的內文。", u"<strong>第三層：附帶檔案</strong>。內文說「需要時請讀 references/api.md」或「執行 scripts/check.py」時，才去讀或執行。"]),
   kw("disc", u"調整 Skill 數量與長度，比較漸進式載入與全部載入的上下文用量："),
   ("h", u"實務建議"),
   ("ul", [u"<strong>SKILL.md 保持精簡</strong>：Claude Code 文件建議 500 行以內；更長的內容拆到 references。", u"<strong>描述要精準</strong>：描述永遠在上下文裡，寫得太長也是負擔。Claude Code 列出 Skill 時，每個描述（加上 when_to_use）會被截到 1,536 個字元，所以最關鍵的使用情境要放在最前面。", u"<strong>能交給腳本的就交給腳本</strong>：腳本被執行時只有輸出進入上下文，程式碼本身不佔空間。", u"<strong>定期整理</strong>：停用很少用的 Skill，避免描述越積越多（第 42 課）。"]),
   ("note", u"上下文壓縮之後", [("p", u"長對話會被自動壓縮。Claude Code 會在壓縮後重新附上最近用過的 Skill 內容，但有預算限制（文件寫的是每個保留前 5,000 token、總共 25,000 token）。長任務最好另外用進度檔記錄狀態（第 27 課）。")]),
  ],
  u"漸進式載入分三層：啟動時只載入名稱與描述、需要時讀 SKILL.md 全文、內文指示時才讀參考檔或執行腳本，讓安裝大量 Skill 也不會塞滿上下文。實務上 SKILL.md 保持在約 500 行內，描述精準且把關鍵情境放前面，固定操作交給腳本，並定期停用少用的 Skill。",
  [u"漸進式載入的三個層次是什麼？", u"為什麼腳本比寫在內文裡的長說明更省上下文？", u"裝了 200 個 Skill 會有什麼問題？"]),

lesson(u"Skill 和其他機制的差別",
  u"專案說明檔、斜線指令、MCP、子代理、Hooks、外掛：各自適合做什麼",
  [u"分辨 Skill 與其他擴充機制", u"知道什麼情況該用哪一種", u"理解它們如何組合"],
  [("t", [u"機制", u"是什麼", u"什麼時候載入", u"適合"],
    [[u"專案說明檔（CLAUDE.md／AGENTS.md）", u"專案的長期規則與背景", u"每次對話一開始就載入", u"程式風格、測試指令、禁止事項等「永遠適用」的事"],
     [u"Skill", u"一套可重複使用的做法", u"需要時才載入", u"特定任務的流程：寫週報、做審查、除錯"],
     [u"斜線指令", u"使用者手動呼叫的快捷提示", u"使用者輸入 /名稱 時", u"在 Claude Code 中，Skill 也能用 /名稱 呼叫，指令與 Skill 已經合流"],
     [u"MCP 伺服器", u"讓 AI 連接外部工具與資料的協定", u"一直可用（工具清單）", u"查資料庫、操作 GitHub、讀雲端文件"],
     [u"子代理（subagent）", u"有自己上下文的另一個 AI 助手", u"主代理派工作時", u"隔離上下文、平行處理（第 14 課）"],
     [u"Hooks", u"在特定事件自動執行的程式", u"事件發生時（例如每次改檔後）", u"一定要執行、不能靠 AI 記得的事：格式化、檢查、記錄"],
     [u"外掛（plugin）", u"把以上幾種打包在一起分享", u"安裝後", u"團隊或社群發布一整套工具"]]),
   ("h", u"一個簡單的判斷方法"),
   ("ul", [u"「<strong>每次</strong>都要遵守」→ 專案說明檔。", u"「<strong>做某類工作時</strong>要這樣做」→ Skill。", u"「需要<strong>連接外部系統</strong>」→ MCP。", u"「<strong>絕對不能忘</strong>，最好不要靠 AI 自覺」→ Hooks。", u"「工作量大、會<strong>塞爆上下文</strong>或可以<strong>平行</strong>」→ 子代理。"]),
   ("h", u"組合使用"),
   ("p", u"這些機制常常一起出現：一個「發布新版」的 Skill 會呼叫 MCP 讀取 issue、派子代理平行跑測試，而 Hook 確保每次改檔都自動格式化；最後把它們包成外掛分享給團隊。"),
   ("note", u"MCP 與 Skill 的分工", [("p", u"MCP 提供「手」（能做什麼），Skill 提供「方法」（怎麼做比較好）。例如 GitHub 的 MCP 讓 AI 能讀寫 PR，而「PR 看守」Skill 告訴它遇到 CI 失敗時該怎麼處理（第 29 課）。")]),
  ],
  u"專案說明檔放永遠適用的規則，Skill 放特定任務的做法並按需載入，斜線指令在 Claude Code 中已與 Skill 合流，MCP 連接外部工具與資料，子代理提供隔離上下文與平行處理，Hooks 在事件發生時強制執行，外掛把它們打包分享。MCP 提供能力，Skill 提供方法。",
  [u"「每次提交前都要跑格式化」適合用 Skill 還是 Hook？為什麼？", u"MCP 和 Skill 怎麼分工？", u"什麼情況下應該使用子代理？"]),
]),

(u"模組 B｜怎麼寫出好 Skill", [

lesson(u"描述決定會不會被觸發",
  u"寫清楚做什麼、什麼時候用、什麼時候不要用",
  [u"寫出容易被正確觸發的描述", u"避免太廣或太窄的描述", u"學會用「不要用於」避免誤觸發"],
  [("p", u"AI 看不到 Skill 的內文，只看得到描述，就要決定要不要載入它。所以描述就是 Skill 的「門面」：寫不好，再好的內容也不會被用到；寫得太廣，又會在不相干的時候跳出來。"),
   TRIGGER,
   ("h", u"好描述的三個部分"),
   ("ol", [u"<strong>做什麼</strong>：一句話、動詞開頭。", u"<strong>什麼時候用</strong>：寫出使用者實際會說的話與情境（「要寫 commit 訊息」「CI 失敗」「整理會議逐字稿」）。", u"<strong>什麼時候不要用</strong>：和其他 Skill 劃清界線，避免誤觸發。"]),
   ("t", [u"", u"例子", u"問題"],
    [[u"太模糊", u"<code>Helps with code.</code>", u"什麼時候都像、什麼時候都不像"],
     [u"太窄", u"<code>Fixes the null pointer in UserService.java.</code>", u"只能用一次"],
     [u"只寫做什麼", u"<code>Generates weekly reports.</code>", u"沒寫觸發情境，使用者說「這週做了什麼」時可能不會被載入"],
     [u"好", u"<code>Write the weekly status report from merged pull requests and closed issues. Use when the user asks for a weekly report, status update, or what was shipped. Do not use for a single PR summary.</code>", u"—"]]),
   ("h", u"手動呼叫"),
   ("p", u"使用者也可以直接點名：Claude Code 用 <code>/名稱</code>，Codex 用 <code>$名稱</code>。有副作用的 Skill（例如部署、發文）常設定成<strong>只能手動呼叫</strong>，避免 AI 自己決定執行（Claude Code 的 <code>disable-model-invocation: true</code>，第 10 課）。"),
   ("note", u"描述用英文還是中文", [("p", u"兩種都可以。英文描述在跨工具、分享給國際團隊時比較方便；中文描述能直接寫進使用者的說法。也可以在英文描述裡加入幾個常用的中文關鍵詞。本課程的範本用英文寫，方便直接複製使用。")]),
  ],
  u"描述是 AI 決定是否載入 Skill 的唯一依據，應包含做什麼、何時用（使用者實際的說法與情境）與何時不要用。避免太模糊、太窄或只寫功能。使用者可用 Claude Code 的 /名稱 或 Codex 的 $名稱 手動呼叫，有副作用的 Skill 宜設為只能手動呼叫。",
  [u"好的描述應該包含哪三個部分？", u"為什麼要寫「什麼時候不要用」？", u"哪些 Skill 應該設定為只能手動呼叫？"]),

lesson(u"內文怎麼寫",
  u"步驟、判斷規則、完成條件與禁止事項",
  [u"掌握 SKILL.md 內文的常用結構", u"知道什麼該寫死、什麼該留給模型判斷", u"避免常見的寫法錯誤"],
  [("h", u"推薦的結構"),
   C(u"""
# 名稱

## 1. 先做什麼（準備、確認需求）
## 2. 主要步驟（編號，每一步附檢查方式）
## 3. 驗證
## Done when（完成的條件）
## Never / Stop（禁止事項、何時停下來問人）
"""),
   ("h", u"寫作原則"),
   ("ul", [u"<strong>用命令句、編號步驟</strong>：「Run the tests」比「It would be good to run tests」清楚。", u"<strong>每一步都要能檢查</strong>：附上指令、預期輸出或要存在的檔案。", u"<strong>規則寫成「如果……就……」</strong>：「If the same test fails 3 times, stop and report.」", u"<strong>給例子</strong>：一兩個前後對照，比十句形容詞有效。", u"<strong>寫出完成條件</strong>：沒有完成條件，代理很容易提早宣布完成（第 30 課）。", u"<strong>寫出禁止事項</strong>：特別是不可逆或對外的動作（第 31、39 課）。"]),
   ("h", u"寫死還是留彈性"),
   ("t", [u"情況", u"做法"],
    [[u"有唯一正確做法、出錯代價高（格式、指令參數、檔案路徑）", u"寫死，甚至交給腳本"],
     [u"需要依情況判斷（審查重點、文件語氣）", u"給原則與例子，留給模型判斷"],
     [u"模型本來就很會（一般寫作、通用程式知識）", u"不用寫，寫了反而浪費上下文"]]),
   ("h", u"常見錯誤"),
   ("ul", [u"把整本手冊塞進 SKILL.md。", u"只寫目標不寫步驟（「做出高品質的報告」）。", u"互相矛盾的規則。", u"依賴對話中才有的背景（Skill 也可能在子代理中執行，看不到原對話）。", u"假設某個工具一定存在（跨工具的 Skill 要寫「如果有子代理就……，否則……」）。"]),
   SK("plan-execute-verify"),
  ],
  u"SKILL.md 內文建議依序寫準備、編號步驟（每步附檢查）、驗證、完成條件、禁止事項與停止條件。用命令句、if-then 規則與具體例子。唯一正確且代價高的做法要寫死或交給腳本，需要判斷的給原則，模型本來就會的不必寫。避免塞整本手冊、只寫目標、規則矛盾、依賴對話背景與假設特定工具存在。",
  [u"為什麼每一步都要附檢查方式？", u"什麼樣的內容應該交給腳本而不是寫在內文？", u"跨工具使用的 Skill 寫法要注意什麼？"]),

lesson(u"附帶腳本與參考資料",
  u"讓程式做程式擅長的事，讓模型做判斷",
  [u"知道何時該寫腳本", u"學會在內文中引用附帶檔案", u"注意腳本的安全與可攜性"],
  [("h", u"什麼時候寫腳本"),
   ("ul", [u"<strong>需要精確</strong>：計算、格式轉換、驗證 JSON 結構。", u"<strong>重複而機械</strong>：收集資料、重新命名、產生檔案清單。", u"<strong>模型容易出錯</strong>：複雜的指令參數、特定 API 的呼叫順序。", u"<strong>結果要可重現</strong>：同樣的輸入每次都要一樣的輸出。"]),
   ("h", u"在內文中引用"),
   C(u"""
## 2. Collect data
Run `python scripts/collect.py --days 7` and read its JSON output.

## 3. Format
Follow the section order in references/format.md.
Only read references/edge-cases.md if a PR has no linked issue.
"""),
   ("p", u"Claude Code 提供 <code>${CLAUDE_SKILL_DIR}</code> 代表 Skill 所在的資料夾，可以用來寫出不受工作目錄影響的路徑；它也能在 <code>allowed-tools</code> 中預先允許執行自己附帶的腳本，例如 <code>Bash(${CLAUDE_SKILL_DIR}/scripts/render.sh *)</code>。"),
   ("h", u"動態背景"),
   ("p", u"Claude Code 的 Skill 可以在內文中寫 <code>!`git diff HEAD`</code>：在 AI 讀到 Skill 之前先執行指令，把輸出直接放進內文。這樣 AI 一開始就看到最新狀態。指令失敗會讓整個 Skill 載入失敗，可能失敗的指令要加上 <code>|| true</code>。"),
   ("h", u"安全與可攜性"),
   ("ul", [u"腳本以使用者的權限執行，等於讓 AI 執行你給它的程式：要像審查程式一樣審查腳本（第 40 課）。", u"不要在腳本或參考檔裡寫密碼、API 金鑰。", u"註明需要的語言版本與套件；跨平台的腳本避免依賴特定作業系統的指令。"]),
  ],
  u"需要精確、重複機械、容易出錯或要可重現的步驟應寫成腳本，在內文中明確寫出何時執行哪個腳本、何時讀哪份參考檔。Claude Code 提供 ${CLAUDE_SKILL_DIR} 路徑與 !`指令` 動態背景，allowed-tools 可預先允許附帶腳本。腳本以使用者權限執行，需審查、不可含密鑰並註明依賴。",
  [u"舉兩個應該寫成腳本的步驟。", u"!`git diff HEAD` 在 Skill 中有什麼作用？", u"為什麼附帶腳本也需要安全審查？"]),

lesson(u"測試與改進",
  u"有裝和沒裝 Skill，到底差多少？",
  [u"設計 Skill 的測試案例", u"比較有無 Skill 的差異", u"根據結果改描述或內文"],
  [("p", u"寫完 Skill 不代表它有用。最常見的情況是：AI 本來就會做，Skill 只是多佔上下文；或 Skill 從來沒被觸發。所以 Skill 需要像程式一樣測試。"),
   ("h", u"兩種測試"),
   ("t", [u"測什麼", u"怎麼測", u"沒通過時改哪裡"],
    [[u"觸發", u"寫 3～5 句應該觸發、2～3 句不該觸發的需求，看 AI 有沒有正確載入", u"描述"],
     [u"效果", u"同樣的任務，有 Skill 與沒有 Skill 各做幾次，比較結果", u"內文、腳本"]]),
   ("h", u"怎麼評估效果"),
   ("ul", [u"<strong>可自動檢查的</strong>：測試是否通過、輸出格式是否正確、是否包含必要欄位。", u"<strong>需要判斷的</strong>：用評分標準（rubric）由人或另一個模型評分；評分者最好看不出哪份有用 Skill。", u"多跑幾次：AI 的輸出有隨機性，一次的好壞不代表什麼。"]),
   ("h", u"工具"),
   ("ul", [u"Anthropic 官方範例庫的 <strong>skill-creator</strong> Skill 包含建立、修改與評估 Skill 的流程。", u"Codex 內建 <strong>$skill-creator</strong>，引導建立新 Skill。", u"Claude Code 提供 <code>/skill-doctor</code> 等工具，檢查哪些 Skill 在沒被使用時也佔用上下文。"]),
   SK("anthropic-skill-creator", "codex-skill-creator", "skill-author"),
   ("note", u"一個常被忽略的結果", [("p", u"如果測試發現有沒有 Skill 結果差不多，最好的決定是<strong>刪掉它</strong>。Skill 不是越多越好。")]),
  ],
  u"Skill 要測觸發（應觸發與不應觸發的需求）與效果（有無 Skill 的結果比較）。可自動檢查的用測試與格式驗證，需判斷的用評分標準並盲評，且要多跑幾次。可使用 Anthropic 的 skill-creator、Codex 內建的 $skill-creator 與 Claude Code 的 /skill-doctor。效果差不多的 Skill 應該刪除。",
  [u"Skill 的觸發測試要準備哪兩類需求？", u"為什麼評分者最好看不出哪份結果有用 Skill？", u"測試後發現 Skill 沒有幫助，該怎麼辦？"]),

lesson(u"版本、分享與團隊共用",
  u"把 Skill 放進 git、做成外掛、在團隊之間流通",
  [u"知道個人與專案層級 Skill 的差別", u"學會用 git 與外掛分享 Skill", u"建立 Skill 的版本管理習慣"],
  [("h", u"放在哪裡決定誰能用"),
   ("t", [u"層級", u"Claude Code", u"Codex", u"誰能用"],
    [[u"專案", u"<code>.claude/skills/&lt;name&gt;/</code>", u"<code>.agents/skills/&lt;name&gt;/</code>", u"所有 clone 這個 repo 的人（提交進 git）"],
     [u"個人", u"<code>~/.claude/skills/&lt;name&gt;/</code>", u"<code>~/.agents/skills/&lt;name&gt;/</code>", u"你自己，所有專案"],
     [u"組織／管理員", u"由管理設定部署的目錄", u"<code>/etc/codex/skills</code>", u"整台機器或整個組織"],
     [u"外掛", u"外掛裡的 <code>skills/</code>，呼叫時是 <code>/外掛名:skill名</code>", u"透過外掛（plugins）安裝", u"安裝外掛的人"]]),
   ("p", u"同名衝突時，Claude Code 的優先順序是組織 > 個人 > 專案；Codex 則有自己的範圍順序（第 12 課）。"),
   ("h", u"版本管理"),
   ("ul", [u"Skill 就是文字檔，放進 git 和程式碼一起管理：每次修改都能看差異、回復。", u"重大修改寫在 commit 訊息或 Skill 內的變更紀錄裡。", u"團隊共用的 Skill 經過審查再合併，就像程式碼審查。"]),
   ("h", u"做成外掛分享"),
   ("p", u"Claude Code 的<strong>外掛市集</strong>可以把多個 Skill、子代理、Hooks、MCP 設定打包發布。例如 Anthropic 官方範例：<code>/plugin marketplace add anthropics/skills</code> 加入市集，再 <code>/plugin install example-skills@anthropic-agent-skills</code> 安裝。Codex 也有外掛（plugins）機制可安裝套件。"),
   SK("changelog-writer"),
  ],
  u"Skill 放在專案（.claude/skills 或 .agents/skills，提交進 git 共用）、個人（~/.claude/skills 或 ~/.agents/skills）、組織或外掛中，位置決定誰能用。Skill 是文字檔，應以 git 管理版本並經過審查。Claude Code 的外掛市集與 Codex 的外掛機制可打包分享多個 Skill 與相關設定。",
  [u"專案層級和個人層級的 Skill 各適合放什麼？", u"為什麼團隊的 Skill 要經過審查才合併？", u"外掛和單一 Skill 有什麼不同？"]),
]),

(u"模組 C｜平台與安裝", [

lesson(u"Claude Code 的 Skill",
  u"位置、擴充欄位、/呼叫、參數、子代理執行",
  [u"知道 Claude Code 從哪裡載入 Skill", u"了解 Claude Code 的擴充欄位", u"會使用參數與子代理執行"],
  [("h", u"載入位置"),
   ("ul", [u"個人：<code>~/.claude/skills/&lt;name&gt;/SKILL.md</code>", u"專案：<code>.claude/skills/&lt;name&gt;/SKILL.md</code>（子資料夾裡的 <code>.claude/skills/</code> 也會在該資料夾工作時載入）", u"外掛：<code>&lt;plugin&gt;/skills/&lt;name&gt;/SKILL.md</code>", u"組織：管理設定目錄下的 <code>.claude/skills/</code>", u"修改 Skill 不需重新啟動；新增頂層的 <code>.claude/skills/</code> 目錄時用 <code>/reload-skills</code>。"]),
   ("h", u"常用擴充欄位"),
   ("t", [u"欄位", u"作用"],
    [[u"<code>when_to_use</code>", u"補充觸發情境，接在描述後面"],
     [u"<code>disable-model-invocation: true</code>", u"只能由使用者用 /名稱 呼叫，Claude 不會自己載入（適合部署、發文等有副作用的流程）"],
     [u"<code>user-invocable: false</code>", u"從 / 選單隱藏，只讓 Claude 自己判斷使用"],
     [u"<code>allowed-tools</code>", u"這個 Skill 執行時可以免確認使用的工具"],
     [u"<code>disallowed-tools</code>", u"執行時移除某些工具"],
     [u"<code>context: fork</code>／<code>agent</code>", u"在子代理中執行，搭配 agent 指定子代理類型（Explore、Plan 等）"],
     [u"<code>model</code>／<code>effort</code>", u"指定模型或推理強度"],
     [u"<code>paths</code>", u"只在處理符合路徑的檔案時自動載入"],
     [u"<code>arguments</code>／<code>argument-hint</code>", u"定義參數與輸入提示"]]),
   ("h", u"參數"),
   C(u"""
---
name: fix-issue
description: Fix a GitHub issue by number
argument-hint: "[issue-number]"
disable-model-invocation: true
---

Fix issue #$ARGUMENTS. Read the issue, reproduce it, write a failing test,
fix it, and run the full test suite.
"""),
   ("p", u"輸入 <code>/fix-issue 123</code> 時，<code>$ARGUMENTS</code> 會被換成 <code>123</code>；也可以用 <code>$0</code>、<code>$1</code> 取第幾個參數。"),
   ("h", u"在子代理中執行"),
   C(u"""
---
name: deep-research
description: Research a topic thoroughly
context: fork
agent: Explore
---

Research $ARGUMENTS thoroughly ...
"""),
   ("p", u"設定 <code>context: fork</code> 後，Skill 的內容會成為子代理的任務說明，子代理<strong>看不到原本的對話</strong>，工作完成後只把結果帶回來。中間大量的搜尋與閱讀不會塞進主對話——這是多工 Skill 的重要工具（模組 D、E）。"),
   ("note", u"權限控制", [("p", u"可以在設定中用 <code>Skill(名稱)</code> 規則允許或禁止特定 Skill，或用 <code>skillOverrides</code> 把某個 Skill 設為關閉、只顯示名稱、只能手動呼叫。")]),
  ],
  u"Claude Code 從個人、專案（含子資料夾）、外掛與組織目錄載入 Skill，修改免重啟。擴充欄位包括 when_to_use、disable-model-invocation、user-invocable、allowed-tools、disallowed-tools、context: fork 與 agent、model、effort、paths、arguments。/名稱 後的文字以 $ARGUMENTS 或 $0、$1 帶入；context: fork 讓 Skill 在看不到原對話的子代理中執行。可用 Skill(名稱) 規則與 skillOverrides 控制權限。",
  [u"disable-model-invocation 和 user-invocable: false 有什麼不同？", u"context: fork 有什麼好處？子代理看得到原對話嗎？", u"/fix-issue 123 中的 123 怎麼被帶進 Skill？"]),

lesson(u"Claude 網頁版、桌面版與 API 中的 Skill",
  u"上傳 Skill、使用內建的文件 Skill，以及 API 的限制",
  [u"知道在 Claude 應用程式中使用 Skill 的方式", u"了解 API 中的 Skill", u"知道不同環境支援的欄位差異"],
  [("h", u"Claude 應用程式"),
   ("ul", [u"Anthropic 的範例 Skill（包括文件處理的 docx、pdf、pptx、xlsx）已提供給付費方案使用。", u"可以在設定中上傳自己的 Skill（通常是把資料夾壓縮成 zip），之後在對話中被自動使用。", u"在 Claude Code 中登入同一個帳號時，帳號裡的 Skill 也可以同步使用。"]),
   ("h", u"API 中的 Skill"),
   ("ul", [u"開發者可以透過 Claude API 使用 Anthropic 預先建立的 Skill，或上傳自訂 Skill。", u"Skill 搭配程式碼執行環境使用：模型在容器中讀取 Skill、執行附帶的腳本、產生檔案。", u"細節（端點、版本）請以官方文件的 Skills 指南為準。"]),
   ("h", u"欄位限制"),
   ("p", u"在 Claude Code 以外（上傳到 Claude 網頁版、透過 Skills API），只允許 <code>name</code>、<code>description</code>、<code>license</code>、<code>compatibility</code>、<code>metadata</code>、<code>allowed-tools</code> 這幾個欄位，其他欄位會造成錯誤。所以：<strong>要跨環境使用的 Skill，不要加 Claude Code 專用的擴充欄位</strong>。"),
   SK("anthropic-doc-skills", "anthropic-doc-coauthoring"),
   ("note", u"適合在應用程式中使用的 Skill", [("p", u"應用程式裡沒有你的程式碼庫，最適合的是<strong>文件與分析</strong>類 Skill：會議紀錄、資料報告、品牌格式、簡報與試算表。需要操作專案檔案、跑測試、開 PR 的 Skill，則適合 Claude Code 與 Codex。")]),
  ],
  u"Claude 應用程式提供 Anthropic 範例 Skill（含 docx、pdf、pptx、xlsx 文件 Skill）並可上傳自訂 Skill，登入的 Claude Code 也能同步。API 可使用預建或自訂 Skill，搭配程式碼執行環境運作。Claude Code 以外只允許 name、description、license、compatibility、metadata、allowed-tools 欄位，跨環境的 Skill 不應加 Claude Code 專用欄位。",
  [u"在 Claude 網頁版上傳的 Skill，可以使用 context: fork 嗎？為什麼？", u"API 中的 Skill 怎麼執行附帶的腳本？", u"哪些類型的 Skill 最適合在應用程式中使用？"]),

lesson(u"Codex 的 Skill 與開放規格",
  u"OpenAI Codex 的 Skill 位置、呼叫方式，以及跨工具使用",
  [u"知道 Codex 從哪裡載入 Skill", u"會在 Codex 中安裝與呼叫 Skill", u"理解開放規格帶來的可攜性"],
  [("p", u"OpenAI 的 Codex（命令列 CLI、桌面 App、IDE 外掛與雲端版）也支援 Agent Skills，官方文件說明它建立在 agentskills.io 的開放規格上。"),
   ("h", u"載入位置與範圍"),
   ("t", [u"範圍", u"位置", u"說明"],
    [[u"REPO（專案）", u"<code>.agents/skills/</code>", u"在目前工作目錄、上一層與 repo 根目錄尋找"],
     [u"USER（個人）", u"<code>$HOME/.agents/skills/</code>", u"所有專案都能用"],
     [u"ADMIN（管理員）", u"<code>/etc/codex/skills/</code>", u"整台機器或容器的預設"],
     [u"SYSTEM（系統）", u"隨 Codex 內建", u"例如 skill-creator"]]),
   ("p", u"舊版的 <code>~/.codex/skills</code> 已被視為舊路徑。"),
   ("h", u"呼叫與安裝"),
   ("ul", [u"<strong>自動</strong>：需求和描述相符時，Codex 自動使用。", u"<strong>手動</strong>：在提示中用 <code>$名稱</code> 點名，例如 <code>$skill-creator</code>。", u"<strong>安裝</strong>：用 <code>$skill-installer</code> 從範例庫安裝，例如 <code>$skill-installer gh-address-comments</code>；安裝後重新啟動 Codex。", u"<strong>停用</strong>：在 <code>~/.codex/config.toml</code> 中以 <code>[[skills.config]]</code> 設定。", u"<strong>選用的 agents/openai.yaml</strong>：放介面顯示資訊、呼叫政策與相依的工具設定。"]),
   ("h", u"專案說明：AGENTS.md"),
   ("p", u"Codex 用 <code>AGENTS.md</code> 存放專案的長期規則（類似 Claude Code 的 <code>CLAUDE.md</code>）。永遠適用的規則放 AGENTS.md，特定任務的做法放 Skill。"),
   ("h", u"一份 Skill，兩邊都能用"),
   C(u"""
# 同一份 Skill 放到兩個位置（或用符號連結）
mkdir -p .claude/skills/tdd-loop .agents/skills/tdd-loop
cp SKILL.md .claude/skills/tdd-loop/
cp SKILL.md .agents/skills/tdd-loop/
"""),
   ("p", u"只要 Skill 只用 <code>name</code>、<code>description</code> 與 Markdown 內文，不依賴某個工具專屬的指令名稱，就能在 Claude Code 與 Codex 之間共用。開放規格也被許多其他程式開發工具採用，但各工具的支援細節不同，使用前請查閱各自的文件。"),
   SK("codex-gh-address-comments"),
   ("note", u"Codex 的子代理", [("p", u"撰寫時，Codex 的多代理功能被標示為實驗性功能，需要在設定中開啟；開啟後可以平行產生多個專門的代理再彙整結果。也可以用非互動的 <code>codex exec</code> 搭配多個 git worktree 平行執行（第 14、16 課）。")]),
  ],
  u"Codex 依 REPO（.agents/skills，從工作目錄到 repo 根）、USER（$HOME/.agents/skills）、ADMIN（/etc/codex/skills）、SYSTEM（內建）四個範圍載入 Skill，舊路徑 ~/.codex/skills 已淘汰。可自動觸發或以 $名稱 呼叫，用 $skill-installer 安裝（需重啟），在 config.toml 停用，agents/openai.yaml 為選用設定；專案規則放 AGENTS.md。只用 name、description 的 Skill 可在 Claude Code 與 Codex 共用。",
  [u"Codex 的專案層級 Skill 放在哪個資料夾？", u"在 Codex 中怎麼手動呼叫一個 Skill？", u"要讓同一份 Skill 在 Claude Code 與 Codex 都能用，要注意什麼？"]),
]),
]
