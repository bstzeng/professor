# -*- coding: utf-8 -*-
from kx_base import table, guide
import kem_a as C
REFERENCES = [table(u"速查表", u"嵌入式系統速查表", u"位元操作、週邊與通訊", [
  (u"位元操作", [u"動作", u"C 程式碼"], [[u"設定第 n 位", u"reg |= (1u << n);"], [u"清除第 n 位", u"reg &= ~(1u << n);"], [u"切換第 n 位", u"reg ^= (1u << n);"], [u"檢查第 n 位", u"if (reg & (1u << n))"], [u"寫入多位元欄位", u"reg = (reg & ~(MASK << s)) | (val << s);"]]),
  (u"常用公式", [u"項目", u"公式"], [[u"計時器頻率", u"f_clk ÷ ((PSC+1)(ARR+1))"], [u"PWM 工作週期", u"CCR ÷ (ARR+1)"], [u"ADC 換算", u"V = 讀值 ÷ 2^n × Vref"], [u"ADC 理想 SNR", u"6.02n + 1.76 dB"], [u"LED 限流電阻", u"(Vcc − Vf) ÷ I"], [u"平均電流", u"Σ(電流 × 時間比例)"]]),
  (u"序列通訊比較", [u"", u"UART", u"I²C", u"SPI", u"CAN"], [[u"線數", u"2", u"2", u"3 + CS", u"2（差動）"], [u"時脈", u"非同步", u"同步", u"同步", u"非同步"], [u"多裝置", u"點對點", u"7 位元位址", u"每台一條 CS", u"訊息 ID 仲裁"], [u"速度", u"≤ 數 Mbps", u"100k～1 MHz", u"數十 MHz", u"1 Mbps（FD 更快）"]]),
  (u"ISR 守則", [u"守則", u"原因"], [[u"越短越好", u"不延誤其他中斷"], [u"清除旗標", u"否則一直重入"], [u"共用變數 volatile", u"避免被最佳化"], [u"多位元組共用資料關中斷保護", u"避免競爭條件"], [u"不呼叫 printf、malloc", u"不可重入、太慢"]]),
]), guide(u"互動實驗室", u"嵌入式系統互動實驗室", [(u"按鍵彈跳（第 7 課）", C.BOUNCE), (u"輪詢與中斷（第 8 課）", C.IRQ), (u"PWM（第 10 課）", C.PWM), (u"ADC 量化（第 11 課）", C.ADC)], C.KEMLIB, u"本課程的四個互動練習")]
