---
title: "Khazix-Skills 横纵对比：HiClaw vs Clawith"
source: raw/external/微信公众号/使用Khazix-Skills对Hiclaw和clawith进行横纵对比.md
created: 2026-05-11
tags:
  - summary
  - HiClaw
  - Clawith
  - 多智能体协作
  - 竞品分析
  - Khazix-Skills
---

# 摘要：Khazix-Skills 横纵对比 HiClaw vs Clawith

## 一句话总结

使用 Khazix-Skills 的横纵分析法对两个多智能体协作平台（HiClaw 和 Clawith）进行深度竞品分析，结论是两者分别代表基础设施层和应用层两种范式，互补而非直接竞争。

## 核心发现

### HiClaw（阿里巴巴 / Higress 团队）
- **架构**：基于 Matrix IM 协议 + K8s Operator，Agent 通过聊天房间协作
- **理念**：Human-in-the-Loop by Default，所有交互在 Matrix 房间中公开可见
- **优势**：多运行时（OpenClaw + CoPaw + Hermes）、凭证隔离（Higress Gateway）、K8s 原生、4,400 stars
- **劣势**：学习曲线陡峭、IM 渠道集成薄弱、企业治理功能不足

### Clawith（DataElem / BISHENG 团队）
- **架构**：Web 应用（React + FastAPI + PostgreSQL），Agent 是"数字员工"
- **理念**：Agent 有自主意识（Aware 系统），触发器驱动自主工作
- **优势**：全渠道集成（7+ 平台）、完整企业治理（RBAC/审批/审计/配额）、快速迭代（62 天 15+ 版本）、3,509 stars
- **劣势**：单运行时限制、封闭性（交互在平台内）

### 综合对比

| 维度 | HiClaw | Clawith |
|------|--------|---------|
| 架构透明度 | 全公开 | 结构化 UI |
| Agent 自主性 | 被调度 | Aware 自主 |
| 企业治理 | 基础 | 完整 |
| 多运行时 | 原生 3 种 | 单一平台 |
| 渠道集成 | Matrix | 全渠道 |
| 部署难度 | K8s 复杂 | 简单统一 |

## 横纵分析法应用

- **纵向（历时）**：追溯两个项目从诞生到当前版本的演进路线，揭示团队基因如何塑造产品
- **横向（共时）**：6 个维度的竞争图谱对比
- **横纵交汇**：历史根源解释当前优势/劣势，推演三种未来剧本

## 来源

[[raw/external/微信公众号/使用Khazix-Skills对Hiclaw和clawith进行横纵对比.md]]

## 相关概念

- [[概念/横纵分析法]] - 本文使用的分析方法论
- [[wiki/concepts/编译工具对比]] - 提到 Hermes 和 Skills 生态
