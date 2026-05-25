---
title: "Hermes Agent v0.14.0 Foundation Release"
source: 微信公众号 · 李嘉乐的数字花园
date: 2026-05-17
tags: [summary, clippings, Hermes, 版本发布, v0.14.0]
compiled: 2026-05-21
---

# Hermes Agent v0.14.0 Foundation Release

## 一句话总结
The Foundation Release（基石版本）：PyPI 一键安装、Windows 原生支持、启动快约 19 秒、浏览器工具 180 倍加速、LSP 语义诊断、供应链安全扫描、会话迁移、22 个消息平台。

## 核心内容

### 数据概览
808 次提交 | 633 合并 PR | 1,393 文件变更 | 165,061 行代码 | 545 Issue 关闭 | 12 P0 + 50 P1 | 215 贡献者

### 关键更新
1. **Windows 原生支持**（early beta）：cmd.exe/PowerShell、MinGit 自动安装、40+ Windows 修复
2. **PyPI 安装**：`pip install hermes-agent` + `hermes` 直接可用
3. **性能提升**：冷启动 -19 秒、browser_console 180 倍加速（持久 WebSocket）
4. **依赖懒加载**：按需安装/加载 + 供应链安全检查器
5. **LSP 语义诊断**：write_file/patch 后自动运行 language server 检查类型错误/未定义变量
6. **/handoff**：会话迁移到另一个 model/persona/profile，保留完整上下文
7. **跨会话 prompt cache**：system prompt/skills/memory 跨会话复用 1 小时
8. **hermes proxy**：本地 OpenAI-compatible endpoint，复用 Claude/ChatGPT/Grok 订阅
9. **22 个消息平台**：新增 LINE、SimpleX、Microsoft Graph/Teams
10. **9 个新 Skill**：Hyperliquid、Yahoo Finance、API 测试、EVM 多链等
11. **安全加固**：12 P0 + 50 P1（sudo 暴力破解拦截、SSRF 加固、Dashboard API 鉴权）

### 更新方法
```bash
hermes update
# 或新安装：
pip install hermes-agent
```

## 来源
[[raw/external/微信公众号/Hermes Agent v0.14.0 已发布！1分钟速览更新内容.md]]

## 相关笔记
- [[Hermes Agent v0.13.0 Tenacity Release]]
- [[Hermes Agent 日报 5月11日-18日]]
- [[Hermes proxy 订阅转API]]
