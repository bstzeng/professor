# -*- coding: utf-8 -*-
import kds_a, kds_ref
TOPIC = {"id": "distributed-systems", "category": "tech",
  "title": u"分散式系統與共識：讓很多台電腦像一台一樣可靠", "short": u"分散式系統與共識", "crumb": u"分散式系統", "icon": u"🌐",
  "description": u"八個謬誤、部分失效、網路分割與不可靠的時鐘；Lamport 時鐘、向量時鐘、NTP 與 TrueTime、因果一致性；主從、多主與無主複製、Quorum、複製延遲、衝突解決與 CRDT；線性一致性、CAP 與 PACELC、最終一致性與一致性光譜；FLP 不可能結果、兩階段提交、Paxos、Raft、拜占庭容錯與區塊鏈共識；分割與一致性雜湊、Saga、Kafka 事件流、Spanner、DynamoDB、etcd 與大規模故障檢討。附 Raft 模擬器、Quorum、邏輯時鐘與兩階段提交四個互動模擬。"}
MODULES = kds_a.MODULES
REFERENCES = kds_ref.REFERENCES
