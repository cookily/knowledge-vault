---
title: "一行命令把杂乱文件变成知识图谱——我的知识库搭建流程"
source: 微信公众号
date: 2026-04-14
tags:
  - summary
  - graphify
  - 知识图谱
  - 知识管理
  - Claude-Code
compiled: 2026-04-30
---

# 一行命令把杂乱文件变成知识图谱

## 一句话总结

把所有文件丢进一个文件夹，`/graphify .` 自动建知识图谱——**不需要提前分类，信息自己找位置**。

## graphify 核心思路：两轮提取

| 轮次 | 内容 | Token 消耗 |
|------|------|------------|
| 第一轮 | AST 解析代码（类、函数、导入、调用图） | 0（纯本地） |
| 第二轮 | 语义提取文档/图片（并行子代理） | 按需 |

**关系类型**：
- `EXTRACTED`：原文直接找到
- `INFERRED`：合理推断（带置信度）
- `AMBIGUOUS`：需人工复核

## 安装与使用

```bash
pip install graphifyy    # 注意：包名两个y
graphify install         # 注册到 Claude Code
```

## 核心命令

| 命令 | 功能 |
|------|------|
| `/graphify .` | 扫描当前目录生成图谱 |
| `/graphify . --update` | 增量更新（SHA256 缓存） |
| `/graphify . --watch` | 后台监听变更 |
| `/graphify query "问题"` | 问两个概念的关系 |
| `/graphify path A B` | 找 A 到 B 的最短路径 |
| `/graphify explain "概念"` | 解释某个节点的所有连接 |
| `graphify hook install` | Git 提交后自动重建 |

## 输出文件

- `graphify-out/graph.html` — 交互式图谱（浏览器打开）
- `graphify-out/GRAPH_REPORT.md` — 文字报告（核心节点、意外连接）
- `graphify-out/graph.json` — 持久化数据（数周后可查询）

## 实战结果（Beacon Ash 游戏项目）

- 471 个文件（180 代码 + 153 文档 + 138 截图）
- → 1394 个节点、1930 条边、193 个社区

**意外发现**：`DOCXSchemaValidator` 连接数比游戏引擎还多——被 docx 和 pptx 两个技能共享，底层 OOXML 验证框架复用。

## 适用场景

✅ 接手陌生项目，快速了解结构
✅ 发现代码和文档之间的隐藏关联
✅ 不需要提前设计分类体系

**不适合**：替代人工思考和总结

## 来源

[[一行命令把杂乱文件变成知识图谱——我的知识库搭建流程]]

## 相关概念

- [[graphify]]
- [[AI驱动知识管理]]
- [[第二大脑]]
