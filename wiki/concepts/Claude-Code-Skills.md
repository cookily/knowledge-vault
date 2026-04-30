---
title: "Claude Code Skills"
tags:
  - concept
  - Claude-Code
  - tools
created: 2026-04-30
aliases:
  - "Skills"
  - "Claude Code Skills"
---

# 概念：Claude Code Skills

## 定义

Skills 是 Claude Code 的扩展功能模块，通过 `clawhub install` 安装后可增强 AI 的特定能力。

## 分类体系

### 🛠️ 开发提效类

| Skill | 功能 | 适用场景 |
|-------|------|----------|
| github | 操作 GitHub（PR/Issue/CI） | 开发者标配 |
| code-review | 结构化代码审查 | 团队协作 |
| waza | 轻量规范集合 | 个人项目 |
| superpowers | 严格工程化流程 | 中大型项目 |

### 🔍 信息获取类

| Skill | 功能 |
|-------|------|
| multi-search-engine | 多引擎聚合搜索 |
| agent-browser | 真实浏览器操作 |

### 🚀 进化 & 蒸馏类

| Skill | 功能 |
|-------|------|
| self-improving-agent | AI 自我学习改进 |
| proactive-agent | 定时触发自动化 |
| dot-skill | 蒸馏人为 AI |

## 安装方式

```bash
# 安装 clawhub CLI
npm i -g clawhub

# 安装 Skill
clawhub install skill名字
```

## 推荐顺序

1. **github** - 最基础
2. **self-improving-agent** - 长期收益最高
3. **code-review** - 兜底检查
4. **multi-search-engine** - 技术调研

## 核心原则

> 先装能解决每天痛点的，再装看起来有趣的。

## 相关概念

- [[概念/AI驱动知识管理]]
- [[概念/第二大脑]]

## 来源

[[raw/external/微信公众号/Claude Code 神级开发者 9 个 Skills 推荐：别乱装，先装这几类.md]]