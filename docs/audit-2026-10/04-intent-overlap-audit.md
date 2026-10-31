# 04 — 意图重叠审计（Intent Overlap）

## 一、方法与判据

对审计规格指定的 8 组候选，逐组判断：**意图是否相同 / 大段重复 / 冲突信息 / 各自独立价值**，不预设重复。全部候选页已逐字阅读。

---

## 二、逐组结论

### 组 1：incense-terminology-glossary vs incense-terminology-reference
- **意图**：不同。glossary = **形态术语表**（stick/coil/cone/resin/powder + 香道/合香/隔火焚香/篆香/四般闲事）；reference = **249 词数据集的导航索引**（明确"本页是指引不是字典"）。
- **重复**：仅"隔火焚香"定义在两者都出现（术语级正常重叠）。
- **冲突**：无。
- **独立价值**：glossary 供人读形态词；reference 指向 dataset + 分组方向（材质/香气/形态/技法/工具/文本/制造/地理/文化/掺假）。
- **处理建议**：均 KEEP。目标 URL 不变。**无蚕食。**

### 组 2-4：incense-vs-candles-vs-diffusers（hub）/ incense-vs-essential-oil-diffuser / incense-vs-reed-diffuser-wax-melts
- **意图**：hub = 三法总览 + "要不要烟"单问决策；两篇 article = 分别深挖（香 vs 精油扩香器；香 vs 芦苇扩香器 vs 蜡融）。
- **重复**：三页共享"燃烧 vs 蒸发""natural≠safe""要不要烟"框架（观点复用，非段落复制）。
- **冲突**：无（事实一致：香=燃烧产 PM，扩香器=不燃）。
- **独立价值**：各针对独立关键词与独立决策维度（hub 是入口，article 是深度）。
- **处理建议**：均 KEEP。**唯一建议**：hub 页内链已正确指向两个 spoke，结构健康；可选在 article 页减少对同一"natural≠safe"段的逐页重写（P2 轻度去重，非必要）。

### 组 5：incense-powder-vs-wood-chips vs agarwood-powder-vs-chips（**最接近的一组**）
- **意图**：相近但范围不同。generic 页 = 任意香木（檀/沉/乳香没药）；agarwood 页 = 沉香专属。
- **重复**：两者共用"同材两形 / 表面积决定释放 / 粉=制香、片=品香"框架，段落结构相似度高。
- **冲突**：无。
- **独立价值**：agarwood 页**多出关键增量**——奇楠"研磨即诈骗信号"、CITES、沉香专属掺假筛查（白烟/沉水）。generic 页覆盖乳香没药"泪滴=片"等非沉香材质。
- **处理建议**：均 KEEP。**可选 P2**：generic 页开头加一句"沉香专项见 agarwood-powder-vs-chips"以强化层级（现有已部分互链），避免被误判为近似页。**不合并**（材质范围不同）。

### 组 6：oem-vs-private-label vs oem-private-label-guide
- **意图**：不同。vs 页 = **决策对比**（谁开发产品→控制/速度权衡）；guide 页 = **流程指南**（brief→打样→迭代→量产→包装→QC→文档）。
- **重复**：定义段（OEM vs PL 定义）两页都有，但 vs 页是深度对比、guide 页是流程入口，且 guide 明确"完整对比见 vs 页"。
- **冲突**：无。
- **独立价值**：vs 页给决策框架 + 对比表；guide 页给 brief 清单 + 5 个必问问题 + 项目流程。
- **处理建议**：均 KEEP。目标 URL 不变。

### 组 7：incense-safety-guide vs how-to-burn-incense-safely
- **意图**：不同。safety-guide = **风险枢纽**（火灾+烟雾两大风险 + "natural≠smoke-free" + 何时需谨慎 + 簇目录）；how-to-burn = **操作指南**（按形态的炉具/摆放/熄灭）。
- **重复**：核心安全规则（通风、勿无人看管、散热面）在两页都出现（安全内容合理重复，非关键词蚕食）。
- **冲突**：无。
- **独立价值**：safety-guide 是"为什么"（why），how-to 是"怎么做"（how）。
- **处理建议**：均 KEEP。

### 组 8（规格补列）：incense-smoke-air-quality-evidence vs incense-ventilation-indoor-air vs incense-safety-guide
- **意图**：三者是**证据→缓解→总则**的递进关系。smoke-air-quality = 研究证据（45mg/g vs 10mg/g、PMC 引用）；ventilation = 通风缓解；safety = 总则枢纽。
- **处理建议**：均 KEEP。已正确互链（cluster directory 完整）。

---

## 三、汇总

| 组 | 是否有蚕食 | 建议 |
|---|---|---|
| terminology glossary vs reference | 否 | 均 KEEP |
| vs-candles/diffuser/reed（3） | 否（hub-spoke） | 均 KEEP |
| powder-vs-chips vs agarwood-powder | 轻度结构相似，无蚕食 | 均 KEEP（可选 P2 强化层级） |
| oem-vs-pl vs oem-guide | 否 | 均 KEEP |
| safety-guide vs burn-safely | 否 | 均 KEEP |
| smoke-evidence vs ventilation vs safety | 否（递进） | 均 KEEP |

**结论：8 组候选均无"意图相同 + 大段重复 + 冲突信息"的蚕食问题。** 本站采用的是标准的 hub-and-spoke 与 glossary-vs-index 结构，交叉内链正确。最接近重复的 powder-vs-chips 组仍是"通用 vs 材质专属"的合理分层，不是重复页。

**零合并、零重定向、零 noindex。**
