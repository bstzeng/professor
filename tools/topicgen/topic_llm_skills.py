# -*- coding: utf-8 -*-
"""LLM Skill 專區的規格。"""
import skl_a, skl_d, skl_f, skl_h, skl_ref

TOPIC = {
    "id": "llm-skills",
    "category": "ai",
    "title": u"LLM Skill 專區：讓 AI 代理多工、自主完成任務的技能收藏",
    "short": u"LLM Skill 專區",
    "crumb": u"LLM Skill 專區",
    "icon": u"🧩",
    "description": u"Agent Skills 完整介紹與收藏庫：SKILL.md 構造、漸進式載入、與 MCP／子代理／Hooks 的差別；怎麼寫出會被正確觸發、可測試的 Skill；Claude Code、Claude 應用程式與 API、Codex 的用法；"
                   u"操縱代理：子代理、平行分派與彙整、git worktree、編排模式；多工 Skill（平行研究、批次處理、多角度審查、跨 repo 修改）與自主完成 Skill（規劃驗證、測試迴圈、系統化除錯、進度檔、循環任務、PR 看守、完成定義、停止條件）；"
                   u"權限、提示注入與第三方 Skill 審核。附可一鍵複製的 Skill 收藏庫、Skill 產生器與互動模擬。",
}

MODULES = skl_a.MODULES + skl_d.MODULES + skl_f.MODULES + skl_h.MODULES

REFERENCES = skl_ref.REFERENCES
