---
title: "Skill 自进化训练框架"
tags: [concept, AI训练, Skill, 自进化, 方法论]
created: 2026-05-21
---

# 概念：Skill 自进化训练框架

## 核心定义
借鉴深度学习训练范式，让 AI Skill 自主迭代优化自身的工程化框架。核心思想：Skill 不是手工打磨的工艺品，而是可以被训练、回滚、选优的对象。

## 关键要点

| 要点 | 说明 |
|------|------|
| **Skill = Harness** | Skill 不是 prompt，是系统工程（触发边界+安全规则+一致性+版本兼容） |
| **8 阶段 Loop** | Setup → Review → Ideate → Modify → Commit → Verify → Gate → Log → Loop |
| **三层评测** | L1 快速门卫（秒级/程序检查）→ L2 Dev Eval（分钟级/全量GT）→ L3 Strict Eval（条件触发/holdout+回归） |
| **5 维 AND 门控** | 质量+安全+Token+结构+覆盖，全 YES 才保留，任一 NO 就 revert |
| **分层 mutation** | Layer1 触发词 → Layer2 SKILL.md → Layer3 脚本/references，成本递增 |
| **Trace 驱动诊断** | 原始执行轨迹比摘要效果好 44%（Stanford Meta-Harness 论文） |
| **程序控制 LLM** | 门控函数不通过就 git revert，程序掌握控制流，LLM 只管单点生成 |

## 三大技术支柱

```
Karpathy autoresearch     → 外循环骨架（迭代、回滚、保留）
Stanford Meta-Harness     → Trace 驱动诊断（完整执行轨迹）
Anthropic skill-creator   → 评测引擎（quick_validate + grader + comparator）
```

## 核心认知
- "能跑"只是语法通过，"真的好"是行为 match 数据分布
- Meta-evolution 最大价值：替你跑你永远跑不到的路径
- 每一步都验证：LLM 会偷懒、过拟合、自作主张

## 相关概念
- [[graphify]]
- [[Claude-Code-Skills]]
- [[知识库编译流程]]

## 来源
- [[Skill自进化训练框架 skill-evolver]]
