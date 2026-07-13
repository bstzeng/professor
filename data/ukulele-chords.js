// 烏克麗麗和弦資料庫（標準 GCEA 調音）。
// strings 陣列固定 4 個元素，順序為 [G, C, E, A]（由左到右，符合面對指板時的視覺順序）。
// fret: 0 = 空弦。finger: 1=食指 2=中指 3=無名指 4=小指。
// 涵蓋 12 個調的大和弦、小和弦、屬七和弦（共 36 個），指法皆為電腦驗證過音名正確的
// 最低把位版本，和市面上常見的烏克麗麗和弦表一致。

window.UKULELE_CHORD_DATA = {
  C: {
    name: "C",
    startFret: 1,
    strings: [{ fret: 0 }, { fret: 0 }, { fret: 0 }, { fret: 3, finger: 1 }]
  },
  Cm: {
    name: "Cm",
    startFret: 1,
    strings: [{ fret: 0 }, { fret: 3, finger: 1 }, { fret: 3, finger: 2 }, { fret: 3, finger: 3 }]
  },
  C7: {
    name: "C7",
    startFret: 1,
    strings: [{ fret: 0 }, { fret: 0 }, { fret: 0 }, { fret: 1, finger: 1 }]
  },
  Csharp: {
    name: "C♯",
    startFret: 1,
    strings: [{ fret: 1, finger: 1 }, { fret: 1, finger: 2 }, { fret: 1, finger: 3 }, { fret: 4, finger: 4 }]
  },
  Csharpm: {
    name: "C♯m",
    startFret: 1,
    strings: [{ fret: 1, finger: 1 }, { fret: 1, finger: 2 }, { fret: 0 }, { fret: 4, finger: 3 }]
  },
  Csharp7: {
    name: "C♯7",
    startFret: 1,
    strings: [{ fret: 1, finger: 1 }, { fret: 1, finger: 2 }, { fret: 1, finger: 3 }, { fret: 2, finger: 4 }]
  },
  D: {
    name: "D",
    startFret: 1,
    strings: [{ fret: 2, finger: 1 }, { fret: 2, finger: 2 }, { fret: 2, finger: 3 }, { fret: 0 }]
  },
  Dm: {
    name: "Dm",
    startFret: 1,
    strings: [{ fret: 2, finger: 2 }, { fret: 2, finger: 3 }, { fret: 1, finger: 1 }, { fret: 0 }]
  },
  D7: {
    name: "D7",
    startFret: 1,
    strings: [{ fret: 2, finger: 1 }, { fret: 2, finger: 2 }, { fret: 2, finger: 3 }, { fret: 3, finger: 4 }]
  },
  Dsharp: {
    name: "D♯",
    startFret: 1,
    strings: [{ fret: 0 }, { fret: 3, finger: 2 }, { fret: 3, finger: 3 }, { fret: 1, finger: 1 }]
  },
  Dsharpm: {
    name: "D♯m",
    startFret: 1,
    strings: [{ fret: 3, finger: 3 }, { fret: 3, finger: 4 }, { fret: 2, finger: 2 }, { fret: 1, finger: 1 }]
  },
  Dsharp7: {
    name: "D♯7",
    startFret: 1,
    strings: [{ fret: 3, finger: 1 }, { fret: 3, finger: 2 }, { fret: 3, finger: 3 }, { fret: 4, finger: 4 }]
  },
  E: {
    name: "E",
    startFret: 1,
    strings: [{ fret: 1, finger: 1 }, { fret: 4, finger: 3 }, { fret: 0 }, { fret: 2, finger: 2 }]
  },
  Em: {
    name: "Em",
    startFret: 1,
    strings: [{ fret: 0 }, { fret: 4, finger: 2 }, { fret: 0 }, { fret: 2, finger: 1 }]
  },
  E7: {
    name: "E7",
    startFret: 1,
    strings: [{ fret: 1, finger: 1 }, { fret: 2, finger: 2 }, { fret: 0 }, { fret: 2, finger: 3 }]
  },
  F: {
    name: "F",
    startFret: 1,
    strings: [{ fret: 2, finger: 2 }, { fret: 0 }, { fret: 1, finger: 1 }, { fret: 0 }]
  },
  Fm: {
    name: "Fm",
    startFret: 1,
    strings: [{ fret: 1, finger: 1 }, { fret: 0 }, { fret: 1, finger: 2 }, { fret: 3, finger: 3 }]
  },
  F7: {
    name: "F7",
    startFret: 1,
    strings: [{ fret: 2, finger: 2 }, { fret: 3, finger: 3 }, { fret: 1, finger: 1 }, { fret: 3, finger: 4 }]
  },
  Fsharp: {
    name: "F♯",
    startFret: 1,
    strings: [{ fret: 3, finger: 4 }, { fret: 1, finger: 1 }, { fret: 2, finger: 3 }, { fret: 1, finger: 2 }]
  },
  Fsharpm: {
    name: "F♯m",
    startFret: 1,
    strings: [{ fret: 2, finger: 2 }, { fret: 1, finger: 1 }, { fret: 2, finger: 3 }, { fret: 0 }]
  },
  Fsharp7: {
    name: "F♯7",
    startFret: 1,
    strings: [{ fret: 3, finger: 2 }, { fret: 4, finger: 3 }, { fret: 2, finger: 1 }, { fret: 4, finger: 4 }]
  },
  G: {
    name: "G",
    startFret: 1,
    strings: [{ fret: 0 }, { fret: 2, finger: 1 }, { fret: 3, finger: 3 }, { fret: 2, finger: 2 }]
  },
  Gm: {
    name: "Gm",
    startFret: 1,
    strings: [{ fret: 0 }, { fret: 2, finger: 2 }, { fret: 3, finger: 3 }, { fret: 1, finger: 1 }]
  },
  G7: {
    name: "G7",
    startFret: 1,
    strings: [{ fret: 0 }, { fret: 2, finger: 2 }, { fret: 1, finger: 1 }, { fret: 2, finger: 3 }]
  },
  Gsharp: {
    name: "G♯",
    startFret: 1,
    strings: [{ fret: 1, finger: 1 }, { fret: 3, finger: 2 }, { fret: 4, finger: 4 }, { fret: 3, finger: 3 }]
  },
  Gsharpm: {
    name: "G♯m",
    startFret: 1,
    strings: [{ fret: 1, finger: 1 }, { fret: 3, finger: 3 }, { fret: 4, finger: 4 }, { fret: 2, finger: 2 }]
  },
  Gsharp7: {
    name: "G♯7",
    startFret: 1,
    strings: [{ fret: 1, finger: 1 }, { fret: 3, finger: 3 }, { fret: 2, finger: 2 }, { fret: 3, finger: 4 }]
  },
  A: {
    name: "A",
    startFret: 1,
    strings: [{ fret: 2, finger: 2 }, { fret: 1, finger: 1 }, { fret: 0 }, { fret: 0 }]
  },
  Am: {
    name: "Am",
    startFret: 1,
    strings: [{ fret: 2, finger: 1 }, { fret: 0 }, { fret: 0 }, { fret: 0 }]
  },
  A7: {
    name: "A7",
    startFret: 1,
    strings: [{ fret: 0 }, { fret: 1, finger: 1 }, { fret: 0 }, { fret: 0 }]
  },
  Asharp: {
    name: "A♯",
    startFret: 1,
    strings: [{ fret: 3, finger: 4 }, { fret: 2, finger: 3 }, { fret: 1, finger: 1 }, { fret: 1, finger: 2 }]
  },
  Asharpm: {
    name: "A♯m",
    startFret: 1,
    strings: [{ fret: 3, finger: 4 }, { fret: 1, finger: 1 }, { fret: 1, finger: 2 }, { fret: 1, finger: 3 }]
  },
  Asharp7: {
    name: "A♯7",
    startFret: 1,
    strings: [{ fret: 1, finger: 1 }, { fret: 2, finger: 4 }, { fret: 1, finger: 2 }, { fret: 1, finger: 3 }]
  },
  B: {
    name: "B",
    startFret: 1,
    strings: [{ fret: 4, finger: 4 }, { fret: 3, finger: 3 }, { fret: 2, finger: 1 }, { fret: 2, finger: 2 }]
  },
  Bm: {
    name: "Bm",
    startFret: 1,
    strings: [{ fret: 4, finger: 4 }, { fret: 2, finger: 1 }, { fret: 2, finger: 2 }, { fret: 2, finger: 3 }]
  },
  B7: {
    name: "B7",
    startFret: 1,
    strings: [{ fret: 2, finger: 1 }, { fret: 3, finger: 4 }, { fret: 2, finger: 2 }, { fret: 2, finger: 3 }]
  }
};
