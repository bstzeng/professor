# -*- coding: utf-8 -*-
"""第 6 課（Claude API 版）：SDK 的 @beta_tool 會從函式簽名與 docstring 自動產生工具定義。"""
import json
from anthropic import beta_tool


@beta_tool
def search_books(query: str, max_results: int = 5, in_stock_only: bool = False) -> str:
    """在書店庫存中搜尋書籍，依相關度排序。

    Args:
        query: 關鍵字，例如書名或作者
        max_results: 最多回傳幾本
        in_stock_only: 只列出有庫存的書
    """
    return json.dumps([])


# 印出 SDK 產生、實際會送給 Claude 的工具定義
print(json.dumps(search_books.to_dict(), ensure_ascii=False, indent=2))
