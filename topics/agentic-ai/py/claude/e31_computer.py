# -*- coding: utf-8 -*-
"""第 31 課（Claude API 版）：computer use 工具組（computer_toolset_20260801，Claude Opus 5.5 只接受這個形式）。
Claude 的 tool_use 名稱就是動作（screenshot、left_click、type…），並帶 toolset_name="computer"；
每個 tool_result 也要回傳 toolset_name="computer"。截圖與實際操作需要你自己實作
（例如在虛擬機或容器裡用 pyautogui、xdotool）。務必在隔離環境中執行！"""
import base64
import anthropic

client = anthropic.Anthropic()


def take_screenshot_png():
    raise NotImplementedError("在隔離的虛擬桌面中截圖，回傳 PNG bytes")


def perform(action, args):
    raise NotImplementedError("在虛擬桌面執行 %s %s" % (action, args))


messages = [{"role": "user", "content": "打開瀏覽器，搜尋今天的天氣。"}]
for _ in range(30):                                     # 動作上限
    r = client.messages.create(model="claude-opus-5-5", max_tokens=16000,
                               tools=[{"type": "computer_toolset_20260801"}], messages=messages)
    messages.append({"role": "assistant", "content": r.content})
    if r.stop_reason != "tool_use":
        break
    results = []
    for b in r.content:
        if b.type != "tool_use":
            continue
        if b.name in ("screenshot", "zoom"):
            img = base64.standard_b64encode(take_screenshot_png()).decode()
            content = [{"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": img}}]
        else:
            perform(b.name, b.input)
            content = "OK"
        results.append({"type": "tool_result", "tool_use_id": b.id, "toolset_name": "computer", "content": content})
    messages.append({"role": "user", "content": results})
