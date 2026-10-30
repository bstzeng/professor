# -*- coding: utf-8 -*-
"""Ontology 深度解析：從亞里斯多德到知識圖譜、LLM 與 Palantir（ont_）。"""
import ont_a, ont_c, ont_f, ont_h, ont_j, ont_ref

TOPIC = {
    "id": "ontology",
    "category": "ai",
    "title": u"Ontology 深度解析：從亞里斯多德到語意網、知識圖譜、LLM 與 Palantir",
    "short": u"Ontology",
    "crumb": u"Ontology",
    "icon": u"🕸️",
    "description": u"「存在的是什麼？」從亞里斯多德的範疇、波菲利之樹、共相之爭，到萊布尼茲、專家系統與格魯伯的定義；類別、屬性、公理、描述邏輯與推理機；RDF、OWL、SPARQL、SHACL 與鏈結資料；BFO、Gene Ontology、schema.org、Wikidata、FIBO；本體工程、企業知識圖譜、GraphRAG 與 LLM 輔助建構；最後深入 Palantir：Gotham、Foundry、物件與動作、AIP、案例與爭議。程式範例以 Python（rdflib、owlready2、pySHACL）為主，附十個互動工具。",
}

MODULES = ont_a.MODULES + ont_c.MODULES + ont_f.MODULES + ont_h.MODULES + ont_j.MODULES
REFERENCES = ont_ref.REFERENCES
