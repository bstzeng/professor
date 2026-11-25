# -*- coding: utf-8 -*-
from kx_base import table, guide
import kcv_a as C
REFERENCES = [table(u"速查表", u"電腦視覺速查表", u"方法、模型年表、任務與指標", [
  (u"經典方法", [u"方法", u"年份", u"用途"], [[u"Sobel", u"1968", u"梯度"], [u"Otsu", u"1979", u"自動二值化門檻"], [u"RANSAC", u"1981", u"抵抗離群值的模型估計"], [u"Lucas–Kanade", u"1981", u"光流"], [u"Canny", u"1986", u"邊緣偵測"], [u"Harris", u"1988", u"角點"], [u"SIFT", u"1999", u"尺度不變特徵"], [u"Viola–Jones", u"2001", u"即時人臉偵測"]]),
  (u"深度學習年表", [u"年份", u"模型", u"貢獻"], [[u"1998", u"LeNet-5", u"CNN 辨識手寫數字"], [u"2012", u"AlexNet", u"深度學習革命"], [u"2015", u"ResNet", u"殘差連接"], [u"2015", u"U-Net", u"分割"], [u"2016", u"YOLO", u"即時偵測"], [u"2020", u"ViT、NeRF、DETR", u"Transformer 視覺、神經渲染"], [u"2021", u"CLIP、MAE", u"圖文對齊、遮罩自監督"], [u"2023", u"SAM、3D Gaussian Splatting", u"分割基礎模型、即時重建"]]),
  (u"任務與指標", [u"任務", u"輸出", u"常用指標"], [[u"分類", u"類別", u"Top-1 / Top-5 準確率"], [u"偵測", u"邊界框", u"IoU、mAP"], [u"分割", u"每像素類別或遮罩", u"mIoU"], [u"姿態", u"關鍵點", u"PCK、OKS"], [u"追蹤", u"帶編號的軌跡", u"MOTA、IDF1"]]),
  (u"公式", [u"名稱", u"公式"], [[u"立體深度", u"Z = f · B ÷ d"], [u"光流", u"Iₓu + I_yv + Iₜ = 0"], [u"Hough 直線", u"ρ = x cos θ + y sin θ"], [u"IoU", u"交集面積 ÷ 聯集面積"]]),
]), guide(u"互動實驗室", u"電腦視覺互動實驗室", [(u"卷積核（第 4 課）", C.CONV), (u"邊緣偵測（第 5 課）", C.EDGE), (u"IoU 與 NMS（第 18 課）", C.IOU), (u"立體視覺（第 24 課）", C.STEREO)], C.KCVLIB, u"本課程的四個互動模擬")]
