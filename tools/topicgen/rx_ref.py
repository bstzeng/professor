# -*- coding: utf-8 -*-
"""AI 新藥研發與癌症標靶：參考頁——互動工具箱、資料庫與工具速查、名詞中英對照。"""
from rx_common import RXLIB, LS, rw, EXPR, NET
from rx_c import _TARGETS
from rx_e import _FP, _MPO

GUIDE = {
    "file": "guide.html", "title": u"新藥研發互動工具箱", "h1": u"新藥研發互動工具箱", "icon": u"🧰",
    "description": u"研發漏斗、突變型態、依賴分數、表面抗原、網路傳播、標靶評分卡、AlphaFold 信心、分子指紋、類藥性、虛擬篩選、資料洩漏、主動學習、劑量反應、藥動學、存活曲線",
    "body": [
        ("raw", u"<script>%s</script>" % RXLIB),
        ("p", u"所有互動圖使用教學用的模擬資料，用來理解方法，不代表任何真實基因、藥物或試驗。"),
        ("h", u"1. 研發漏斗（第 2 課）"), rw("funnel"),
        ("h", u"2. 致癌基因與抑癌基因的突變型態（第 6 課）"), rw("lolli"),
        ("h", u"3. 依賴分數分布（第 12、18 課）"), rw("dep"),
        ("h", u"4. 合成致死（第 19 課）"), rw("synleth", a=u"BRCA", b=u"PARP"),
        ("h", u"5. 表面抗原的安全窗（第 13、20 課）"), EXPR,
        ("h", u"6. 網路傳播（第 21 課）"), NET,
        ("h", u"7. 標靶評分卡（第 25 課）"), _TARGETS,
        ("h", u"8. AlphaFold 信心分數（第 28 課）"), rw("af"),
        ("h", u"9. 分子指紋與相似度（第 31 課）"), _FP,
        ("h", u"10. 虛擬篩選富集（第 32 課）"), rw("enrich"),
        ("h", u"11. 資料洩漏（第 22、33 課）"), rw("leak"),
        ("h", u"12. 主動學習（第 36 課）"), rw("al"),
        ("h", u"13. 多目標優化（第 37 課）"), _MPO,
        ("h", u"14. 類藥性規則（第 38 課）"), rw("lip"),
        ("h", u"15. 劑量反應（第 41 課）"), rw("hill"),
        ("h", u"16. 藥動學（第 41 課）"), rw("pk"),
        ("h", u"17. 存活曲線與風險比（第 45 課）"), rw("km"),
    ],
}

