# -*- coding: utf-8 -*-
"""GPU 與平行運算：參考頁——名詞表、CUDA 速查。"""
from gpu_common import LS, code

GLOSSARY = {
    "file": "glossary.html", "title": u"名詞表", "h1": u"GPU 與平行運算名詞表", "icon": u"📖",
    "description": u"本課程用到的 GPU 與平行運算名詞",
    "body": [
        ("t", [u"名詞", u"意思", u"課"], [
            [u"功耗牆", u"時脈無法再提高的物理限制", LS(2)], [u"SIMD／SIMT", u"單指令多資料／多執行緒", LS(3)], [u"阿姆達定律", u"序列部分決定平行加速的上限", LS(4)],
            [u"SM", u"串流多處理器，GPU 的基本運算單元群", LS(7)], [u"Tensor Core", u"專做矩陣乘加的單元", LS(7)], [u"warp", u"32 個同步執行的執行緒", LS(8)], [u"佔用率", u"SM 上實際掛著的 warp 比例", LS(8)],
            [u"分支發散", u"同一 warp 走不同分支而必須先後執行", LS(9)], [u"HBM", u"高頻寬記憶體，垂直堆疊的 DRAM", LS(10)], [u"運算強度", u"每位元組的浮點運算次數", LS(11)], [u"Roofline", u"效能上限＝min(峰值, 頻寬×強度)", LS(11)],
            [u"kernel", u"在 GPU 上平行執行的函式", LS(13)], [u"區塊、網格", u"執行緒的組織層級", LS(14)], [u"合併存取", u"相鄰執行緒讀相鄰位址", LS(15)], [u"共享記憶體", u"區塊內共用的晶片上記憶體", LS(16)],
            [u"tiling", u"切塊載入、重複使用資料", LS(16)], [u"bank 衝突", u"共享記憶體同一 bank 的存取排隊", LS(16)], [u"原子操作", u"不可分割的讀改寫", LS(17)], [u"歸約", u"把許多值合併成一個", LS(17)],
            [u"串流", u"GPU 工作佇列；不同串流可同時執行", LS(18)], [u"GEMM", u"一般矩陣乘法", LS(20)], [u"BF16、FP8", u"AI 常用的低精度格式", LS(21)], [u"FlashAttention", u"IO 感知的注意力演算法", LS(22)],
            [u"NVLink", u"GPU 之間的高速互連", LS(23)], [u"脈動陣列", u"TPU 的矩陣乘法結構", LS(26)], [u"CoWoS", u"台積電的 2.5D 先進封裝", LS(28)],
        ]),
    ],
}

CHEAT = {
    "file": "cuda.html", "title": u"CUDA 速查", "h1": u"CUDA 速查表", "icon": u"🟩",
    "description": u"常用的 CUDA 語法與內建變數",
    "body": [
        ("t", [u"語法", u"意思"], [
            [u"__global__", u"kernel：由 CPU 啟動、在 GPU 執行"], [u"__device__", u"只能在 GPU 上被呼叫的函式"], [u"__shared__", u"區塊共享記憶體"],
            [u"threadIdx, blockIdx", u"執行緒在區塊中、區塊在網格中的索引"], [u"blockDim, gridDim", u"區塊與網格的大小"], [u"__syncthreads()", u"區塊內的柵欄同步"],
            [u"atomicAdd()", u"原子加法"], [u"cudaMalloc / cudaFree", u"配置／釋放 GPU 記憶體"], [u"cudaMemcpy / cudaMemcpyAsync", u"CPU 與 GPU 之間複製資料"], [u"cudaDeviceSynchronize()", u"CPU 等待 GPU 完成所有工作"],
        ]),
        ("h", u"全域索引的公式"),
        code(u"""
int i = blockIdx.x * blockDim.x + threadIdx.x;          // 一維
int x = blockIdx.x * blockDim.x + threadIdx.x;          // 二維
int y = blockIdx.y * blockDim.y + threadIdx.y;
int blocks = (n + threads - 1) / threads;                // 無條件進位
"""),
    ],
}

REFERENCES = [GLOSSARY, CHEAT]
