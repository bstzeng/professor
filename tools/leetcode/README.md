# LeetCode 題解產生器

`topics/leetcode/` 底下的頁面全部由這裡產生，不要直接編輯產生出來的 HTML。

## 檔案

```
meta.py            題目清單（題號、英中標題、難度、標籤、描述）
bodies/NNNN.html   每一題的題解內容（HTML 片段，只有 <article> 裡面的部分）
gen.py             讀 meta.py + bodies/ → 產生 topics/leetcode/problem-NNNN.html
mkindex.py         產生 topics/leetcode/index.html，並更新 data/topics.js
verify-NNNN.py     該題所有 Python 解法的正確性測試（含隨機壓力測試）
```

## 新增一題

1. 在 `meta.py` 的 `PROBLEMS` 加一筆：

   ```python
   {
       "num": 4,
       "en": "Median of Two Sorted Arrays",
       "zh": "兩個有序陣列的中位數",
       "difficulty": "Hard",
       "tags": ["陣列", "二分搜尋", "分治"],
       "desc": "一句話摘要，會放進 <meta name=description>。",
   },
   ```

2. 寫 `bodies/0004.html`。結構照既有的來：

   - `.lc-statement.is-en` 英文題目敘述
   - `.lc-statement` 中文翻譯
   - 範例、限制條件、原題連結
   - 每個解法一個 `.lc-approach`（最佳解加 `is-optimal`）
   - 複雜度對照表、邊界條件檢查清單、延伸題目、`.self-check`

   縮排從 8 個空格開始（會被塞進 `<article>` 裡）。
   程式碼放在 `<div class="code-block">` 裡，**要自己跳脫 `<` `>` `&`**。

3. （建議）寫 `verify-0004.py`，把所有解法跑過一遍再貼進題解。

4. 產生：

   ```bash
   python3 tools/leetcode/gen.py
   python3 tools/leetcode/mkindex.py
   ```

`mkindex.py` 可以重複執行：`data/topics.js` 裡既有的 `leetcode` 項目會被整個取代，
不會產生重複條目。

## 側邊欄怎麼運作

左側題目列表由 `js/leetcode-nav.js` 在瀏覽器端從 `data/topics.js` 動態產生，
依 `<body data-problem="N">` 標出目前這一題。

所以「新增一題」不會動到既有題目頁的內容——它們會自動看到新的列表。
（`gen.py` 仍然會重新產生所有頁面，因為上一題的「下一題」連結需要更新。）

## 分組

題目每 25 題自動分成一組（`meta.GROUP_SIZE`），
組名像「第 026–050 題」，不需要手動維護。
