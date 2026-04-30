---
title: "Karpathy 式 AI 知识库搭建指南"
source: raw/Karpathy 式 AI 知识库搭建指南：让 Claude Code + Obsidian 成为你的第二大脑 1.md
created: 2026-04-30
tags:
  - summary
  - knowledge-management
  - AI-tools
---

# 摘要

## 核心观点

Karpathy 的方法核心是**让 AI 代替人类做知识整理工作**。不依赖向量数据库和 RAG 架构，直接让 LLM 读写 Markdown 文件。类比软件工程：`raw/` = `src/`（源代码），`wiki/` = `build/`（编译产物）。

## 工具栈

1. **Obsidian** - 本地知识库容器，免费的本地优先笔记应用
2. **Claude Code** - AI 引擎，可直接操作文件夹中的文件
3. **Claudian** - Obsidian 插件，将 Claude Code 以图形化界面接入

## 四阶段工作流

| 阶段 | 功能 | 说明 |
|------|------|------|
| Ingest（摄入） | 收集原始资料 | 使用 Web Clipper 保存网页到 raw/ |
| Compile（编译） | AI 自动整理 | 生成摘要、提取概念、建立索引 |
| Query（查询） | 问答检索 | 通过自然语言提问 |
| Lint（维护） | 定期检查 | 找出不一致、补充链接、更新内容 |

## 关键命令

- `/ingest [url]` - 摄入网页内容
- `/compile` - 编译知识库（自动生成摘要、提取概念、更新索引）
- `/lint` - 健康检查

## 预期效果

- 每周节省 10-15 小时整理时间
- 知识留存率提升 300%
- 不再有"收藏从未阅读"的焦虑

## 三层目录结构

```
knowledge-vault/
├── raw/          # 原始资料（只进不改）
├── wiki/         # 编译产物（LLM 维护）
│   ├── indexes/  # All-Sources.md, All-Concepts.md
│   ├── concepts/ # 概念条目
│   └── summaries/ # 逐篇摘要
├── outputs/      # 运行时输出
├── blog/          # 可发布的博客文章
└── brain/        # 个人目标和模式
```

## 关键概念

- [[概念/AI驱动知识管理]] - 用 AI 代替手动整理
- [[概念/知识库编译流程]] - Ingest → Compile → Query → Lint
- [[概念/第二大脑]] - 让 AI 成为知识管家

## 延伸资源

- Karpathy 原始 Gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Claudian GitHub: https://github.com/YishenTu/claudian