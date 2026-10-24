# -*- coding: utf-8 -*-
"""用 Python 做數值模擬主題的規格。產生頁面時會把 Python 範例複製到 topics/numerical-simulation/py/ 並打包成 zip。"""
import io
import os
import shutil
import zipfile
import nsm_a, nsm_e, nsm_ref
from nsm_common import PYDIR, PUBLISH

TOPIC = {
    "id": "numerical-simulation",
    "category": "math",
    "title": u"用 Python 做數值模擬：從差分到蝕刻腔與游泳池",
    "short": u"Python 數值模擬",
    "crumb": u"數值模擬",
    "icon": u"🌊",
    "description": u"從零開始用 Python 做數值模擬，每課完整推導、每支程式都實際執行：誤差、驗證與確認、NumPy／SciPy／Matplotlib／Numba；"
                   u"有限差分、熱傳導與波動方程式、穩定性與 CFL、邊界條件、稀疏矩陣、網格加密；Navier–Stokes、投影法、方腔流與 Ghia 基準、渦度–流函數、晶格波茲曼法。"
                   u"兩個案例：電漿蝕刻腔（氣流、軸對稱、晶圓溫度、自由基與均勻度、Knudsen 數、設計比較）與游泳池水面波紋（色散、反射干涉、頻譜法、互動水池、池底焦散、效能）。",
}

MODULES = nsm_a.MODULES + nsm_e.MODULES

REFERENCES = nsm_ref.REFERENCES


def _publish():
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "topics", TOPIC["id"], "py")
    if os.path.isdir(out):
        shutil.rmtree(out)
    os.makedirs(out)
    for n in PUBLISH:
        shutil.copyfile(os.path.join(PYDIR, n + ".py"), os.path.join(out, n + ".py"))
    readme = (u"用 Python 做數值模擬：課程範例\n\n"
              u"需要 Python 3.9 以上：pip install numpy scipy matplotlib（numba 可選）。\n"
              u"每支程式都可以單獨執行：python 檔名.py\n\n"
              u"蝕刻腔：先 python chamber_lbm.py（產生 chamber_flow.npz），再 python chamber_species.py；chamber_design.py 會自己重算流場。\n"
              u"互動水池：python pool_live.py（有螢幕時會開視窗，點水面滴水）。\n")
    with zipfile.ZipFile(os.path.join(out, "numerical-simulation-examples.zip"), "w", zipfile.ZIP_DEFLATED) as z:
        def add(name, data):
            info = zipfile.ZipInfo("numerical-simulation/" + name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, data)
        add("README.txt", readme.encode("utf-8"))
        for n in PUBLISH:
            add(n + ".py", io.open(os.path.join(PYDIR, n + ".py"), "rb").read())


_publish()
