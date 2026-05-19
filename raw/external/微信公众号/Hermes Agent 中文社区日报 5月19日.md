李嘉乐的数字花园 *2026年5月19日 08:31*

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

> “
> 
> 今日汇总 16 条消息，共 2579 字，预计需要 6 分钟阅读。

### 1\. 警惕来路不明的免费 API 中转站，可能泄露密钥与敏感请求数据

**来源** ：Hermes 中文社区 法律

免费第三方 API 中转服务可能记录、留存或转售用户请求内容。使用此类服务时，API Key、隐私信息、业务数据甚至钱包助记词都可能外泄。建议优先使用官方渠道或可信服务商，并避免把敏感数据发送到无法审计的中转站。

### 2\. 分享AI辅助生成的UI原型创意灵感库，适用于产品前期构思与需求验证

**来源** ：Hermes Agent 中文社区微信群 15

该站点目前为原型展示阶段，主要提供创意参考与交互设计示例。开发者可借鉴其内容组织方式，用于Agent项目的界面灵感收集或Prompt效果测试。

**链接** ：

- https://zsc3001.top/inspireWorks/szyc/index.html
- https://zsc3001.top/inspireWorks/index.html

### 3\. 针对Agent跨天记忆丢失问题，建议每日自动生成Markdown文档记录并提取关键信息

**来源** ：Hermes Agent 中文社区微信群 41

针对Agent在长时间运行或跨会话时容易遗忘历史任务的问题，可采用每日任务结束后自动让Agent生成结构化Markdown总结的方法。通过定期提取和归档该文档，可有效弥补上下文窗口限制，实现长期任务状态的持久化与回溯。

### 4\. 建议按项目维度而非单一任务分类管理文件，以提升资料检索与Agent调用效率

**来源** ：Hermes Agent 中文社区微信群 43

针对非开发场景，将同一项目的相关资料集中存放于统一文件夹中，避免碎片化创建。该结构能优化上下文检索路径，使Agent在调用历史文档时更精准高效。

### 5\. 东方财富模拟组合免费可用，接口自动化能力需以账号权限与平台政策为准

**来源** ：Hermes 中文社区 金融 量化 财会

东方财富官方页面显示模拟组合为免费功能，可用于股票模拟交易与收益核算，适合作为 AI 策略早期的低成本验证入口。若要进一步接入量化接口或 miniQMT 等工具搭建自动化盯盘、回测流程，需确认账号权限、接口稳定性和平台使用政策。

### 6\. 社区实践建议优先使用 CLI 交互，定时提醒可接入飞书或 CalDAV 替代微信 iLink

**来源** ：Hermes Agent 中文社区微信群 45

社区实践反馈，CLI 更便于文件读取、日志排查与自然语言配置；微信 iLink 在部分长时间闲置场景可能出现推送不稳定。定时提醒可考虑接入飞书或支持 CalDAV 的日历服务，把提醒交给标准日历系统承载，但具体稳定性仍需按部署环境验证。

### 7\. DeepSeek V4 Flash 已开放文本模型，图像视频识别需辅助模型；商汤试用额度以控制台为准

**来源** ：Hermes Agent 中文社区微信群 45

DeepSeek 官方已开放 V4 Pro/Flash API 与开源权重，公开模型卡标注为文本生成模型。当前用于图片或视频识别时，仍建议通过 Hermes 配置 MiniMax 等多模态辅助模型，或本地调用 ComfyUI。社区反馈商汤 SenseNova 控制台可试用 DeepSeek V4 Flash，但免费周期、刷新频率与限流规则需以控制台实时显示为准。

**链接** ：

- https://platform.sensenova.cn/console

### 8\. 使用 \`last30days-cn\` 技能增强国内搜索，本地部署门槛属于社区经验建议

**来源** ：Hermes Agent 中文社区微信群 46

