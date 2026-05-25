---
title: "Hermes-Kanban 多代理看板"
tags: [concept, Hermes, 多Agent, 任务管理, 协作]
created: 2026-05-21
---

# 概念：Hermes-Kanban 多代理看板

## 核心定义
基于 SQLite 的持久化任务看板，支持多个 AI Agent 并行协作。任务通过状态机驱动（triage→todo→ready→running→blocked→done），Dispatcher 每 60 秒自动调度。

## 关键要点

| 要点 | 说明 |
|------|------|
| **持久化队列** | SQLite 存储，任务不丢失，Agent 重启后继续执行 |
| **状态机驱动** | triage → todo → ready → running → blocked → done |
| **多 Agent 并行** | Dispatcher 每 60s 扫描 ready 任务分配给 Worker |
| **依赖管理** | Link（父子关系），父任务完成后子任务自动晋升 ready |
| **人工介入** | 任何阶段可评论介入、block/unblock |
| **审计跟踪** | 完整状态流转记录，永远可查 |

## Kanban vs delegate_task

| 维度 | delegate_task | Kanban |
|------|---------------|--------|
| 模式 | 阻塞等待，fire-and-forget | 持久队列，状态机驱动 |
| 恢复性 | 失败就失败 | crash reclaim 支持 |
| 可介入 | 不支持 | 任何阶段可评论 |
| 协作 | 单代理 | 多代理并行/管道 |
| 审计 | 上下文压缩后丢失 | SQLite 持久化 |

## 典型协作流程
```
researcher（调研）→ architect（设计）→ backend（后端）→ frontend（前端）→ reviewer（审查）→ tester（测试）→ deployer（部署）
```

## 核心价值
1. **持久化**：任务不丢失
2. **协作**：管道式多 Agent 协作
3. **透明**：实时日志 + 审计
4. **容错**：block/unblock + crash reclaim + 熔断

## 相关概念
- [[Hermes-Agent与WebUI]]
- [[Skill自进化训练框架]]

## 来源
- [[Hermes Kanban 多代理看板实战]]
- [[Hermes Agent v0.13.0 Tenacity Release]]
