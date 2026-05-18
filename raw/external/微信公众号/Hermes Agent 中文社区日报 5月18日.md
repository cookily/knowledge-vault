李嘉乐的数字花园 *2026年5月18日 08:39*

![图片](https://mmbiz.qpic.cn/mmbiz_png/kHh2ibPRjHicGszwJytRCDsw5BNLxY2ViaDzaBcEUZC0AXEO9q9Lo0NNUtK6Yf3HicTUsMM9f8Mo1DvP7oicXKE3zkdqHvHjQDtU9kZibnxVSCE3Q/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

> “
> 
> 今日汇总 18 条消息，共 2325 字，预计需要 5 分钟阅读。

### 1\. 实测 browser-harness 工具反馈良好，运行效果符合预期。

**来源** ：Hermes 中文社区 法律

有开发者根据社区指引对 browser-harness 项目进行了实际测试，确认其在相关场景中表现稳定。该工具可作为浏览器自动化或测试任务的备选方案，建议有类似需求的开发者尝试接入。

**链接** ：

- https://github.com/browser-use/browser-harness

### 2\. 分享两款AI内容检测工具，适用于论文AI率自查与降重参考。

**来源** ：Hermes Agent 中文社区微信群 40

针对 AI 引文检测/虚假文献检测及文本AI生成率检测需求，群友推荐了Citely与PaperBeego平台。两者可作为传统查重系统的补充，提供在线评估功能，可辅助进行内容合规性检查与针对性降重。

**链接** ：

- https://citely.ai/zh
- https://www.paperbeego.com/login?invite\_code=UZQRSZC166VSLG1YZDTO

### 3\. Hermes中，用于生成对话标题的辅助模型(auxiliary model)不配置不会影响使用，可使用低成本模型替代。

**来源** ：Hermes Agent 中文社区微信群 21

该辅助模型仅用于会话概括与标题生成，缺失不会影响主要功能。建议选用低成本模型作为辅助模型，或直接让 Hermes 分析源码以获取设计逻辑与解决路径。

### 4\. 群友开源 Skill 自动维护工具，支持任务后自动生成 Skill。

**来源** ：Hermes 中文社区 互联网 IT 软件

该项目可实现自动扫描、整理、注册、去重、修复 SKILL.md，支持开箱即用。有助于自动化沉淀工作流经验，减少手动编写配置文件的成本，适合长期运行的 Agent 系统。

**链接** ：

- https://github.com/jangyuxue/skill-auto-maintain

### 5\. 群友开源Hermes自媒体视频创作双技能套件。

**来源** ：Hermes Agent 中文社区飞书群 1

包含「艺术生花」（抖音爆款拆解）和「灵感象限」（全自动剪辑流水线）两个技能，支持分析视频结构并自动剪辑成片。提供依赖检查、MiniMax API配置及常见问题解决方案，完全开源免费。

**链接** ：

- https://github.com/503496348-ops/hermes-skill-ideasphere

### 6\. 群友推荐开源多智能体协作框架 agents-hive。

**来源** ：Hermes Agent 中文社区微信群 45

社区分享了基于多智能体协作的开源项目 agents-hive，适用于需要复杂任务调度与多 Agent 协同的开发场景，可作为当前生态的补充或替代方案参考。

**链接** ：

- https://github.com/chef-guo/agents-hive

### 7\. 推荐轻量化 Agent 框架 pi，支持树状 Session 管理与回滚。

**来源** ：Hermes 中文社区 互联网 IT 软件

该框架极度轻量，核心特性为树状 Session 结构，支持会话状态回滚与精细控制。内置大量 Hook，Agent 仅负责会话管理、Bash 调用与模型路由，适合追求低资源占用与高定制化的工作流场景。

**链接** ：

- https://github.com/earendil-works/pi

### 8\. 多 Hermes 实例调度与 IM 消息路由优化方案。

**来源** ：Hermes 中文社区 互联网 IT 软件

实例管理可参考开源的 clawmanager 项目。另外，社区讨论认为，针对 IM 群聊高密度消息，建议增设路由 Agent 进行消息分拣与合并推送，避免多 Bot 盲目拉取消耗 Token；将会话共享并外置思考过程，可有效降低上下文窗口压力。

**链接** ：

- https://github.com/Yuan-lab-LLM/ClawManager

### 9\. Hermes 与外部编程工具的协作实践。

**来源** ：Hermes Agent 中文社区飞书群 1

Hermes 可通过 ACP、MCP 或 API 与外部编程工具协作，更适合作为任务规划与调度中枢；Claude Code、OpenCode 等 CLI 工具可作为被封装和调度的执行端探索。

### 10\. 使用 Termux 可在手机端部署运行 Hermes Agent。

**来源** ：Hermes Agent 中文社区微信群 38

针对移动端运行需求，可通过安装 Termux 终端模拟器在 Android 设备上配置环境并运行 Hermes。该方法为轻量级本地部署提供了可行路径，适合移动调试或便携使用场景。

### 11\. 社区分享开源项目 rtk-hermes。

**来源** ：Hermes Agent 中文社区微信群 44

该仓库提供了与Hermes相关的集成方案或工具链，适合有定制化开发需求的开发者参考。建议结合官方文档评估其功能边界与兼容性后再引入生产环境。

**链接** ：

- https://github.com/ogallotti/rtk-hermes

### 12\. Hermes 记忆系统优化策略与多 Agent 成本控制经验。

**来源** ：Hermes 中文社区 互联网 IT 软件

针对长上下文记忆易丢失或检索不准的问题，可采用标签化管理按活跃度分级，或引入子 Agent 直接查询数据库。多 Agent 并行易快速消耗 Token，建议将跨项目通用能力沉淀为 Skill 复用，或采用单一大模型多线程调度以平衡效果与成本。

### 13\. 结合内网穿透与 Agent 自建网页，可实现 Hermes 的远程跨端访问。

**来源** ：Hermes Agent 中文社区微信群 40

通过 SSH tunnel/reverse tunnel，并配合认证与防火墙等协议完成内网穿透后，可指要求 Hermes 编写简易 Web 交互界面，即可在任意网络环境下安全访问本地实例。

### 14\. Hermes Agent v0.14.0 新版本提升了 Windows 直接部署的兼容性，但目前仍为测试性支持。

**来源** ：Hermes Agent 中文社区微信群 14

该版本在原有基础上进一步优化了 Windows 环境下的本地部署流程，降低了环境配置门槛。需注意当前 Windows 支持仍处于测试阶段，建议开发者在测试环境中验证稳定性，生产环境可优先考虑 MacOS，Linux 或容器化方案。

### 15\. 为 Hermes 扩展视觉能力可搭配独立视觉模型或切换至多模态模型。

**来源** ：Hermes Agent 中文社区微信群 38

如Deepseek这类的纯文本模型无法直接处理图像视频，需额外接入视觉组件。建议直接选用原生支持多模态的模型，或采用主文本模型搭配独立视觉模型的架构方案，推荐Minimax及Qwen系列多模态模型。

### 16\. Hermes Agent 支持在回复过程中插入评论，并可实现任务间的关联配置。

**来源** ：Hermes Agent 中文社区微信群 17

针对连续对话场景，系统允许在模型生成回复时中途插入评论或指令，无需等待完整输出。同时支持配置不同任务节点之间的依赖与关联关系，便于构建复杂工作流。适用于需要动态干预或编排多步骤 Agent 的开发场景。

### 17\. 在DGX Spark 本地部署大模型推荐 vLLM 服务，结合 Docker 容器化与 nvfp4 量化可提升稳定性与速度。

**来源** ：Hermes Agent 中文社区微信群 31

可通过 AI Agent通过 SSH 连接 Spark 自动完成环境配置。需注意当前 Coding Agent 缺乏 DGX Spark 相关知识，直接操作易导致配置失败。建议先引导 Agent 读取 NVIDIA 官方文档及最新配置教程，再执行部署任务。

### 18\. 大PDF处理工作流推荐：mineru、扣子、RAGFlow。

**来源** ：Hermes Agent 中文社区QQ群

RAGFlow为开源方案，自带网页问答界面，支持自动拆分PDF建知识库；mineru支持本地部署。

扫码加入 Hermes Agent 中文社区微信群

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**微信扫一扫赞赏作者**

Hermes Agent 中文社区日报 · 目录

继续滑动看下一个

李嘉乐的数字花园

向上滑动看下一个