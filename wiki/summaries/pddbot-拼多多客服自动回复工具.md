---
title: "pddbot - 拼多多客服自动回复工具"
source: raw/external/github/zhaoytapddbot.md
created: 2026-05-11
tags:
  - summary
  - 拼多多
  - 客服
  - 自动化
  - LangGraph
  - Playwright
---

# 摘要：pddbot - 拼多多客服自动回复工具

## 一句话总结

面向拼多多商家工作台的开源客服消息监听与自动回复工具，基于 Playwright + LangGraph + PySide6，本地运行，数据自主可控。

## 核心内容

- **技术栈**：Python 3.11 · Playwright（浏览器自动化）· PySide6（桌面 GUI）· LangGraph/LangChain（LLM 编排）· SQLite（本地存储）· DeepSeek API
- **工作流程**：监听聊天事件 → 去重 → 会话激活 → 订单上下文 → 规则匹配 → LLM 生成回复 → 发送（或干跑记录）
- **业务阶段**：按咨询、引导核销、执行核销、发资料等阶段切换策略，敏感场景可转人工或静默
- **GUI 管理**：模型配置、商品-资料映射、风控参数、日志查看；支持 `DRY_RUN` 干跑模式和 `BOT_ENABLED` 总开关
- **跨平台**：macOS / Linux / Windows，启动脚本自动安装 uv、创建虚拟环境、安装 Playwright Chromium

## 与商用方案对比

| 维度 | pddbot（开源自建） | 商用方案（阿奇索/旺财等） |
|------|-------------------|-------------------------|
| 费用 | 源码开源（Apache 2.0），仅付 LLM API 费 | 订阅制，约 ¥30/月·店 |
| 数据 | 本地 SQLite，可审计代码 | 闭源，数据依厂商设计 |
| 维护 | 社区自维护，页面改版需自行调整 | 厂商跟进适配 |

## 安全注意

- `storage_state.json`（浏览器登录态）和 `.env` 含敏感信息，勿提交 Git
- 自动化可能触发平台风控，当前版本未实现节流逻辑，需自行评估频率

## 来源

[[raw/external/github/zhaoytapddbot.md]]

## 相关概念

- [[概念/AI驱动知识管理]] - AI 自动化应用的实践案例
