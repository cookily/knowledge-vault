---
title: "Skill 自进化训练框架 skill-evolver"
source: 微信公众号 · 腾讯云开发者（张思宇）
date: 2026-05-19
tags: [summary, clippings, Skill, 自进化, AI训练, 方法论]
compiled: 2026-05-21
---

# Skill 自进化训练框架 skill-evolver

## 一句话总结
借鉴深度学习训练范式，让 Skill 自己迭代优化自己：8 阶段 Loop + 三层评测 + 5 维 AND 门控 + Trace 驱动诊断，19 轮自进化实现零回滚。

## 核心内容

### Skill-Evolver = 三大技术支柱
- **Karpathy autoresearch**：外循环骨架（迭代试错、回滚、保留）
- **Anthropic skill-creator**：评测引擎底座（quick_validate + grader + comparator）
- **Stanford Meta-Harness**：trace 驱动诊断（完整执行轨迹比摘要效果好 44%）

### 8 阶段 Loop
Phase 0 Setup → Phase 1 Review（读 git log + results） → Phase 2 Ideate（基于 trace 诊断提出改动） → Phase 3 Modify（原子化改动，一句话测试） → Phase 4 Commit → Phase 5 Verify（三层评测） → Phase 6 Gate（5 维 AND 门控） → Phase 7 Log → Phase 8 Loop

### 三层评测
| 层 | 成本 | 频率 | 方式 |
|----|------|------|------|
| L1 快速门卫 | 秒级 | 每轮 | 纯程序检查（结构/安全/格式） |
| L2 Dev Eval | 分钟级 | 每轮 | 全量 dev 集 GT case + 8 种 assertion |
| L3 Strict Eval | ~10 分钟 | 条件触发 | holdout 集 + regression 集 + A/B 对比 |

### 5 维 AND 门控（全 YES 才保留）
1. 质量不退化
2. 安全不降低
3. Token 消耗合理
4. 结构完整性
5. 功能覆盖

### 分层 mutation（成本递增）
Layer 1 改触发关键词 → Layer 2 改 SKILL.md 正文 → Layer 3 改辅助脚本/references

### 实战成果
- 19 轮全 keep、零回滚
- 测试用例 17→31，通过率 100%（71/71 检查点）
- 主文件 1411→557 行（减 60%），拆成 13 个单职责文件
- 客服问答 skill：路径召回从 86% 拉到 98.67%

### 核心认知
- Skill 不是 prompt，是 harness（系统工程）
- LLM 不是好的状态机控制器，程序掌握控制流，LLM 只管单点生成
- Meta-evolution 的价值不是省时间，是替你跑你永远跑不到的路径

## 来源
[[raw/external/微信公众号/让Skill自己训练自己：8阶段Loop、3层评测、5维AND门控，从此实现自进化.md]]

## 相关概念
- [[Skill自进化训练框架]]

## 相关笔记
- [[Claude Code 神级开发者 9 个 Skills 推荐]]
- [[Hermes Agent v0.14.0 Foundation Release]]
