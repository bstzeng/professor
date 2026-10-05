# -*- coding: utf-8 -*-
"""Agentic AI 的運行原理主題的規格。產生頁面時也會把 Python 範例複製到 topics/agentic-ai/py/ 並打包成 zip。"""
import io
import os
import shutil
import zipfile
import ag_a, ag_e, ag_ref
from ag_common import PYDIR

TOPIC = {
    "id": "agentic-ai",
    "category": "tech",
    "title": u"Agentic AI 的運行原理",
    "short": u"Agentic AI",
    "crumb": u"Agentic AI",
    "icon": u"🤖",
    "description": u"Agentic AI 完整導讀，每一個動作都附 Python 範例（離線假 LLM 版可直接執行＋Claude API 版）：代理迴圈、工具定義與往返、平行呼叫、錯誤處理、Tool Runner；"
                   u"思考、ReAct、規劃、待辦清單、反思與停止條件；上下文視窗、歷史管理、嵌入、RAG、長期記憶、提示快取、上下文工程；"
                   u"執行程式、檔案、上網、MCP、computer use 與迷你程式代理；多代理；結構化輸出、防護欄、人在迴路、沙箱、提示注入、評估、追蹤、成本；"
                   u"Claude Code 與 Codex 案例剖析、部署與未來。附六個互動工具與完整範例下載。",
}

MODULES = ag_a.MODULES + ag_e.MODULES

REFERENCES = ag_ref.REFERENCES


def _publish():
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "topics", TOPIC["id"], "py")
    if os.path.isdir(out):
        shutil.rmtree(out)
    os.makedirs(os.path.join(out, "claude"))
    files = sorted(f for f in os.listdir(PYDIR) if f.endswith(".py") and f != "ag_run.py")
    cfiles = sorted(f for f in os.listdir(os.path.join(PYDIR, "claude")) if f.endswith(".py"))
    for f in files:
        shutil.copyfile(os.path.join(PYDIR, f), os.path.join(out, f))
    for f in cfiles:
        shutil.copyfile(os.path.join(PYDIR, "claude", f), os.path.join(out, "claude", f))
    readme = (u"Agentic AI 的運行原理：Python 範例\n\n"
              u"離線版（本資料夾）：python a01_chat_vs_agent.py\n"
              u"  需要 Python 3.9 以上；mockllm.py 是模仿 Anthropic SDK 介面的假 LLM，不需 API 金鑰、不需網路。\n\n"
              u"Claude API 版（claude/ 資料夾）：\n"
              u"  pip install anthropic\n  export ANTHROPIC_API_KEY=你的金鑰\n  python claude/a01_chat_vs_agent.py\n"
              u"  會實際呼叫 Claude API 並計費。API 細節以 Anthropic 官方文件為準。\n")
    with zipfile.ZipFile(os.path.join(out, "agentic-ai-examples.zip"), "w", zipfile.ZIP_DEFLATED) as z:
        def add(name, data):
            info = zipfile.ZipInfo("agentic-ai-examples/" + name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, data)
        add("README.txt", readme.encode("utf-8"))
        for f in files:
            add(f, io.open(os.path.join(PYDIR, f), "rb").read())
        for f in cfiles:
            add("claude/" + f, io.open(os.path.join(PYDIR, "claude", f), "rb").read())


_publish()
