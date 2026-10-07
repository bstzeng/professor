# -*- coding: utf-8 -*-
"""GitHub 從零到協作主題的規格。"""
import gh_a, gh_e, gh_ref

TOPIC = {
    "id": "github",
    "category": "tech",
    "title": u"GitHub 從零到協作：Git 版本控制與團隊開發",
    "short": u"GitHub 從零到協作",
    "crumb": u"GitHub 從零到協作",
    "icon": u"🐙",
    "description": u"從安裝、第一個 commit 開始，學會 Git 的三個區域、分支、合併與衝突、rebase、復原與救援，再到 GitHub 的 Pull Request、Code Review、Fork、Issue、Projects、分支保護、"
                   u"GitHub Actions、Pages、Secrets、Releases、Dependabot，以及 Git 的內部原理。所有指令範例都實際執行過並附上真實輸出；附三個區域模擬器、分支模擬器、衝突練習、"
                   u".gitignore 測試器、雜湊計算與復原決策樹等互動工具。",
}

MODULES = gh_a.MODULES + gh_e.MODULES

REFERENCES = gh_ref.REFERENCES
