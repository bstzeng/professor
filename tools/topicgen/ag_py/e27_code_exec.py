# -*- coding: utf-8 -*-
"""第 27 課：讓代理執行程式碼——模型寫程式，我們在「隔離的子行程」裡跑，設時間限制，把輸出回傳。"""
import json
import subprocess
import sys
import tempfile
from mockllm import MockClient, text, tool_use

def run_python(code, timeout=5):
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8") as f:
        f.write(code)
    try:
        p = subprocess.run([sys.executable, "-I", f.name], capture_output=True, text=True, timeout=timeout,
                           cwd=tempfile.gettempdir())             # -I：隔離模式，不讀使用者環境
        return {"stdout": p.stdout[-2000:], "stderr": p.stderr[-2000:], "return_code": p.returncode}
    except subprocess.TimeoutExpired:
        return {"stdout": "", "stderr": "執行超過 %d 秒，已中止" % timeout, "return_code": -1}

CODE_V1 = "data = [12, 7, 3, 25, 8]\nprint('平均', sum(data) / len(data))\nprint('標準差', statistics.stdev(data))"
CODE_V2 = "import statistics\n" + CODE_V1

def policy(ctx):
    if ctx.turn == 0:
        return [text("我寫程式來算。"), tool_use("run_python", {"code": CODE_V1})]
    out = ctx.data()
    if out["return_code"] != 0:
        return [text("忘了 import，修正後再跑。"), tool_use("run_python", {"code": CODE_V2})]
    return text("結果：\n" + out["stdout"].strip())

tools = [{"name": "run_python", "description": "在沙箱中執行 Python 程式碼，回傳 stdout、stderr 與結束碼",
          "input_schema": {"type": "object", "properties": {"code": {"type": "string"}}, "required": ["code"]}}]
client, msgs = MockClient(policy), [{"role": "user", "content": "這組數字 12,7,3,25,8 的平均與標準差？"}]
while True:
    r = client.messages.create(model="mock", max_tokens=1000, tools=tools, messages=msgs)
    msgs.append({"role": "assistant", "content": r.content})
    if r.stop_reason != "tool_use":
        break
    b = next(x for x in r.content if x.type == "tool_use")
    out = run_python(**b.input)
    print("執行結果：return_code=%d %s" % (out["return_code"], (out["stderr"].strip().splitlines() or [""])[-1]))
    msgs.append({"role": "user", "content": [{"type": "tool_result", "tool_use_id": b.id, "content": json.dumps(out, ensure_ascii=False)}]})
print(r.content[0].text)
print(run_python("while True: pass", timeout=1)["stderr"])
