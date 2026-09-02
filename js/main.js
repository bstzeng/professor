document.getElementById("year").textContent = new Date().getFullYear();

function countCourses(topic) {
  if (topic.modules) {
    return topic.modules.reduce((sum, m) => sum + (m.courses ? m.courses.length : 0), 0);
  }
  return topic.courses ? topic.courses.length : 0;
}

function topicCardHTML(topic) {
  const courseCount = countCourses(topic);
  const href = topic.url && topic.url.length > 0 ? topic.url : "#";
  const badge = courseCount > 0 ? `<span class="course-count">${courseCount} 堂課程</span>` : "";
  return `
    <a class="topic-card" href="${href}">
      <div class="topic-icon">${topic.icon || "📘"}</div>
      <h3>${topic.title}</h3>
      <p>${topic.description || ""}</p>
      ${badge}
    </a>
  `;
}

function renderTopics() {
  const container = document.getElementById("topics-grid");
  const toggleBtn = document.getElementById("toggle-all-btn");
  const topics = (window.SITE_DATA && window.SITE_DATA.topics) || [];
  const categories = (window.SITE_DATA && window.SITE_DATA.categories) || [];

  if (topics.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        尚未新增主題，敬請期待。
      </div>
    `;
    if (toggleBtn) toggleBtn.hidden = true;
    return;
  }

  // 沒有分類資料時，退回原本的單一格狀列表。
  if (categories.length === 0) {
    container.innerHTML = `<div class="topics-grid">${topics.map(topicCardHTML).join("")}</div>`;
    if (toggleBtn) toggleBtn.hidden = true;
    return;
  }

  const byCategory = new Map();
  categories.forEach((c) => byCategory.set(c.id, []));
  const uncategorized = [];

  topics.forEach((topic) => {
    if (topic.category && byCategory.has(topic.category)) {
      byCategory.get(topic.category).push(topic);
    } else {
      uncategorized.push(topic);
    }
  });

  const sections = categories
    .filter((c) => byCategory.get(c.id).length > 0)
    .map((c) => {
      const topicsInGroup = byCategory.get(c.id);
      return `
        <details class="category-group">
          <summary class="category-summary">
            <span class="category-chevron" aria-hidden="true"></span>
            <span class="category-icon">${c.icon || "📁"}</span>
            <span class="category-label">${c.label}</span>
            <span class="category-count">${topicsInGroup.length} 個主題</span>
          </summary>
          <div class="topics-grid category-topics-grid">
            ${topicsInGroup.map(topicCardHTML).join("")}
          </div>
        </details>
      `;
    });

  if (uncategorized.length > 0) {
    sections.push(`
      <details class="category-group">
        <summary class="category-summary">
          <span class="category-chevron" aria-hidden="true"></span>
          <span class="category-icon">📁</span>
          <span class="category-label">其他</span>
          <span class="category-count">${uncategorized.length} 個主題</span>
        </summary>
        <div class="topics-grid category-topics-grid">
          ${uncategorized.map(topicCardHTML).join("")}
        </div>
      </details>
    `);
  }

  container.innerHTML = sections.join("");

  if (toggleBtn) {
    toggleBtn.hidden = false;
    toggleBtn.textContent = "全部展開";
    toggleBtn.onclick = () => {
      const groups = container.querySelectorAll(".category-group");
      if (groups.length === 0) return;
      const allOpen = Array.from(groups).every((g) => g.open);
      groups.forEach((g) => { g.open = !allOpen; });
      toggleBtn.textContent = allOpen ? "全部展開" : "全部收合";
    };
  }
}

renderTopics();
