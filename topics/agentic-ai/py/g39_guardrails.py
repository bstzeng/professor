# -*- coding: utf-8 -*-
"""第 39 課：防護欄（guardrails）——在代理的輸入、工具呼叫、輸出三個關口設檢查。"""
import re

def input_guard(msg):
    if re.search(r"\b\d{4}-?\d{4}-?\d{4}-?\d{4}\b", msg):
        return "請不要在對話中貼信用卡號。"
    if len(msg) > 5000:
        return "訊息太長。"
    return None

ALLOWED_TOOLS = {"search_orders", "get_order"}             # 這個客服代理只能「讀」，不能退款或刪除
def tool_guard(name, args):
    if name not in ALLOWED_TOOLS:
        return "工具 %s 不在允許清單內" % name
    if name == "get_order" and not re.fullmatch(r"[A-Z]\d{5}", args.get("order_id", "")):
        return "訂單編號格式錯誤"
    return None

def output_guard(reply):
    reply = re.sub(r"[\w.+-]+@[\w-]+\.[\w.]+", "[email 已遮蔽]", reply)          # 遮蔽個資
    reply = re.sub(r"09\d{2}-?\d{3}-?\d{3}", "[電話已遮蔽]", reply)
    if "保證獲利" in reply:
        return "（此回覆因含不當承諾而被攔下，已轉人工）"
    return reply

print("輸入：", input_guard("我的卡號是 4111-1111-1111-1111，幫我查"))
for call in [("get_order", {"order_id": "A12345"}), ("refund", {"order_id": "A12345"}), ("get_order", {"order_id": "1 OR 1=1"})]:
    print("工具 %-10s %-28s → %s" % (call[0], call[1], tool_guard(*call) or "放行 ✓"))
print("輸出：", output_guard("已通知負責人 amy@shop.com，電話 0912-345-678。"))
print("輸出：", output_guard("這支基金保證獲利！"))
print("\n原則：防護欄放在『程式』裡，而不是只寫在提示裡拜託模型遵守——模型可能被說服，程式不會。")
