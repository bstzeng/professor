document.getElementById("year").textContent = new Date().getFullYear();

function renderTopics() {
  const grid = document.getElementById("topics-grid");
  const topics = (window.SITE_DATA && window.SITE_DATA.topics) || [];

  if (topics.length === 0) {
    grid.innerHTML = `
      <div class="empty-state">
        尚未新增主題，敬請期待。
      </div>
    `;
    return;
  }

  grid.innerHTML = topics
    .map((topic) => {
      const courseCount = topic.courses ? topic.courses.length : 0;
      const href = topic.url && topic.url.length > 0 ? topic.url : "#";
      return `
        <a class="topic-card" href="${href}">
          <div class="topic-icon">${topic.icon || "📘"}</div>
          <h3>${topic.title}</h3>
          <p>${topic.description || ""}</p>
          <span class="course-count">${courseCount} 堂課程</span>
        </a>
      `;
    })
    .join("");
}

renderTopics();
