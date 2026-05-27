---
title: "AI编程三件套工作流"
tags: [concept, AI编程, 工作流, 方法论, OpenSpec, Superpowers]
created: 2026-05-27
---

# 概念：AI编程三件套工作流

## 核心定义
解决 AI 编程三大痛点（需求漂移/流程失控/纪律缺失）的铁三角工作流，三个开源工具各管一层：OpenSpec 管需求、Superpowers 管流程、Agent Skills 管纪律。

## 关键要点

| 要点 | 说明 |
|------|------|
| **三层架构** | 需求层（OpenSpec）→ 流程层（Superpowers）→ 纪律层（Agent Skills） |
| **顺序不可跳** | 跳过需求层→漂移，跳过流程层→混乱，跳过纪律层→质量失控 |
| **工具互补** | OpenSpec tasks.md → Superpowers writing-plans → Agent Skills 约束执行 |
| **Spec-Driven** | 写代码前先对齐预期，不是瀑布重文档，是轻量协议 |
| **子 Agent 并行** | Superpowers 支持每个任务派发独立子 Agent + 两阶段审查 |
| **技能生命周期** | Agent Skills 用 npm 包的方式管理 AI 行为规则（init/verify/install/on/off） |

## 三件套速查

| 工具 | Stars | 核心命令 | 解决什么 |
|------|-------|----------|----------|
| **OpenSpec** | 43.2k | `/opsx:propose` → `/opsx:apply` → `/opsx:archive` | 需求漂移 |
| **Superpowers** | 169k | brainstorming → writing-plans → subagent-dev → TDD → review | 流程失控 |
| **Agent Skills** | 24.3k | `agent-skills install` → `on test-coverage code-structure` | 纪律缺失 |

## 完整工作流
```
① /opsx:propose          ← OpenSpec 生成需求文档
② brainstorming          ← Superpowers 需求澄清
③ /opsx:apply            ← OpenSpec 确认方案
④ writing-plans          ← Superpowers 拆任务
⑤ subagent-driven-dev    ← Superpowers 子 Agent 并行开发
⑥ test-driven-dev        ← Agent Skills 强制 TDD
⑦ requesting-code-review ← Superpowers 代码审查
⑧ /opsx:archive          ← OpenSpec 归档
```

## 相关概念
- [[Claude-Code-Skills]]
- [[Skill自进化训练框架]]
- [[知识库编译流程]]

## 来源
- [[AI编程三件套 OpenSpec + Superpowers + Agent Skills]]
