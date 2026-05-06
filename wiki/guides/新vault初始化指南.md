---
title: "新 Vault 初始化指南"
tags: [guide, 个人, 知识库]
created: 2026-05-06
---

# 新 Vault 初始化指南

## 概述

从零开始搭建基于 Karpathy 工作流 + graphify 的知识库。

## Step 1 - 创建目录结构

```bash
mkdir -p raw wiki/summaries wiki/concepts wiki/indexes graphify-out
```

目录说明：
- `raw/` - 存放原始资料（外部文章、个人笔记），只进不改
- `wiki/summaries/` - 编译后的摘要文件
- `wiki/concepts/` - 提取的核心概念
- `wiki/indexes/` - 索引文件
- `graphify-out/` - graphify 生成的图谱输出

## Step 2 - 复制工具文件

复制以下文件到 vault 根目录：

| 文件 | 用途 |
|------|------|
| `compiled-manifest.py` | 编译清单管理，追踪哪些文件已编译 |
| `_populate_manifest.py` | 自动生成/更新清单的脚本 |
| `CLAUDE.md` | 项目级指南，定义编译流程 |

## Step 3 - 创建初始清单

```bash
echo '{"_comment":"compiled manifest","_version":"1.0","entries":{}}' > compiled-manifest.json
```

## Step 4 - 一键初始化命令

合并为一条命令：

```bash
mkdir -p raw wiki/summaries wiki/concepts wiki/indexes graphify-out && \
echo '{"_comment":"compiled manifest","_version":"1.0","entries":{}}' > compiled-manifest.json
```

然后手动复制 `compiled-manifest.py`、`_populate_manifest.py`、`CLAUDE.md` 到 vault 根目录。

## 日常使用

### 编译新文件
1. 把原始资料丢到 `raw/`
2. 说 `/compile` → 技能自动处理
3. 运行 `python _populate_manifest.py` 更新清单
4. 运行 `python compiled-manifest.py check` 确认状态

### 生成知识图谱
```bash
/graphify . --graphml    # 生成 Gephi 可读的图谱
/graphify . --wiki       # 生成 Obsidian 可读的 wiki
```

### 查看编译状态
```bash
python compiled-manifest.py status
python compiled-manifest.py check   # 真实状态，以这个为准
```

> ⚠️ `/compile` 技能的 Step 1 用文件名对比查找未编译文件，仅供参考。
> **清单 `check` 才是真实状态**。

## 工具说明

| 命令 | 作用 |
|------|------|
| `python compiled-manifest.py status` | 查看编译状态 |
| `python compiled-manifest.py check` | 自动化检查待编译文件 |
| `python compiled-manifest.py add <raw> <summary>` | 手动标记已编译 |
| `python compiled-manifest.py remove <raw>` | 移除编译记录 |
| `python _populate_manifest.py` | 增量更新清单（不破坏已有条目） |
| `python compiled-manifest.py reset` | 清空清单（慎用）|

## 相关文档

- [[wiki/guides/Karpathy-Graphify完整工作流指南]]
- [[wiki/concepts/AI驱动知识管理]]
- [[wiki/concepts/第二大脑]]
