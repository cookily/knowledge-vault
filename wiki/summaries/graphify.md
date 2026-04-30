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

## 与知识库的关联

| 关联项 | 说明 |
|--------|------|
| [[wiki/summaries/Karpathy 式 AI 知识库搭建指南]] | graphify 解决了 Karpathy 提出的 `/raw` 文件夹问题 |
| [[wiki/summaries/Claude Code 神级开发者 9 个 Skills 推荐]] | graphify 本身就是推荐的 Skills 之一 |
| [[wiki/concepts/第二大脑]] | 作为构建第二大脑的工具 |
| [[wiki/concepts/知识库编译流程]] | 可替代 `/compile` 工作流 |

## 来源

[[raw/external/网页文章/graphify.md]]