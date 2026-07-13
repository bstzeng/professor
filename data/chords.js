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
  }
};
