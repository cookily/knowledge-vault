---
title: "OpenClaw 网络搜索 MCP 配置"
source: raw/personal/openclaw/
created: 2026-04-30
tags:
  - summary
  - OpenClaw
  - MCP
  - 网络搜索
---

# 摘要：OpenClaw 网络搜索 MCP 配置

## 前提条件

需要龙虾服务能访问国外

## 安装步骤

### 1. 安装 mcporter

```bash
npm install -g mcporter --registry=https://registry.npmmirror.com
```

### 2. 获取 Tavily API Key

访问 https://app.tavily.com/home 注册获取

### 3. 配置 MCP

```bash
mcporter config add tavily "https://mcp.tavily.com/mcp/?tavilyApiKey=替换为你的key"
```

### 4. 重启 OpenClaw

```bash
openclaw-cn gateway restart
```

## 调试命令

```bash
# 查看已配置的 MCP 服务器
mcporter list

# 查看工具列表
mcporter list tavily --schema

# 测试调用
mcporter call tavily.search query="人工智能最新资讯"
```

## 来源

[[raw/personal/openclaw/openclaw-cn安装网络搜索mcp-已实践.md]]