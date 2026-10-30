# -*- coding: utf-8 -*-
"""Ontology：模組 C 從哲學走到電腦（13～18）、D Ontology 的組成（19～25）、E 邏輯基礎（26～30）。"""
from ont_common import *

MODULES = [
(u"模組 C｜從哲學走到電腦", [

lesson(u"萊布尼茲的夢：通用語言與推理演算",
  u"「讓我們來算一算！」——用計算解決一切爭論",
  [u"認識萊布尼茲的通用文字與推理演算", u"理解布爾與弗雷格的邏輯形式化", u"看出知識表示的思想源頭"],
  [("p", u"17 世紀的萊布尼茲（1646～1716）有一個宏大的夢想，由兩部分組成："),
   ("ul", [u"<strong>通用文字</strong>（characteristica universalis）：一套能表達所有概念的符號系統，每個複雜概念由簡單概念組合而成，就像數字由質數相乘而成。", u"<strong>推理演算</strong>（calculus ratiocinator）：在這套符號上進行機械化的推理。"]),
   ("p", u"他想像，將來兩位哲學家意見不合時，不必再爭吵，只要坐下來說：「讓我們來算一算（Calculemus）！」"),
   ("h", u"概念的「質因數分解」"),
   ("p", u"萊布尼茲甚至提出具體的方案：給每個基本概念一個質數，複合概念就是質數的乘積。例如「動物」= 2、「理性」= 3，則「人」= 2 × 3 = 6。要判斷「人是動物嗎？」只要看 6 能不能被 2 整除。"),
   check(u"萊布尼茲的概念編碼：判斷 A 是否為 B 的一種", [["a", u"概念 A 的編碼（例：人 = 6）", 6, 1, 1000, 1], ["b", u"概念 B 的編碼（例：動物 = 2）", 2, 1, 1000, 1]],
         [[u"A 是 B 的一種嗎（A 能被 B 整除，1 = 是）", "(a%b===0)?1:0"]], u"這正是今天「包含關係推理」（subsumption）的雛形：A 的定義包含 B 的所有特徵，A 就是 B 的子類別。"),
   ("h", u"從萊布尼茲到現代邏輯"),
   ("t", [u"人物", u"年代", u"貢獻"],
    [[u"布爾", u"1854", u"《思維規律》：把邏輯寫成代數（布林代數）"], [u"弗雷格", u"1879", u"《概念文字》：第一個完整的一階謂詞邏輯，有量詞 ∀ ∃"],
     [u"羅素與懷海德", u"1910～1913", u"《數學原理》：試圖把數學化約為邏輯"], [u"圖靈", u"1936", u"可計算性：定義了什麼是「機械化的計算」"]]),
   ("p", u"弗雷格的概念文字，就是萊布尼茲夢想的一部分實現：一套精確到可以機械檢查的語言。今天的 OWL 建立在描述邏輯之上，而描述邏輯是一階邏輯的一個可判定片段（第 27 課）。"),
   ("note", u"夢想的極限", [("p", u"哥德爾不完備定理（1931）與圖靈的停機問題（1936）告訴我們：萊布尼茲的完整夢想無法實現——足夠強的形式系統總有無法判定的命題。Ontology 語言的設計，正是在「表達力」和「可以計算」之間找平衡（第 30 課）。")]),
  ],
  u"萊布尼茲夢想以通用文字表達所有概念，以推理演算機械地解決爭論，並提出以質數乘積編碼概念、以整除判斷包含關係，正是 subsumption 推理的雛形。布爾的代數、弗雷格的概念文字、羅素與懷海德的《數學原理》與圖靈的可計算性逐步實現了形式化。哥德爾與圖靈也指出其極限，Ontology 語言因此要在表達力與可計算性之間取捨。",
  [u"用萊布尼茲的方法，若「女性」= 5，「母親」應該怎麼編碼？", u"弗雷格的概念文字比亞里斯多德的三段論多了什麼？", u"為什麼萊布尼茲的完整夢想無法實現？"]),

lesson(u"圖書分類與生物分類",
  u"杜威十進分類、林奈的二名法：大規模知識組織的先驅",
  [u"認識林奈的生物分類系統", u"認識圖書館的分類法", u"理解分面分類的概念"],
  [("h", u"林奈的生物分類（1735）"),
   ("p", u"瑞典博物學家林奈在《自然系統》中建立了階層分類：界、綱、目、屬、種（後來加入門、科），並推廣<strong>二名法</strong>：每個物種用「屬名 + 種小名」命名，例如智人 <em>Homo sapiens</em>。這是波菲利之樹在自然界的大規模應用。"),
   ("p", u"達爾文之後，分類開始反映演化關係；今天的<strong>系統發生學</strong>用 DNA 定序重建演化樹，常常推翻傳統的分類（例如鳥類其實是恐龍的後代）。生物分類一再修正，提醒我們：分類是理論，不是不變的真理。"),
   ("h", u"圖書館的分類"),
   ("t", [u"系統", u"年代", u"特點"],
    [[u"杜威十進分類法", u"1876", u"把知識分成 10 大類（000 總類、100 哲學、200 宗教……），每類再十進細分，例如 510 數學、516 幾何"], [u"美國國會圖書館分類法", u"1897 起", u"字母加數字，大型學術圖書館常用"],
     [u"中國圖書分類法", u"1929（賴永祥修訂版廣用於台灣）", u"仿杜威十進，台灣多數圖書館使用"], [u"冒號分類法", u"1933（阮甘納桑）", u"<strong>分面分類</strong>的開創者"]]),
   ("h", u"分面分類"),
   ("p", u"印度圖書館學家阮甘納桑發現，嚴格的樹狀分類無法處理「台灣十九世紀的茶葉貿易史」這種主題——它該放在台灣、歷史、茶、貿易的哪個分支下？他的解法是<strong>分面</strong>：先定義幾個獨立的面向（主題、空間、時間、形式……），一本書在每個面向上各取一個值，再組合起來。"),
   ("p", u"電商網站的篩選器（品牌、價格、顏色、尺寸）就是分面分類。從 Ontology 的角度看，分面就是多個<strong>獨立的屬性</strong>，而不是一棵大樹——這也是 Ontology 比分類法更有彈性的原因（第 3 課）。"),
   PY(u"""
# 分面分類：每本書在每個面向上各有一個值，可以任意組合篩選
books = [
    {"title": "台灣茶業史", "subject": "茶", "place": "台灣", "period": "19世紀", "form": "專書"},
    {"title": "福爾摩沙貿易", "subject": "貿易", "place": "台灣", "period": "19世紀", "form": "論文集"},
    {"title": "英國茶文化", "subject": "茶", "place": "英國", "period": "18世紀", "form": "專書"},
]
def facet(items, **conds):
    return [b["title"] for b in items if all(b[k] == v for k, v in conds.items())]

print(facet(books, subject="茶"))                    # 兩本
print(facet(books, place="台灣", period="19世紀"))     # 兩本
"""),
  ],
  u"林奈 1735 年建立界綱目屬種的階層分類與二名法，演化論與系統發生學後來持續修正分類，顯示分類是理論而非不變真理。圖書館有杜威十進分類、國會圖書館分類、台灣常用的中國圖書分類法。阮甘納桑的冒號分類法開創分面分類，以多個獨立面向組合描述主題，即電商篩選器的原理，對應 Ontology 的多個獨立屬性。",
  [u"智人的學名中，哪部分是屬名、哪部分是種小名？", u"為什麼嚴格的樹狀分類難以處理跨領域的主題？", u"分面分類和 Ontology 的屬性有什麼關係？"]),

lesson(u"AI 的知識表示：語意網路、框架與規則",
  u"1960～1970 年代，AI 研究者怎麼把知識放進電腦",
  [u"認識語意網路與 is-a 階層", u"認識明斯基的框架與預設值", u"認識產生式規則與前向／後向推理"],
  [("p", u"早期 AI 研究者很快發現：要讓電腦表現得有智慧，光有推理演算法不夠，還需要大量<strong>知識</strong>。怎麼表示知識，成了核心問題。"),
   ("h", u"語意網路（1960 年代）"),
   ("p", u"奎利恩（Quillian, 1968）用節點表示概念、用帶標籤的邊表示關係，建立了語意網路。最重要的邊是 <strong>is-a</strong>，屬性沿著它<strong>繼承</strong>：知道「金絲雀 is-a 鳥」「鳥 會飛」，就能推出「金絲雀會飛」。"),
   ("p", u"心理學實驗發現，人判斷「金絲雀會唱歌」比「金絲雀有皮膚」快，好像真的要沿著網路往上走比較多步——這讓語意網路一度被視為人類記憶的模型。"),
   ("h", u"框架（1974）"),
   ("p", u"明斯基提出<strong>框架</strong>：每個概念是一個有很多「槽」（slot）的結構，槽裡可以填值、<strong>預設值</strong>、或附帶的程序。走進一個「餐廳」框架，你預期有桌子、菜單、服務生，除非看到相反的證據。"),
   PY(u"""
# 框架：槽、預設值與繼承
frames = {
    "鳥":     {"is_a": None,  "會飛": True,  "腳數": 2},
    "企鵝":   {"is_a": "鳥",  "會飛": False},          # 覆寫預設值
    "金絲雀": {"is_a": "鳥",  "顏色": "黃"},
}
def get(frame, slot):
    while frame:
        if slot in frames[frame]:
            return frames[frame][slot]
        frame = frames[frame]["is_a"]                  # 沿 is-a 往上找
    return None

print(get("金絲雀", "會飛"))   # True（繼承）
print(get("企鵝", "會飛"))     # False（例外覆寫）
"""),
   ("p", u"預設值與例外很方便，但也很危險：它讓推理變成<strong>非單調</strong>的——加入新知識可能推翻舊結論。OWL 刻意<strong>不</strong>支援預設推理，以保持邏輯的單調性與可判定性（第 29 課）。"),
   ("h", u"產生式規則"),
   ("p", u"另一種方式是用「如果……則……」的規則表示知識。<strong>前向推理</strong>從已知事實出發，不斷套用規則產生新事實；<strong>後向推理</strong>從目標出發，反推需要哪些事實。今天的 SWRL、Datalog、以及許多商業規則引擎都延續這個傳統。"),
   ow("reason", u"這就是前向推理：從原始事實出發，反覆套用規則，直到沒有新事實為止："),
   ("note", u"「is-a」的混亂", [("p", u"1983 年，布拉赫曼發表〈IS-A 是什麼，又不是什麼〉，指出早期系統把 is-a 用在至少六種不同的意思上（子類別、實例、相似……）。這篇論文推動了知識表示走向嚴格的邏輯語意，直接導向描述邏輯的誕生。")]),
  ],
  u"早期 AI 認識到知識表示的重要。奎利恩的語意網路以節點與邊表示概念，屬性沿 is-a 繼承。明斯基的框架以槽、預設值與程序組織知識，但預設與例外使推理非單調，OWL 因此不支援預設推理。產生式規則支援前向與後向推理，延續到 SWRL 與規則引擎。布拉赫曼指出 is-a 的語意混亂，推動知識表示走向描述邏輯。",
  [u"語意網路中的「繼承」是怎麼運作的？", u"為什麼框架的預設值會讓推理變成非單調？", u"前向推理與後向推理有什麼不同？"]),

lesson(u"專家系統與知識獲取瓶頸",
  u"1980 年代的 AI 熱潮，以及它為什麼退燒",
  [u"認識專家系統的架構與代表作", u"理解知識獲取瓶頸", u"從專家系統的失敗看 Ontology 的價值"],
  [("p", u"1970～1980 年代，AI 從追求通用智慧，轉向解決特定領域的問題：把專家的知識寫成規則，讓電腦在狹窄的領域中做出專家級的判斷。這就是<strong>專家系統</strong>。"),
   ("t", [u"系統", u"年代", u"領域"],
    [[u"DENDRAL", u"1965 起", u"從質譜資料推測有機分子結構"], [u"MYCIN", u"1970 年代", u"診斷血液感染並建議抗生素，約 600 條規則，表現接近專科醫師"], [u"XCON（R1）", u"1980", u"為迪吉多公司的 VAX 電腦配置訂單，據報每年省下數千萬美元"]]),
   ("h", u"專家系統的架構"),
   ("ul", [u"<strong>知識庫</strong>：規則與事實。", u"<strong>推理引擎</strong>：套用規則的程式（前向或後向推理）。", u"<strong>解釋模組</strong>：說明「為什麼得到這個結論」——MYCIN 可以回答「為什麼你要問這個問題？」"]),
   ("h", u"知識獲取瓶頸"),
   ("p", u"專家系統的最大問題不在推理，而在<strong>把知識放進去</strong>："),
   ("ul", [u"專家很難把直覺說清楚，訪談耗時耗力。", u"規則一多，彼此衝突、重複，維護變得非常困難（XCON 後期有上萬條規則）。", u"每個系統都從頭建立自己的知識庫，<strong>無法共享與重用</strong>。", u"系統很脆弱：遇到稍微超出範圍的情況就完全失效。"]),
   ("p", u"1980 年代後期，專家系統的商業市場崩潰，迎來 AI 的第二次寒冬。"),
   ("h", u"教訓：知識需要能共享的結構"),
   ("p", u"研究者反省：如果不同的系統能<strong>共用</strong>同一套對領域的概念化，就不必每次從頭開始。1991 年美國 DARPA 的<strong>知識共享計畫</strong>（Knowledge Sharing Effort）正是為此而生，它直接催生了格魯伯的本體定義與 Ontolingua 等早期本體工具（第 18 課）。"),
   PY(u"""
# 一個極簡的後向推理專家系統（MYCIN 風格）
rules = [
    ({"發燒", "頸部僵硬"}, "疑似腦膜炎"),
    ({"疑似腦膜炎", "革蘭氏陰性"}, "建議做腰椎穿刺並會診"),
]
def prove(goal, facts, depth=0):
    if goal in facts:
        return True
    for conds, concl in rules:
        if concl == goal and all(prove(c, facts, depth + 1) for c in conds):
            print("  " * depth + f"由 {conds} 推得 {goal}")
            return True
    return False

prove("建議做腰椎穿刺並會診", {"發燒", "頸部僵硬", "革蘭氏陰性"})
"""),
  ],
  u"專家系統把專家知識寫成規則，在狹窄領域表現出色，如 DENDRAL、MYCIN 與為迪吉多配置電腦的 XCON。架構包括知識庫、推理引擎與解釋模組。最大問題是知識獲取瓶頸：專家難以表述、規則衝突難維護、知識無法共享且系統脆弱，導致 1980 年代後期的 AI 寒冬。反省後的知識共享計畫，催生了可共享的本體概念。",
  [u"專家系統的三個主要部分是什麼？", u"什麼是知識獲取瓶頸？", u"專家系統的失敗如何催生了 Ontology 的概念？"]),

lesson(u"Cyc 計畫：把常識全部寫下來",
  u"四十年、數千萬條斷言：史上最大的手工知識工程",
  [u"認識 Cyc 計畫的目標與規模", u"理解常識知識的難度", u"從 Cyc 看手工本體與機器學習的對比"],
  [("p", u"1984 年，道格拉斯・勒納特（Douglas Lenat）提出一個大膽的想法：專家系統之所以脆弱，是因為它們缺乏<strong>常識</strong>。如果把人類的常識全部寫成邏輯斷言，AI 就能像人一樣理解世界。這就是 <strong>Cyc</strong>（取自 encyclopedia）。"),
   ("h", u"Cyc 裡面有什麼"),
   ("ul", [u"一套上層本體與大量的領域知識，用自己的邏輯語言 CycL 表示（比一階邏輯更強，有高階與模態的功能）。", u"「你不能同時在兩個地方」「人死了就不能再死一次」「水往低處流」「東西被拿走就不在原處」這類人人都知道、卻沒有人會寫下來的知識。", u"<strong>微理論</strong>（microtheory）：把知識分成許多情境，各自內部一致，彼此可以矛盾（例如「哈利波特世界」裡魔法存在）。", u"多年下來累積了數十萬個概念、數千萬條斷言，投入超過一千人年的工作。"]),
   ("h", u"成果與爭議"),
   ("ul", [u"Cyc 證明了大規模、邏輯嚴謹的知識庫是可能建立的，並在醫療、國防等領域有商業應用。", u"但它始終沒有實現「讀懂任何文字、具備通用常識」的承諾。批評者認為常識太龐大、太模糊，手工寫不完。", u"公開版本 OpenCyc 曾開放部分本體，後來停止更新。勒納特於 2023 年過世。"]),
   ("h", u"手工知識 vs. 機器學習"),
   ("t", [u"", u"Cyc 式手工知識", u"大型語言模型"],
    [[u"知識來源", u"人工撰寫的邏輯斷言", u"從海量文字中統計學習"], [u"可解釋性", u"高：每條推理都能追溯", u"低：知識分散在數十億個參數中"],
     [u"一致性", u"可以用邏輯檢查", u"可能自相矛盾、產生幻覺"], [u"涵蓋範圍", u"受限於人力", u"極廣"]]),
   ("p", u"有趣的是，兩者正在走向結合：用 LLM 從文字中抽取知識來建構本體（第 53 課），再用本體約束 LLM 的輸出、減少幻覺（第 52 課）。勒納特晚年也撰文主張兩者互補。"),
   ("note", u"教訓", [("p", u"Cyc 告訴我們：<strong>常識是知識表示最困難的部分</strong>。實務上，成功的本體幾乎都聚焦在明確的領域與目的（醫學、基因、金融），而不是試圖描述整個世界。")]),
  ],
  u"勒納特 1984 年啟動 Cyc，主張專家系統缺乏常識，試圖以邏輯斷言寫下人類常識。它使用 CycL 語言與微理論，累積數十萬概念、數千萬斷言，投入逾千人年，有商業應用但未實現通用常識的承諾。手工知識可解釋、可檢查一致性但涵蓋有限，LLM 涵蓋極廣但難解釋且會幻覺，兩者正走向結合。成功的本體多聚焦明確領域。",
  [u"什麼是 Cyc 的「微理論」？為什麼需要它？", u"手工知識庫與大型語言模型各有什麼優缺點？", u"為什麼常識是知識表示中最難的部分？"]),

lesson(u"格魯伯的定義與 Ontology 工程的誕生",
  u"1990 年代：從 AI 實驗室走向工程方法",
  [u"了解知識共享計畫與 Ontolingua", u"理解本體設計的基本準則", u"認識瓜里諾的本體分類"],
  [("p", u"1991 年，DARPA 的知識共享計畫發表報告，主張建立可共享、可重用的知識元件。在這個計畫中，史丹佛的格魯伯開發了 <strong>Ontolingua</strong>：一個讓研究者在網路上協作建立本體、並轉換成不同知識表示系統的伺服器。"),
   ("p", u"1993 年，格魯伯在論文中給出本體的經典定義（第 1 課），1995 年又提出本體設計的五個準則："),
   ("t", [u"準則", u"意思"],
    [[u"<strong>清晰</strong>（clarity）", u"定義要客觀、盡量形式化，並附上自然語言說明"], [u"<strong>一致</strong>（coherence）", u"推論出的結果不能和定義矛盾"],
     [u"<strong>可擴充</strong>（extendibility）", u"能在不修改既有定義的情況下加入新術語"], [u"<strong>最小編碼偏差</strong>", u"概念化不應依賴某種特定的符號或實作方式"],
     [u"<strong>最小本體論承諾</strong>", u"只承諾足以支援目標的最少內容，讓更多人能採用"]]),
   ("p", u"最後一條直接呼應了蒯因（第 11 課）與奧坎剃刀（第 8 課）。"),
   ("h", u"瓜里諾的本體分類（1998）"),
   ("p", u"義大利學者瓜里諾（Nicola Guarino）依照通用程度，把本體分成幾種："),
   ("ul", [u"<strong>上層本體</strong>：最通用的概念——空間、時間、物體、事件、過程（DOLCE 就是他的團隊開發的）。", u"<strong>領域本體</strong>：特定領域的概念（醫學、汽車）。", u"<strong>任務本體</strong>：特定任務的概念（診斷、銷售）。", u"<strong>應用本體</strong>：特定應用，同時引用領域與任務本體。"]),
   ("h", u"OntoClean"),
   ("p", u"瓜里諾和威爾提（Welty）還提出 <strong>OntoClean</strong> 方法，用哲學概念（剛性、同一性、統一性、依存性）檢查分類階層是否合理。例如「學生」不是剛性的（一個人可以不再是學生），所以「人 ⊑ 學生」或把「學生」放在「人」上層都是錯的（第 25 課）。"),
   ("note", u"從 AI 到網路", [("p", u"1990 年代末，全球資訊網爆炸成長。柏納斯–李看到：如果網頁上的資料也能用本體描述，整個網路就會變成一個巨大的知識庫。這就是 2001 年的語意網願景（第 31 課），本體從此走出 AI 實驗室。")]),
  ],
  u"DARPA 知識共享計畫催生了格魯伯的 Ontolingua 與 1993 年的本體定義；他 1995 年提出清晰、一致、可擴充、最小編碼偏差、最小本體論承諾五項設計準則。瓜里諾依通用程度分出上層、領域、任務、應用本體，並與威爾提提出以剛性、同一性等哲學概念檢查階層的 OntoClean。1990 年代末網路的成長，使本體走出 AI 實驗室，走向語意網。",
  [u"格魯伯的「最小本體論承諾」是什麼意思？為什麼重要？", u"上層本體、領域本體、任務本體、應用本體各舉一例。", u"OntoClean 為什麼認為「學生」不能是「人」的上層類別？"]),
]),

(u"模組 D｜Ontology 的組成", [

lesson(u"類別與個體",
  u"Class 與 Individual：最基本的區分",
  [u"理解類別、個體與 rdf:type", u"理解類別的外延與內涵", u"避免類別與個體混淆"],
  [("p", u"Ontology 的兩種基本元素："),
   ("ul", [u"<strong>類別</strong>（Class）：一群具有共同特徵的東西，例如「小說」「作家」「借閱紀錄」。", u"<strong>個體</strong>（Individual，也叫實例）：具體的一個東西，例如《魔戒》、托爾金、第 20231105-001 號借閱紀錄。"]),
   ("p", u"個體和類別之間的關係叫 <strong>rdf:type</strong>（「是一個」）：《魔戒》rdf:type 小說。"),
   ("h", u"外延與內涵"),
   ("ul", [u"<strong>外延</strong>：類別包含哪些個體——「小說」的外延是所有小說的集合。OWL 的語意就是用集合定義的：類別 = 個體的集合。", u"<strong>內涵</strong>：類別的定義或意義——「小說」是「篇幅較長的虛構散文敘事作品」。"]),
   ("p", u"兩個類別可以外延相同、內涵不同：「有心臟的動物」與「有腎臟的動物」（在現實中剛好是同一群動物）。OWL 只看外延，所以如果宣告兩者等價，推理機不會反對。"),
   PY(u"""
from owlready2 import get_ontology, Thing

onto = get_ontology("http://example.org/lib.owl")
with onto:
    class Book(Thing): pass
    class Novel(Book): pass            # Novel ⊑ Book
    class Author(Thing): pass

    lotr = Novel("LOTR")               # 個體：rdf:type Novel
    tolkien = Author("Tolkien")

print(lotr.is_a)                       # [lib.Novel]
print(list(Novel.instances()))         # [lib.LOTR]
print(Book in Novel.ancestors())       # True
"""),
   ("h", u"常見的混淆"),
   ("t", [u"情況", u"問題", u"較好的做法"],
    [[u"把「台北」做成類別", u"台北是一個具體的城市，不是一群東西", u"台北是「城市」這個類別的個體"], [u"把每個產品型號做成類別", u"「iPhone 16」是型號，「我手上這支」才是個體，兩者都有可能需要", u"依用途決定；必要時用「產品型號」與「產品單品」兩個類別"],
     [u"把顏色「紅色」做成類別", u"看用途：要描述「紅色的東西」還是「紅色這種顏色」", u"通常做成「顏色」類別的個體"]]),
   ("note", u"雙關（punning）", [("p", u"有時候同一個名字需要同時當類別和個體：「金鷹」這個物種是一個類別（包含所有金鷹），但它本身也可以有屬性（保育等級：一級）。OWL 2 允許同一個 IRI 同時當類別和個體使用，稱為 <strong>punning</strong>，但兩種身分在邏輯上是分開處理的。")]),
  ],
  u"類別是具共同特徵的一群東西，個體是具體的一個，兩者以 rdf:type 連結。外延是類別包含的個體集合，內涵是其定義，OWL 只看外延。常見錯誤是把具體城市做成類別，或不分產品型號與單品。OWL 2 的 punning 允許同一 IRI 兼作類別與個體，但邏輯上分開處理。",
  [u"「托爾金」和「作家」，哪個是類別、哪個是個體？", u"什麼是類別的外延和內涵？", u"什麼情況下需要 punning？"]),

lesson(u"階層與繼承：is-a 與 part-of",
  u"最常見的建模錯誤：把「部分」當成「子類別」",
  [u"理解 subClassOf 的集合語意", u"區分 is-a、instance-of 與 part-of", u"理解多重繼承"],
  [("p", u"<strong>subClassOf</strong>（⊑）的意思是：A 的每一個個體，都是 B 的個體。用集合來說，A 是 B 的子集。"),
   F(r"A \sqsubseteq B \iff \forall x\,(A(x) \rightarrow B(x))"),
   ("p", u"這個簡單的定義，排除了許多日常語言中的「是」："),
   ("t", [u"句子", u"關係", u"是 subClassOf 嗎？"],
    [[u"小說是一種書", u"子類別", u"是：每本小說都是書"], [u"《魔戒》是一本小說", u"個體屬於類別（rdf:type）", u"<strong>不是</strong>"], [u"車輪是車的一部分", u"部分與整體", u"<strong>不是</strong>：車輪不是一種車"],
     [u"鋼是汽車的材料", u"組成材料", u"<strong>不是</strong>"], [u"經理是一種員工", u"子類別（假設所有經理都是員工）", u"是"], [u"台北在台灣", u"空間包含", u"<strong>不是</strong>"]]),
   ("h", u"繼承"),
   ("p", u"子類別<strong>繼承</strong>上層類別的所有性質：如果「書都有書名」，那「小說都有書名」。推理機會自動把個體歸入所有上層類別（第 24 課）。"),
   ow("reason", u"看「型別繼承」規則怎麼把《魔戒》一路推成小說、書、出版品："),
   ("h", u"多重繼承"),
   ("p", u"一個類別可以有多個上層類別：「電子書」⊑「書」且「電子書」⊑「數位資源」。這讓階層變成<strong>有向無環圖</strong>而不是樹。多重繼承很有用，但手動維護容易出錯；好的做法是只手寫單一主要階層，其他上層關係用定義讓推理機自動算出（第 24 課的「正規化」）。"),
   PY(u"""
from rdflib import Graph
g = Graph().parse(data='''
@prefix :     <http://example.org/lib#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
:Novel   rdfs:subClassOf :Book .
:EBook   rdfs:subClassOf :Book, :DigitalResource .     # 多重繼承
:Wheel   :partOf :Car .                                 # 部分關係，不是 subClassOf
''', format="turtle")

q = '''SELECT ?c ?super WHERE { ?c rdfs:subClassOf+ ?super }'''
for r in g.query(q, initNs={"rdfs": "http://www.w3.org/2000/01/rdf-schema#"}):
    print(r.c.split("#")[1], "⊑", r.super.split("#")[1])
"""),
   ("note", u"部分關係怎麼表示", [("p", u"部分與整體要用<strong>物件屬性</strong>表示（例如 partOf），而且通常宣告為傳遞屬性。在 OWL 中，「每輛車都有輪子」寫成 Car ⊑ ∃hasPart.Wheel，而不是 Wheel ⊑ Car。")]),
  ],
  u"subClassOf 的意思是 A 的每個個體都是 B 的個體，即子集關係。它排除了個體屬於類別（rdf:type）、部分與整體、組成材料與空間包含等日常語言的「是」。子類別繼承上層的性質，推理機自動向上歸類。多重繼承使階層成為有向無環圖，宜手寫單一主階層、其餘由定義推出。部分關係以傳遞的物件屬性表示，如 Car ⊑ ∃hasPart.Wheel。",
  [u"「車輪 ⊑ 車」錯在哪裡？應該怎麼寫？", u"「經理是一種員工」在什麼情況下不成立？", u"為什麼多重繼承最好交給推理機算出來？"]),

lesson(u"屬性：物件屬性與資料屬性",
  u"東西和東西之間的關係，以及東西和數值之間的關係",
  [u"區分物件屬性與資料屬性", u"認識資料型別", u"理解註解屬性"],
  [("p", u"OWL 有三種屬性："),
   ("t", [u"屬性", u"連結", u"例子"],
    [[u"<strong>物件屬性</strong>（ObjectProperty）", u"個體 → 個體", u"《魔戒》作者是 托爾金；書架A3 位於 三樓"], [u"<strong>資料屬性</strong>（DatatypeProperty）", u"個體 → 常值（數字、字串、日期）", u"《魔戒》出版年 1954；托爾金 姓名 \"J. R. R. Tolkien\""],
     [u"<strong>註解屬性</strong>（AnnotationProperty）", u"附加說明，不參與推理", u"rdfs:label、rdfs:comment、skos:definition、作者、版本"]]),
   ("h", u"資料型別"),
   ("p", u"資料屬性的值有型別，多採用 XML Schema 的資料型別：xsd:string、xsd:integer、xsd:decimal、xsd:boolean、xsd:dateTime 等。也可以限制範圍，例如「年齡是 0 到 150 的整數」。"),
   ("h", u"屬性也有階層"),
   ("p", u"屬性可以有子屬性：「母親是」⊑「父母是」⊑「祖先是」。如果安的母親是瑪麗，推理機就會推出安的父母是瑪麗、安的祖先是瑪麗。"),
   F(r"\text{hasMother} \sqsubseteq \text{hasParent} \sqsubseteq \text{hasAncestor}"),
   PY(u"""
from owlready2 import get_ontology, Thing, ObjectProperty, DataProperty, FunctionalProperty
import datetime

onto = get_ontology("http://example.org/lib.owl")
with onto:
    class Book(Thing): pass
    class Person(Thing): pass

    class written_by(Book >> Person): pass                 # 物件屬性
    class year(Book >> int, FunctionalProperty): pass      # 資料屬性（函數性：只有一個值）
    class isbn(Book >> str, FunctionalProperty): pass

    class has_parent(Person >> Person): pass
    class has_mother(has_parent): pass                     # 子屬性

    lotr = Book("LOTR", year=1954, isbn="978-0-261-10325-2")
    lotr.written_by = [Person("Tolkien")]
"""),
   ("h", u"用註解讓人看得懂"),
   ("p", u"每個類別與屬性都應該有人類可讀的標籤（rdfs:label，可以有多種語言，例如 \"小說\"@zh-TW、\"Novel\"@en）與定義（skos:definition）。IRI 只是給機器的識別碼；沒有好的註解，本體很快就沒人看得懂。"),
   ("note", u"屬性值是物件還是常值？", [("p", u"「出生地」該填字串 \"台北\" 還是個體 :台北？若只是顯示用，字串就夠；若要查詢「出生在台灣北部的作家」，就必須是個體，才能沿著「位於」關係走下去。這又是一次本體論承諾的選擇（第 11 課）。")]),
  ],
  u"OWL 有物件屬性（連結兩個個體）、資料屬性（連結個體與型別化常值，常用 XML Schema 型別）與不參與推理的註解屬性。屬性可以有階層，如 hasMother ⊑ hasParent ⊑ hasAncestor，推理機會沿子屬性推出上層屬性。每個概念都應有多語標籤與定義。屬性值做成常值或個體，取決於是否需要沿著它繼續查詢。",
  [u"「出版年」應該是物件屬性還是資料屬性？", u"為什麼「出生地」有時候應該是個體而不是字串？", u"子屬性在推理時有什麼作用？"]),

lesson(u"關係的性質：傳遞、對稱、反向、函數性",
  u"讓推理機知道關係「怎麼運作」",
  [u"認識物件屬性的各種特性", u"理解每種特性能推出什麼", u"知道誤用特性的後果"],
  [("p", u"宣告屬性的數學性質，推理機就能自動推出許多新事實："),
   ("t", [u"特性", u"定義", u"例子"],
    [[u"<strong>傳遞</strong>", u"R(a,b) ∧ R(b,c) ⇒ R(a,c)", u"位於、祖先是、部分是"], [u"<strong>對稱</strong>", u"R(a,b) ⇒ R(b,a)", u"朋友、配偶、鄰接"], [u"<strong>非對稱</strong>", u"R(a,b) ⇒ ¬R(b,a)", u"父母是、大於"],
     [u"<strong>反向</strong>", u"R(a,b) ⇔ S(b,a)", u"作者是 ↔ 寫了；父母是 ↔ 子女是"], [u"<strong>函數性</strong>", u"每個 a 最多一個 b", u"生母是、出生日期"], [u"<strong>反函數性</strong>", u"每個 b 最多一個 a", u"身分證字號是、電子郵件"],
     [u"<strong>自反</strong>／<strong>非自反</strong>", u"R(a,a) 總是成立／永不成立", u"認識自己／是…的父母"]]),
   ow("reason", u"打開或關掉不同的規則，看看推理結果怎麼變化。特別注意「位於」的傳遞與「朋友」的對稱："),
   ("h", u"函數性帶來的「同一」推理"),
   ("p", u"開放世界中沒有唯一名稱假設（第 29 課）。如果「生母是」是函數性的，又寫了「安 生母是 瑪莉亞」「安 生母是 瑪麗」，推理機<strong>不會</strong>報錯，而是推出「瑪莉亞 = 瑪麗」（owl:sameAs）。反函數性也一樣：兩筆紀錄有相同的身分證字號，就推出是同一個人——這是資料整合中<strong>實體解析</strong>的利器。"),
   PY(u"""
from owlready2 import (get_ontology, Thing, TransitiveProperty, SymmetricProperty,
                       FunctionalProperty, InverseFunctionalProperty, sync_reasoner)

onto = get_ontology("http://example.org/rel.owl")
with onto:
    class Place(Thing): pass
    class Person(Thing): pass
    class located_in(Place >> Place, TransitiveProperty): pass
    class friend_of(Person >> Person, SymmetricProperty): pass
    class national_id(Person >> str, FunctionalProperty, InverseFunctionalProperty): pass
    class written_by(Thing >> Person): pass
    class wrote(Person >> Thing): inverse_property = written_by

    shelf, floor, lib = Place("ShelfA3"), Place("Floor3"), Place("MainLibrary")
    shelf.located_in = [floor]; floor.located_in = [lib]

sync_reasoner()                     # 需要 Java；會呼叫 HermiT 推理機
print(shelf.located_in)             # 推理後包含 MainLibrary
"""),
   ("h", u"誤用的代價"),
   ("ul", [u"把「認識」宣告成傳遞的：我認識你、你認識總統，就推出我認識總統。", u"把「部分是」宣告成傳遞，又把成員關係也當成部分關係：手是樂團的一部分（第 12 課）。", u"把「姓名」宣告成反函數性：同名同姓的人會被合併成同一個人。"]),
  ],
  u"物件屬性可宣告傳遞、對稱、非對稱、反向、函數性、反函數性、自反與非自反等特性，推理機據此自動推出新事實。在無唯一名稱假設下，函數性與反函數性會推出 sameAs，是實體解析的利器。owlready2 可宣告這些特性並以 HermiT 推理。誤用特性（如把認識設為傳遞、把姓名設為反函數性）會導致荒謬推論或錯誤合併。",
  [u"「比…高」是傳遞的嗎？對稱的嗎？", u"為什麼函數性屬性會推出兩個個體相同？", u"把「姓名」設為反函數性有什麼危險？"]),

lesson(u"定義域、值域與限制條件",
  u"屬性可以用在哪些東西上？類別的成員必須滿足什麼條件？",
  [u"理解 domain 與 range 的推論語意", u"認識存在、全稱、基數與值限制", u"會用限制條件描述類別"],
  [("h", u"定義域與值域"),
   F(r"\text{domain}(P) = C \;:\; P(x,y) \Rightarrow C(x),\qquad \text{range}(P) = D \;:\; P(x,y) \Rightarrow D(y)"),
   ("p", u"這是 RDFS／OWL 中最常被誤解的地方：domain 與 range <strong>不是檢查規則</strong>，而是<strong>推論規則</strong>。寫了「作者是」的 domain 是「書」，再寫「托爾金 作者是 某人」，推理機不會報錯，而是推出「托爾金是一本書」。"),
   ow("reason", u"看「納尼亞 type 書」怎麼被定義域推出來的："),
   ("h", u"限制條件"),
   ("p", u"OWL 用<strong>屬性限制</strong>描述類別的成員必須滿足什麼條件。每個限制本身就是一個（匿名）類別："),
   ("t", [u"限制", u"描述邏輯寫法", u"意思", u"例子"],
    [[u"存在限制", M(r"\exists P.C"), u"至少有一個 P 值屬於 C", u"父母 ≡ 人 ⊓ ∃有子女.人"], [u"全稱限制", M(r"\forall P.C"), u"所有的 P 值都屬於 C（可能一個都沒有）", u"素食者 ⊑ ∀吃.植物"],
     [u"基數限制", M(r"{\geq}n\,P,\;{\leq}n\,P,\;{=}n\,P"), u"P 值的個數", u"人 ⊑ =2 有生物學上的父母"], [u"值限制", M(r"\exists P.\{a\}"), u"P 值包含某個特定個體", u"台灣人 ≡ 人 ⊓ ∃國籍.{台灣}"]]),
   ("h", u"全稱限制的陷阱"),
   ("p", u"「素食者 ⊑ ∀吃.植物」的意思是：如果素食者吃了東西，那東西一定是植物。一個<strong>什麼都不吃</strong>的人也滿足這個條件（空真）。所以全稱限制通常要搭配存在限制：素食者 ⊑ ∃吃.植物 ⊓ ∀吃.植物。"),
   PY(u"""
from owlready2 import get_ontology, Thing, ObjectProperty

onto = get_ontology("http://example.org/food.owl")
with onto:
    class Food(Thing): pass
    class Plant(Food): pass
    class Meat(Food): pass
    class Person(Thing): pass
    class eats(Person >> Food): pass
    class has_child(Person >> Person): pass

    class Parent(Person):
        equivalent_to = [Person & has_child.some(Person)]          # ∃ 存在限制
    class Vegetarian(Person):
        is_a = [eats.some(Plant), eats.only(Plant)]                # ∃ 與 ∀ 搭配
    class BigFamily(Person):
        equivalent_to = [Person & has_child.min(3, Person)]        # 基數限制
"""),
   ("note", u"必要條件 vs. 必要且充分條件", [("p", u"is_a（⊑）寫的是<strong>必要條件</strong>：素食者一定滿足這些條件，但滿足條件的不一定是素食者。equivalent_to（≡）寫的是<strong>必要且充分條件</strong>：滿足條件的就自動被歸類為父母。這個差別決定了推理機能不能自動分類（下一課）。")]),
  ],
  u"domain 與 range 是推論規則而非檢查規則：P(x,y) 推出 x 屬於定義域、y 屬於值域。OWL 以屬性限制描述類別：存在限制 ∃P.C、全稱限制 ∀P.C、基數限制、值限制，每個限制都是匿名類別。全稱限制有空真陷阱，常需搭配存在限制。is_a 表必要條件，equivalent_to 表必要且充分條件，後者使推理機能自動分類。",
  [u"為什麼說 domain 是推論規則而不是檢查規則？", u"一個什麼都不吃的人，是否屬於 ∀吃.植物？", u"「父母 ≡ 人 ⊓ ∃有子女.人」和「父母 ⊑ 人 ⊓ ∃有子女.人」有什麼不同？"]),

lesson(u"公理與推論：讓電腦自動分類",
  u"寫下定義，讓推理機算出你沒寫的階層",
  [u"理解類別公理的種類", u"理解推理機的自動分類", u"理解正規化的設計策略"],
  [("p", u"<strong>公理</strong>是本體中被斷定為真的陳述。常見的類別公理："),
   ("t", [u"公理", u"寫法", u"意思"],
    [[u"子類別", M(r"A \sqsubseteq B"), u"A 都是 B"], [u"等價", M(r"A \equiv B"), u"A 和 B 外延相同（必要且充分的定義）"], [u"互斥", M(r"A \sqcap B \sqsubseteq \bot"), u"沒有東西同時是 A 和 B（例：貓與狗）"],
     [u"不相交聯集", M(r"A \equiv B \sqcup C,\; B \sqcap C \sqsubseteq \bot"), u"A 恰好分成 B 和 C 兩種"]]),
   ("h", u"自動分類"),
   ("p", u"用 ≡ 寫下每個類別的定義，推理機就能算出類別之間的包含關係——<strong>你沒有手寫的 subClassOf，它會自己找出來</strong>。也能把個體自動歸入所有它符合定義的類別。"),
   ow("classify", u"所有的類別都只寫了定義，沒有寫任何 subClassOf。推理機算出了右邊的階層；再看看「瑪麗」被歸入哪些類別："),
   ("h", u"正規化：只手寫一棵樹"),
   ("p", u"艾倫・雷克特（Alan Rector）提出的<strong>本體正規化</strong>策略：把類別分成兩種——"),
   ("ul", [u"<strong>原始類別</strong>（primitive）：只寫必要條件，排成一棵<strong>單一繼承</strong>的樹，兄弟之間互斥。例如：人、物質、器官。", u"<strong>定義類別</strong>（defined）：用 ≡ 寫必要且充分條件，不手寫上層類別。例如：父母、心臟病藥物、有女兒的母親。", u"所有多重繼承，都交給推理機自動算出。"]),
   ("p", u"這樣做的好處：大型醫學本體（例如 SNOMED CT 有數十萬個概念）不可能人工維護正確的多重繼承；讓推理機算，就能保證一致。"),
   PY(u"""
from owlready2 import get_ontology, Thing, sync_reasoner

onto = get_ontology("http://example.org/family.owl")
with onto:
    class Person(Thing): pass
    class Woman(Person): pass
    class has_child(Person >> Person): pass
    class Parent(Thing):  equivalent_to = [Person & has_child.some(Person)]
    class Mother(Thing):  equivalent_to = [Woman & has_child.some(Person)]
    class MotherOfDaughter(Thing): equivalent_to = [Woman & has_child.some(Woman)]

    mary, ann = Woman("Mary"), Woman("Ann")
    mary.has_child = [ann]

sync_reasoner()
print(Mother.is_a)                  # 推理機加入 Parent（自動算出 Mother ⊑ Parent）
print(MotherOfDaughter.is_a)        # Mother
print(mary.is_a)                    # Woman, MotherOfDaughter（自動分類）
"""),
  ],
  u"公理是本體中斷定為真的陳述，包括子類別、等價、互斥與不相交聯集。以 ≡ 寫下必要且充分的定義後，推理機能自動算出類別階層並把個體歸入符合的類別。雷克特的正規化策略：原始類別排成單一繼承、兄弟互斥的樹，定義類別只寫定義，多重繼承交給推理機，使數十萬概念的醫學本體得以維持一致。",
  [u"什麼是互斥公理？舉一個例子。", u"正規化策略中，原始類別和定義類別各怎麼寫？", u"為什麼大型本體需要讓推理機算出多重繼承？"]),

lesson(u"常見的建模錯誤",
  u"角色當類別、is-a 濫用、忘了時間：OntoClean 與實務陷阱",
  [u"辨認常見的建模錯誤", u"理解剛性與 OntoClean 的檢查", u"認識處理時間與變化的方法"],
  [("h", u"錯誤一：把角色當成類別階層的一部分"),
   ("p", u"「學生」「員工」「病人」「客戶」是<strong>角色</strong>：一個人可以開始或停止扮演它們。OntoClean（第 18 課）稱之為<strong>非剛性</strong>的。如果寫「學生 ⊑ 人」再寫「研究助理 ⊑ 學生 ⊓ 員工」還算合理；但寫「人 ⊑ 員工」或用「員工」當成某人唯一的類別，畢業或離職時就得改變他的類別，這是不對的。"),
   ("p", u"較好的做法：角色可以是一個獨立的實體（某人在某段時間擔任某角色），或用「擔任」關係連結人與角色。"),
   ("h", u"錯誤二：is-a 濫用"),
   ("ul", [u"部分當子類別：「引擎 ⊑ 汽車」。", u"實例當子類別：「台北 ⊑ 城市」。", u"「或」當子類別：「書或期刊」做成「書」的上層類別，再把期刊也放進去，結果階層亂成一團。", u"用類別表示屬性值：「紅色的車」「藍色的車」「白色的車」……每種顏色一個子類別，不如用一個顏色屬性。"]),
   ("h", u"錯誤三：忽略時間與變化"),
   ("p", u"「瑪麗 配偶 約翰」——什麼時候？離婚後這條三元組還成立嗎？RDF 的三元組本身沒有時間。常見的處理方法："),
   ("t", [u"方法", u"做法"],
    [[u"具體化（第 8 課）", u"把婚姻做成實體，加上開始與結束日期"], [u"命名圖（named graph）", u"把一組三元組放進一個有名字的圖，再描述這個圖的有效時間"],
     [u"RDF-star", u"讓三元組本身可以當作主詞，直接標註時間：<< :瑪麗 :配偶 :約翰 >> :自 2015 ."], [u"Wikidata 的限定詞", u"每個陳述可以附加「開始時間」「結束時間」「來源」等限定詞（第 42 課）"]]),
   ("h", u"錯誤四：混淆開放世界與封閉世界"),
   ("p", u"期待 OWL 的 domain、基數限制幫你檢查資料（第 23、29 課）。結果資料有錯也不報錯，反而推出奇怪的結論。"),
   ("h", u"錯誤五：沒有註解與定義"),
   ("p", u"只有 IRI、沒有 rdfs:label 與 skos:definition，半年後連作者都不記得某個類別的意思。"),
   PY(u"""
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import XSD

EX = Namespace("http://example.org/#")
g = Graph()
# RDF 1.2 / RDF-star 的寫法（rdflib 對 RDF-star 的支援依版本而定，這裡用具體化示範）
m = EX.Marriage42
g.add((m, EX.partner, EX.Mary)); g.add((m, EX.partner, EX.John))
g.add((m, EX.validFrom, Literal("2015-06-20", datatype=XSD.date)))
g.add((m, EX.validTo,   Literal("2021-03-01", datatype=XSD.date)))
"""),
  ],
  u"常見建模錯誤：把非剛性的角色（學生、員工）放進類別階層，應改以角色實體或擔任關係表示；is-a 濫用，包括部分當子類別、實例當子類別、以子類別表示屬性值；忽略時間，可用具體化、命名圖、RDF-star 或 Wikidata 式限定詞處理；混淆開放與封閉世界；缺少註解與定義。",
  [u"為什麼「員工」不適合當作一個人唯一的類別？", u"「紅色的車」「藍色的車」做成子類別有什麼問題？", u"有哪些方法可以表示「瑪麗和約翰 2015 年到 2021 年是夫妻」？"]),
]),

(u"模組 E｜邏輯基礎", [

lesson(u"一階邏輯回顧",
  u"謂詞、量詞與模型：Ontology 語言的根",
  [u"複習一階邏輯的語法", u"理解模型與滿足的概念", u"理解一階邏輯為什麼太強"],
  [("p", u"一階謂詞邏輯（FOL）有："),
   ("ul", [u"<strong>常數</strong>：特定的個體，如 托爾金、魔戒。", u"<strong>謂詞</strong>：一元謂詞（類別）如 Book(x)；二元謂詞（關係）如 writtenBy(x, y)。", u"<strong>連接詞</strong>：¬、∧、∨、→、↔。", u"<strong>量詞</strong>：∀（對所有）、∃（存在）。"]),
   ("h", u"把本體寫成一階邏輯"),
   ("t", [u"本體陳述", u"一階邏輯"],
    [[u"小說 ⊑ 書", M(r"\forall x\,(\text{Novel}(x)\rightarrow\text{Book}(x))")], [u"父母 ≡ 人 ⊓ ∃有子女.人", M(r"\forall x\,(\text{Parent}(x)\leftrightarrow \text{Person}(x)\wedge\exists y\,(\text{hasChild}(x,y)\wedge\text{Person}(y)))")],
     [u"位於 是傳遞的", M(r"\forall x\,\forall y\,\forall z\,(\text{in}(x,y)\wedge\text{in}(y,z)\rightarrow\text{in}(x,z))")], [u"作者是 的定義域是 書", M(r"\forall x\,\forall y\,(\text{writtenBy}(x,y)\rightarrow\text{Book}(x))")]]),
   ("h", u"模型與蘊涵"),
   ("p", u"一個<strong>模型</strong>（解釋）是一個「可能世界」：指定論域裡有哪些東西、每個謂詞對哪些東西為真。一個知識庫 KB <strong>蘊涵</strong> φ（KB ⊨ φ），意思是：在<strong>所有</strong>讓 KB 為真的模型中，φ 都為真。推理機做的事，就是判斷蘊涵。"),
   F(r"\text{KB} \models \varphi \iff \text{每一個滿足 KB 的模型都滿足 } \varphi"),
   ("h", u"一階邏輯太強了"),
   ("p", u"一階邏輯的蘊涵問題是<strong>不可判定</strong>的（丘奇與圖靈，1936）：不存在一個演算法，能對任意的 KB 和 φ 在有限時間內正確回答 KB ⊨ φ。推理機可能永遠跑不完。"),
   ("p", u"所以本體語言採取的策略是：只取一階邏輯中<strong>夠用、又可判定</strong>的一部分——這就是描述邏輯（下一課）。"),
   PY(u"""
# 用 Python 在一個小模型上檢查一階公式是否成立（有限論域時可以窮舉）
domain = {"魔戒", "哈比人", "托爾金", "路易斯"}
Book   = {"魔戒", "哈比人"}
Person = {"托爾金", "路易斯"}
writtenBy = {("魔戒", "托爾金"), ("哈比人", "托爾金")}

# ∀x ∀y (writtenBy(x,y) → Book(x) ∧ Person(y))
ok = all((x in Book and y in Person) for (x, y) in writtenBy)
# ∀x (Book(x) → ∃y writtenBy(x,y))
every_book_has_author = all(any((b, y) in writtenBy for y in domain) for b in Book)
print(ok, every_book_has_author)
"""),
  ],
  u"一階邏輯有常數、謂詞、連接詞與量詞，本體陳述都可以翻譯成一階公式：subClassOf 是全稱蘊含、存在限制含存在量詞、傳遞性與定義域都是全稱公式。模型是一個可能世界，KB ⊨ φ 指所有滿足 KB 的模型都滿足 φ，推理機即判斷蘊涵。一階邏輯的蘊涵不可判定，因此本體語言只取可判定的片段，也就是描述邏輯。",
  [u"把「每本書都至少有一位作者」寫成一階公式。", u"KB ⊨ φ 是什麼意思？", u"為什麼不直接用完整的一階邏輯當本體語言？"]),

lesson(u"描述邏輯：從 ALC 到 SROIQ",
  u"OWL 背後的邏輯：一階邏輯的可判定片段",
  [u"認識描述邏輯的語法與語意", u"理解 ALC 與擴充的命名方式", u"知道 OWL 2 DL 對應 SROIQ(D)"],
  [("p", u"<strong>描述邏輯</strong>（Description Logic, DL）是一族專門描述「概念」（類別）與「角色」（關係）的邏輯。它只能寫特定形式的公式，換來推理的<strong>可判定性</strong>。"),
   ("h", u"基本語言 ALC"),
   ("t", [u"構造子", u"寫法", u"集合語意"],
    [[u"原子概念", u"A", M(r"A^{\mathcal I} \subseteq \Delta^{\mathcal I}")], [u"頂與底", u"⊤、⊥", u"所有東西、空集合"], [u"交集", u"C ⊓ D", M(r"C^{\mathcal I} \cap D^{\mathcal I}")], [u"聯集", u"C ⊔ D", M(r"C^{\mathcal I} \cup D^{\mathcal I}")],
     [u"否定", u"¬C", M(r"\Delta^{\mathcal I} \setminus C^{\mathcal I}")], [u"存在限制", u"∃R.C", M(r"\{x \mid \exists y\,(x,y)\in R^{\mathcal I} \wedge y\in C^{\mathcal I}\}")], [u"全稱限制", u"∀R.C", M(r"\{x \mid \forall y\,(x,y)\in R^{\mathcal I} \rightarrow y\in C^{\mathcal I}\}")]]),
   ("p", u"ALC 就是「Attributive Language with Complements」。描述邏輯是一階邏輯的片段：∃R.C 翻成一階邏輯就是 ∃y (R(x,y) ∧ C(y))，但描述邏輯的寫法不需要變數，比較簡潔。"),
   ("h", u"擴充的命名"),
   ("t", [u"字母", u"增加的功能"],
    [[u"S", u"ALC + 傳遞角色"], [u"H", u"角色階層（hasMother ⊑ hasParent）"], [u"R", u"複雜角色包含（hasParent ∘ hasBrother ⊑ hasUncle）、自反、非對稱等"], [u"O", u"名目（具體個體組成的類別：{台灣, 日本}）"],
     [u"I", u"反向角色（writtenBy⁻）"], [u"N／Q", u"基數限制（不限定／限定類別）"], [u"F", u"函數性角色"], [u"(D)", u"資料型別"]]),
   ("p", u"所以 OWL 1 DL 對應 <strong>SHOIN(D)</strong>，OWL 2 DL 對應 <strong>SROIQ(D)</strong>。"),
   F(r"\text{hasParent} \circ \text{hasBrother} \sqsubseteq \text{hasUncle}"),
   ("p", u"上式是 SROIQ 的角色鏈：父母的兄弟就是叔伯舅。這在 OWL 1 裡寫不出來。"),
   ow("classify", u"這裡的分類器只用到 ⊓ 與 ∃（屬於更小的 EL 語言），已經足以自動算出類別階層："),
   PY(u"""
# owlready2 的類別運算式與 DL 構造子對應
from owlready2 import get_ontology, Thing, Not
onto = get_ontology("http://example.org/dl.owl")
with onto:
    class Person(Thing): pass
    class Woman(Person): pass
    class has_child(Person >> Person): pass
    expr1 = Woman & has_child.some(Person)          # Woman ⊓ ∃hasChild.Person
    expr2 = Person & Not(Woman)                     # Person ⊓ ¬Woman
    expr3 = has_child.only(Woman)                   # ∀hasChild.Woman
    expr4 = has_child.exactly(2, Person)            # =2 hasChild.Person   （Q）
    print(expr1, expr2, expr3, expr4, sep="\\n")
"""),
  ],
  u"描述邏輯是專門描述概念與角色的一階邏輯可判定片段。ALC 有原子概念、頂底、交、聯、否定、存在與全稱限制，各有集合語意。擴充以字母命名：S 傳遞、H 角色階層、R 角色鏈與角色性質、O 名目、I 反向、N/Q 基數、F 函數性、(D) 資料型別。OWL 1 DL 對應 SHOIN(D)，OWL 2 DL 對應 SROIQ(D)，例如角色鏈 hasParent ∘ hasBrother ⊑ hasUncle。",
  [u"把 ∀hasChild.Woman 翻成一階邏輯。", u"SROIQ 中的 O 和 I 分別是什麼？", u"為什麼「父母的兄弟是叔伯」在 OWL 1 裡寫不出來？"]),

lesson(u"推理服務：包含、一致性與實例檢查",
  u"推理機到底在「推」什麼？Tableau 演算法入門",
  [u"認識標準的推理服務", u"理解各服務之間的轉換", u"理解 Tableau 演算法的直覺"],
  [("p", u"描述邏輯推理機提供幾種標準服務："),
   ("t", [u"服務", u"問題", u"用途"],
    [[u"<strong>概念可滿足性</strong>", u"C 有可能有成員嗎？", u"找出定義有矛盾的類別（例如 素食者 ⊓ 吃肉的人）"], [u"<strong>包含</strong>", u"C ⊑ D 嗎？", u"自動分類（第 24 課）"],
     [u"<strong>一致性</strong>", u"整個知識庫有沒有矛盾？", u"品質檢查"], [u"<strong>實例檢查</strong>", u"個體 a 屬於 C 嗎？", u"自動歸類、查詢"], [u"<strong>分類</strong>", u"算出所有具名類別之間的包含階層", u"本體瀏覽與維護"]]),
   ("h", u"它們可以互相轉換"),
   F(r"C \sqsubseteq D \iff C \sqcap \neg D \text{ 不可滿足}"),
   ("p", u"所以只要能判斷「可滿足性」，其他問題都能解。推理機的核心就是一個可滿足性檢查器。"),
   ("h", u"Tableau 演算法的直覺"),
   ("p", u"要檢查 C 是否可滿足，就試著<strong>建構</strong>一個 C 的成員："),
   ("ol", [u"先假設存在一個個體 x 屬於 C。", u"把 C 拆開：遇到 ⊓ 就把兩邊都加進 x 的標籤；遇到 ⊔ 就分岔，兩種可能都試；遇到 ∃R.D 就造一個新的 R-鄰居 y 屬於 D；遇到 ∀R.D 就把 D 加到所有 R-鄰居。", u"如果某個分支出現矛盾（x 同時屬於 A 和 ¬A），這個分支失敗。", u"所有分支都失敗 → 不可滿足；有一個分支走完沒有矛盾 → 可滿足（這個分支就是一個模型）。"]),
   PY(u"""
# 極簡的 ALC tableau（只處理 ⊓、⊔、¬原子、∃、∀），判斷概念是否可滿足
def sat(labels, depth=0):
    labels = set(labels)
    for c in list(labels):                       # 展開交集
        if c[0] == "and": return sat(labels - {c} | {c[1], c[2]}, depth)
    for c in list(labels):                       # 聯集：分岔
        if c[0] == "or":
            rest = labels - {c}
            return sat(rest | {c[1]}, depth) or sat(rest | {c[2]}, depth)
    atoms = {c[1] for c in labels if c[0] == "atom"}
    if any(c[0] == "not" and c[1] in atoms for c in labels):
        return False                             # 衝突：A 與 ¬A
    for c in labels:                             # 存在：造一個鄰居
        if c[0] == "some":
            succ = {c[2]} | {d[2] for d in labels if d[0] == "all" and d[1] == c[1]}
            if not sat(succ, depth + 1): return False
    return True

A = ("atom", "Meat")
veg_meat = ("and", ("all", "eats", ("not", "Meat")), ("some", "eats", A))
print(sat({veg_meat}))     # False：∀eats.¬Meat ⊓ ∃eats.Meat 不可滿足
"""),
   ("h", u"常用的推理機"),
   ("ul", [u"<strong>HermiT</strong>（牛津）：超 tableau 演算法，owlready2 內建。", u"<strong>Pellet</strong>：支援 SWRL 規則與解釋。", u"<strong>FaCT++</strong>、<strong>Konclude</strong>：高效能。", u"<strong>ELK</strong>：專門處理 OWL 2 EL，數十萬概念的醫學本體幾秒內分類完成。"]),
  ],
  u"推理機提供概念可滿足性、包含、一致性、實例檢查與分類等服務，它們可互相轉換，例如 C ⊑ D 等價於 C ⊓ ¬D 不可滿足，因此核心是可滿足性檢查。Tableau 演算法試著建構概念的成員：交集加入標籤、聯集分岔、存在造鄰居、全稱傳播，出現 A 與 ¬A 則該分支失敗。常用推理機有 HermiT、Pellet、FaCT++、Konclude 與專攻 EL 的 ELK。",
  [u"怎麼把「C ⊑ D 嗎？」轉換成可滿足性問題？", u"Tableau 遇到聯集時為什麼要分岔？", u"為什麼 ELK 能那麼快地分類大型醫學本體？"]),

lesson(u"開放世界與封閉世界假設",
  u"OWL 和資料庫最根本的差別",
  [u"理解開放世界假設與封閉世界假設", u"理解唯一名稱假設", u"知道什麼時候該用哪一種"],
  [("t", [u"", u"封閉世界假設（CWA）", u"開放世界假設（OWA）"],
    [[u"沒寫的事", u"是假的", u"是未知的"], [u"代表", u"關聯式資料庫、SQL、Prolog、大多數程式", u"OWL、RDF 的語意、一階邏輯"], [u"適合", u"資料完整、由自己掌控的系統（訂單、帳戶）", u"資料來自多個來源、永遠不完整的網路"],
     [u"唯一名稱假設", u"有：不同名字 = 不同東西", u"沒有：不同名字可能是同一個東西"]]),
   ow("owa", u"同樣的事實，在兩種假設下得到完全不同的答案。試著加入事實，看答案怎麼改變："),
   ("h", u"為什麼語意網選擇開放世界"),
   ("p", u"在網路上，沒有任何人擁有完整的資訊。某個資料集沒提到托爾金寫過《精靈寶鑽》，不代表他沒寫——只是這個資料集不知道。如果採用封閉世界，合併兩個資料集時就會得到互相矛盾的結論。"),
   ("h", u"開放世界的後果"),
   ("ul", [u"<strong>基數限制不會報錯</strong>：「每人恰好一位生母」加上兩位生母，推理機會推出兩人是同一個人；只有當它們被明確宣告為不同（owl:differentFrom）時，才會出現矛盾。", u"<strong>最少限制會推出未知的東西</strong>：「每位學生至少修一門課」，瑪麗是學生卻沒有修課紀錄 → 推出瑪麗修了某門未知的課。", u"<strong>否定很難證明</strong>：要證明「瑪麗沒有小孩」，必須明確寫出 瑪麗 ⊑ =0 有子女 或類似的公理。"]),
   ("h", u"兩者都需要：OWL + SHACL"),
   ("p", u"實務上常見的組合：用 <strong>OWL</strong>（開放世界）描述概念與推論，用 <strong>SHACL</strong>（封閉世界）驗證某個資料集是否完整、格式正確（第 37 課）。另外也有「局部封閉世界」的做法：對自己掌控的資料當作完整，對外部資料保持開放。"),
   PY(u"""
from rdflib import Graph
g = Graph().parse(data='''
@prefix : <http://example.org/#> .
:約翰 a :學生 ; :修 :課程101 .
:瑪麗 a :學生 .
''', format="turtle")

# SPARQL 的 FILTER NOT EXISTS 是「封閉世界」的查詢：資料裡沒有 = 沒有
q = '''SELECT ?s WHERE { ?s a :學生 . FILTER NOT EXISTS { ?s :修 ?c } }'''
print([str(r.s) for r in g.query(q, initNs={"": "http://example.org/#"})])  # 瑪麗
# 但在 OWL 推理的意義下，「瑪麗沒修課」並沒有被證明
"""),
  ],
  u"封閉世界假設認為沒寫的就是假，並有唯一名稱假設，適合資料庫等完整自控的系統；開放世界假設認為沒寫的是未知、不同名字可能指同一物，是 OWL 與 RDF 的語意，適合永遠不完整的網路資料。後果包括基數限制推出 sameAs、最少限制推出未知個體、否定難以證明。實務上以 OWL 描述與推論、以 SHACL 做封閉世界驗證，或採局部封閉世界。",
  [u"為什麼語意網選擇開放世界假設？", u"在 OWA 下，「每位學生至少修一門課」遇到沒有修課紀錄的學生會怎樣？", u"SPARQL 的 FILTER NOT EXISTS 屬於哪一種假設？"]),

lesson(u"可判定性與複雜度：表達力的代價",
  u"OWL 2 的三個輕量子語言：EL、QL、RL",
  [u"理解表達力與推理複雜度的取捨", u"認識 OWL 2 的三個設定檔", u"知道如何依需求選擇"],
  [("p", u"描述邏輯越強，推理越難。SROIQ（OWL 2 DL）的概念可滿足性問題是 <strong>N2EXPTIME 完全</strong>的——理論上最壞情況是雙重指數時間。實務上推理機很聰明，多數本體跑得動，但大型本體可能非常慢。"),
   ("t", [u"語言", u"推理複雜度（概念可滿足性）"],
    [[u"一階邏輯", u"不可判定"], [u"SROIQ（OWL 2 DL）", u"N2EXPTIME 完全"], [u"SHOIN（OWL 1 DL）", u"NEXPTIME 完全"], [u"ALC", u"EXPTIME 完全（一般 TBox）"], [u"EL（OWL 2 EL）", u"多項式時間"], [u"DL-Lite（OWL 2 QL）", u"查詢回答可化為 SQL"]]),
   check(u"多項式與指數的差距（以 n = 概念數估計步驟數）：", [["n", u"n", 30, 5, 200, 1]],
         [[u"n³", "Math.pow(n,3)"], [u"2ⁿ", "Math.pow(2,n)"], [u"log₁₀(2^(2ⁿ)) 的位數感（2ⁿ × log₁₀2）", "Math.pow(2,n)*Math.log10(2)"]]),
   ("h", u"OWL 2 的三個設定檔（profile）"),
   ("t", [u"設定檔", u"保留什麼", u"拿掉什麼", u"適合"],
    [[u"<strong>OWL 2 EL</strong>", u"⊓、∃、類別階層、角色鏈", u"∀、否定、聯集、基數", u"大型術語本體：SNOMED CT、Gene Ontology"],
     [u"<strong>OWL 2 QL</strong>", u"能改寫成 SQL 查詢的部分", u"角色鏈、∃ 在左側等", u"在既有關聯式資料庫上做本體查詢（OBDA）"],
     [u"<strong>OWL 2 RL</strong>", u"能用規則（Datalog）實作的部分", u"在右側的 ∃ 等", u"大量實例資料的規則式推理，例如 RDF 資料庫內建推理"]]),
   ("h", u"怎麼選"),
   ("ul", [u"概念很多、要自動分類 → EL + ELK 推理機。", u"資料在 SQL 資料庫裡、要用本體詞彙查詢 → QL（例如 Ontop 系統把 SPARQL 改寫成 SQL）。", u"三元組很多、要快速物化推論結果 → RL（例如 GraphDB、Jena 的規則推理）。", u"需要完整表達力、資料量不大 → OWL 2 DL + HermiT。"]),
   PY(u"""
# owlrl：在 rdflib 圖上用 OWL 2 RL 規則做前向推理（物化）
from rdflib import Graph
import owlrl

g = Graph().parse(data='''
@prefix :     <http://example.org/#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
:Novel rdfs:subClassOf :Book .
:locatedIn a owl:TransitiveProperty .
:LOTR a :Novel ; :locatedIn :ShelfA3 .
:ShelfA3 :locatedIn :Floor3 .
''', format="turtle")

before = len(g)
owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(g)
print(before, "→", len(g), "triples")   # 推論出 :LOTR a :Book、:LOTR :locatedIn :Floor3 等
"""),
  ],
  u"描述邏輯表達力越強推理越難：一階邏輯不可判定，SROIQ 為 N2EXPTIME 完全，ALC 為 EXPTIME 完全，EL 為多項式時間，DL-Lite 可化為 SQL。OWL 2 提供三個設定檔：EL 保留交與存在，適合大型術語本體；QL 可改寫為 SQL，適合以本體查詢關聯式資料庫；RL 可用規則實作，適合大量實例的物化推理。依資料規模與需求選擇。",
  [u"為什麼 SNOMED CT 適合用 OWL 2 EL？", u"OWL 2 QL 為什麼可以在 SQL 資料庫上使用？", u"什麼是推論的「物化」？"]),
]),
]
