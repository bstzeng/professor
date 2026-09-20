# -*- coding: utf-8 -*-
"""bodies/*.html 的靜態檢查：標籤配對、code-block 內是否有未跳脫的 < >、常見手滑。"""
import io, os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
PAIRED = ["div", "p", "ul", "ol", "li", "h2", "h3", "table", "thead", "tbody",
          "tr", "th", "td", "svg", "g", "text", "code", "strong", "em", "a"]
VOID = set(["br", "hr", "img", "rect", "line", "circle", "path", "polygon",
            "polyline", "ellipse", "use", "stop", "input", "meta", "link"])

bad = 0
files = sorted(glob.glob(os.path.join(HERE, "bodies", "*.html")))
for f in files:
    src = io.open(f, encoding="utf-8").read()
    name = os.path.basename(f)

    # 1. code-block 內容必須已跳脫
    for m in re.finditer(r'<div class="code-block">(.*?)</div>', src, re.S):
        inner = m.group(1)
        if "<" in inner or ">" in inner:
            print("%s: code-block 內有未跳脫的角括號: %r" % (name, inner[:80]))
            bad += 1

    # 2. 標籤配對
    stripped = re.sub(r'<div class="code-block">.*?</div>', "", src, flags=re.S)
    stack = []
    for m in re.finditer(r"<(/?)([a-zA-Z][a-zA-Z0-9]*)([^>]*?)(/?)>", stripped):
        close, tag, attrs, selfclose = m.group(1), m.group(2).lower(), m.group(3), m.group(4)
        if tag in VOID or selfclose == "/":
            continue
        if tag not in PAIRED:
            continue
        if close:
            if not stack or stack[-1] != tag:
                print("%s: 標籤不配對，遇到 </%s>，堆疊頂端是 %s"
                      % (name, tag, stack[-1] if stack else "(空)"))
                bad += 1
                break
            stack.pop()
        else:
            stack.append(tag)
    else:
        if stack:
            print("%s: 有未關閉的標籤 %s" % (name, stack))
            bad += 1

    # 3. 不該出現的東西
    for pat, msg in [(r"\{(?:num|en|zh|desc|diff_en|diff_zh|diffclass|tagspans|body|nav)\}",
                      "疑似未替換的 gen.py 樣板變數"),
                     (r"TODO|FIXME", "留下了 TODO"),
                     (r"<pre>", "用了 <pre>（本站慣例是 .code-block）")]:
        for m in re.finditer(pat, src):
            print("%s: %s -> %r" % (name, msg, m.group(0)))
            bad += 1

    # 4. 必備區塊
    for need in ['class="lc-statement is-en"', 'class="lc-statement"',
                 'class="lc-approach', 'class="self-check"']:
        if need not in src:
            print("%s: 缺少 %s" % (name, need))
            bad += 1

print("檢查 %d 個檔案，%d 個問題" % (len(files), bad))
sys.exit(1 if bad else 0)
