---
title: "Hermes Agent 日报 4月23日-30日"
source: raw/external/微信公众号/Hermes Agent 中文社区日报 4月23日.md
created: 2026-05-18
tags:
  - summary
  - Hermes
  - 社区日报
  - 周汇总
---

# 摘要：Hermes Agent 中文社区日报 4月23日-30日

## 一句话总结

4 月最后一周 AI 圈大事密集：GPT-5.5 发布、DeepSeek V4 开源、Hermes v0.11 适配新模型，社区同时产出大量实操经验（插件/部署/记忆）。

## 核心内容

### AI 世界要闻

- **GPT-5.5（Spud）发布**：幻觉率较 5.4 降低 60%，SWT-bench 达 88.7%，已上线 ChatGPT 和 Codex
- **DeepSeek V4 Preview**：Pro（1.6T 参数）和 Flash（284B），原生百万 token 上下文，MIT 开源
- **GPT-Image-2**：首个内置推理的图像模型，12 小时内登顶 Image Arena 全品类第一
- **Anthropic Mythos 泄露**：仅限 Amazon/Apple 等少数公司测试的漏洞检测模型遭未授权访问
- **ICLR 2026「推理陷阱」**：模型推理能力越强，工具调用幻觉越严重，Deloitte 调研显示 47% 企业 AI 用户曾基于幻觉做重大决策

### Hermes 生态亮点

- **Nous Portal**：Kimi K2.6（32B MoE，256K 上下文）24 小时限免，Hermes Agent 用户直接 `hermes update` 后切换体验
- **Awesome Hermes Agent 清单**：聚合 98 个社区项目，Atlas 实时监测
- **v0.11.0 发布**：适配 DeepSeek-V4 模型，腾讯 Hy3-Preview 可通过 OpenRouter 调用
- **多 Agent Kanban**（v0.12.0 回滚前）：多 worker 自动认领任务，含心跳检测、僵尸清理、重试预算

### 5 个新插件补日常缝隙

| 插件 | 功能 | 地址 |
|------|------|------|
| hermes-lcm | 对话 DAG 压缩，`lcm_grep`/`lcm_expand` 历史展开 | github.com/stephenschoettler/hermes-lcm |
| hermes-neurovision | 85 种 ASCII 状态仪表盘随工具调用变化 | github.com/Tranquil-Flow/hermes-neurovision |
| supermemory | 知识图谱路线记忆方案，生命周期钩子 | supermemory.ai |
| Hermes WebUI | CLI 搬浏览器，三栏布局+实时 token 用量 | 见中文社区 |
| browser-harness | 浏览器自动化/测试备选方案 | github.com/browser-use/browser-harness |

### 本地部署推荐

- **首选**：Qwen3.5-35B（稳定、吞吐 57 tokens/s、中文好、消费级显卡友好）
- **Qwen3.6-35B-A3B**：实测可玩性高，nvfp4 量化推荐
- **上下文要求**：最小 64K，本地 llama.cpp 需手动配置 `n_ctx` 参数
- **新手建议**：优先用 DeepSeek-V4-Flash 等云端 API，暂不推荐本地部署

### 记忆与技能管理

- **记忆文件**（soul/memory/agent profile）仅用于初始化，真实记忆存向量数据库
- **推荐使用**：Hindsight（每日自动摘要）、memOS（国产，简便）、Honcho（开源，PostgreSQL）
- **预装 90 个 Skill**：多数实用性低，建议禁用大部分以提升稳定性
- **Curator**（v0.12+）：每 7 天自动打分、合并、归档 Skill

### 平台与渠道

- **推荐**：飞书 > 企业微信 > 个人微信（稳定性、API 权限、多媒体支持）
- **Hermes Workspace**：替代 Web UI，支持多 profile 并行管理
- **WSL 注意事项**：输入法兼容性问题；不推荐手动迁移至非系统盘（易崩溃）

## 来源

[[raw/external/微信公众号/Hermes Agent 中文社区日报 4月23日.md]]
[[raw/external/微信公众号/Hermes Agent 中文社区日报 4月24日.md]]
[[raw/external/微信公众号/Hermes Agent 中文社区日报 4月27日 星期一.md]]
[[raw/external/微信公众号/Hermes Agent 中文社区日报 4月28日.md]]
[[raw/external/微信公众号/Hermes Agent 中文社区日报 4月29日.md]]
[[raw/external/微信公众号/Hermes Agent 中文社区日报 4月30日.md]]
[[raw/external/微信公众号/推荐几个最近刚发布的 Hermes Agent 小工具.md]]

## 相关概念

- [[wiki/summaries/Hermes配网关告别模型超时]] - LiteLLM 网关故障转移
- [[wiki/summaries/Hermes Agent 与 Web UI 可视化界面]] - Web UI 功能介绍
