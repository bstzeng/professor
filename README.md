# 教學網站

純靜態網頁（HTML / CSS / JS），沒有後端，可直接用 GitHub Pages 部署。

## 結構

```
index.html          首頁
css/style.css        樣式
js/main.js           首頁邏輯（讀取 data/topics.js 並渲染主題卡片）
data/topics.js        主題與課程資料（之後新增主題只要編輯這個檔案）
topics/               各主題的內容頁面（依需要新增資料夾）
```

## 如何新增主題

1. 在 `data/topics.js` 的 `topics` 陣列中新增一個物件（格式範例已寫在檔案註解中）。
2. 若該主題有獨立頁面，在 `topics/<topic-id>/` 底下新增 HTML 頁面，並在資料裡填上 `url`。
3. 存檔後首頁會自動出現新的主題卡片，不需要修改 `index.html` 或 `js/main.js`。

## 本機預覽

直接用瀏覽器打開 `index.html`，或用簡單的本機伺服器（例如 `python3 -m http.server`）避免部分瀏覽器對本機檔案的限制。

## 部署

推送到 GitHub 後，在 repo 設定的 Pages 選項中選擇從 `main` 分支的根目錄部署即可。
