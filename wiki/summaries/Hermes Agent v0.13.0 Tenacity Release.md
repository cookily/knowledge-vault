---
title: "Hermes Agent v0.13.0 Tenacity Release"
source: 微信公众号 · 李嘉乐的数字花园
date: 2026-05-09
tags: [summary, clippings, Hermes, 版本发布, v0.13.0]
compiled: 2026-05-21
---

# Hermes Agent v0.13.0 Tenacity Release

## 一句话总结
The Tenacity Release（长程运行版）：Kanban 多 Agent 重做上线、/goal 持久目标、Checkpoints v2 重写、会话扛重启、8 个 P0 安全漏洞修复、Google Chat 上线（20 个平台）。

## 核心内容

### 关键更新
1. **多 Agent Kanban 正式上线**：v0.12.0 回滚后完整重做，心跳检测、僵尸 worker 清理、重试预算、幻觉门
2. **/goal 持久目标**：Agent 锚定目标不跑偏，对话轮次严格约束
3. **Checkpoints v2**：单一存储架构 + 剪枝机制 + 磁盘爆满保护
4. **会话扛重启**：Gateway 重启/升级后会话自动恢复，未处理提示词自动保留
5. **8 个 P0 安全漏洞修复**：脱敏默认开启、Discord 跨 guild 绕过（CVSS 8.1）、WhatsApp 默认拒绝陌生人、auth.json TOCTOU 竞态等
6. **Google Chat 上线**：平台数 20 个，通用平台插件 hook
7. **Provider 可插拔**：第三方模型供应商通过 `ProviderProfile` 抽象类直接接入
8. **video_analyze**：多模态视频理解
9. **xAI Custom Voices**：声音克隆 TTS
10. **7 国语言 i18n**：中/日/德/西/法/乌/土
11. **写入即校验**：post-write delta lint（Python/JSON/YAML/TOML）
12. **Cron no_agent 模式**：纯脚本定时任务

### 新模型
- x-ai/grok-4.3、deepseek/deepseek-v4-pro

### 更新方法
```bash
hermes update
```

## 来源
[[raw/external/微信公众号/Hermes Agent v0.13.0 已发布！1分钟速览更新内容.md]]

## 相关笔记
- [[Hermes Agent v0.14.0 Foundation Release]]
- [[Hermes Agent v0.12.0 Curator Release]]
- [[Hermes Agent 日报 5月4日-9日]]
