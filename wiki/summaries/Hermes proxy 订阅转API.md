---
title: "Hermes proxy — 一行命令把订阅变成标准 API"
source: raw/external/微信公众号/20刀月费秒变API！Hermes一行命令就能用上Claude、ChatGPT订阅.md
created: 2026-05-19
tags:
  - summary
  - Hermes
  - proxy
  - API
  - Grok
  - OpenClaw
---

# 摘要：Hermes proxy — 一行命令把订阅变成标准 API

## 一句话总结

Hermes Agent v0.14 新增 `hermes proxy` 命令，在本地拉起 OpenAI 兼容 API 端点，通过 OAuth 穿透 ChatGPT Pro/Claude Pro/SuperGrok 订阅额度，零额外成本驱动 Codex CLI、Aider 等全套开发工具，同时 Grok 全面接入 Hermes 和 OpenClaw 生态。

## 核心内容

### hermes proxy 机制

- 本地启动 HTTP 端点，暴露标准 OpenAI 兼容 API 格式
- 推理请求穿透已有 OAuth 授权，走订阅调用额度
- **$20/月 ChatGPT Pro** → 零额外成本跑 Codex CLI（GPT-5.5 代码编写/审查/重构）
- **Claude Pro** → 无缝驱动 Aider / Claude Code
- **SuperGrok** → Grok 4.3 全套能力（文本/语音/图片/视频/音频转录），100 万 token 上下文

### Grok 全面杀入 Agent 生态

- xAI 官方下场，Grok 全套能力栈接入 Hermes（OAuth 认证）
- Grok 4.3 上下文窗口拉到 100 万 token
- 默认开启跨请求 prompt 缓存，重复 system prompt 不重复计费
- xAI 官网发布专门接入指南：`x.ai/news/grok-hermes`
- OpenClaw 5.18 同步修复 Grok OAuth PKCE 兼容问题

### 风险提示

- Claude Max 用户因工作目录遗留 `hermes.md` 文件触发 Anthropic 第三方调用风控，被倒扣 $200.98 API 账单
- 大厂可能的反制：物理限流、修改 ToS

### Hermes v0.14 其他亮点

| 特性 | 说明 |
|------|------|
| 冷启动 | 砍掉 19 秒，重型依赖按需安装 |
| x_search | 原生内置，支持 OAuth + API Key 双通道搜索 𝕏 平台 |
| LSP 语义诊断 | 写文件后强制自动跑 language server，终结"嘴上说加了函数但没保存" |
| /handoff | 活跃会话实时迁移，Claude↔Grok 切换上下文不丢 |
| PyPI 安装 | `pip install hermes-agent` 即装即跑 |

### OpenClaw 5.18

- 100+ bugfix 修复（架构瘦身阵痛期）
- 修复浏览器弹窗操控、上线 Android 实时语音流
- 原生打通 Grok OAuth 认证
- 5.18 发布 4 小时后跟上 5.19 beta（373K star 项目接近 SaaS hotfix 速度）

## 来源

[[raw/external/微信公众号/20刀月费秒变API！Hermes一行命令就能用上Claude、ChatGPT订阅.md]]

## 相关概念

- [[wiki/summaries/Hermes Agent 日报 5月11日-18日]] - v0.14 Foundation Release 详情
- [[wiki/summaries/Hermes Agent v0.12.0 Curator Release]] - Hermes 版本演进
- [[wiki/summaries/Hermes Agent 日报 4月23日-30日]] - GPT-5.5 发布背景
