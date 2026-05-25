---
title: "Kiro 反代免费接入 Claude-Opus 到 Hermes"
source: 微信公众号 · 智能运维前线
date: 2026-05-19
tags: [summary, clippings, Kiro, Hermes, 反代, Claude-Opus]
compiled: 2026-05-21
---

# Kiro 反代免费接入 Claude-Opus 到 Hermes

## 一句话总结
通过 kiro-gateway 反代项目，将 Kiro IDE 的免费 Claude-Opus 额度导出为 OpenAI/Anthropic 兼容 API，接入 Hermes Agent 和 Claude Code 自由使用。

## 核心内容
- **Kiro 免费额度**：一个月 1000 积分，实际消耗不快，接入 Hermes 后加速但仍可控
- **kiro-gateway 项目**：Python 反代服务，支持 OpenAI-compatible 和 Anthropic-compatible API
  - GitHub: https://github.com/jwadow/kiro-gateway
- **认证方式**：读取 `~/.aws/sso/cache/kiro-auth-token.json`，在 `.env` 中配置 `PROXY_API_KEY` 和 `KIRO_CREDS_FILE`
- **Hermes 接入**：`hermes model` → Custom endpoint → `http://localhost:9000/v1`，推荐模型 `claude-opus-4.6`
- **Claude Code 接入**：通过 CC Switch 配置 `localhost:9000`
- **限制**：免费额度有限，4.7 有时限流，推荐 4.6

## 来源
[[raw/external/微信公众号/极客玩法：手把手教反代 Kiro，将免费顶级 Claude-Opus 模型完美注入爱马仕 Hermes.md]]

## 相关笔记
- [[Hermes proxy 订阅转API]]
- [[Hermes Agent v0.14.0 Foundation Release]]
