# -*- coding: utf-8 -*-
"""史蒂芬・金：參考頁——互動圖鑑、人物與名詞表。"""
from nv_common import LS, NVLIB
import sk_a, sk_c, sk_f

GUIDE = {
    "file": "guide.html", "title": u"史蒂芬・金互動圖鑑", "h1": u"史蒂芬・金互動圖鑑", "icon": u"🗺️",
    "description": u"閱讀路線、作品年表、緬因州虛構地圖、生平年表、黑塔卡泰特與作品連結圖",
    "body": [
        ("raw", u"<script>%s</script>" % NVLIB),
        ("h", u"1. 閱讀路線（第 37 課）"), sk_f._ORDER,
        ("h", u"2. 作品年表（第 37 課）"), sk_f._WORKS,
        ("h", u"3. 緬因州虛構地圖（第 35 課）"), sk_f._MAINE,
        ("h", u"4. 金的生平（第 1 課）"), sk_a._LIFE,
        ("h", u"5. 黑塔的卡泰特（第 18 課）"), sk_c._KATET,
        ("h", u"6. 作品與黑塔的連結（第 21 課）"), sk_c._LINKS,
    ],
}

_H = [u"中文", u"原文", u"說明", u"課"]

GLOSSARY = {
    "file": "glossary.html", "title": u"史蒂芬・金名詞表", "h1": u"史蒂芬・金名詞表", "icon": u"📖",
    "description": u"人物、地名、術語中英對照",
    "body": [
        ("h", u"1. 人物"),
        ("t", _H,
         [[u"嘉莉・懷特", u"Carrie White", u"有念力的受欺凌少女", LS(4)], [u"傑克・托倫斯", u"Jack Torrance", u"全景飯店的冬季管理員", LS(6)],
          [u"丹尼・托倫斯", u"Danny Torrance", u"有閃靈的男孩，長大成為安眠醫生", LS(24)], [u"迪克・哈洛蘭", u"Dick Hallorann", u"有閃靈的廚師", LS(6)],
          [u"藍道・佛萊格", u"Randall Flagg", u"黑衣人，金宇宙最大的反派", LS(7)], [u"潘尼懷斯", u"Pennywise", u"德瑞的小丑怪物「牠」", LS(11)],
          [u"羅蘭・德斯欽", u"Roland Deschain", u"最後的槍客", LS(18)], [u"卡拉漢神父", u"Father Callahan", u"撒冷地與黑塔中的神父", LS(5)],
          [u"安妮・威克斯", u"Annie Wilkes", u"《戰慄遊戲》的頭號書迷", LS(13)], [u"約翰・柯菲", u"John Coffey", u"《綠色奇蹟》的死囚", LS(15)],
          [u"安迪・杜佛蘭", u"Andy Dufresne", u"蕭山克監獄的銀行家", LS(30)], [u"荷莉・吉布尼", u"Holly Gibney", u"私家偵探，金最喜愛的角色", LS(29)],
          [u"比爾・霍吉斯", u"Bill Hodges", u"退休警探", LS(28)], [u"布雷迪・哈茨菲爾德", u"Brady Hartsfield", u"賓士先生", LS(28)],
          [u"傑克・艾平", u"Jake Epping", u"《11/22/63》的時間旅行者", LS(23)], [u"路克・艾利斯", u"Luke Ellis", u"《機構》的天才少年", LS(26)],
          [u"查理・里德", u"Charlie Reade", u"《童話》的主角", LS(27)], [u"艾斯・梅瑞爾", u"Ace Merrill", u"城堡岩的不良少年", LS(31)]]),
        ("h", u"2. 地名"),
        ("t", _H,
         [[u"德瑞", u"Derry", u"《牠》的小鎮", LS(35)], [u"城堡岩", u"Castle Rock", u"金最常用的小鎮", LS(35)],
          [u"耶路撒冷地", u"Jerusalem's Lot", u"《撒冷地》的小鎮", LS(5)], [u"全景飯店", u"The Overlook Hotel", u"《鬼店》的飯店", LS(6)],
          [u"切斯特磨坊", u"Chester's Mill", u"《穹頂之下》的小鎮", LS(22)], [u"蕭山克監獄", u"Shawshank State Prison", u"安迪服刑之處", LS(30)],
          [u"中世界", u"Mid-World", u"羅蘭的世界", LS(18)], [u"恩皮斯", u"Empis", u"《童話》的王國", LS(27)]]),
        ("h", u"3. 術語"),
        ("t", _H,
         [[u"閃靈", u"the shining", u"心電感應與預知的天賦", LS(6)], [u"卡", u"ka", u"黑塔中的命運", LS(18)],
          [u"卡泰特", u"ka-tet", u"被命運綁在一起的一群人", LS(18)], [u"光束", u"the Beams", u"支撐黑塔的力量線", LS(18)],
          [u"血紅之王", u"the Crimson King", u"想摧毀黑塔的存在", LS(20)], [u"死光", u"the Deadlights", u"潘尼懷斯的真身", LS(12)],
          [u"失敗者俱樂部", u"the Losers' Club", u"《牠》的七個孩子", LS(11)], [u"真結族", u"the True Knot", u"吸食「蒸氣」的族群", LS(24)],
          [u"巴克曼", u"Richard Bachman", u"金的筆名", LS(16)], [u"一元寶寶", u"Dollar Babies", u"一美元授權的學生短片", LS(36)],
          [u"蘭格利爾人", u"the langoliers", u"吞食過去的怪物", LS(34)], [u"兔子洞", u"the rabbit hole", u"《11/22/63》的時光通道", LS(23)]]),
    ],
}

REFERENCES = [GUIDE, GLOSSARY]
