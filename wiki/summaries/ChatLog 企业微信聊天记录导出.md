---
title: "ChatLog — 一键导出企业微信聊天记录的本地分析平台"
source: raw/external/微信公众号/老板监工神器：ChatLog！支持一键监听企业微信聊天记录!.md
created: 2026-05-19
tags:
  - summary
  - 聊天记录
  - 企业微信
  - MCP
  - 数据分析
---

# 摘要：ChatLog — 一键导出企业微信聊天记录的本地分析平台

## 一句话总结

ChatLog（github.com/sjzar/chatlog）是本地运行的聊天记录分析平台，支持微信/企业微信/QQ/Telegram 数据解析，具备词云/时间轴/社交网络可视化，通过 HTTP API + MCP SSE 协议可无缝对接 AI 助手。

## 核心内容

### 核心价值

| 特性 | 说明 |
|------|------|
| 智能洞察 | 自动识别高频词汇、情感走向、活跃时段 |
| 全平台兼容 | 微信 3.x/4.0、企业微信、QQ、Telegram |
| 可视化 | 词云、时间轴图表、社交关系网络 |
| 隐私安全 | 所有数据本地处理，零云端传输 |
| 自动报告 | 一键生成 PDF/Excel 分析报告 |

### 技术特性

- **跨平台**：Windows/macOS 全兼容
- **双模式**：Terminal UI + 命令行
- **多媒体解密**：支持图片、语音等解密
- **多账号管理**

### AI 集成能力

通过 **HTTP API** 和 **MCP SSE 协议**（`http://127.0.0.1:5030/sse`）对接 AI 助手（如 ChatWise），实现：
- 聊天记录查询
- 联系人管理
- 群组数据分析

### 安装方式

- **预编译版本**：`github.com/sjzar/chatlog/releases` 下载即用
- **源码编译**：`go install github.com/sjzar/chatlog@latest`

### 注意事项

- macOS 获取密钥需临时关闭 SIP（`csrutil disable`）
- Windows 推荐使用 Windows Terminal 运行
- 记录不全可通过微信"聊天记录迁移"从手机端导入

## 来源

[[raw/external/微信公众号/老板监工神器：ChatLog！支持一键监听企业微信聊天记录!.md]]

## 相关概念

- [[wiki/summaries/WeFlow 微信聊天记录浏览器]] - 另一款同类工具对比
- [[wiki/summaries/微信消息发给AI，却存错了地方]] - 微信通道上下文路由问题
