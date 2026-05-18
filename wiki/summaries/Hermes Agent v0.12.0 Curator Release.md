---
title: "Hermes Agent v0.12.0 The Curator Release"
source: raw/external/微信公众号/Hermes Agent v0.12.0 已发布！1分钟速览更新内容.md
created: 2026-05-18
tags:
  - summary
  - Hermes
  - 版本发布
---

# 摘要：Hermes Agent v0.12.0 The Curator Release

## 一句话总结

v0.12.0 代号 **The Curator release（管家版）**，核心变化：Hermes 现在能自己照顾自己——自动整理 Skill 库、自我改进能力大改、4 家新模型供应商、2 个新聊天平台接入、启动速度提升约 50%。

## 一句话总结

- **Curator**：自动整理 Skill 库的"技能管家"，每 7 天跑一次
- **自我改进**：Memory Nudge、Skill Nudge、Background Review Fork 四引擎升级
- **新平台**：Microsoft Teams、腾讯元宝接入
- **新模型供应商**：4 家（详见社区文档）
- **启动速度**：快约 50%
- **默认技能升级**：ComfyUI、TouchDesigner 升级为默认内置

## Curator（技能管家）详解

时间一长装的 Skill 越来越多，难免重复或长期未用。Curator 默认每 7 天自动执行：

- 给每个 Skill 打分
- 合并功能重复的 Skill
- 清理已无用的 Skill
- 生成报告告知用户操作内容

**这是 Hermes"自我改善"能力的核心体现之一**——从用户被动管理 → 系统主动维护。

## 自我改进四引擎

| 引擎 | 频率 | 作用 |
|------|------|------|
| Memory Nudge | 每 10 轮对话 | 判断值得长期保存的偏好/环境信息 |
| Skill Nudge | 每 10 次工具调用 | 将操作提炼为可复用 Skill |
| Background Review Fork | 对话过程中 | 后台线程审查对话提取知识 |
| Curator | 每 7 天 | 技能库打分/合并/清理 |

## 升级建议

- **强烈建议升级**：Curator 机制对长期使用者价值大
- **升级前备份**：`SOUL.md`、`MEMORY.md`、`skills/` 目录
- **国内用户**：可让 Hermes 帮你切换中文社区镜像

## 来源

[[raw/external/微信公众号/Hermes Agent v0.12.0 已发布！1分钟速览更新内容.md]]
[[raw/external/微信公众号/Hermes Agent v0.12.0 已发布！1分钟速览更新内容 1.md]]

## 相关概念

- [[wiki/summaries/Hermes Agent 日报 5月4日-9日]] - v0.13.0 The Tenacity Release
- [[wiki/summaries/Hermes Agent 日报 5月11日-18日]] - v0.14.0 The Foundation Release
