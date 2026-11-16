# -*- coding: utf-8 -*-
"""曼哈頓計畫：參考頁——年表、人物、文獻。"""
from mhp_common import LS


def mono(s):
    return u'<span style="font-family:ui-monospace,Menlo,monospace;font-size:0.9em">%s</span>' % s


TIMELINE = {
    "file": "timeline.html", "title": u"年表", "h1": u"曼哈頓計畫與核時代年表", "icon": u"📅",
    "description": u"從放射性的發現到新削減戰略武器條約到期",
    "body": [
        ("t", [u"時間", u"事件", u"課"], [
            [u"1896", u"貝克勒發現放射性", LS(2)], [u"1932", u"查兌克發現中子", LS(2)], [u"1933 年 9 月", u"西拉德想到連鎖反應", LS(6)],
            [u"1934", u"費米的中子轟擊與慢中子", LS(3)], [u"1938 年 12 月", u"哈恩與史特拉斯曼發現核分裂；邁特納與弗里希解釋", LS(4)],
            [u"1939 年 8 月 2 日", u"愛因斯坦簽署給羅斯福的信", LS(7)], [u"1940 年 3 月", u"弗里希—派爾斯備忘錄", LS(8)], [u"1941 年 7 月", u"MAUD 報告", LS(8)],
            [u"1942 年 9 月", u"格羅夫斯接掌曼哈頓工程區", LS(17)], [u"1942 年 12 月 2 日", u"芝加哥一號堆臨界", LS(14)], [u"1943 年春", u"洛斯阿拉莫斯開始運作", LS(20)],
            [u"1944 年 7 月", u"鈽槍式設計取消，轉向內爆", LS(24)], [u"1944 年 9 月", u"漢福德 B 反應爐啟動", LS(19)], [u"1945 年 7 月 16 日", u"三位一體試爆", LS(26)],
            [u"1945 年 8 月 6 日", u"廣島", LS(29)], [u"1945 年 8 月 9 日", u"蘇聯參戰；長崎", LS(30)], [u"1945 年 8 月 15 日", u"玉音放送", LS(32)],
            [u"1949 年 8 月 29 日", u"蘇聯 RDS-1", LS(35)], [u"1952 年 11 月 1 日", u"常春藤麥克", LS(38)], [u"1953 年 6 月 19 日", u"羅森堡夫婦被處決", LS(34)],
            [u"1954 年 3 月 1 日", u"城堡喝采；第五福龍丸", LS(39)], [u"1954 年 4～6 月", u"歐本海默聽證會", LS(42)], [u"1961 年 10 月 30 日", u"沙皇炸彈", LS(38)],
            [u"1962 年 10 月", u"古巴飛彈危機", LS(40)], [u"1963", u"部分禁止核試條約", LS(39)], [u"1968／1970", u"核不擴散條約簽署／生效", LS(45)],
            [u"1986 年前後", u"全球核彈頭約 7 萬枚的高峰", LS(41)], [u"2022 年 12 月", u"美國能源部撤銷 1954 年對歐本海默的決定", LS(42)],
            [u"2024", u"日本被團協獲諾貝爾和平獎", LS(33)], [u"2026 年 2 月", u"新削減戰略武器條約到期", LS(45)],
        ]),
    ],
}