RESOURCES = {
    "file": "resources.html", "title": u"資料庫與工具速查", "h1": u"資料庫與工具速查", "icon": u"🗂️",
    "description": u"本課程提到的公開資料庫、平台與軟體工具，以及它們在流程中的位置",
    "body": [
        ("h", u"1. 腫瘤與基因體資料"),
        ("t", [u"名稱", u"內容", u"用在", u"課"], [
            [u"TCGA", u"約 33 種癌症、一萬一千多名病人的多體學與臨床資料", u"找驅動基因、族群比例", LS(11)],
            [u"ICGC／PCAWG", u"國際癌症基因體、全基因體分析", u"非編碼區突變", LS(11)],
            [u"COSMIC", u"體細胞突變目錄、癌症基因普查", u"查突變頻率與已知驅動", LS(11)],
            [u"cBioPortal", u"癌症基因體資料的網頁查詢介面", u"不寫程式查詢與繪圖", LS(51)],
            [u"DepMap", u"一千多株癌細胞的 CRISPR 依賴性、表現、突變", u"依賴性與合成致死", LS(12)],
            [u"GTEx", u"約 50 多種正常組織的 RNA 表現", u"安全性評估", LS(13)],
            [u"人類蛋白質圖譜", u"組織與細胞層次的蛋白質定位", u"表面抗原與安全性", LS(13)],
            [u"CPTAC", u"腫瘤蛋白質體與磷酸化蛋白質體", u"補足 RNA 資料", LS(14)],
            [u"人類細胞圖譜", u"單細胞參考圖譜", u"標靶表現於哪種細胞", LS(14)]]),
        ("h", u"2. 整合、化學與結構"),
        ("t", [u"名稱", u"內容", u"用在", u"課"], [
            [u"Open Targets", u"標靶－疾病證據整合、可處理性、安全性", u"標靶排序", LS(16)],
            [u"ChEMBL", u"化合物對標靶的活性資料", u"訓練 QSAR、找化學起點", LS(16)],
            [u"PubChem", u"化合物與篩選資料", u"化合物資訊", LS(16)],
            [u"PDB", u"實驗解出的生物大分子結構", u"結構導向設計", LS(16)],
            [u"AlphaFold 資料庫", u"兩億多個預測結構", u"沒有實驗結構的標靶", LS(27)],
            [u"ClinicalTrials.gov", u"全球臨床試驗登錄", u"競爭態勢、試驗設計", LS(16)],
            [u"Therapeutics Data Commons", u"ADMET 等機器學習資料集", u"模型比較", LS(38)]]),
        ("h", u"3. 模型與軟體"),
        ("t", [u"名稱", u"類型", u"課"], [
            [u"AlphaFold 2／3、RoseTTAFold、ColabFold", u"結構與複合體預測", LS(27)],
            [u"AlphaMissense", u"錯義變異效應預測", LS(17)],
            [u"ESM-2、ESMFold、ESM3", u"蛋白質語言模型", LS(30)],
            [u"RFdiffusion、ProteinMPNN、AlphaProteo", u"蛋白質設計", LS(40)],
            [u"RDKit", u"化學資訊工具組", LS(52)],
            [u"AutoDock Vina", u"分子對接", LS(32)],
            [u"GROMACS、OpenMM", u"分子動力學", LS(29)],
            [u"FEP（自由能微擾）", u"結合自由能計算", LS(39)],
            [u"AiZynthFinder、ASKCOS", u"逆合成規劃", LS(35)],
            [u"Scanpy、Seurat", u"單細胞分析", LS(52)]]),
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"新藥研發名詞中英對照", "h1": u"新藥研發名詞中英對照", "icon": u"📖",
    "description": u"新藥研發、癌症生物學與 AI 方法的中英名詞",
    "body": [
        ("t", [u"中文", u"英文", u"課"], [
            [u"標靶", u"Drug Target", LS(1)], [u"苗頭化合物", u"Hit", LS(1)], [u"先導化合物", u"Lead", LS(1)], [u"臨床試驗申請", u"IND（Investigational New Drug）", LS(1)],
            [u"上市機率", u"Likelihood of Approval（LOA）", LS(2)], [u"藥物形式", u"Modality", LS(3)], [u"抗體藥物複合體", u"Antibody–Drug Conjugate（ADC）", LS(3)],
            [u"標靶蛋白降解劑", u"PROTAC", LS(48)], [u"癌症特徵", u"Hallmarks of Cancer", LS(5)], [u"致癌基因", u"Oncogene", LS(6)], [u"抑癌基因", u"Tumor Suppressor Gene", LS(6)],
            [u"致癌基因成癮", u"Oncogene Addiction", LS(6)], [u"驅動突變／乘客突變", u"Driver／Passenger Mutation", LS(7)], [u"腫瘤突變負荷", u"Tumor Mutational Burden（TMB）", LS(9)],
            [u"免疫檢查點", u"Immune Checkpoint", LS(9)], [u"腫瘤微環境", u"Tumor Microenvironment", LS(9)], [u"腫瘤異質性", u"Tumor Heterogeneity", LS(10)],
            [u"體細胞突變", u"Somatic Mutation", LS(11)], [u"拷貝數變化", u"Copy Number Alteration", LS(11)], [u"基因效應分數", u"Gene Effect Score", LS(12)],
            [u"共同必需基因", u"Common Essential Gene", LS(12)], [u"選擇性依賴", u"Selective Dependency", LS(18)], [u"單細胞 RNA 定序", u"Single-cell RNA-seq", LS(14)],
            [u"空間轉錄體", u"Spatial Transcriptomics", LS(14)], [u"全基因組關聯研究", u"GWAS", LS(15)], [u"孟德爾隨機化", u"Mendelian Randomization", LS(15)],
            [u"合成致死", u"Synthetic Lethality", LS(19)], [u"旁觀者效應", u"Bystander Effect", LS(20)], [u"網路傳播", u"Network Propagation", LS(21)],
            [u"知識圖譜", u"Knowledge Graph", LS(21)], [u"正例－未標記學習", u"Positive-Unlabeled Learning", LS(22)], [u"資料洩漏", u"Data Leakage", LS(22)],
            [u"可成藥性", u"Druggability", LS(23)], [u"隱藏口袋", u"Cryptic Pocket", LS(29)], [u"回補實驗", u"Rescue Experiment", LS(26)],
            [u"類器官", u"Organoid", LS(26)], [u"病人衍生異種移植", u"Patient-Derived Xenograft（PDX）", LS(26)], [u"預測局部距離差異", u"pLDDT", LS(28)],
            [u"預測對齊誤差", u"Predicted Aligned Error（PAE）", LS(28)], [u"分子動力學", u"Molecular Dynamics", LS(29)], [u"蛋白質語言模型", u"Protein Language Model", LS(30)],
            [u"分子指紋", u"Molecular Fingerprint", LS(31)], [u"分子對接", u"Molecular Docking", LS(32)], [u"富集因子", u"Enrichment Factor", LS(32)],
            [u"定量構效關係", u"QSAR", LS(33)], [u"活性懸崖", u"Activity Cliff", LS(31)], [u"逆合成分析", u"Retrosynthesis", LS(35)],
            [u"主動學習", u"Active Learning", LS(36)], [u"DNA 編碼化合物庫", u"DNA-Encoded Library（DEL）", LS(36)], [u"多目標優化", u"Multi-Parameter Optimization", LS(37)],
            [u"吸收、分布、代謝、排除、毒性", u"ADMET", LS(38)], [u"自由能微擾", u"Free Energy Perturbation（FEP）", LS(39)], [u"互補決定區", u"CDR", LS(40)],
            [u"藥動學／藥效學", u"Pharmacokinetics／Pharmacodynamics", LS(41)], [u"伴隨診斷", u"Companion Diagnostic", LS(42)], [u"液態切片", u"Liquid Biopsy", LS(42)],
            [u"多實例學習", u"Multiple Instance Learning", LS(43)], [u"外部對照組", u"External Control Arm", LS(44)], [u"新抗原", u"Neoantigen", LS(44)],
            [u"整體存活／無惡化存活", u"OS／PFS", LS(45)], [u"風險比", u"Hazard Ratio", LS(45)], [u"新方法學", u"New Approach Methodologies（NAMs）", LS(46)],
            [u"藥物再利用", u"Drug Repurposing", LS(46)]]),
    ],
}

REFERENCES = [GUIDE, RESOURCES, GLOSSARY]
