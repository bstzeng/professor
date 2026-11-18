# -*- coding: utf-8 -*-
"""GPU 與平行運算的規格。"""
import gpu_a, gpu_f, gpu_ref

TOPIC = {
    "id": "gpu-computing",
    "category": "tech",
    "title": u"GPU 與平行運算：從 CUDA 到 AI 晶片",
    "short": u"GPU 與平行運算",
    "crumb": u"GPU",
    "icon": u"🟩",
    "description": u"CPU 與 GPU、功耗牆、資料平行與 SIMT、阿姆達定律；從繪圖卡到 CUDA 與 AlexNet、SM 與 Tensor Core、warp 與分支發散、記憶體階層與 HBM、Roofline；"
                   u"kernel、執行緒與區塊、合併存取、共享記憶體與 tiling、同步與歸約、串流；矩陣乘法優化、低精度、FlashAttention、多 GPU 與 NVLink；CUDA 護城河、TPU 與其他加速器、資料中心功耗、台積電 CoWoS 與 HBM。附阿姆達定律、warp 分支、Roofline 與 tiling 四個互動模擬。",
}

MODULES = gpu_a.MODULES + gpu_f.MODULES
REFERENCES = gpu_ref.REFERENCES
