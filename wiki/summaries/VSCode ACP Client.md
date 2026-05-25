---
title: "VSCode ACP Client - Agent Client Protocol 客户端"
source: GitHub · formulahendry
date: 2026-05
tags: [summary, clippings, VSCode, ACP, Agent, 开源工具]
compiled: 2026-05-21
---

# VSCode ACP Client

## 一句话总结
VSCode 扩展，通过 Agent Client Protocol（ACP）在编辑器内连接任意 AI 编程 Agent，预置 11 个 Agent 配置。

## 核心内容
- **ACP 协议**：基于 JSON-RPC 2.0 over stdio 的标准协议，统一 Agent 与客户端通信
- **预置 11 个 Agent**：GitHub Copilot、Claude Code、Gemini CLI、Qwen Code、Codex CLI、OpenCode、OpenClaw、Kiro CLI、Hermes Agent 等
- **核心功能**：
  - 多 Agent 切换（单次只激活一个）
  - 会话管理与历史恢复
  - 文件系统读写 + 终端命令执行
  - Thinking 显示、Slash 命令、模式/模型切换
  - 协议流量日志查看
- **相关项目**：ACP UI（跨平台桌面客户端）、WeChat ACP（微信桥接 ACP Agent）
- **GitHub**: https://github.com/formulahendry/vscode-acp

## 来源
[[raw/external/网页文章/formulahendryvscode-acp Agent Client Protocol client for VS Code — connect to any ACP-compatible AI coding agent (Claude, Codex, Copilot, Qwen, Gemini, OpenCode, Kiro, OpenClaw, Hermes and more).md]]

## 相关笔记
- [[MCP 到底是什么]]
- [[Claude Code vs Cursor vs Codex]]
