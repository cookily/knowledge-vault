李嘉乐的数字花园 *2026年5月4日 12:46*

![图片](https://mmbiz.qpic.cn/mmbiz_png/kHh2ibPRjHicG5MkQzrjfoyjOKYadeqGEWZIibwDJNI8J10iaoS2u829v7HAzRh2rkCTaI0nGCKokZsHFXnBXWKUQfArEuuZxs5diaQLB62uMAibU/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

> “
> 
> 今日汇总 17 条消息，共 2168 字，预计需要 5 分钟阅读。

### 1\. 开源AI法律平台mike获1.4k星，聚焦垂直赛道专业化工具

**来源** ：Hermes 中文社区 法律

该项目定位为开源AI法律平台。随着AI Agent向行业细分演进，通用模型将主要作为底层生态，而由行业从业者搭建的垂直专业化工具将成为实际业务落地的核心。

**链接** ：

- https://github.com/willchen96/mike

### 2\. 建议利用Codex，Claude Code等自主开发适配特定业务场景的定制化工具

**来源** ：Hermes 中文社区 法律

面对高度专业化的行业需求，直接调用通用Agent，如Hermes，龙虾等往往难以满足深度要求。通过代码生成工具自主设计与编写专属小程序或工具链，能更精准地贴合业务逻辑并提升交付效率。

### 3\. 调用应用截图失败时，可通过提示Agent先最小化所有窗口提升成功率

**来源** ：Hermes Agent 中文社区微信群 25

在使用ds-v4-flash等模型进行屏幕截图时，复杂桌面环境易导致识别失败。实测表明，在指令中明确要求Agent先执行“最小化所有窗口”操作，可有效规避界面遮挡问题。该方案适用于多窗口重叠场景下的自动化任务调试。

### 4\. 社区站上线文档MCP端点，可直接配置接入解决文档读取问题

**来源** ：Hermes Agent 中文社区微信群 24

中文社区网站已升级为L5级Agent-Ready，文档MCP服务正式上线。针对Agent无法读取文档的常见问题，直接配置该MCP端点即可打通解析链路，避免格式或权限导致的读取失败。

**链接** ：

- https://mcp.hermesagent.org.cn/v1

### 5\. Claude Code 与 Hermes Agent 适用场景对比：前者擅长代码开发，后者适合个人常驻助手。

**来源** ：Hermes Agent 中文社区微信群 8

实际使用反馈表明，Claude Code 在编程与工程开发场景下体验更优。而 Hermes Agent 在作为个人日常助理或长期驻留的智能体时表现更稳定，两者可互补使用。

### 6\. 新手建议优先使用低成本联网大模型，暂不推荐本地部署。

**来源** ：Hermes Agent 中文社区微信群 2

消费级硬件能本地部署的模型基本在30B参数以内，且需要较高硬件成本，并且实际Agent效果较差。建议初学者先通过MiniMax等廉价联网API跑通流程，再考虑本地化方案。

### 7\. 探讨Agent记忆系统设计，建议采用分层与遗忘机制避免上下文冗余。

**来源** ：Hermes 中文社区 互联网 计算机 IT

Agent无需记住所有信息，可通过临时存储、重要性评估、分类日记及关键词多跳联想来优化记忆。推荐参考人类记忆系统相关理论，结合定时任务与技能框架实现轻量化记忆管理，有效节省检索Token并提升任务专注度。

### 8\. 解决多Agent间通信受限问题，推荐基于文档沉淀与快照读取的替代方案。

**来源** ：Hermes 中文社区 互联网 计算机 IT

针对当前框架缺乏原生跨Agent通信机制的情况，可采用将关键信息沉淀至外部文档或生成任务快照的方式。其他Agent通过主动读取文档或快照获取上下文，配合定时遗忘与里程碑进度管理，可实现轻量级协作。

### 9\. 社区分享多款Agent工作流、记忆技能插件及网易Agent邮箱工具。

**来源** ：Hermes 中文社区 互联网 计算机 IT

分享了基于TDD驱动的开发工作流、Agent睡眠与做梦记忆技能、Token消耗可视化小票生成器，以及网易推出的可对接Hermes的Agent邮箱管理平台，该平台正在内测中。相关工具涵盖上下文隔离、记忆优化与外部服务集成场景。

**链接** ：

- https://gitee.com/hongmaple/scale-engine
- https://github.com/Hchen1218/token-receipt
- https://github.com/jessieissocute/afterdream-skill
- https://claw.163.com/projects/dashboard/#/

### 10\. 多Agent场景下Skill工具索引易占用大量上下文Token，可通过配置实现技能隔离。

**来源** ：Hermes Agent 中文社区QQ群

当挂载数十个Skill时，基础上下文Token消耗显著上升。无需修改源码，仅需在配置文件中为不同Agent分配独立的项目与技能集，即可实现上下文隔离，有效控制Token成本并提升多项目并行效率。

### 11\. 飞书免费版提供每月100万次API调用额度，可通过App ID与Secret快速接入Hermes。

**来源** ：Hermes Agent 中文社区QQ群

在飞书开放平台创建应用后，将获取的凭证提供给系统即可自动完成配置。该额度对个人开发者较为充裕，适合作为日常对话或轻量级自动化任务的IM通道。

**链接** ：

- https://open.feishu.cn/app

### 12\. MiniMax 29元套餐不支持生图功能，49元套餐起支持，写代码推荐DeepSeek。

**来源** ：Hermes Agent 中文社区QQ群

29元套餐限制为5小时700次调用，上下文200K，适合日常文本交互。若需图像生成需升级至49元档。在代码生成场景下，DeepSeek模型的综合表现与性价比更优。

### 13\. 长文本与编程场景模型选型建议及本地部署参数参考

**来源** ：Hermes Agent 中文社区微信群 31

针对长文本处理推荐 nemotron，编程推荐 qwen 系列，数学逻辑推荐 gemma。本地部署建议参数量控制在 30B 以内以保证响应速度，复杂任务建议调用云端大模型。

### 14\. 推荐 Tavily 搜索引擎与 Agent Browser 工具

**来源** ：Hermes Agent 中文社区微信群 31

DuckDuckGo 限速严重时，可注册 Tavily 获取 API Key 作为替代搜索API。若需 Agent 操控浏览器，可部署开源项目 agent-browser 增强网页交互能力。

**链接** ：

- https://app.tavily.com/home
- https://github.com/vercel-labs/agent-browser

### 15\. 多智能体协作架构与记忆插件实践建议

**来源** ：Hermes Agent 中文社区微信群 31

飞书多 Agent 协作可将所有机器人拉入同一群由主控协调，但机器人互@无响应，建议通过主控下发任务或让 Agent 动态生成子 Agent。记忆插件方面，Plan-solve 模式为当前最佳实践；长时记忆本质依赖上下文与向量检索，本地轻量使用无需过度配置复杂记忆系统。

### 16\. 飞书长消息截断问题的自动分段发送方案

**来源** ：Hermes Agent 中文社区飞书群 1

飞书单条消息上限约30KB（中文约1万字），超限会被截断。可通过代码逻辑按自然断点（段落>换行>标点）将长文本切割，首段使用reply回复，后续段使用send发送，并清理控制字符与未闭合Markdown标记，该方案已稳定运行。

### 17\. 微信机器人进群限制与飞书代码块折叠问题

**来源** ：Hermes Agent 中文社区飞书群 1

微信目前尚未开放机器人主动加入群聊的权限（接口已预留）。飞书iOS端存在代码块折叠后无法点击展开的显示Bug，临时方案可要求模型输出纯文本格式，或改用桌面端查看完整内容。

扫码加入 Hermes Agent 中文社区微信群

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

图片版

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**微信扫一扫赞赏作者**

Hermes Agent 中文社区日报 · 目录

继续滑动看下一个

李嘉乐的数字花园

向上滑动看下一个