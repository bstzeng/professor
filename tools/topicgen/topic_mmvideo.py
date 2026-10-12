# -*- coding: utf-8 -*-
"""多模態 LLM 與影片生成的內部運作主題的規格。"""
import mv_a, mv_b, mv_e, mv_ref

TOPIC = {
    "id": "multimodal-video-internals",
    "category": "ai",
    "title": u"多模態 LLM 與影片生成的內部運作：完整推導",
    "short": u"多模態 LLM 與影片生成",
    "crumb": u"多模態 LLM 與影片生成",
    "icon": u"🎬",
    "description": u"〈多模態與生成式 AI〉的進階版：從注意力、RoPE、對比學習與 VQ-VAE 出發，拆解 LLaVA、Q-Former、Flamingo、早期融合與不用編碼器的多模態 LLM，推導兩階段訓練與 DPO；"
                   u"音訊編碼、全雙工語音與影片理解；再完整推導影片生成：DDPM、flow matching、噪音排程與時間步平移、影片 VAE、時空 patch 與 Video DiT、CFG、鏡頭控制、影音同步、長影片與開源模型拆解；"
                   u"最後是注意力成本、蒸餾、量化、世界模型、評測與浮水印。附 token、注意力、flow matching、排程、抽幀與 VRAM 等互動工具。",
}

MODULES = mv_a.MODULES + mv_b.MODULES + mv_e.MODULES

REFERENCES = mv_ref.REFERENCES
