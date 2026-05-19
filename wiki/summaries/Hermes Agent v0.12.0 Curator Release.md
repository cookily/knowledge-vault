---
title: "Hermes Agent v0.12.0 The Curator Release"
source: raw/external/微信公众号/Hermes Agent v0.12.0 已发布！1分钟速览更新内容.md
created: 2026-05-18
tags:
  - summary
  - Hermes
  - 版本发布
---

# 摘要：Hermes Agent v0.12.0 The Curator Release

## 一句话总结

v0.12.0 代号 **The Curator release（管家版）**，核心变化：Hermes 现在能自己照顾自己——自动整理 Skill 库、自我改进能力大改、4 家新模型供应商、2 个新聊天平台接入、Spotify/Google Meet 内置、启动速度提升约 57%，合入 360 个 bug 修复。

## 核心亮点

### Curator（技能管家）

时间一长装的 Skill 越来越多，难免重复或长期未用。Curator 默认每 7 天自动执行：

- 给每个 Skill 打分
- 合并功能重复的 Skill
- 清理已无用的 Skill
- 生成报告告知用户操作内容

内置核心 Skill 有保护不会被误删。`hermes curator status` 查看使用情况。

### 自我改进四引擎

| 引擎 | 频率 | 作用 |
|------|------|------|
| Memory Nudge | 每 10 轮对话 | 判断值得长期保存的偏好/环境信息 |
| Skill Nudge | 每 10 次工具调用 | 将操作提炼为可复用 Skill |
| Background Review Fork | 对话过程中 | 后台线程审查对话提取知识 |
| Curator | 每 7 天 | 技能库打分/合并/清理 |

**v0.12 改进**：改为评分卡打分（不再自由发挥）、优先更新刚用过的 Skill、后台进程正确继承主进程模型和账号、只允许改记忆和 Skill 不再误用 shell。

### 新 Skill 生态

| Skill | 变化 |
|-------|------|
| ComfyUI v5 | 从可选升级为默认内置 |
| TouchDesigner-MCP | 默认内置，新增 9 篇参考文档 |
| Humanizer | 把 AI 腔文字洗成正常人话 |
| claude-design | 生成 HTML 演示页 |
| design-md | 写 DESIGN.md 规范文档 |
| airtable | 接 Airtable |
| pretext | 浏览器创意演示 |
| spike + sketch | 一次性实验脚本和静态 HTML 原型 |

新能力：可从 HTTP 链接直接安装 Skill；新增 `/reload-skills` 热加载。

### 新模型供应商

| 路径 | 说明 |
|------|------|
| GMI Cloud | 一等 API key 接入 |
| Azure AI Foundry | 自动检测、完整接入 |
| MiniMax OAuth | 浏览器一键登录 |
| 腾讯 Tokenhub | 新接入 |

LM Studio 升级为正式 provider（专属鉴权、`hermes doctor` 检查、实时拉模型列表）。

### 新聊天平台

- **Microsoft Teams**：第 19 个平台，走"插件"机制接入
- **腾讯元宝**：第 18 个平台，文字 + 媒体

其他改进：Telegram/Discord/Slack/Mattermost/邮件/Signal 统一支持原生多图发送；Signal 支持 markdown 渲染、引用回复、表情反应。

### Spotify + Google Meet

- **Spotify**：7 个工具（播放/搜索/队列/歌单/设备控制），浏览器一键登录，支持 cron 定时
- **Google Meet**：加入会议/转录/发声/跟进，整套流水线打包成插件

### CLI 改进

- `hermes -z <提示词>`：跑完退出，不进交互模式
- `hermes update --check`：升级前预检
- `hermes fallback`：管理回退 provider
- 升级时可自动备份 HERMES_HOME

### TUI 与 Dashboard

- **Dashboard Models 标签页**：每个模型使用情况分析，浏览器内切换主/副模型
- **TUI**：LaTeX 渲染、`/reload` 热加载 .env、自动恢复最近会话、浅色终端自动识别、`/resume` 按 `d` 删除会话

### 值得注意的变化

- **默认关闭密钥脱敏**（之前经常误伤代码 patch）
- **模型 catalog 改为远端拉取**（新模型不用等发版）
- **多模态图像智能路由**（按模型实际视觉能力分发）
- **Prompt 缓存可延长到 1 小时**（默认 5 分钟）
- **TUI 冷启动时间砍掉约 57%**

### 移除/回滚

- Kanban 多 profile 协作看板上线后回滚
- computer-use 的 cua-driver 整体回滚
- 内置 BOOT.md hook 移除
- `/provider`、`/plan` 命令删除

## 升级建议

- **强烈建议升级**：360 个 bug 修复（流式输出/上下文压缩/工具调用/推理内容）
- **升级前备份**：`SOUL.md`、`MEMORY.md`、`skills/` 目录
- **国内用户**：可让 Hermes 帮你切换中文社区镜像（`cnb.cool/hermesagent-cn/hermes-agent-cn-mirror`）

## 来源

[[raw/external/微信公众号/Hermes Agent v0.12.0 已发布！1分钟速览更新内容.md]]
[[raw/external/微信公众号/Hermes Agent v0.12.0 已发布！1分钟速览更新内容 1.md]]

## 相关概念

- [[wiki/summaries/Hermes Agent 日报 5月4日-9日]] - v0.13.0 The Tenacity Release
- [[wiki/summaries/Hermes Agent 日报 5月11日-18日]] - v0.14.0 The Foundation Release
- [[wiki/summaries/Hermes Agent 日报 4月23日-30日]] - 社区日报提及 v0.12 动态
