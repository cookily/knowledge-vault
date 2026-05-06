---
title: "graphify"
source: https://github.com/safishamsi/graphify
created: 2026-04-30
tags:
  - summary
  - AI-tools
  - knowledge-graph
  - Claude-Code
---

# 摘要：graphify - AI 编码助手知识图谱技能

## 核心功能

将代码、文档、图片转换成可查询的知识图谱。在 Claude Code、Codex 等工具中输入 `/graphify` 即可使用。

## 核心优势

**Token 压缩**：相比直接读取原文件，查询消耗降低 **71.5 倍**

## 工作原理

两轮执行：
1. **AST 提取**：确定性分析代码结构（类、函数、调用图）
2. **语义提取**：Claude 并行处理文档/图片，提取概念和关系

## 聚类方式

- 使用 Leiden 社区发现算法
- **基于图拓扑，不依赖 embeddings**
- 不需要向量数据库

## 输出结构

```
graphify-out/
├── graph.html      # 可交互图谱
├── GRAPH_REPORT.md # 审计报告（god nodes、意外连接）
├── graph.json      # 持久化图谱
└── cache/          # SHA256 缓存
```

## 关系标记

| 标记 | 含义 |
|------|------|
| `EXTRACTED` | 源材料直接找到 |
| `INFERRED` | 合理推断（含置信度） |
| `AMBIGUOUS` | 有歧义，需复核 |

## 安装

```bash
pip install graphifyy && graphify install
```

## 与 Karpathy 方法的关系

> "Andrej Karpathy 会维护一个 `/raw` 文件夹，把论文、推文、截图和笔记都丢进去。graphify 就是在解决这类问题"

## 支持的文件类型

| 类型 | 扩展名 | 提取方式 |
|------|--------|----------|
| 代码 | .py .ts .js .go... | tree-sitter AST |
| 文档 | .md .txt | Claude 提取 |
| 论文 | .pdf | 引文挖掘 |
| 图片 | .png .jpg | Claude Vision |

## 关键命令

```
/graphify .              # 分析当前目录
/graphify ./raw          # 分析指定目录
/graphify query "..."    # 查询图谱
/graphify --wiki         # 生成 wiki
/graphify --obsidian     # 生成 Obsidian vault
```

## 导出到外部工具

### 导出到 Gephi

Gephi 是一款开源的图可视化软件，适合做高级社区分析、布局调优、过滤节点。

**步骤：**
1. 运行命令：
   ```bash
   /graphify <path> --graphml
   ```
2. 打开 `graphify-out/graph.graphml`
3. 在 Gephi 里：
   - 左侧选择 **"Open"** 标签页，加载文件
   - 在 **"概览"** 标签页调整布局（如 ForceAtlas2）
   - 节点颜色按社区区分，社区 ID 存在属性里

---

### 导出到 Neo4j

Neo4j 是一款图数据库，适合做复杂查询、Cypher 脚本、大规模数据管理。

**方式一：导出 Cypher 文件，手动导入**
```bash
/graphify <path> --neo4j
```
生成 `graphify-out/cypher.txt`，然后在终端运行：
```bash
cypher-shell < graphify-out/cypher.txt
```
（需要 Neo4j 已运行，且配置好环境变量或 URI）

**方式二：直接推送到 Neo4j**
```bash
/graphify <path> --neo4j-push bolt://localhost:7687
```
首次运行会提示输入用户名和密码（默认用户名是 `neo4j`）。

> **注意**：推送使用 `MERGE` 语句，重复运行不会产生重复数据，可以安全地重新导入。

**导入后的查询示例（Cypher）：**
```cypher
-- 查看所有节点数量
MATCH (n) RETURN count(n)

-- 查看社区分布
MATCH (n) RETURN n.community, count(n) ORDER BY count(n) DESC

-- 查看某个节点的直接邻居
MATCH (n {id: "某个节点ID"})-[r]-(neighbor) RETURN n, r, neighbor
```

---

### 三种导出格式对比

| 格式 | 工具 | 适合场景 | 难度 |
|------|------|----------|------|
| `--graphml` | Gephi | 交互式可视化、社区分析 | ⭐ |
| `--neo4j` | Neo4j | 复杂查询、脚本化分析 | ⭐⭐ |
| `--neo4j-push` | Neo4j | 直接导入，不想要中间文件 | ⭐⭐ |

## 与知识库的关联

| 关联项 | 说明 |
|--------|------|
| [[wiki/summaries/Karpathy 式 AI 知识库搭建指南]] | graphify 解决了 Karpathy 提出的 `/raw` 文件夹问题 |
| [[wiki/summaries/Claude Code 神级开发者 9 个 Skills 推荐]] | graphify 本身就是推荐的 Skills 之一 |
| [[wiki/concepts/第二大脑]] | 作为构建第二大脑的工具 |
| [[wiki/concepts/知识库编译流程]] | 可替代 `/compile` 工作流 |

## 来源

[[raw/external/网页文章/graphify.md]]