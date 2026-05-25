---
title: "Hermes Kanban 多代理看板实战"
source: 微信公众号 · AIGClaw（阿飞）
date: 2026-05-16
tags: [summary, clippings, Hermes, Kanban, 多Agent, 协作]
compiled: 2026-05-21
---

# Hermes Kanban 多代理看板实战

## 一句话总结
Hermes Kanban 是基于 SQLite 的持久化任务看板，支持多 Agent 并行协作，任务状态机驱动（triage→todo→ready→running→blocked→done），每 60 秒自动调度分配。

## 核心内容

### 核心概念
| 概念 | 说明 |
|------|------|
| Board（看板） | 独立任务队列，支持多项目隔离 |
| Task（任务） | 卡片，状态流转：triage→todo→ready→running→blocked→done |
| Worker | 被调度器 spawn 的代理进程，有独立执行环境和持久记忆 |
| Dispatcher | 每 60 秒扫描 ready 任务分配给 Agent |
| Link（链接） | 父子依赖，父任务完成后子任务自动晋升 ready |

### Kanban vs delegate_task
- delegate_task：阻塞等待，fire-and-forget，单代理
- Kanban：持久队列，状态机驱动，多代理并行，可人工介入，SQLite 审计

### 典型应用场景
需求分析（researcher）→ 架构设计（architect）→ 后端开发（backend）→ 前端开发（frontend）→ 代码审查（reviewer）→ 测试（tester）→ 部署（deployer）

### 操作入口
- 命令行：`hermes dashboard` → WebUI（http://127.0.0.1:9119）
- 支持创建 Agent、分配任务、查看工作日志、手动介入

### 核心价值
1. **持久化**：任务不丢失，Agent 重启后继续执行
2. **协作**：多 Agent 管道式协作，依赖自动管理
3. **透明**：实时日志、完整审计跟踪
4. **容错**：block/unblock、crash reclaim、熔断机制

## 来源
[[raw/external/微信公众号/AI 团队协作新方式：Hermes Agent Kanban 多代理看板实战.md]]

## 相关笔记
- [[Hermes Agent v0.13.0 Tenacity Release]]
- [[Hermes Agent 日报 5月11日-18日]]
- [[Hermes Agent 日报 5月4日-9日]]
