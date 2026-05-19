---
title: "wx-cli — 让 AI Agent 直接读取本地微信数据"
source: raw/external/微信公众号/终于有人让 Codex 直接读微信了.md
created: 2026-05-19
tags:
  - summary
  - 微信
  - CLI
  - Agent
  - Rust
  - 开源工具
---

# 摘要：wx-cli — 让 AI Agent 直接读取本地微信数据

## 一句话总结

wx-cli（github.com/jackwener/wx-cli）是 Rust 编写的本地微信数据 CLI 工具，通过后台 daemon 持久化解密数据库，支持会话/聊天/搜索/联系人/朋友圈/收藏/公众号文章查询，可一键安装为 Claude Code/Cursor/Codex 的 Agent Skill，让 AI 直接检索和分析你的微信数据。

## 核心内容

### 核心特性

| 特性 | 说明 |
|------|------|
| 零依赖 | 单一 Rust 二进制，一行命令安装 |
| 毫秒级响应 | daemon 持久化解密数据库，mtime 未变则复用缓存 |
| AI 友好 | `history`/`search`/`sessions` 等返回 `{..., meta}` wrapper，含 freshness/source |
| 完全本地 | 数据不出本机，实时解密，无需全量预解密 |
| Agent Skill | `npx skills add jackwener/wx-cli` 一键装到 Claude Code/Cursor/Codex |

### 功能覆盖

| 命令 | 功能 |
|------|------|
| `wx sessions` / `wx unread` / `wx new-messages` | 会话列表、未读、增量消息 |
| `wx history "张三"` / `wx search "关键词"` | 聊天记录、全文搜索 |
| `wx sns-feed` / `wx sns-search` / `wx sns-notifications` | 朋友圈浏览/搜索/互动通知 |
| `wx biz-articles` | 公众号文章推送 |
| `wx contacts` / `wx members "群名"` | 联系人、群成员 |
| `wx favorites` / `wx stats "群名"` | 收藏、聊天统计 |
| `wx export "张三" --format markdown` | 导出聊天记录 |
| `wx attachments` / `wx extract` | 图片附件解密提取 |

### 架构设计

```
wx (CLI) ──Unix socket──▶ wx-daemon (后台进程)
                              │
                    DBCache (mtime 感知复用) + 联系人缓存
```

- daemon 首次解密后将数据库和 mtime 持久化到 `~/.wx-cli/cache/`
- 重启后 mtime 未变则直接复用，无需重解密
- 群聊消息附带稳定身份三件套：`sender_username`(wxid) / `sender_contact_display` / `sender_group_nickname`

### 与同类工具对比

| | wx-cli | ChatLog | WeFlow | wechat-decrypt |
|--|--------|---------|--------|----------------|
| 语言 | Rust | Go | Node.js | Python |
| 架构 | CLI + daemon | Terminal UI | 桌面 GUI | CLI + Web UI |
| 特色 | Agent Skill 一键集成 | MCP SSE 协议 | 朋友圈解密/年度报告 | 企业微信支持 |
| AI 集成 | 原生 Skill | HTTP API + MCP | HTTP API | MCP Server |

### 安全原理

微信 4.x 使用 SQLCipher 4 加密（AES-256-CBC + HMAC-SHA512，PBKDF2 256K 次迭代）。wx-cli 扫描微信进程内存提取 raw key，macOS 用 Mach VM API、Linux 用 `/proc/<pid>/mem`、Windows 用 `ReadProcessMemory`。

## 来源

[[raw/external/微信公众号/终于有人让 Codex 直接读微信了.md]]
[[raw/external/网页文章/jackwenerwx-cli WeChat local data CLI with daemon architecture.md]]

## 相关概念

- [[wiki/summaries/ChatLog 企业微信聊天记录导出]] - 同类工具对比
- [[wiki/summaries/WeFlow 微信聊天记录浏览器]] - 同类工具对比
- [[wiki/summaries/wechat-decrypt 微信数据库解密工具]] - 同类工具对比
