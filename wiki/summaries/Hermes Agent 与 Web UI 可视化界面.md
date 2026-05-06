---
title: "Hermes Agent 与 Web UI 可视化界面"
source: 微信公众号
date: 2026-04-27
tags:
  - summary
  - AI-Agent
  - Hermes
  - Web-UI
  - 开源工具
compiled: 2026-04-30
---

# Hermes Agent 与 Web UI 可视化界面

## 一句话总结

Hermes Agent 是 11 万 Star 的开源 AI Agent，只有终端；**hermes-web-ui** 给它加了浏览器界面，让高频用户从「敲命令」变成「点鼠标」。

## Hermes Agent 核心能力

| 能力 | 实现方式 |
|------|----------|
| 记忆 | `MEMORY.md` + `USER.md`，每次会话自动注入 |
| 历史 | SQLite 存储，随时检索 |
| 自学 | 工具调用超过 5 次自动沉淀成「技能」 |
| 模型 | OpenAI/Anthropic/Google/DeepSeek/Ollama 一键切换 |
| 定时 | 内置 cron，无需 crontab |
| 触达 | Telegram/Discord/Slack 等 10+ 平台 |

## hermes-web-ui 核心功能

- **流式响应 + 工具调用卡片**：Token 一个个冒出来，工具调用可折叠
- **危险命令拦截**：`rm -rf` 等高危操作弹出四选一确认
- **Token 表盘**：实时显示用量、花费、模型上限
- **会话管理**：项目分组、标签过滤、归档
- **定时任务可视化**：查看、新建、编辑、暂停
- **手机访问**：Tailscale + Web UI，完整工作台搬手机上

## 技术栈亮点

```
后端：纯 Python
前端：原生 JavaScript（无框架、无构建步骤）
启动：./start.sh 三行搞定
端口：http://localhost:8787
```

## 安装方式

1. **本地**：先装 Hermes，再 `python3 bootstrap.py`
2. **Docker**：`docker compose up -d`
3. **远程**：SSH 隧道 `ssh -N -L 8787:127.0.0.1:8787`

## 适用场景

✅ 长期高频用 Hermes
✅ VPS 上跑 Agent 不想开 SSH
✅ 手机上