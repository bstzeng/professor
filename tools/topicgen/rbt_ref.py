# -*- coding: utf-8 -*-
"""機器人與自動駕駛：參考頁——互動實驗室、名詞對照。"""
from rbt_common import RBTLIB, LS, rw

LAB = {
    "file": "lab.html", "title": u"機器人互動實驗室", "h1": u"機器人互動實驗室", "icon": u"🧪",
    "description": u"PID、卡爾曼濾波、逆向運動學、粒子濾波、路徑規劃，以及感測器資料量、算力、功耗、robotaxi 經濟學、人形回本與全球硬體需求計算器",
    "body": [
        ("raw", u"<script>%s</script>" % RBTLIB),
        ("p", u"把課程中的互動工具集中在這裡。前五個是原理，後六個是硬體與產業的計算器。"),
        ("h", u"1. PID 調參（第 11 課）"), rw("pid"),
        ("h", u"2. 卡爾曼濾波（第 18 課）"), rw("kalman"),
        ("h", u"3. 兩軸手臂逆向運動學（第 7 課）"), rw("ik"),
        ("h", u"4. 粒子濾波定位（第 19 課）"), rw("pf"),
        ("h", u"5. A*、Dijkstra 與 RRT（第 24 課）"), rw("plan"),
        ("h", u"6. 感測器資料量（第 37 課）"), rw("sensor"),
        ("h", u"7. 算力與記憶體頻寬（第 35、36 課）"), rw("compute"),
        ("h", u"8. 功耗與電池（第 39 課）"), rw("power"),
        ("h", u"9. Robotaxi 單位經濟學（第 48 課）"), rw("taxi"),
        ("h", u"10. 人形機器人回本期（第 50 課）"), rw("roi"),
        ("h", u"11. 全球硬體需求推算（第 44 課）"), rw("demand"),
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"機器人名詞對照", "h1": u"機器人名詞對照", "icon": u"📖",
    "description": u"控制、感知、AI、硬體與產業名詞的中英對照",
    "body": [
        ("t", [u"中文", u"英文", u"白話解釋", u"課"], [
            [u"感知—規劃—控制", u"sense–plan–act", u"機器人的基本循環", LS(1)], [u"運行設計範圍", u"ODD", u"自駕系統能運作的道路與條件", LS(2)],
            [u"端到端", u"end-to-end", u"從感測輸入直接學到控制輸出", LS(4)], [u"齊次轉換矩陣", u"homogeneous transform", u"把旋轉與平移合成一個矩陣", LS(5)],
            [u"自由度", u"degree of freedom (DoF)", u"可以獨立運動的方向數", LS(6)], [u"正向／逆向運動學", u"forward / inverse kinematics", u"由角度算位置／由位置算角度", LS(7)],
            [u"雅可比矩陣", u"Jacobian", u"關節速度與末端速度的換算表", LS(8)], [u"奇異點", u"singularity", u"某方向速度消失的姿勢", LS(8)],
            [u"零力矩點", u"zero moment point (ZMP)", u"雙足平衡的關鍵點", LS(10)], [u"PID 控制", u"PID control", u"比例、積分、微分控制器", LS(11)],
            [u"狀態空間", u"state space", u"以狀態描述系統的模型", LS(12)], [u"線性二次調節器", u"LQR", u"最佳回授控制", LS(13)],
            [u"模型預測控制", u"MPC", u"滾動預測未來並最佳化", LS(14)], [u"阻抗控制", u"impedance control", u"控制位置與力的關係", LS(15)],
            [u"全身控制", u"whole-body control (WBC)", u"同時協調所有關節", LS(16)], [u"光達", u"LiDAR", u"雷射測距感測器", LS(17)],
            [u"慣性量測單元", u"IMU", u"加速度計加陀螺儀", LS(17)], [u"卡爾曼濾波", u"Kalman filter", u"結合預測與量測的最佳估計", LS(18)],
            [u"粒子濾波", u"particle filter", u"以大量樣本表示不確定性", LS(19)], [u"感測器融合", u"sensor fusion", u"結合多種感測器", LS(20)],
            [u"同時定位與建圖", u"SLAM", u"一邊建地圖一邊定位", LS(21)], [u"鳥瞰圖", u"bird's-eye view (BEV)", u"俯瞰的統一表示", LS(22)],
            [u"佔據網格", u"occupancy grid", u"空間是否被佔據", LS(22)], [u"快速探索隨機樹", u"RRT", u"隨機取樣的路徑規劃", LS(24)],
            [u"加加速度", u"jerk", u"加速度的變化率，影響舒適度", LS(25)], [u"模仿學習", u"imitation learning", u"從示範中學習", LS(28)],
            [u"遙控操作", u"teleoperation", u"人遠端操作機器人收集資料", LS(28)], [u"強化學習", u"reinforcement learning", u"從獎勵中試錯學習", LS(29)],
            [u"模擬到真實", u"sim-to-real", u"把模擬中學到的策略用在真實機器人", LS(29)], [u"領域隨機化", u"domain randomization", u"訓練時隨機改變模擬參數", LS(29)],
            [u"視覺語言動作模型", u"VLA", u"看、懂、做的機器人基礎模型", LS(31)], [u"世界模型", u"world model", u"預測動作後世界的變化", LS(32)],
            [u"資料飛輪", u"data flywheel", u"部署帶來資料、資料帶來更好的產品", LS(33)], [u"物料清單", u"bill of materials (BOM)", u"產品的零件與成本", LS(34)],
            [u"記憶體頻寬", u"memory bandwidth", u"每秒能搬多少資料", LS(36)], [u"諧波減速器", u"strain wave gear", u"小巧精密的高減速比減速器", LS(38)],
            [u"行星滾柱螺桿", u"planetary roller screw", u"把旋轉變直線的高推力螺桿", LS(38)], [u"準直驅", u"quasi-direct drive", u"低減速比、可反向驅動的致動器", LS(38)],
            [u"扭矩密度", u"torque density", u"每公斤致動器的輸出扭矩", LS(38)], [u"功能安全", u"functional safety (ISO 26262)", u"電子系統故障時的安全", LS(40)],
            [u"遠端協助", u"remote assistance", u"人員遠端給無人車建議", LS(42)], [u"萊特定律", u"Wright's law", u"累積產量加倍、成本下降固定比例", LS(43)],
            [u"機器人即服務", u"robots as a service (RaaS)", u"按月或按工時付費使用機器人", LS(50)],
        ]),
    ],
}

REFERENCES = [LAB, GLOSSARY]
