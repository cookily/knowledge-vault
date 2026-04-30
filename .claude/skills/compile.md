---
name: compile
description: Use when organizing raw files from raw/ into summaries and concepts in a knowledge base. Triggers after ingesting new articles, notes, or external content that needs to be compiled into structured knowledge.
---

# 知识库编译流程

## 概述

将 `raw/` 中的原始资料编译成结构化知识库文件。输入是未整理的笔记/文章，输出是摘要和概念文件。

## 何时使用

- 原始资料存入 `raw/` 后
- 需要将外部文章整理到知识库时
- 知识库缺乏系统性整理时

## 编译流程

### 1. 扫描待处理文件

```bash
# 列出 raw/ 下所有 md 文件
glob "raw/**/*.md"

# 列出已编译的摘要（用于对比）
glob "wiki/summaries/*.md"
```

对比两个列表，找出未编译的文件。

### 2. 生成摘要文件

写入 `wiki/summaries/{处理后的文件名}.md`

**Frontmatter 模板**：
```yaml
---
title: "文件标题"
source: 来源（微信公众号/个人笔记/网页文章等）
date: 原文件日期
tags: [summary, 相关标签]
compiled: 2026-04-30
---
```

**内容结构**：
```markdown
# 文件标题

## 一句话总结
提取核心观点，一句话说清楚。

## 核心内容
- 要点1
- 要点2
- 要点3

## 来源
[[原始文件链接]]
```

### 3. 决定是否提取概念

**需要提取概念的情况**：
- 方法论、框架、理念类文章
- 可复用的设计模式或最佳实践
- 技术原理深度解析

**不需要提取概念的情况**：
- 操作手册、配置记录
- 一次性问题解决
- 碎片化笔记

**概念文件**写入 `wiki/concepts/{概念名}.md`：
```yaml
---
title: "概念名称"
tags: [concept, 相关标签]
created: 2026-04-30
---

# 概念：概念名称

## 核心定义
什么是这个概念。

## 关键要点
| 要点 | 说明 |
|------|------|
| ... | ... |

## 相关概念
- [[相关概念1]]
- [[相关概念2]]
```

### 4. 更新索引

**All-Sources.md**：追加到对应日期分组下
```markdown
| [[摘要文件名]] | 来源 | #clippings | 一句话描述 |
```

**All-Concepts.md**（仅当创建了新概念时）：
```markdown
| [[wiki/concepts/xxx.md]] | #concept #标签 | 描述 |
```

### 5. 建立交叉链接

在摘要和概念文件中相互链接：
- 摘要 → 来源文件
- 摘要 → 相关概念
- 概念 → 相关概念
- 概念 → 来源摘要

## 文件名规范

**规则**：
- 去掉 `、`（顿号）、`，`（逗号）等特殊符号
- 用 `vs` 代替顿号
- 空格保留
- 去掉开头/结尾的特殊符号

**示例**：
| 原始文件名 | 编译后文件名 |
|------------|--------------|
| Claude Code、Cursor 和 Codex，到底选哪个？ | Claude Code vs Cursor vs Codex |
| 从Alibaba-Cola到DDD... | DDD领域驱动设计 |

## 快速参考

| 步骤 | 操作 |
|------|------|
| 1. 扫描 | glob raw/ → glob wiki/summaries/ → 对比 |
| 2. 读文件 | Read 原始文件 |
| 3. 写摘要 | Write wiki/summaries/{文件名}.md |
| 4. 判断概念 | 方法论/框架类 → 创建概念；操作手册 → 跳过 |
| 5. 更新索引 | Edit All-Sources.md / All-Concepts.md |
| 6. 建链接 | 摘要↔概念↔来源 互相链接 |

## 常见错误

| 错误 | 正确做法 |
|------|----------|
| 文件名含顿号/逗号 | 去掉或用 `vs` 替代 |
| 每个文件都创建概念 | 只对方法论/框架类提取概念 |
| 追加到索引末尾 | 按日期分组插入到对应位置 |
| 忘记链接来源 | 摘要必须链接原始文件 |
