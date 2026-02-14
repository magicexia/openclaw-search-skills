# 学术搜索使用示例

本文件提供学术检索功能的详细使用示例。

## 目录

- [基础学术搜索](#基础学术搜索)
- [按期刊类型搜索](#按期刊类型搜索)
- [学术对比分析](#学术对比分析)
- [最新研究动态](#最新研究动态)
- [引用与被引分析](#引用与被引分析)
- [参数组合示例](#参数组合示例)

---

## 基础学术搜索

### 示例 1：搜索特定论文

```bash
# 搜索 Transformer 架构的原始论文
python3 search-layer/scripts/search.py \
  "Transformer attention is all you need" \
  --mode deep \
  --intent academic \
  --num 10
```

**输出示例：**
```
1. Attention Is All You Need [arxiv.org] ⭐0.95
   https://arxiv.org/abs/1706.03762
   We propose a new simple network architecture, the Transformer...
```

### 示例 2：搜索特定研究领域

```bash
# 搜索机器学习在材料科学中的应用
python3 search-layer/scripts/search.py \
  "machine learning materials science" \
  --mode deep \
  --intent academic \
  --domain-boost nature.com,science.org,arxiv.org \
  --freshness py
```

---

## 按期刊类型搜索

### 示例 3：顶级期刊搜索

```bash
# 仅搜索 Nature 和 Science 发表的研究
python3 search-layer/scripts/search.py \
  "CRISPR gene editing" \
  --mode deep \
  --intent academic \
  --domain-boost nature.com,sciencemag.org,cell.com \
  --num 15
```

### 示例 4：预印本搜索

```bash
# 搜索 arXiv 最新预印本
python3 search-layer/scripts/search.py \
  "quantum computing" \
  --mode deep \
  --intent academic \
  --domain-boost arxiv.org \
  --freshness pm
```

### 示例 5：会议论文搜索

```bash
# 搜索 IEEE 会议论文
python3 search-layer/scripts/search.py \
  "neural networks computer vision" \
  --mode deep \
  --intent academic \
  --domain-boost ieee.org,ieeexplore.ieee.org,acm.org \
  --num 10
```

---

## 学术对比分析

### 示例 6：两种方法的学术对比

```bash
# 对比 BERT 和 GPT 模型的学术研究
python3 search-layer/scripts/search.py \
  "BERT vs GPT language models comparison" \
  --mode deep \
  --intent comparison \
  --freshness py
```

### 示例 7：不同期刊的同类研究

```bash
# 对比 Nature 和 Cell 发表的结构生物学研究
python3 search-layer/scripts/search.py \
  "structural biology cryo-EM" \
  --mode deep \
  --intent academic \
  --domain-boost nature.com,cell.com,science.org \
  --num 10
```

---

## 最新研究动态

### 示例 8：追踪最新研究进展

```bash
# 搜索过去一个月的化学合成突破
python3 search-layer/scripts/search.py \
  "organic synthesis breakthrough" \
  --mode deep \
  --intent status \
  --freshness pm
```

### 示例 9：领域发展趋势

```bash
# 搜索可持续能源研究的最新趋势
python3 search-layer/scripts/search.py \
  "sustainable energy research trends 2025" \
  --mode deep \
  --intent exploratory \
  --freshness py \
  --num 15
```

---

## 引用与被引分析

### 示例 10：高被引论文搜索

```bash
# 搜索领域内高被引论文
python3 search-layer/scripts/search.py \
  "high impact papers lithium ion battery" \
  --mode deep \
  --intent academic \
  --domain-boost nature.com,sciencemag.org,pubs.acs.org \
  --num 10
```

---

## 参数组合示例

### 示例 11：完整学术搜索

```bash
# 综合搜索：最新 + 高影响力 + 多期刊
python3 search-layer/scripts/search.py \
  "machine learning protein folding" \
  --mode deep \
  --intent academic \
  --freshness py \
  --domain-boost nature.com,cell.com,arxiv.org,science.org \
  --num 20
```

### 示例 12：跨学科搜索

```bash
# 搜索跨学科研究（生物 + 计算机）
python3 search-layer/scripts/search.py \
  "bioinformatics genomics computational biology" \
  --mode deep \
  --intent exploratory \
  --domain-boost ncbi.nlm.nih.gov,pubmed.gov,arxiv.org \
  --num 15
```

### 示例 13：方法学搜索

```bash
# 搜索特定研究方法的论文
python3 search-layer/scripts/search.py \
  "single-cell RNA sequencing methodology" \
  --mode deep \
  --intent academic \
  --freshness py \
  --num 10
```

---

## 高级用法

### 学术关键词扩展

系统会自动扩展学术查询：

| 原始查询 | 扩展查询 |
|----------|----------|
| "AI ethics" | "AI ethics research paper" |
| "neural networks" | "neural networks study publication" |
| "CRISPR" | "CRISPR Cas9 research paper" |

### 期刊名称识别

系统自动识别以下期刊名称并提升权威权重：

| 期刊 | 权威等级 | 域名 |
|------|----------|------|
| Nature | Tier 1 | nature.com |
| Science | Tier 1 | sciencemag.org |
| Cell | Tier 1 | cell.com |
| NEJM | Tier 1 | nejm.org |
| The Lancet | Tier 1 | thelancet.com |

---

## 输出解读

### 评分构成

学术搜索结果的综合评分由以下部分组成：

```
total_score = w_keyword × keyword_match + w_freshness × freshness_score + w_authority × authority_score
```

学术搜索默认权重：
- 关键词匹配：0.2
- 新鲜度：0.1
- 权威性：0.7 ⭐（学术搜索最看重权威性）

### 权威等级标记

| 标记 | 含义 |
|------|------|
| ⭐1.0 | Tier 1 学术平台 |
| ⭐0.8 | Tier 2 学术平台 |
| ⭐0.6 | Tier 3 学术平台 |
| ⭐0.4 | Tier 4 学术平台 |

---

## 常见问题

### Q1: 如何只搜索预印本？

```bash
# 使用 --domain-boost 限定 arxiv.org
python3 search-layer/scripts/search.py "quantum computing" \
  --mode deep \
  --intent academic \
  --domain-boost arxiv.org,biorxiv.org,chemrxiv.org
```

### Q2: 如何找到导师推荐阅读？

```bash
# 搜索经典综述和高被引论文
python3 search-layer/scripts/search.py \
  "review article comprehensive survey" \
  --mode deep \
  --intent academic \
  --domain-boost nature.com,science.org,cell.com \
  --num 10
```

### Q3: 如何搜索特定年份的研究？

```bash
# 搜索 2024-2025 年的研究
python3 search-layer/scripts/search.py \
  "metal organic frameworks" \
  --mode deep \
  --intent status \
  --freshness py
```

---

## 相关资源

- 意图分类指南：`../references/intent-guide.md`
- 域名权威配置：`../references/authority-domains.json`
- 完整参数说明：见 `search.py --help`