PEOPLE = {
    "file": "people.html", "title": u"人物", "h1": u"曼哈頓計畫的人物", "icon": u"👥",
    "description": u"本課程中出現的主要人物",
    "body": [
        ("t", [u"人物", u"角色", u"課"], [
            [u"莉澤・邁特納、奧托・弗里希", u"解釋核分裂", LS(4)], [u"奧托・哈恩", u"發現核分裂，1944 年諾貝爾化學獎", LS(4)],
            [u"恩里科・費米", u"慢中子、芝加哥一號堆", LS(14)], [u"里歐・西拉德", u"連鎖反應構想、愛因斯坦的信、反對投彈的請願", LS(6)],
            [u"阿爾伯特・愛因斯坦", u"簽署給羅斯福的信", LS(7)], [u"魯道夫・派爾斯", u"弗里希—派爾斯備忘錄", LS(8)],
            [u"維爾納・海森堡", u"德國核計畫", LS(9)], [u"仁科芳雄", u"日本陸軍核計畫", LS(10)], [u"伊戈爾・庫爾恰托夫", u"蘇聯核計畫", LS(35)],
            [u"萊斯利・格羅夫斯", u"曼哈頓計畫總負責人", LS(17)], [u"J・羅伯特・歐本海默", u"洛斯阿拉莫斯主任", LS(17)],
            [u"格倫・西博格", u"發現鈽", LS(15)], [u"約翰・惠勒", u"氙中毒", LS(19)], [u"漢斯・貝特、理查・費曼", u"洛斯阿拉莫斯理論部", LS(20)],
            [u"埃米利奧・塞格雷", u"鈽 240 的量測", LS(24)], [u"約翰・馮紐曼、喬治・基斯佳科夫斯基", u"內爆與爆炸透鏡", LS(25)],
            [u"約瑟夫・羅特布拉特", u"唯一因德國不再是威脅而離開的科學家", LS(11)], [u"哈里・杜魯門", u"下令投彈", LS(28)],
            [u"克勞斯・福克斯、泰德・霍爾", u"原子間諜", LS(34)], [u"愛德華・泰勒、史坦尼斯瓦夫・烏拉姆", u"氫彈構型", LS(37)],
            [u"安德烈・沙卡洛夫", u"蘇聯氫彈，後成為異議人士", LS(38)], [u"久保山愛吉", u"第五福龍丸無線電長", LS(39)],
            [u"瓦西里・阿爾希波夫", u"拒絕發射核魚雷", LS(40)], [u"佐佐木禎子", u"千羽鶴", LS(29)],
        ]),
    ],
}

BOOKS = {
    "file": "books.html", "title": u"延伸閱讀", "h1": u"文獻與延伸閱讀", "icon": u"📚",
    "description": u"原始文獻、經典歷史著作與研究",
    "body": [
        ("t", [u"文獻", u"出處", u"課"], [
            [u"Meitner, Frisch：Disintegration of Uranium by Neutrons: a New Type of Nuclear Reaction", mono(u"Nature 143, 239 (1939)"), LS(4)],
            [u"Bohr, Wheeler：The Mechanism of Nuclear Fission", mono(u"Phys. Rev. 56, 426 (1939)"), LS(5)],
            [u"Frisch, Peierls：Memorandum on the Properties of a Radioactive \"Super-bomb\"", mono(u"1940"), LS(8)],
            [u"Serber：The Los Alamos Primer", mono(u"LA-1 (1943)；1992 年出版註解版"), LS(20)],
            [u"Konopinski, Marvin, Teller：Ignition of the Atmosphere with Nuclear Bombs", mono(u"LA-602 (1946)"), LS(26)],
            [u"Stimson：The Decision to Use the Atomic Bomb", mono(u"Harper's Magazine, Feb. 1947"), LS(32)],
            [u"Rhodes：The Making of the Atomic Bomb（《原子彈祕史》）", mono(u"1986，普立茲獎"), LS(1)],
            [u"Rhodes：Dark Sun: The Making of the Hydrogen Bomb", mono(u"1995"), LS(37)],
            [u"Bird, Sherwin：American Prometheus（《奧本海默》電影原著）", mono(u"2005，普立茲獎"), LS(42)],
            [u"Hasegawa：Racing the Enemy（長谷川毅）", mono(u"2005"), LS(32)],
            [u"Alperovitz：Atomic Diplomacy", mono(u"1965"), LS(32)],
            [u"Hersey：Hiroshima（《廣島》）", mono(u"The New Yorker, 1946"), LS(29)],
            [u"Selby 等：A New Yield Assessment for the Trinity Nuclear Test, 75 Years Later", mono(u"Nucl. Technol. 207 (2021)"), LS(26)],
            [u"Kristensen, Korda 等：Status of World Nuclear Forces", mono(u"美國科學家聯盟，逐年更新"), LS(41)],
        ]),
    ],
}

REFERENCES = [TIMELINE, PEOPLE, BOOKS]
