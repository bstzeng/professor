# -*- coding: utf-8 -*-
"""第 6 課：工具＝函式＋說明書（JSON Schema）。
模型看不到你的程式碼，只看得到 name、description、input_schema。
這裡寫一個小工具：從 Python 函式的型別標註與 docstring 自動產生工具定義。"""
import inspect
import json

PY2JSON = {str: "string", int: "integer", float: "number", bool: "boolean", list: "array", dict: "object"}

def to_tool(fn):
    sig = inspect.signature(fn)
    doc = inspect.getdoc(fn) or ""
    summary = doc.split("\n")[0]
    arg_docs = {}
    for line in doc.split("\n"):                       # 解析「參數名: 說明」
        line = line.strip()
        if ":" in line and line.split(":")[0] in sig.parameters:
            k, v = line.split(":", 1)
            arg_docs[k] = v.strip()
    props, required = {}, []
    for name, p in sig.parameters.items():
        props[name] = {"type": PY2JSON.get(p.annotation, "string")}
        if name in arg_docs:
            props[name]["description"] = arg_docs[name]
        if p.default is inspect.Parameter.empty:
            required.append(name)
        else:
            props[name]["default"] = p.default
    return {"name": fn.__name__, "description": summary,
            "input_schema": {"type": "object", "properties": props, "required": required}}

def search_books(query: str, max_results: int = 5, in_stock_only: bool = False):
    """在書店庫存中搜尋書籍，依相關度排序。

    query: 關鍵字，例如書名或作者
    max_results: 最多回傳幾本
    in_stock_only: 只列出有庫存的書
    """
    return []

print(json.dumps(to_tool(search_books), ensure_ascii=False, indent=2))
print("\n模型決定要不要用這個工具，完全依賴上面這段文字——說明寫得好不好，直接影響代理表現。")
