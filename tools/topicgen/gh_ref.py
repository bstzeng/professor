# -*- coding: utf-8 -*-
"""GitHub 從零到協作：參考頁——互動工具箱與名詞速查。"""
from gh_common import *
import gh_a, gh_e

GUIDE = {
    "file": "guide.html", "title": u"Git 互動工具箱", "h1": u"Git 互動工具箱", "icon": u"🧰",
    "description": u"三個區域、分支模擬器、reset 模式、合併衝突、.gitignore 測試器、雜湊計算、PR 流程、復原與救援決策樹、指令速查",
    "body": [
        ("raw", u"<script>%s</script>" % GHLIB),
        ("p", u"本頁集中課程中所有互動工具，方便隨時練習與查詢。"),
        ("h", u"1. 三個區域（第 3 課）"), gh_a._AREAS,
        ("h", u"2. 分支模擬器（第 21、25 課）"), gh_a._GRAPH,
        ("h", u"3. reset 的三種模式（第 15 課）"), ghw({"t": "reset", "q": u"git reset 的三種模式（歷史 A → B → C，main 指向 C）："}),
        ("h", u"4. 合併衝突練習（第 24 課）"), ghw({"t": "conflict", "q": u"解開這個衝突：", "file": "app.py", "br": "feature-greet", "ours": "print(\"Hello!\")", "theirs": "print(\"你好\")"}),
        ("h", u"5. .gitignore 測試器（第 14 課）"), ghw({"t": "ignore", "q": u"修改規則與路徑，看哪些檔案被忽略："}),
        ("h", u"6. blob 雜湊計算（第 46 課）"), ghw({"t": "hash", "q": u"輸入檔案內容，算出 Git 的物件 ID："}),
        ("h", u"7. Pull Request 流程（第 29 課）"), gh_e._PRFLOW,
        ("h", u"8. 我要復原（第 15 課）"), gh_a._RESTORE_TREE,
        ("h", u"9. 災難救援（第 49 課）"), gh_e._RESCUE,
        ("h", u"10. 指令速查（第 53 課）"), gh_e._CARDS,
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"名詞速查", "h1": u"Git 與 GitHub 名詞速查", "icon": u"📖",
    "description": u"Git 與 GitHub 常見名詞的中英對照與說明",
    "body": [
        ("raw", u"<script>%s</script>" % GHLIB),
        gh_e._CARDS,
        ("h", u"Git 名詞"),
        ("t", [u"名詞", u"說明", u"課"],
         [[u"repository（倉庫）", u"被 Git 管理的專案，歷史存在 .git", LS(9)], [u"commit", u"專案在某時間點的快照，有唯一雜湊", LS(4)], [u"working directory", u"工作目錄，你正在編輯的檔案", LS(3)],
          [u"staging area／index", u"暫存區，下一個 commit 的草稿", LS(3)], [u"HEAD", u"指向目前所在分支的指標", LS(21)], [u"branch（分支）", u"指向 commit 的可移動標籤", LS(21)],
          [u"merge", u"合併分支；快轉或產生合併 commit", LS(23)], [u"fast-forward", u"快轉：只移動分支標籤", LS(23)], [u"conflict（衝突）", u"兩邊改了同一處，需人工決定", LS(24)],
          [u"rebase", u"把 commit 重新播放到新的基礎上", LS(25)], [u"remote／origin", u"遠端倉庫；clone 的來源預設叫 origin", LS(10)], [u"upstream", u"fork 時慣用來指原專案的遠端名稱", LS(33)],
          [u"fetch／pull／push", u"取回／取回並合併／送出", LS(12)], [u"stash", u"暫時收起未 commit 的修改", LS(17)], [u"tag", u"替 commit 取的固定名字，常用於版本", LS(18)],
          [u"reflog", u"HEAD 在本機走過的紀錄", LS(28)], [u"cherry-pick", u"複製單一 commit", LS(28)], [u"detached HEAD", u"HEAD 直接指向 commit 而非分支", LS(47)],
          [u"blob／tree", u"Git 物件：檔案內容／資料夾", LS(46)], [u"packfile", u"打包壓縮後的物件檔", LS(48)], [u".gitignore", u"列出不要追蹤的檔案規則", LS(14)]]),
        ("h", u"GitHub 名詞"),
        ("t", [u"名詞", u"說明", u"課"],
         [[u"Pull Request（PR）", u"請求把分支合併的審查與討論", LS(29)], [u"Code Review", u"在 PR 上逐行審查", LS(30)], [u"Squash and merge", u"把 PR 壓成一個 commit 合併", LS(31)],
          [u"Fork", u"把倉庫複製到自己帳號下", LS(32)], [u"Issue", u"問題回報與待辦討論串", LS(34)], [u"Projects", u"看板與表格式的工作管理", LS(35)],
          [u"Rulesets／Branch protection", u"分支保護規則", LS(36)], [u"CODEOWNERS", u"指定檔案負責人並自動請求審查", LS(36)], [u"Organization", u"組織帳號，以 Teams 管理成員", LS(37)],
          [u"GitHub Actions", u"自動化工作流程", LS(38)], [u"CI", u"持續整合：每次推送自動測試", LS(39)], [u"GitHub Pages", u"從倉庫發布靜態網站", LS(40)], [u"Secrets", u"加密保存的機密值", LS(41)],
          [u"Release", u"建立在 tag 上的發布頁面", LS(42)], [u"Dependabot", u"自動更新有漏洞或過時的套件", LS(43)], [u"Push protection", u"推送時擋下外洩的金鑰", LS(43)],
          [u"Codespaces", u"雲端開發環境", LS(45)], [u"Git LFS", u"大型檔案儲存", LS(50)]]),
    ],
}

REFERENCES = [GUIDE, GLOSSARY]
