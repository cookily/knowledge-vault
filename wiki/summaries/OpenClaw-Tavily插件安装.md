---
title: "OpenClaw Tavily 插件安装"
source: raw/personal/openclaw/
created: 2026-04-30
tags:
  - summary
  - OpenClaw
  - Tavily
---

# 摘要：OpenClaw Tavily 插件安装

## 前提条件

需要龙虾服务能访问国外

## 安装步骤

### 1. 安装插件

```bash
openclaw-cn plugins install openclaw-tavily
```

### 2. 获取 Tavily API Key

访问 https://app.tavily.com/home 注册

### 3. 配置环境变量

文件：`~/.openclaw/.env`

```env
TAVILY_API_KEY=tvly-dev-xxxxxxxx
```

### 4. 重启

```bash
openclaw-cn gateway restart
```

## 来源

[[raw/personal/openclaw/openclaw-cn安装网络搜索插件openclaw-tavily安装配置-已实践.md]]