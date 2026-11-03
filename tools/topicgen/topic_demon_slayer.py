# -*- coding: utf-8 -*-
"""鬼滅之刃主題的規格。"""
import kny_a, kny_c, kny_e, kny_ref

TOPIC = {
    "id": "demon-slayer",
    "category": "anime",
    "title": u"鬼滅之刃全紀錄：呼吸法、劇情與人物完整解析",
    "short": u"鬼滅之刃",
    "crumb": u"鬼滅之刃",
    "icon": u"👹",
    "description": u"吾峠呼世晴的原作、大正時代與 ufotable 的動畫；鬼與鬼舞辻無慘、鬼殺隊與產屋敷、呼吸法、日輪刀與階級、十二鬼月、斑紋與赫刀；從竈門家的悲劇、無限列車、遊郭、刀匠村到無限城與最終章（含漫畫結局劇透）；"
                   u"炭治郎、禰豆子、善逸、伊之助、九柱、上弦之鬼、繼國緣壹與黑死牟、無慘；家人、鬼的悲劇、傳承與和風元素。含呼吸法傳承圖、故事年表、九柱與十二鬼月圖鑑。",
}

MODULES = kny_a.MODULES + kny_c.MODULES + kny_e.MODULES
REFERENCES = kny_ref.REFERENCES
