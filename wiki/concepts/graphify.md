---
title: "graphify"
tags:
  - concept
  - AI-tools
  - knowledge-graph
created: 2026-04-30
aliases:
  - "Knowledge Graph"
---

# 概念：graphify

## 定义

一个面向 AI 编码助手的技能（Skill），用于将代码、文档、图片转换为可查询的知识图谱。

## 核心理念

> "相比直接读取原文件，每次查询的 token 消耗可降低 **71.5 倍**"

## 工作原理

**两轮执行模式**：

1. **第一轮 - AST 提取**（确定性，无 LLM）
   - tree-sitter 分析代码结构
   - 提取类、函数、导入、调用图

2. **第二轮 - 语义提取**（需要 LLM）
   - Claude 并行处理文档/论文/图片
   - 提取概念、关系、设计动机

## 聚类算法

**Leiden 社区发现**
- 基于图拓扑结构
- **不需要 embeddings**
- **不需要向量数据库**

## 关系类型

| 标记 | 含义 | 置信度 |
|------|------|--------|
| `EXTRACTED` | 源材料直接找到 | 1.0 |
| `INFERRED` | 合理推断 | 0.0-1.0 |
| `AMBIGUOUS` | 有歧义 | 需复核 |

## 输出产物

| 文件 | 内容 |
|------|------|
| `graph.html` | 可交互图谱 |
| `GRAPH_REPORT.md` | 审计报告 |
| `graph.json` | 持久化图谱 |

## 与 Karpathy 方法的关系

graphify 是对 Karpathy `/raw` 文件夹理念的**工具化实现**，解决了：
- 降低 token 消耗（71.5x）
- 跨会话持久保存
- 区分 EXTRACTED vs INFERRED

## 相关概念

- [[概念/第二大脑]]
- [[概念/AI驱动知识管理]]
- [[概念/Claude-Code-Skills]]
- [[概念/知识库编译流程]]

## 关联说明

graphify 与知识库系统的关联：

| 关联概念 | 关系 |
|----------|------|
| [[概念/第二大脑]] | 都是第二大脑方案的组成部分 |
| [[概念/AI驱动知识管理]] | 提供技术实现手段 |
| [[概念/Claude-Code-Skills]] | graphify 本身就是一个 Claude Code Skill |
| [[概念/知识库编译流程]] | 可作为 Compile 阶段的工具 |

graphify 的 `/graphify .` 命令可以类比为 `compile` 指令，用于构建知识图谱。

## 来源

[[raw/external/网页文章/graphify.md]]