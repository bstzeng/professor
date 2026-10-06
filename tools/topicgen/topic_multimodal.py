# -*- coding: utf-8 -*-
"""多模態與生成式 AI 主題的規格。"""
import mm_a, mm_e, mm_ref

TOPIC = {
    "id": "multimodal-ai",
    "category": "ai",
    "title": u"多模態與生成式 AI：圖像、語音與影片",
    "short": u"多模態與生成式 AI",
    "crumb": u"多模態與生成式 AI",
    "icon": u"🎨",
    "description": u"電腦怎麼看圖、聽聲音，又怎麼畫圖、說話、拍影片：生成模型四大家族、VAE、GAN 與 deepfake；擴散模型的加噪去噪、U-Net、取樣器、CFG、"
                   u"Latent Diffusion、Stable Diffusion、DiT 與 flow matching；提示詞、參數、img2img、ControlNet、LoRA、ComfyUI；ViT、CLIP 與視覺語言模型；"
                   u"頻譜圖、Whisper、TTS、聲音複製、neural codec、即時語音對話；AI 音樂、影片生成、世界模型、NeRF 與 Gaussian Splatting；著作權、浮水印與工具地圖。附六個互動工具。",
}

MODULES = mm_a.MODULES + mm_e.MODULES

REFERENCES = mm_ref.REFERENCES
