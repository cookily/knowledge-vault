---
title: "wechat-decrypt — 微信 4.0 本地数据库解密工具集"
source: raw/external/网页文章/ylytdengwechat-decrypt WeChat 4.0 database decryptor - extract keys from memory, decrypt SQLCipher 4 databases, real-time message monitor.md
created: 2026-05-19
tags:
  - summary
  - 微信
  - 数据库解密
  - Python
  - 开源工具
---

# 摘要：wechat-decrypt — 微信 4.0 本地数据库解密工具集

## 一句话总结

wechat-decrypt（github.com/ylytdeng/wechat-decrypt）是跨平台（Windows/macOS/Linux）微信 4.0 + 企业微信 5.x 本地数据库解密工具集，从进程内存提取密钥解密 SQLCipher 4 数据库，支持实时消息监听（Web UI SSE）、批量导出（JSON/CSV/HTML）、图片解密、语音转录、朋友圈导出、MCP Server 接入 Claude AI。

## 核心内容

### 能力矩阵

| 能力 | 说明 |
|------|------|
| 数据库解密 | 个人微信 4.0（SQLCipher 4）+ 企业微信 5.x（wxSQLite3 AES-128） |
| 实时消息监听 | Web UI (SSE) / 命令行 / MCP Server（Claude AI 集成） |
| 批量导出 | 全部聊天→JSON/CSV/HTML，含增量+日期范围+dry-run |
| 图片解密 | V1/V2/wxgf 三种 .dat 格式 + 朋友圈缓存 |
| 语音转录 | SILK→WAV→文本（local Whisper / OpenAI / whisper.cpp） |
| 朋友圈 | SnsTimeLine 解析 + 缓存图片解密 + HTML 时间线 |
| 桌面 GUI | tkinter 界面 + PyInstaller 单 exe 打包 |

### 技术原理

微信 4.0 使用 SQLCipher 4 加密本地数据库：
- **加密**：AES-256-CBC + HMAC-SHA512
- **KDF**：PBKDF2-HMAC-SHA512，256,000 次迭代
- **密钥提取**：扫描进程内存匹配 `x'<64hex_key><32hex_salt>'` 格式

### 平台支持

| 平台 | 密钥提取方式 | 前置条件 |
|------|-------------|---------|
| Windows | 扫描 Weixin.exe 内存 | 管理员权限 + 微信运行中 |
| macOS | C + Mach VM API | ad-hoc 重签名 WeChat.app + root |
| Linux | /proc/\<pid\>/mem | root 或 CAP_SYS_PTRACE |

### MCP Server（Claude AI 集成）

`claude mcp add wechat -- python mcp_server.py` 注册后，20+ 工具可用：`get_chat_history`、`search_messages`、`decode_voice`、`transcribe_voice`、`get_contacts` 等。

### 企业微信支持（实验）

Windows 5.x 企业微信数据库使用 wxSQLite3 AES-128-CBC（非 SQLCipher），需要单独的密钥提取和解密流程。

### 安全注意

- `all_keys.json` 包含明文 raw key，chmod 0600 保护，**勿提交 git 或共享**
- 解密后 `.db` 是明文 SQLite，包含全部联系人/群/消息
- 朋友圈 XML 解析有 XXE 防护

## 来源

[[raw/external/网页文章/ylytdengwechat-decrypt WeChat 4.0 database decryptor - extract keys from memory, decrypt SQLCipher 4 databases, real-time message monitor.md]]

## 相关概念

- [[wiki/summaries/wx-cli 微信本地数据CLI工具]] - 同类工具，wx-cli 致谢本项目
- [[wiki/summaries/ChatLog 企业微信聊天记录导出]] - 同类工具对比
- [[wiki/summaries/WeFlow 微信聊天记录浏览器]] - 同类工具对比
