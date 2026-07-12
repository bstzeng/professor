// 主題頁共用邏輯：讀取 data/topics.js，依 <body data-topic-id="..."> 找出對應主題並渲染。
// 之後新增主題時，只要建立 topics/<id>/index.html 並在 <body> 標籤加上
// data-topic-id="<id>"，這支腳本就能自動渲染模組與課程列表，不需要另外寫渲染程式碼。

function renderTopicPage() {
  const topicId = document.body.getAttribute("data-topic-id");
  const topics = (window.SITE_DATA && window.SITE_DATA.topics) || [];
  const topic = topics.find((t) => t.id === topicId);
  // data/topics.js 裡的 url 一律是相對於網站根目錄的路徑；
  // 主題頁本身位於子目錄，所以要用 SITE_BASE 換算回正確的相對路徑。
  const basePath = window.SITE_BASE || "";

  if (!topic) return;

  document.title = topic.title + " ｜ 教學網站";

  const heroTitle = document.getElementById("topic-title");
  const heroDesc = document.getElementById("topic-description");
  if (heroTitle) heroTitle.textContent = topic.title;
  if (heroDesc) heroDesc.textContent = topic.description || "";

  const container = document.getElementById("modules-container");
  if (!container || !topic.modules) return;

  let lessonNumber = 0;

  container.innerHTML = topic.modules
    .map((module) => {
      const rows = module.courses
        .map((course) => {
          lessonNumber += 1;
          const num = String(lessonNumber).padStart(2, "0");
          const isPublished = !!course.url;

          if (isPublished) {
            return `
              <li>
                <a class="lesson-row is-published" href="${basePath}${course.url}">
                  <span class="lesson-num">${num}</span>
                  <span class="lesson-title">${course.title}</span>
                  <span class="lesson-status">已發布</span>
                </a>
              </li>
            `;
          }

          return `
            <li>
              <div class="lesson-row is-pending">
                <span class="lesson-num">${num}</span>
                <span class="lesson-title">${course.title}</span>
                <span class="lesson-status">敬請期待</span>
              </div>
            </li>
          `;
        })
        .join("");

      return `
        <div class="module-block">
          <h2>${module.title}</h2>
          <ul class="lesson-list">${rows}</ul>
        </div>
      `;
    })
    .join("");
}

renderTopicPage();
