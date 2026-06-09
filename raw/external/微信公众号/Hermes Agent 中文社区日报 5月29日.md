李嘉乐的数字花园 *2026年5月29日 08:29*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kHh2ibPRjHicHVszEgkX8aSSEialsvxIFgJ4MicOuPqp1xUeBPzuJ0VmIzfbf3M86OzDZ4CwVcWw2bDkf86EBMSY15Yxpy4KQQF3QRibhVP2BkWM/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

> “
> 
> 今日汇总 16 条消息，共 2169 字，预计需要 5 分钟阅读。

### 1\. Hermes Agent v0.15.0 发布：性能、多 Agent 看板与安全能力大幅升级

v0.15.0「The Velocity Release」于 5 月 28 日发布，核心是提速与工程化：核心 agent 循环从 1.6 万行重构到约 3.8 千行，Kanban 升级为多 Agent 协作平台，支持任务自动拆解、Swarm 拓扑、计划任务、任务级模型覆盖与 worktree-per-task。新版本还带来 session\_search 约 4500 倍提速、47% 更少的单轮函数调用、Promptware 防护、Bitwarden Secrets Manager、ntfy 平台、Skill bundles、TUI 多会话编排、Krea/FAL 图像生成、Nous MCP 目录、OpenHands 编排技能与更深入的 xAI 集成。

**链接** ：

- https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.28

### 2\. 扣子平台现已支持直接接入ChatGPT Codex模型

扣子（Coze）平台已开放对ChatGPT Codex的直接调用支持。开发者可在智能体或工作流配置中快速集成该代码生成能力，适用于自动化编程与代码辅助场景。接入时建议关注相关API的合规要求与平台调用限制。

### 3\. 在 NAS 部署官方 Docker 版 Hermes 并配合 Watchtower 实现自动更新

针对容器化部署场景，推荐直接拉取官方 Docker 镜像而非第三方修改版。结合 Watchtower 工具可监听镜像仓库变化，实现服务的自动拉取与无缝重启，有效降低手动维护成本。适用于 NAS 或 Linux 服务器环境。

### 4\. 清华大学发布 PilotDeck 项目以优化 Agent 架构痛点

该项目针对现有智能体在任务规划与执行中的常见瓶颈进行了针对性改进。技术迭代速度较快，建议开发者结合官方文档评估其与现有工作流的兼容性。

**链接** ：

- https://github.com/OpenBMB/PilotDeck

### 5\. 推荐Open Design作为Claude Design的平替方案

可通过Codex等AI编程工具一键部署Open Design。该工具定位为Claude Design的平替，适合需要本地化或低成本设计辅助流程的开发者使用。

**链接** ：

- https://github.com/nexu-io/open-design

### 6\. 解决自定义规则被Agent选择性忽略的方法

当Agent忽略部分自定义规则时，通常是因为模型存在偷懒倾向。可在项目提示词中引入强化约束的提示词技巧，明确执行标准与反馈机制，以提升规则遵循度。也可以考虑使用更听话的模型，比如GPT-5.5。

### 7\. 讯飞Maas平台GLM5.1默认关闭思考模式，需手动开启以保证输出质量

讯飞Maas平台上的GLM5.1模型默认未启用思考模式，直接调用会导致回答质量显著下降。实际使用时需在请求参数中显式开启思考功能，建议业务侧在接入时注意该默认行为差异并调整提示词策略。

### 8\. Hermes直连微信推荐使用官方扫码方式，避免群聊接入导致封号

连接微信或飞书时，可直接通过智能体引导在浏览器内扫码完成绑定。若尝试将智能体直接拉入群聊等非标方式接入，存在较高的账号封禁风险，建议严格遵循官方推荐的扫码授权流程。

### 9\. 基于飞书看板实现多Agent接力协作，代码生成环节建议直连专用CLI

利用飞书Kanban作为任务状态流转中枢，可高效串联多个Hermes Agent进行接力执行。针对代码研发场景，通用Agent的产出质量与速度通常不及垂直工具，建议在该环节直接调用Codex CLI等专用代码模型。

### 10\. 推荐DeepSeek生态工具Reasonix，桌面版支持高缓存率与低成本开发

该工具提供桌面客户端，可集成至Hermes Agent中按需调用。实测结合DeepSeek V4 Flash使用可节省约80%成本，缓存率可达99%。

**链接** ：

- https://github.com/esengine/deepseek-reasonix

### 11\. 分享Anima AI绘画模型在CNB平台L40显卡的一键部署教程

提供基于CNB平台的L40显卡环境一键部署方案，环境配置完成后开箱即用，适合快速搭建AI绘画工作流。

**链接** ：

- https://b23.tv/YNki874

### 12\. 使用 /resume 命令可快速恢复历史会话

在对话中断或新建会话后，可通过输入 `/resume 会话ID` 快速加载之前的对话上下文与记忆。该功能适用于多轮调试或跨设备接续任务，避免重复输入背景信息。

### 13\. 提示词精简原则与模型越权行为应对

实测表明提示词堆砌过多反而降低模型遵循度，建议仅保留核心指令与必要上下文。当模型频繁越权决策或产生无效Token消耗时，优先精简提示词结构，若仍无法控制则直接切换指令遵循度更高的模型。

### 14\. 8G 显存本地部署体验不佳，当前 API 套餐性价比更高

实测 3060Ti 运行本地模型速度较慢且易卡顿，仅适合极轻量测试。对比当前 DeepSeek 与 MiniMax 降价后的 API 套餐价格，直接调用云端 API 在成本与效率上均优于个人显卡本地部署。

### 15\. Hermes 定位为通用 Agent，与专注开发的 Claude Code 侧重点不同

Hermes 侧重通用自动化与多模态任务调度，而 Claude Code 专为代码开发优化。相比 OpenClaw，Hermes 当前架构更稳定，破坏性更新较少，更适合生产环境业务流程。

### 16\. 网页抓取建议结合脚本与 RSS，避免 AI 直接解析消耗过多 Token

直接使用 AI 爬取新闻或复杂网页易触发反爬且消耗大量 Token。推荐让 AI 编写专用爬虫脚本、使用 RSS 订阅源，或通过精确提示词限定输出范围，可显著降低成本并提高稳定性。

扫码加入 Hermes Agent 中文社区微信群

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**微信扫一扫赞赏作者**

Hermes Agent 中文社区日报 · 目录

继续滑动看下一个

李嘉乐的数字花园

向上滑动看下一个