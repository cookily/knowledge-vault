李嘉乐的数字花园 *2026年5月9日 08:36*

![图片](https://mmbiz.qpic.cn/mmbiz_png/kHh2ibPRjHicGmyGOmdUrggrQZcm14Vibf25ca1IJPOKK1ibGTdhlcV4gLCWMpPfXCQQm1ITMib5lMf6lguXOgT5HpzL5uIopZom1HncTOicaH9nw/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

发布日期：2026 年 5 月 7 日

这次更新官方代号 **The Tenacity Release（长程运行版）** ，核心变化：Hermes 现在能长时间执行用户给定的任务——任务不烂尾、目标不跑偏、断了能接上。

详尽更新内容中文社区已翻译：

详见：http://hermesagent.org.cn/docs/releases/v0-13-0

## 一句话总结

- 多 Agent Kanban 正式上线（v0.12.0 回滚后重做）
- 新增 `/goal` 命令，让 Agent 锚定一个目标无限循环
- Checkpoints 底层重写，状态持久化更可靠
- Gateway 重启 / 升级后，会话自动接上，不丢上下文
- 集中修复了 **8 个 P0 级别安全漏洞**
- Google Chat 上线，平台数到 20 个
- Model Provider 架构改成可插拔，第三方模型提供商可直接接入
- 7 国语言 i18n 全面落地
- 新增视频理解工具和语音克隆能力

下面挑重点说说。

## 多 Agent Kanban 正式上线

这是 v0.12.0 上线后被回滚的 Kanban 功能的完整重做版。

创建一个看板（Kanban），把任务在看板中进行分发，多个 Hermes worker 会自动认领任务并进行处理。

这次的更新对于多 Agent 加了一整套可靠性保障：心跳检测、僵尸 worker 清理、重试预算、幻觉门。

可以同时运行多个看板，不同 Profile 之间可以共享 board 和 workspace。

## /goal 持久目标：Agent 不再跑偏

过去的 Hermes Agent 在多轮对话中容易偏离初衷。这次新增 `/goal` 命令：设定一个目标，Agent 在后续所有轮次中都会围绕它展开工作，不会跑题、不会遗忘。对话轮次由配置文件严格约束，超出立刻停止。

## Checkpoints v2：彻底重写

旧版 Checkpoints 存在多个存储路径，容易导致孤儿仓库问题。v2 改为单一存储架构，引入了剪枝机制和磁盘爆满保护机制。

## 会话扛重启：断了能接上

这是长程运行版本最关键的基础设施。

Gateway 中途重启、 `hermes update` 升级后重启……有很多种导致 Hermes 重启的情况，之前的版本对于重启的应对仍有问题。这个版本开始，Hermes 重启后，会话会自动恢复，还没有处理完的提示词会自动保留。

## 集中修复 8 个 P0 安全漏洞

这次安全方面的动作比较大，集中关了 8 个 P0 级别漏洞：

- 脱敏功能重新设为默认开启（v0.12.0 曾因误报临时关闭）
- Discord 角色授权修复了一个 CVSS 8.1 的跨 guild 绕过漏洞
- WhatsApp 默认拒绝陌生人消息
- auth.json 和 MCP OAuth 的 TOCTOU 竞态窗口被关闭
- 浏览器 SSRF 下限加固
- Cron 现在会扫描包含 skill 内容的完整 prompt，防范注入攻击
- `.env` / `auth.json` / `state.db` 文件权限恢复 0600

> “
> 
> 强烈建议所有用户升级。

## Google Chat 上线，支持的消息平台数增加到 20 个

消息平台现在能接入 Google Chat 了。

更重要的是，这次引入了 **通用的平台插件 hook** ——第三方适配器自此不需要修改核心代码就能接入。

同时， `allowed_channels` / `allowed_chats` / `allowed_rooms` 白名单配置现已覆盖 Slack 和钉钉。

## Provider 可插拔：第三方模型供应商直接接入

Model Provider 不再写死。通过 `ProviderProfile` 抽象类和 `plugins/model-providers/` 目录，第三方模型供应商可以作为插件灵活新增。

还新增了一个 `transform_llm_output` hook，这个 hook 可以在 LLM 输出对话之前进行调整或过滤，适合做内容审查或上下文压缩。

## video\_analyze：Agent 终于能「看」视频了

新增 `video_analyze` 工具，支持 Gemini 等多模态模型的原生视频理解。Hermes Agent 现在可以直接读取视频内容并给出分析结果。

## xAI Custom Voices：声音克隆

xAI Custom Voices 作为 TTS provider 正式接入。上传样本音频，Hermes 就能以指定音色输出语音。对需要个性化语音输出的场景很实用。

## 7 国语言 i18n 全面落地

CLI 和 Gateway 的消息现已支持 **中文、日文、德文、西班牙文、法文、乌克兰文和土耳其文** 。

## 写入即校验：post-write delta lint

`write_file` 和 `patch` 工具现在会在文件写入后自动执行语法校验，目前覆盖 Python、JSON、YAML 和 TOML。

## Cron no\_agent 模式：纯脚本定时任务

Cron job 新增 **no\_agent 模式** ——不使用 Agent，只执行脚本。如果脚本有输出则原文输出，无输出就静默。适合做健康检查、日志轮转、数据备份等不需要 AI 介入的定时任务。

`context_from` 字段支持把上一个 job 的输出作为下一个 job 的上下文，实现任务链。

## 国内 IM 改进

- **QQBot** ：补齐了审批交互的短板，另外，现在支持分块上传、引用附件等。
- **微信端** ：新增消息内容指纹去重，避免同一条消息被重复处理。
- **飞书端** ：开放机器人接入的配置入口。

## SearXNG 搜索后端

SearXNG 作为原生搜索专用后端正式上线。Web 工具按能力（搜索 / 抽取 / 浏览）拆分为独立后端，用户可以为不同能力配置不同的服务。

## TUI + Dashboard 改进

**TUI** ： `/model` 选择器全面重写，与 `hermes model` 命令行为对齐。状态栏新增上下文压缩次数计数。

**Dashboard** ：新增插件页面和 Profiles 管理页面。支持反向代理部署。Docker 用户可以通过 `HERMES_DASHBOARD=1` 一键启动 dashboard 进程。

## MCP 全面加强

MCP 协议支持升级到 SSE 传输层，其他专业技术细节此处略过。

## 6 个新可选 Skill

- Shopify（GraphQL 双端接入）
- here.now
- shop-app 个人购物助手
- Anthropic financial-services bundle 移植
- kanban-video-orchestrator
- searxng-search

Curator(即自动清理Skill)补全了 `archive` 、 `prune` 、 `list-archived` 三个子命令， `hermes curator run` 指令改为同步执行。

## 新模型

- `x-ai/grok-4.3` 接入 OpenRouter 和 Nous Portal
- `deepseek/deepseek-v4-pro` 新增适配

## Docker 不再以 root 运行

官方 Docker 镜像现在拒绝以 root 身份启动 gateway，node\_modules 目录的属权改为 hermes 用户。这是保障容器安全的防御性配置。

## 谁该升级？

如果有下面的需求，建议优先升级 v0.13.0：

- 需要多 Agent 并行协作（Kanban）
- 需要 Agent 长程锚定一个目标（ `/goal` ）
- 之前经常被 Gateway 重启 / 升级弄丢上下文
- 担忧安全问题（8 个 P0 级漏洞集中修复）
- 需要视频理解或语音克隆
- 在维护自定义 Provider 或写插件

## 如何更新

> “
> 
> ⚠️ 升级前请务必备份这些文件：
> 
> - SOUL.md
> - MEMORY.md
> - `skills/` 目录下你自己写的或 Hermes Agent 自己学习的 skill

更新方法：在终端（Windows 下用 PowerShell）输入：

```
hermes update
```

如果连接官方 GitHub 仓库超时，可以把下面这段提示词丢给 Hermes Agent，让它帮你换成中文社区镜像：

```
请帮我切换 Hermes Agent 的 git 源到中文社区镜像。

仓库通常位于 ~/.hermes/hermes-agent（Windows 下是 用户目录\.hermes\hermes-agent）。

请进入该目录后执行：

把 origin 改为中文社区镜像：https://cnb.cool/hermesagent-cn/hermes-agent-cn-mirror
把官方 GitHub 仓库加为 upstream：https://github.com/NousResearch/hermes-agent.git
用 git remote -v 确认两个 remote 都配置成功
用 git fetch origin 验证镜像能正常拉取

之后再跑一次 hermes update 即可。
```

## 图片版

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**微信扫一扫赞赏作者**

继续滑动看下一个

李嘉乐的数字花园

向上滑动看下一个