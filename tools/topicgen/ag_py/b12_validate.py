# -*- coding: utf-8 -*-
"""第 12 課：參數驗證——永遠不要相信模型給的參數一定正確。
寫一個迷你 JSON Schema 驗證器，在執行工具前先檢查。"""

def validate(schema, data, path="input"):
    errs = []
    t = schema.get("type")
    types = {"object": dict, "string": str, "integer": int, "number": (int, float), "boolean": bool, "array": list}
    if t and not isinstance(data, types[t]) or (t in ("integer", "number") and isinstance(data, bool)):
        return ["%s 應為 %s，收到 %r" % (path, t, data)]
    if "enum" in schema and data not in schema["enum"]:
        errs.append("%s 必須是 %s 之一，收到 %r" % (path, schema["enum"], data))
    if t in ("integer", "number"):
        if "minimum" in schema and data < schema["minimum"]:
            errs.append("%s 不可小於 %s" % (path, schema["minimum"]))
        if "maximum" in schema and data > schema["maximum"]:
            errs.append("%s 不可大於 %s" % (path, schema["maximum"]))
    if t == "object":
        for k in schema.get("required", []):
            if k not in data:
                errs.append("缺少必填欄位 %s.%s" % (path, k))
        props = schema.get("properties", {})
        for k, v in data.items():
            if k in props:
                errs += validate(props[k], v, path + "." + k)
            elif schema.get("additionalProperties") is False:
                errs.append("不允許的欄位 %s.%s" % (path, k))
    return errs

schema = {"type": "object", "additionalProperties": False, "required": ["destination", "passengers"],
          "properties": {"destination": {"type": "string"},
                         "passengers": {"type": "integer", "minimum": 1, "maximum": 8},
                         "cabin": {"type": "string", "enum": ["economy", "business"]}}}
for call in [{"destination": "東京", "passengers": 2},
             {"destination": "東京", "passengers": "兩位"},
             {"passengers": 12, "cabin": "first"},
             {"destination": "大阪", "passengers": 1, "seat": "窗邊"}]:
    e = validate(schema, call)
    print(("✓ 通過 " if not e else "✗ 拒絕 ") + str(call))
    for x in e:
        print("     →", x)
print("被拒絕時，把錯誤文字當成 is_error=True 的 tool_result 回給模型，它通常會自己修正參數。")
