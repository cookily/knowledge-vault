---
title: "Hermes Agent 与 Web UI"
tags:
  - concept
  - AI-Agent
  - 开源工具
  - Web界面
created: 2026-04-30
aliases:
  - "Hermes Agent Web UI"
---

# 概念：Hermes Agent 与 Web UI

## Hermes Agent 简介

| 属性 | 值 |
|------|-----|
| 出品方 | Nous Research |
| GitHub Star | 11 万 |
| 协议 | MIT |
| 语言 | Python |

## 核心能力

### 记忆系统
- `MEMORY.md`：环境和经验
- `USER.md`：用户偏好
- 每次会话自动注入

### 自学机制
- 工具调用超过 5 次 → 自动沉淀成「技能」文件
- 下次遇到同类任务直接复用

### 模型支持
- OpenAI、Anthropic、Google、DeepSeek
- OpenRouter、Ollama（本地模型）
- 一条命令切换

## hermes-web-ui

给 Hermes Agent 添加浏览器界面的开源项目。

### 技术栈

| 层级 | 技术 |
|------|------|
| 后端 | Python（无框架） |
| 前端 | 原生 JS（无框架、无构建） |
| 启动方式 | `./start.sh` 三行 |
| 端口 | 8787 |

### 核心功能

1. **流式响应可视化**
2. **工具调用卡片**（可折叠）
3. **危险命令拦截**（`rm -rf` 等）
4. **Token 表盘**（实时成本监控）
5. **会话管理**（项目、标签、归档）
6. **定时任务可视化**
7. **记忆面板**（直接编辑 MEMORY.md）
8. **多 Profile**（独立配置切换）

### 安全机制

- 默认绑 `127.0.0.1`（本地）
- 公网：`HERMES_WEBUI_PASSWORD` 环境变量
- HMAC 签名 Cookie，24 小时有效
- 安全 Header + SRI 哈希

### 手机访问方案

```
Tailscale + Web UI
手机浏览器 → Tailscale IP:8787
流量走 WireGuard 加密
```

## 项目结构

```
server.py      # HTTP 路由 + 认证（约 154 行）
api/
  auth.py      # 密码认证（约 201 行）
  config.py    # 配置热重载（约 1110 行）
  routes.py    # 所有路由（约 2250 行）
  streaming.py # SSE 引擎（约 660 行）
  workspace.py # 文件操作（约 288 行）
static/
  index.html   # HTML 模板（约 600 行）
  style.css    # CSS 主题（约 1050 行）
  ui.js        # DOM 工具（约 1740 行）
  panels.js    # 面板组件（约 1438 行）
tests/         # 961 个测试函数
```

## 相关概念

- [[AI驱动知识管理]]
- [[AI编程工具三巨头对比]]
