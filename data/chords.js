// 和弦指法資料庫。之後教到新和弦（大和弦、七和弦等）時，只要在這裡新增一筆，
// 課程頁與常見和弦總覽頁就能立刻使用同一份資料畫出指法圖。
//
// strings 陣列固定 6 個元素，順序為 [低音 E, A, D, G, B, 高音 e]。
// fret: 0 = 空弦, "x" = 不彈（悶音), 1~4 = 按在第幾格。
// finger: 1=食指 2=中指 3=無名指 4=小指（空弦或不彈則省略)。
// startFret: 指法圖最上面顯示的格數，1 代表包含琴頭（會畫出琴枕粗線)。
// barre（可選）：{ fret, fromString, toString, finger } 描述封閉和弦的橫按。

window.CHORD_DATA = {
  C: {
    name: "C",
    startFret: 1,
    strings: [
      { fret: "x" },
      { fret: 3, finger: 3 },
      { fret: 2, finger: 2 },
      { fret: 0 },
      { fret: 1, finger: 1 },
      { fret: 0 }
    ]
  },
  G: {
    name: "G",
    startFret: 1,
    strings: [
      { fret: 3, finger: 2 },
      { fret: 2, finger: 1 },
      { fret: 0 },
      { fret: 0 },
      { fret: 0 },
      { fret: 3, finger: 3 }
    ]
  },
  D: {
    name: "D",
    startFret: 1,
    strings: [
      { fret: "x" },
      { fret: "x" },
      { fret: 0 },
      { fret: 2, finger: 1 },
      { fret: 3, finger: 3 },
      { fret: 2, finger: 2 }
    ]
  },
  Em: {
    name: "Em",
    startFret: 1,
    strings: [
      { fret: 0 },
      { fret: 2, finger: 2 },
      { fret: 2, finger: 3 },
      { fret: 0 },
      { fret: 0 },
      { fret: 0 }
    ]
  },
  Am: {
    name: "Am",
    startFret: 1,
    strings: [
      { fret: "x" },
      { fret: 0 },
      { fret: 2, finger: 2 },
      { fret: 2, finger: 3 },
      { fret: 1, finger: 1 },
      { fret: 0 }
    ]
  },
  Dm: {
    name: "Dm",
    startFret: 1,
    strings: [
      { fret: "x" },
      { fret: "x" },
      { fret: 0 },
      { fret: 2, finger: 2 },
      { fret: 3, finger: 3 },
      { fret: 1, finger: 1 }
    ]
  },
  A: {
    name: "A",
    startFret: 1,
    strings: [
      { fret: "x" },
      { fret: 0 },
      { fret: 2, finger: 1 },
      { fret: 2, finger: 2 },
      { fret: 2, finger: 3 },
      { fret: 0 }
    ]
  },
  E: {
    name: "E",
    startFret: 1,
    strings: [
      { fret: 0 },
      { fret: 2, finger: 2 },
      { fret: 2, finger: 3 },
      { fret: 1, finger: 1 },
      { fret: 0 },
      { fret: 0 }
    ]
  },
  Fsimple: {
    // 簡化版 F：只彈上面四條弦，食指小封閉（B、e 弦第 1 格），
    // 給還沒學全封閉和弦（模組 D）的人先用來練 C-G-Am-F 這類進行。
    name: "F（簡易）",
    startFret: 1,
    strings: [
      { fret: "x" },
      { fret: "x" },
      { fret: 3, finger: 3 },
      { fret: 2, finger: 2 },
      { fret: 1, finger: 1 },
      { fret: 1, finger: 1 }
    ],
    barre: { fret: 1, fromString: 4, toString: 5, finger: 1 }
  },
  F: {
    // 完整封閉 F（E 形移動和弦，第 18、19 課），食指封閉全部六條弦。
    name: "F",
    startFret: 1,
    strings: [
      { fret: 1, finger: 1 },
      { fret: 3, finger: 3 },
      { fret: 3, finger: 4 },
      { fret: 2, finger: 2 },
      { fret: 1, finger: 1 },
      { fret: 1, finger: 1 }
    ],
    barre: { fret: 1, fromString: 0, toString: 5, finger: 1 }
  },
  Bm: {
    // Am 形移動和弦（第 18、19 課），食指封閉 A 到高音 e 弦（低音 E 不彈）。
    name: "Bm",
    startFret: 1,
    strings: [
      { fret: "x" },
      { fret: 2, finger: 1 },
      { fret: 4, finger: 3 },
      { fret: 4, finger: 4 },
      { fret: 3, finger: 2 },
      { fret: 2, finger: 1 }
    ],
    barre: { fret: 2, fromString: 1, toString: 5, finger: 1 }
  },

  // 以下和弦是「各調常用和弦總表」（見常見和弦總覽頁）需要、前面課程還沒單獨用到的和弦。
  // 開放和弦（G7、A7、B7、C7、D7、E7）沿用傳統簡易指法；
  // 封閉／移動和弦沿用第 19 課的 E 形（大調）、Em 形（小調）、A 形（大調）、Am 形（小調）系統。

  G7: {
    name: "G7",
    startFret: 1,
    strings: [
      { fret: 3, finger: 3 },
      { fret: 2, finger: 2 },
      { fret: 0 },
      { fret: 0 },
      { fret: 0 },
      { fret: 1, finger: 1 }
    ]
  },
  A7: {
    name: "A7",
    startFret: 1,
    strings: [
      { fret: "x" },
      { fret: 0 },
      { fret: 2, finger: 1 },
      { fret: 0 },
      { fret: 2, finger: 2 },
      { fret: 0 }
    ]
  },
  B7: {
    name: "B7",
    startFret: 1,
    strings: [
      { fret: "x" },
      { fret: 2, finger: 2 },
      { fret: 1, finger: 1 },
      { fret: 2, finger: 3 },
      { fret: 0 },
      { fret: 2, finger: 4 }
    ]
  },
  C7: {
    name: "C7",
    startFret: 1,
    strings: [
      { fret: "x" },
      { fret: 3, finger: 3 },
      { fret: 2, finger: 2 },
      { fret: 3, finger: 4 },
      { fret: 1, finger: 1 },
      { fret: 0 }
    ]
  },
  D7: {
    name: "D7",
    startFret: 1,
    strings: [
      { fret: "x" },
      { fret: "x" },
      { fret: 0 },
      { fret: 2, finger: 3 },
      { fret: 1, finger: 1 },
      { fret: 2, finger: 2 }
    ]
  },
  E7: {
    name: "E7",
    startFret: 1,
    strings: [
      { fret: 0 },
      { fret: 2, finger: 2 },
      { fret: 0 },
      { fret: 1, finger: 1 },
      { fret: 0 },
      { fret: 0 }
    ]
  },
  "F#m": {
    // Em 形移動和弦，根音在低音 E 弦第 2 格。
    name: "F♯m",
    startFret: 2,
    strings: [
      { fret: 2, finger: 1 },
      { fret: 4, finger: 3 },
      { fret: 4, finger: 4 },
      { fret: 2, finger: 1 },
      { fret: 2, finger: 1 },
      { fret: 2, finger: 1 }
    ],
    barre: { fret: 2, fromString: 0, toString: 5, finger: 1 }
  },
  "G#m": {
    // Em 形移動和弦，根音在低音 E 弦第 4 格。
    name: "G♯m",
    startFret: 4,
    strings: [
      { fret: 4, finger: 1 },
      { fret: 6, finger: 3 },
      { fret: 6, finger: 4 },
      { fret: 4, finger: 1 },
      { fret: 4, finger: 1 },
      { fret: 4, finger: 1 }
    ],
    barre: { fret: 4, fromString: 0, toString: 5, finger: 1 }
  },
  Gm: {
    // Em 形移動和弦，根音在低音 E 弦第 3 格。
    name: "Gm",
    startFret: 3,
    strings: [
      { fret: 3, finger: 1 },
      { fret: 5, finger: 3 },
      { fret: 5, finger: 4 },
      { fret: 3, finger: 1 },
      { fret: 3, finger: 1 },
      { fret: 3, finger: 1 }
    ],
    barre: { fret: 3, fromString: 0, toString: 5, finger: 1 }
  },
  "F#": {
    // E 形移動和弦，根音在低音 E 弦第 2 格。
    name: "F♯",
    startFret: 2,
    strings: [
      { fret: 2, finger: 1 },
      { fret: 4, finger: 3 },
      { fret: 4, finger: 4 },
      { fret: 3, finger: 2 },
      { fret: 2, finger: 1 },
      { fret: 2, finger: 1 }
    ],
    barre: { fret: 2, fromString: 0, toString: 5, finger: 1 }
  },
  "F#7": {
    // E7 形移動和弦，根音在低音 E 弦第 2 格。
    name: "F♯7",
    startFret: 2,
    strings: [
      { fret: 2, finger: 1 },
      { fret: 4, finger: 3 },
      { fret: 2, finger: 1 },
      { fret: 3, finger: 2 },
      { fret: 2, finger: 1 },
      { fret: 2, finger: 1 }
    ],
    barre: { fret: 2, fromString: 0, toString: 5, finger: 1 }
  },
  B: {
    // A 形移動和弦（大調），根音在 A 弦第 2 格，低音 E 不彈。
    name: "B",
    startFret: 2,
    strings: [
      { fret: "x" },
      { fret: 2, finger: 1 },
      { fret: 4, finger: 3 },
      { fret: 4, finger: 3 },
      { fret: 4, finger: 3 },
      { fret: 2, finger: 1 }
    ],
    barre: { fret: 2, fromString: 1, toString: 5, finger: 1 }
  },
  Bb: {
    // A 形移動和弦（大調），根音在 A 弦第 1 格，低音 E 不彈。
    name: "B♭",
    startFret: 1,
    strings: [
      { fret: "x" },
      { fret: 1, finger: 1 },
      { fret: 3, finger: 3 },
      { fret: 3, finger: 3 },
      { fret: 3, finger: 3 },
      { fret: 1, finger: 1 }
    ],
    barre: { fret: 1, fromString: 1, toString: 5, finger: 1 }
  },
  "C#m": {
    // Am 形移動和弦，根音在 A 弦第 4 格，低音 E 不彈。
    name: "C♯m",
    startFret: 4,
    strings: [
      { fret: "x" },
      { fret: 4, finger: 1 },
      { fret: 6, finger: 3 },
      { fret: 6, finger: 4 },
      { fret: 5, finger: 2 },
      { fret: 4, finger: 1 }
    ],
    barre: { fret: 4, fromString: 1, toString: 5, finger: 1 }
  },
  "D#m": {
    // Am 形移動和弦，根音在 A 弦第 6 格，低音 E 不彈。
    name: "D♯m",
    startFret: 6,
    strings: [
      { fret: "x" },
      { fret: 6, finger: 1 },
      { fret: 8, finger: 3 },
      { fret: 8, finger: 4 },
      { fret: 7, finger: 2 },
      { fret: 6, finger: 1 }
    ],
    barre: { fret: 6, fromString: 1, toString: 5, finger: 1 }
  }
};
