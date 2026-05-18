---
title: "Hermes Agent 日报 5月4日-9日"
source: raw/external/微信公众号/Hermes Agent 中文社区日报 5月4日.md
created: 2026-05-18
tags:
  - summary
  - Hermes
  - 社区日报
  - 周汇总
---

# 摘要：Hermes Agent 中文社区日报 5月4日-9日

## 一句话总结

5 月第一周 Hermes v0.13.0（The Tenacity Release）正式发布，核心升级长程运行能力（Kanban 重做、Checkpoint v2、/goal 持久目标），同时社区产出大量实操经验。

## 核心内容

### v0.13.0 The Tenacity Release 重点

- **多 Agent Kanban 正式上线**：v0.12 回滚后重做，支持心跳检测、僵尸 worker 清理、重试预算、幻觉门
- **/goal 持久目标**：设定目标后 Agent 无限循环围绕其工作，不跑题不遗忘
- **Checkpoint v2**：单存储架构 + 剪枝 + 磁盘爆满保护，解决孤儿仓库问题
- **会话扛重启**：Gateway 中途重启自动恢复，未处理提示词自动保留
- **集中修复 8 个 P0 安全漏洞**：sudo 暴力破解拦截、Discord CVSS 8.1 绕过、auth.json TOCTOU 等
- **Google Chat 上线**：平台总数到 20 个，通用平台插件 hook 引入
- **video_analyze**：支持 Gemini 等多模态模型原生视频理解
- **xAI Custom Voices**：声音克隆接入
- **Cron no_agent 模式**：纯脚本定时任务，无需 AI 介入

### 模型选型共识

| 场景 | 推荐模型 | 说明 |
|------|----------|------|
| 日常任务 | DeepSeek-V4-Flash | 成本低，缓存命中高（96%+），亿级 Token 不足 15 元 |
| 复杂推理 | DeepSeek-V4-Pro | 1.6T 参数，适合专业场景 |
| 编程 | GLM-5.1 | 国产编程能力突出；Claude Opus 4.7 综合最佳 |
| Agentic Coding | Claude Code + Opus 4.7 | 垂直场景厂商特调最优 |
| 视觉辅助 | MiMo-V2-Omni / GLM-5V | 识图任务推荐 |

**提示词长度优化**：Token 数控制为 128 倍数 + 3-4 边界余量，缓存命中率可达 98%。

### 记忆与上下文管理

- **分层记忆**：临时存储 → 重要性评估 → 分类日记 → 关键词多跳联想
- **跨会话提示缓存**（v0.14+）：system prompt/skills/memory 前缀跨会话复用 1 小时
- **Hindsight**：导入历史记录注意成本，全文总结易激增 Token
- **Honcho**：默认每轮重复调用，建议改为每 10 轮触发一次

### 协作架构实践

- **推荐分工**：Hermes 担任任务规划+记忆管理，Codex/Claude Code 专注代码执行
- **多模型路由策略**：日常用 V4-Flash，复杂推理用 V4-Pro，Agentic Coding 用 GLM-5.1
- **/resume**：恢复历史对话，解决重启后丢失问题
- **Kanban 工作流**：主 Agent 拆解 → 看板分发 → 子 Agent 独立执行

### 部署与硬件

- **云服务器**：2C2G 即可跑 Hermes + 文本任务；推荐 Linux SSH 隧道
- **Mac M3 Ultra**：DeepSeek-V4-Flash GGUF 推理约 26 token/s
- **RTX 50 系**：nvfp4 量化专为 Blackwell 架构优化
- **vLLM 推测解码**：可提升 1.5-2 倍生成速度
- **Termux**：安卓手机可部署，4GB+ 内存

### 飞书/微信注意事项

- **飞书**：支持图片/语音/文件，比企业微信/个人微信更稳定
- **企业微信**：图片/文件接收异常需修改源码
- **个人微信**：仅支持单聊，暂无法加入群聊
- **飞书长文本**：单条约 30KB（中文约 1 万字），超限需分段发送
- **多 Bot 部署**：每个 Bot 需独立 AppID + Secret，避免配置文件冲突

### 实用工具推荐

| 工具 | 用途 |
|------|------|
| browser-harness | 浏览器自动化，延迟优化显著 |
| Tavily | 替代 DuckDuckGo，1000 次/月免费 |
| Kami | Hermes 输出格式控制 |
| liteLLM | Token 监控比 Hermes 内置更准 |
| AgentKey | 聚合多平台社交数据（Tavily/Serper/Brave/Perplexity） |

## 来源

[[raw/external/微信公众号/Hermes Agent 中文社区日报 5月4日.md]]
[[raw/external/微信公众号/Hermes Agent 中文社区日报 5月5日.md]]
[[raw/external/微信公众号/Hermes Agent 中文社区日报 5月6日.md]]
[[raw/external/微信公众号/Hermes Agent 中文社区日报 5月7日.md]]
[[raw/external/微信公众号/Hermes Agent 中文社区日报 5月8日.md]]
[[raw/external/微信公众号/Hermes Agent 中文社区日报 5月9日.md]]
[[raw/external/微信公众号/Hermes Agent v0.13.0 已发布！1分钟速览更新内容.md]]

## 相关概念

- [[wiki/summaries/Hermes配网关告别模型超时]] - LiteLLM 网关
- [[wiki/summaries/Hermes Agent 与 Web UI 可视化界面]] - Web UI / Workspace
