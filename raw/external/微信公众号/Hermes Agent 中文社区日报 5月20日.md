李嘉乐的数字花园 *2026年5月20日 03:58*

![图片](https://mmbiz.qpic.cn/mmbiz_png/kHh2ibPRjHicFncsCXQX6DXbehySbXn4N6icHcHYfZQsaHd112Ckz18W0hltfrQzpaFlfeVlOZ6SPTdxPIgrKNiaezDpkpGgrzMr585t1A71XJE/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

> “
> 
> 今日汇总 18 条消息，共 2273 字，预计需要 5 分钟阅读。

### 1\. Hermes可通过飞书CLI读写飞书文档

**来源** ：Hermes Agent 中文社区飞书群 1

Hermes可配置飞书CLI（lark-cli）并赋予对应权限来实现对飞书云文档的读写。可将项目规范，知识沉淀等上传至飞书云文档方便协作。

### 2\. 企业客服场景建议优先使用Wiki结构化知识库替代纯RAG

**来源** ：Hermes 中文社区 互联网 IT 软件

在高频树状结构的客服业务中，纯RAG方案易因向量化导致长文本语义丢失。采用Wiki或图谱化知识库配合高频自动化与人工兜底的SOP策略，能更好平衡响应速度与可靠性。

### 3\. 推荐Scrapling库解决Agent网页操作反爬验证问题

**来源** ：Hermes 中文社区 互联网 IT 软件

在Agent自动化操作网页时若频繁触发反BOT验证，可引入Scrapling库处理请求。该工具在绕过常见反爬机制方面表现稳定，部分场景能有效提升自动化脚本的执行效率。

**链接** ：

- https://hermesagent.org.cn/docs/user-guide/skills/optional/research/research-scrapling

### 4\. 主流模型指令遵循能力对比与DeepSeek缓存优化建议

**来源** ：Hermes Agent 中文社区飞书群 1

综合实测反馈，GLM编程与长任务能力强但白天高负载易排队；DeepSeek性价比高但能力中规中矩；MiniMax适合执行明确指令但缺乏深度规划。使用DeepSeek时，群友实测，保持同一话题连续对话可使KV Cache命中率提升至90%以上，频繁切换话题会显著降低命中率。

### 5\. Hermes搜索功能配置方案与推荐引擎

**来源** ：Hermes Agent 中文社区微信群 49

Hermes需配置外部搜索引擎方可正常使用搜索功能。推荐方案包括接入Tavily API、Brave Search API，或自建SearXNG实例。SearXNG支持自定义添加国内外数据源，适合有特定行业检索需求或注重数据隐私的场景。

### 6\. 推荐OpenAI Computer Use用于视觉自动化调试，开源多模态模型在屏幕控制任务上仍落后于闭源模型

**来源** ：Hermes Agent 中文社区微信群 43

针对桌面端视觉自动化与IDE调试需求，群内推荐了OpenAI的Computer Use方案。同时讨论指出，在截图识别与坐标控制等视觉任务中，现有开源多模态模型的效果与速度尚无法追平OpenAI或Anthropic的闭源模型，实际落地前需结合具体算力环境进行充分测试验证。

**链接** ：

- https://developers.openai.com/codex/app/computer-use

### 7\. 垂直领域科研建议采用“通用大模型+专业数据库/MCP服务”架构

**来源** ：Hermes Agent 中文社区微信群 39

针对中文及古文等特定语境研究，仅依赖通用大模型易出现理解偏差。推荐结合行业专业数据库或 MCP 服务构建 Agent，利用垂类数据弥补通用模型在细分领域的知识盲区。

### 8\. 群友评测最近发布的 OpenHuman 开源项目

**来源** ：Hermes Agent 中文社区微信群 45

实测 OpenHuman 平台对国内应用支持有限。建议开发者直接在 Hermes 中集成自动拉取数据的工具或插件，以实现更灵活的数据同步与处理方案。

**链接** ：

- https://github.com/tinyhumansai/openhuman

### 9\. 分享两款适用于Hermes的开源Skill：图像生成与Peekaboo监控

**来源** ：Hermes Agent 中文社区飞书群 1

社区开源了Hermes调用图像生成的Provider Skill，以及将OpenClaw的Peekaboo技能包适配为Hermes可用版本。可用于实现AI视觉监控、消息转发与自动化响应等场景，部署后可直接通过指令调用。

**链接** ：

- https://github.com/AiFooooo/imagegen-provider-skill
- https://github.com/openclaw/openclaw/blob/main/skills/peekaboo/SKILL.md

### 10\. DeepSeek API限时折扣至5月31日

**来源** ：Hermes Agent 中文社区微信群 49

DeepSeek开放平台提供DeepSeek API调用 2.5 折优惠，活动截止至5月31日。6月1日起将恢复原价，建议有高频调用或测试需求的开发者提前规划使用量或进行充值。

### 11\. 阿里云Coding Plan Lite已下线抢购页面仅为前端展示

**来源** ：Hermes 中文社区 互联网 IT 软件

阿里云原Coding Plan Lite套餐已停售。建议开发者转向其他按量计费方案或关注官方后续推出的轻量级Token优惠包。

### 12\. 海外开发者正在开发 Hermes Agent iOS 版本

**来源** ：Hermes Agent 中文社区微信群 5

该项目为海外社区开发者开发的 Hermes Agent iOS 版本，仍处于Beta阶段，该项目据称为 Hermes WebUI 项目的衍生版本，可实现联动。

**链接** ：

- https://www.uzairansar.com/hermes-mobile

### 13\. 多Agent协作前清空Hermes记忆可解决上下文污染导致的性能下降问题

**来源** ：Hermes Agent 中文社区微信群 48

长期使用同一个会话导致频繁进行记忆压缩容易造成LLM降智。在使用多Agent协作前建议先手动清空主Agent记忆，避免残留记忆影响性能。建议主Agent保留最高的读取权限，并编写独立模块负责记忆片段的裁剪与分发，实现长期记忆的结构化管理。

### 14\. Hermes 微信机器人当前未开放添加到公开群的功能

**来源** ：Hermes Agent 中文社区微信群 44

微信端机器人目前未开放添加到公开群的功能，仅支持私人使用。如需多用户或群聊场景，可考虑接入 QQ 机器人或使用 napcat 对接，但需注意 napcat 在微信环境存在封号风险。

### 15\. 分享前端UI设计优化资源与Claude Code实战经验

**来源** ：Hermes Agent 中文社区微信群 1(工作群)

推荐了UI/UX设计相关的开源Skill库。实测表明，直接使用Claude Code并赋予高级UI设计师角色提示词，比依赖特定Skill更能高效生成高质量设计稿，适合快速搭建Agent前端界面。

**链接** ：

- https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

### 16\. 开源项目 browser-use 已适配 Hermes 生态

**来源** ：Hermes Agent 中文社区微信群 49

推荐开源项目browser-use用于浏览器自动化操作，该项目已适配Hermes生态。适用于需要Agent直接操控网页、执行复杂交互任务的场景，可作为独立任务执行或工作流编排的底层驱动。

**链接** ：

- https://github.com/browser-use/browser-use

### 17\. 手动触发上下文压缩指令与Profile技能拆分方案

**来源** ：Hermes Agent 中文社区飞书群 1

针对长对话上下文膨胀问题，可使用 `/compress 【主题】` 指令手动压缩，首次执行后系统通常会自动跟进。为节省Token消耗，建议将大量技能拆分至主副Profile，主Profile仅保留核心技能并负责任务分发，副Profile处理专项任务。

### 18\. 利用Codex自动化Rebase实现Hermes魔改内核平滑升级

**来源** ：Hermes 中文社区 互联网 IT 软件

针对二次开发场景，可通过自动化Rebase流程同步官方更新。实测利用AI辅助处理代码合并冲突，可大幅降低跨版本维护成本，实现魔改分支与官方版本的无缝兼容。

扫码加入 Hermes Agent 中文社区微信群

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**微信扫一扫赞赏作者**

Hermes Agent 中文社区日报 · 目录

继续滑动看下一个

李嘉乐的数字花园

向上滑动看下一个