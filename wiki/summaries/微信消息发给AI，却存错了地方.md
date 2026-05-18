---
title: "微信消息发给 AI，却存错了地方：一次 Hermes 路由 Debug 实录"
source: raw/external/微信公众号/微信消息发给 AI，却存错了地方：一次 Hermes 路由 debug 实录.md
created: 2026-05-18
tags:
  - summary
  - Hermes
  - 微信
  - 路由
  - Debug
  - 故障排查
---

# 摘要：微信消息发给 AI，却存错了地方——Hermes 路由 Debug 实录

## 一句话总结

通过微信发指令给 Hermes Agent，行为与终端直接输入不一致——文件存错了库。问题根因是**微信通道进来时上下文与终端不同**，而非 AI 理解能力问题。

## 问题描述

**场景**：本地 Hermes Agent，微信接入，用微信发"日语学习"指令（附带多邻国日语对话）

| 输入方式 | 预期结果 | 实际结果 |
|----------|----------|----------|
| 微信发消息 | 调用 `japanese-learning` skill，按格式存到日语专用库 | 解析正确但文件存到默认 GalaxyMe 库 |
| Hermes 终端直接输入 | 行为完全正常 | 行为完全正常 |

**关键现象**：同一个提示词，终端正常，微信通道就跑偏。

## 根因分析

问题不在 AI，在于**路由层上下文差异**：

- **终端**：完整上下文（当前目录、profile 配置、skill 路径等）全部携带
- **微信通道**：iLink 网关接入后，上下文信息不完整或格式不同

Hermes 拿到的信息不足以判断"日语学习"应该走哪个 skill → fallback 到默认行为 → 文件写到了默认库。

## 解决方案

### 临时方案

在微信消息中**显式包含完整上下文**：
- 指定具体 skill 名称（如"请使用 japanese-learning skill"）
- 指定目标路径（如"存到 ~/knowledge/japanese/"）
- 补充 profile 信息

### 根本解决

微信 iLink 网关配置时，确保与终端 profile 一致：
- 确认 `hermes gateway setup` 用的是正确 profile 启动
- 检查微信通道的 `soul.md` / `memory.md` 是否与终端共享
- 验证 iLink 网关的上下文注入逻辑

### 配置避坑

- 不要在 Hermes 终端里用 prompt 让它自己连微信，会导致终端无限等待（等扫码但二维码未正确渲染）
- 正确方式：直接运行 `hermes gateway setup`，二维码正确显示后再扫码

## 经验总结

| 教训 | 说明 |
|------|------|
| 渠道间行为不一致 | 优先怀疑上下文差异，而非 AI 能力 |
| 微信通道是"弱上下文" | 终端是"强上下文" |
| 跨渠道要验证 | 关键任务在两个通道都测试一遍 |
| iLink 网关配置要小心 | setup 命令会覆盖现有配置 |

## 来源

[[raw/external/微信公众号/微信消息发给 AI，却存错了地方：一次 Hermes 路由 debug 实录.md]]

## 相关概念

- [[wiki/summaries/Hermes Agent 日报 5月11日-18日]] - 飞书 vs 微信稳定性对比
- [[wiki/summaries/Hermes Agent 日报 4月23日-30日]] - Hermes Web UI 替代 Workspace
