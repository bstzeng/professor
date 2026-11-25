# -*- coding: utf-8 -*-
from kx_base import table, guide
import kcg_a as C
REFERENCES = [table(u"速查表", u"電腦圖學速查表", u"管線、公式、貼圖與術語", [
  (u"座標轉換流程", [u"步驟", u"矩陣或運算"], [[u"模型 → 世界", u"模型矩陣 M"], [u"世界 → 視圖", u"視圖矩陣 V（攝影機的反矩陣）"], [u"視圖 → 裁剪", u"投影矩陣 P"], [u"裁剪 → NDC", u"透視除法（除以 w）"], [u"NDC → 螢幕", u"視窗轉換"]]),
  (u"公式", [u"名稱", u"公式"], [[u"點積", u"a·b = |a||b|cos θ"], [u"Lambert 漫反射", u"k_d · max(N·L, 0)"], [u"Phong 鏡面", u"k_s · (R·V)^n"], [u"反射方向", u"R = D − 2(D·N)N"], [u"光線", u"P(t) = O + tD"], [u"線性混合蒙皮", u"v' = Σ wᵢ Mᵢ v"]]),
  (u"貼圖", [u"貼圖", u"用途"], [[u"顏色（albedo）", u"基本顏色"], [u"法線", u"細節凹凸"], [u"粗糙度、金屬度", u"PBR 材質"], [u"AO", u"縫隙陰暗"], [u"陰影貼圖", u"從光源看的深度"], [u"Mipmap", u"縮小時避免閃爍"]]),
  (u"反鋸齒", [u"技術", u"特點"], [[u"SSAA", u"最準、最貴"], [u"MSAA", u"邊緣好、成本適中"], [u"FXAA / SMAA", u"後處理、快但模糊"], [u"TAA", u"跨畫面累積、有殘影"], [u"DLSS / FSR", u"AI 或演算法超解析度"]]),
]), guide(u"互動實驗室", u"電腦圖學互動實驗室", [(u"3D 轉換（第 5 課）", C.XFORM), (u"光柵化（第 9 課）", C.RASTER), (u"Phong 光照（第 15 課）", C.PHONG), (u"迷你光線追蹤器（第 22 課）", C.RAY)], C.KCGLIB, u"本課程的四個互動模擬")]
