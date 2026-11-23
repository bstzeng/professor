# -*- coding: utf-8 -*-
import dun_a
from nv_common import NVLIB

ATLAS = {"file": "atlas.html", "title": u"沙丘遊戲圖鑑", "h1": u"沙丘遊戲圖鑑", "icon": u"📜",
         "description": u"遊戲年表與勢力圖鑑",
         "body": [("raw", u"<script>%s</script>" % NVLIB), ("h", u"1. 遊戲年表"), dun_a.GAMES, ("h", u"2. 勢力圖鑑"), dun_a.HOUSES]}

TOPIC = {
    "id": "dune-games", "category": "games",
    "title": u"沙丘魔堡系列遊戲全劇情：從 1992 到沙丘：覺醒",
    "short": u"沙丘魔堡遊戲", "crumb": u"沙丘魔堡遊戲", "icon": u"🏜️",
    "description": u"Cryo 的沙丘（1992）冒險策略與綠化路線；沙丘魔堡 II 的皇帝比賽、三大家族、門塔特與即時戰略的誕生；沙丘魔堡 2000 的真人過場與伊萊拉夫人；沙丘帝王的刺客之戰、亞崔迪、哈肯能、歐鐸斯戰役、附庸勢力與皇帝蠕蟲；法蘭克·赫伯特之沙丘與 Cryo 破產；香料戰爭的七大勢力；沙丘：覺醒的平行時間線；遊戲與原著的差異與取消的作品（含完整劇透）。附遊戲年表與勢力圖鑑。",
}
MODULES = dun_a.MODULES
REFERENCES = [ATLAS]
