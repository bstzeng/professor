# -*- coding: utf-8 -*-
"""資訊安全與駭客攻防主題的規格。"""
import sec_a, sec_c, sec_e, sec_ref

TOPIC = {
    "id": "infosec",
    "category": "tech",
    "title": u"資訊安全與駭客攻防",
    "short": u"資訊安全",
    "crumb": u"資訊安全",
    "icon": u"🛡️",
    "description": u"CIA 三要素、威脅模型、攻擊者與資安史、妨害電腦使用罪與負責任揭露；雜湊加鹽、密碼破解與撞庫、MFA 與 Passkey、HTTPS、Session 與 OAuth；"
                   u"OWASP Top 10、SQL 注入、XSS、CSRF、SSRF、存取控制、供應鏈與 API 安全；緩衝區溢位、橫向移動、惡意程式、勒索軟體、DDoS、中間人、物聯網與零日漏洞；"
                   u"釣魚與台灣常見詐騙、Equifax、SolarWinds、Log4Shell、xz 後門、國家級攻擊與隱私；零信任、偵測與應變、滲透測試與 CTF、安全開發、個人資安清單。含密碼強度、雜湊、SQL 注入、XSS 與釣魚辨識等互動模擬。",
}

MODULES = sec_a.MODULES + sec_c.MODULES + sec_e.MODULES
REFERENCES = sec_ref.REFERENCES
