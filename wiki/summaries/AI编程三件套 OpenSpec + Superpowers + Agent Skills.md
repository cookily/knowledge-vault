---
title: "AI 编程三件套：OpenSpec + Superpowers + Agent Skills"
source: 微信公众号 · 前端AI行走
date: 2026-04-29
tags: [summary, clippings, AI编程, 方法论, OpenSpec, Superpowers, Agent Skills, 工作流]
compiled: 2026-05-27
---

# AI 编程三件套：OpenSpec + Superpowers + Agent Skills

## 一句话总结
解决 AI 编程三大痛点（需求漂移/流程失控/纪律缺失）的铁三角工作流：OpenSpec 用文档定 AI、Superpowers 用流程带 AI、Agent Skills 用纪律管 AI。

## 核心内容

### 三件套定位
| 工具 | 解决的问题 | 核心理念 | Stars |
|------|-----------|----------|-------|
| **OpenSpec** | 需求漂移 | Spec-Driven Development | 43.2k |
| **Superpowers** | 流程失控 | Agentic Skills Framework | 169k |
| **Agent Skills** | 纪律缺失 | Skill Lifecycle Management | 24.3k |

### OpenSpec — 用文档定 AI
- `/opsx:propose` → AI 自动生成 proposal.md + specs/ + design.md + tasks.md
- `/opsx:apply` → AI 按 tasks.md 逐条实现
- `/opsx:archive` → 归档变更
- 不是瀑布模型的重文档，是轻量级"写代码前先对齐预期"

### Superpowers — 用流程带 AI（169k Stars）
- 15+ 个可组合技能，覆盖完整 SDLC
- 核心工作流：brainstorming → git-worktrees → writing-plans → subagent-driven-dev → TDD → code-review → finishing-branch
- 子 Agent 并行开发 + 两阶段审查

### Agent Skills — 用纪律管 AI（Addy Osmani 出品）
- 20 个技能覆盖需求→设计→开发→测试→安全→生产
- 7 命令生命周期：init → verify → install → on → off → update → uninstall
- 关键约束：文件≤500行、函数≤50行、分支覆盖率≥80%

### 组合原则
```
OpenSpec（需求层）→ Superpowers（流程层）→ Agent Skills（纪律层）
   说清楚              做对事                 做得好
```
- **顺序执行不可跳跃**：跳过任何一层都会导致对应问题
- **工具互补**：OpenSpec 的 tasks.md 是 Superpowers writing-plans 的输入

## 来源
[[raw/external/微信公众号/AI 编程进阶：三件套 OpenSpec 定方向，Superpowers 带节奏，Agent Skills 守纪律，打造可预测的工程化工作流.md]]

## 相关概念
- [[AI编程三件套工作流]]

## 相关笔记
- [[Claude Code vs Cursor vs Codex]]
- [[Claude Code 神级开发者 9 个 Skills 推荐]]
- [[Skill自进化训练框架 skill-evolver]]