为提升国内网络环境下的搜索效果，可加载 \`last30days-cn\` 技能；其仓库说明支持微博、小红书、B站、知乎、抖音、微信、百度、头条等平台。关于本地模型规格，社区经验认为 7B 及以下体验有限，复杂任务可优先尝试 27B 级稠密模型或云端 API（如 DeepSeek V4、GLM 5.1），实际效果仍需按任务和硬件验证。

**链接** ：

- https://github.com/Jesseovo/last30days-skill-cn

### 9\. 基于 Google A2A 协议探索 Hermes、OpenCode 与 WorkBuddy 的多智能体协同工作流

**来源** ：Hermes Agent 中文社区微信群 50

A2A 官方定位为跨框架 Agent 互操作协议，社区实践可让 Hermes 负责统筹调度与规划，OpenCode 专注代码开发，WorkBuddy 处理测试与文档。针对 WorkBuddy 原生不支持 A2A 的情况，可参考 OpenClaw 等 A2A 实现自建适配服务；该方案仍属于实践探索，发布前应标注为社区经验。

### 10\. MiniMax M2.7 高速版可用于提速，任务调度优化属于套餐使用经验

**来源** ：Hermes Agent 中文社区微信群 48

MiniMax 官方文档列出 M2.7 与 M2.7-highspeed，高速版输出速度标称更高。若使用时响应较慢，可检查是否误选低速模型；将固定无人值守任务调度到低峰时段执行属于成本与体验优化经验，具体效果取决于套餐规则、任务负载和当时限流情况。

### 11\. 知乎开放平台已可访问，Token 与搜索权限需以后台认证和接口权限为准

**来源** ：Hermes Agent 中文社区飞书群 1

知乎开放平台页面已上线，开发者登录后可在后台查看文档、认证状态和相关接口能力。用于智能体搜索前，应确认账号是否完成平台要求的认证、是否具备对应 API Token 与搜索接口权限，并对搜索结果中的 SEO 营销内容做交叉验证。

**链接** ：

- https://developer.zhihu.com/

### 12\. 开源项目 OpenHuman 发布，主打本地优先的桌面级 Agentic AI 助手

**来源** ：Hermes Agent 中文社区QQ群

提供 Memory Tree 记忆系统、TokenJuice 压缩层及 118+ 第三方服务一键接入。目前处于 Early Beta 阶段，采用 GPL-3.0 协议，对国内办公生态支持尚不完善，适合关注数据本地化与多平台工作流的开发者尝鲜。

**链接** ：

- https://github.com/tinyhumansai/openhuman

### 13\. Obsidian 以本地 Markdown 和官方 Sync 为核心，Git 与 WebDAV 同步多依赖插件或第三方方案

**来源** ：Hermes Agent 中文社区QQ群

Obsidian 官方说明笔记以本地纯文本 Markdown 文件存储，并提供端到端加密的官方 Sync；Git、WebDAV、网盘等多端同步通常依赖社区插件或第三方工具。配合 Agent 可做自动化整理与复盘，但坚果云、阿里云 OSS 等价格会变动，发布时不宜写死费用。

**链接** ：

- https://obsidian.md/

### 14\. 推荐 ui-ux-pro-max-skill 辅助前端设计，并分享分块迭代提示词策略

**来源** ：Hermes 中文社区 互联网 IT 软件

针对生成复杂前端页面易耗精力的问题，可引入该开源技能库辅助设计。实际操作建议采用分步策略：先定义页面元素生成初版，再分块调整并手动压缩，最后逐步细化内部结构，可有效降低引导成本。

**链接** ：

- https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

### 15\. CanIRun.ai 可评估本地 AI 模型运行档位，部署成本仍需结合硬件与使用频率测算

**来源** ：Hermes 中文社区 互联网 IT 软件

CanIRun.ai 可基于浏览器检测到的硬件信息估算本机可运行哪些 AI 模型及运行档位。实际部署还需综合显存、内存、生成速率、电费、散热和维护成本；个人重度使用场景仍应对比云端 API 性价比，本地部署更适合隐私、离线或特定原型验证需求。

**链接** ：

- https://www.canirun.ai

### 16\. 企业级 Hermes 可探索多网关共享配置架构，但高可用需压测与权限隔离验证

**来源** ：Hermes Agent 中文社区微信群 32

针对单实例服务多用户及高可用需求，可考虑部署多个网关实例并复用同一份 Hermes 核心配置，作为水平扩展方向。该方案是否能稳定支撑负载均衡、状态同步和权限隔离，需要结合实际网关实现、共享存储策略与压测结果验证。

扫码加入 Hermes Agent 中文社区微信群

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**微信扫一扫赞赏作者**

Hermes Agent 中文社区日报 · 目录

继续滑动看下一个

李嘉乐的数字花园

向上滑动看下一个