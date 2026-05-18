李嘉乐 *2026年4月27日 10:05*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kHh2ibPRjHicHOf3NAQgrZNjta0qfx2lR1VVxIHz3wmnH7LSAdBpCWKfvAI0FGNXGIwoW3r7KgORll7jRQT5KcsqNljiclbemAia70ibSyFOq7cE/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

> 今日汇总 20 条消息，共 3349 字，预计需要 7 分钟阅读。

### 1\. OpenAI 发布 GPT-5.5（代号 Spud），幻觉率较 5.4 降低 60%，SWE-bench 达 88.7%，已上线 ChatGPT 和 Codex

**来源** ：Google News

OpenAI 于 4 月 23 日发布 GPT-5.5，分标准版、Thinking 版和 Pro 版三个变体。官方称编码、计算机操作和通用办公能力提升最为显著，Terminal-Bench 2.0 得分 82.7%。付费用户可在 ChatGPT 和 Codex 中使用，API 接入待安全审查后开放。

**链接** ：

- https://www.axios.com/2026/04/23/openai-releases-spud-gpt-model

### 2\. DeepSeek 发布 V4 Preview：Pro（1.6T 参数）和 Flash（284B 参数），原生百万 token 上下文，MIT 开源

**来源** ：Google News

DeepSeek V4 于 4 月 24 日发布，Pro 版 1.6T 总参数/49B 激活，Flash 版 284B 总参数/13B 激活。采用 Hybrid Attention 架构，支持 100 万 token 上下文窗口。Flash 版 API 定价约 0.028），约为 Opus 4.7 的六分之一。MIT 协议开源，可自由商用。

**链接** ：

- https://api-docs.deepseek.com/news/news260424
- https://simonwillison.net/2026/Apr/24/deepseek-v4/

### 3\. Anthropic 内部模型 Mythos 遭未授权访问，该模型专为漏洞检测设计、仅限 Amazon/Apple 等少数公司测试

**来源** ：Google News

Anthropic 的 Mythos 模型作为 Project Glasswing 项目的一部分，仅向 Amazon、Apple、Cisco、JPMorgan Chase、Nvidia 等公司有限开放。一个 Discord 群组通过第三方承包商信息推测出模型位置并获得访问权限。Anthropic 确认正在调查第三方供应商环境中的未授权访问事件。

**链接** ：

- https://fortune.com/2026/04/23/anthropic-mythos-leak-dario-amodei-ceo-cybersecurity-hackers-exploits-ai/

### 4\. OpenAI 发布 GPT-Image-2（ChatGPT Images 2.0），首个内置推理能力的图像模型，12 小时内登顶 Image Arena 全品类第一

**来源** ：Google News

OpenAI 于 4 月 21 日发布 gpt-image-2，支持原生推理、2K 分辨率和多图一致性。文字渲染能力大幅提升，中日韩等多语言文本首次可生成接近母语水平的准确输出。DALL-E 2/3 将于 5 月 12 日正式退役，GPT-Image-2 成为 ChatGPT 和 API 的默认图像模型。

**链接** ：

- https://openai.com/index/introducing-chatgpt-images-2-0/

### 5\. Hermes 支持配置多个飞书机器人，已有用户成功配置三个

**来源** ：Hermes Agent 中文社区微信群 9

提问 Hermes 是否支持配置两个飞书机器人，另一用户确认可行，并指出已实际配置三个飞书机器人且运行正常，说明多飞书机器人接入在当前版本中具备实践基础。

### 6\. Hermes 支持在无公网暴露环境下通过 WebSocket 接入飞书/微信等平台，但本地机器需有互联网连接

**来源** ：Hermes Agent 中文社区微信群 20

本地部署 Hermes（如虚拟机或公司内网电脑）接入飞书或微信机器人时，无需将 8642 等端口暴露至公网，但运行 Hermes 的机器本身需具备稳定公网访问能力，以完成与飞书/微信服务端的 WebSocket 长连接。

### 7\. Hermes Agent 0.11 版本与飞书存在兼容性问题，升级需应用官方补丁修复底层代码冲突

**来源** ：Hermes Agent 中文社区微信群 2

反馈升级 Hermes 到 0.11 后与飞书集成出现冲突；官方已修复该问题并发布补丁；v4 pro 用户升级后验证无异常，建议升级前确认使用的是 v4 系列模型。

### 8\. DeepSeek Pro 模型在 Hermes 中缓存命中率高、成本较低，关闭思考模式使用 Flash 可进一步降低成本

**来源** ：Hermes Agent 中文社区微信群 2

实测 DeepSeek Pro 在 Hermes 中 API 响应快、缓存复用率高；配合关闭深度思考模式（Thinking Mode）并选用 Flash 推理路径，可显著降低调用成本，单次调用低至 0.2 元。

### 9\. Hermes Agent 本地部署建议使用 Qwen3.5-35B 级别模型，9B 级别易出现错别字和重复回复等幻觉问题

**来源** ：Hermes Agent 中文社区微信群 10

群内实测发现 Qwen3.5-9B 在文档处理中常出现错别字；Qwen3.5-35B 在合理上下文长度（如 128）下可稳定运行，吞吐达 57 tokens/s，且支持更长上下文。模型幻觉与上下文长度正相关，压缩策略和温度调优可缓解但非根治。

### 10\. Ollama 本地加载 Qwen3.5-9B、Gemma4-26B/31B 工具调用正常，但长时间运行易出现重复回复类幻觉

**来源** ：Hermes Agent 中文社区微信群 10

用户实测在 Ollama 环境下 Qwen3.5-9B 与 Gemma4 系列模型可正常启用工具调用，但运行一段时间后出现重复输出问题。该现象在官方 26B 模型及破解版中均复现，推测与模型规模及上下文管理有关，非单纯硬件温度导致。

### 11\. 有群友开发 Hermes Agent 人格开发器，支持基于特定‘干活人格’进行个性化微调

**来源** ：Hermes Agent 中文社区微信群 10

该人格开发器可用于构建角色化 Agent，例如预设‘文档处理员’‘代码审查员’等人格模板，并支持在此基础上做轻量微调。适用于需要稳定角色行为与任务专精的本地 Agent 场景。

### 12\. 分享 mem0 本地配置经验，需修改客户端配置指向本地 Qdrant

**来源** ：Hermes Agent 中文社区微信群 8

针对 Hermes Agent 中 mem0 的集成，指出默认配置为云服务，本地部署需手动调整 mem0 获取 Qdrant 客户端的配置；适用于希望零成本、完全本地化运行记忆模块的开发者。

### 13\. Docker 化部署被证实可显著提升 Hermes 相关组件（如 mem0、Qdrant）的运维效率

**来源** ：Hermes Agent 中文社区微信群 8

有群友实践表明，将 Hermes 生态组件（含记忆服务、向量库）统一 Docker 化后，配置隔离、版本控制和故障恢复更便捷；崩溃时可快速重建容器，降低调试成本。

### 14\. DeepSeek（DS）被多位群友认为是当前国产免费模型中综合能力较优的选择

**来源** ：Hermes Agent 中文社区微信群 8

在对比豆包、Qwen、Kimi 等国产模型时，群友基于实际使用反馈指出 DeepSeek 在推理质量与响应稳定性上表现更优；适用于对免费、可直接接入的模型有较高要求的 Hermes Agent 本地实验场景。

### 15\. Hermes 使用 DeepSeek-V4 需适配新对话格式，官方提示深度思考模式下格式已变更

**来源** ：Hermes Agent 中文社区微信群 23

指出 DeepSeek-V4 开启深度思考时，API 对话格式与旧版不兼容，可能导致 Hermes 调用报错；建议检查官方文档并调整请求结构，飞书/微信等渠道均受影响。

### 16\. 国内网络搜索 Skill（如 DuckDuckGo）在 Hermes 中不可用，推荐替换为浏览器类 Skill 或国内可用搜索方案

**来源** ：Hermes Agent 中文社区微信群 23

DuckDuckGo Skill 因网络限制在国内无法调用，导致天气查询等依赖网络搜索的功能失败；建议直接更换为支持国内网络的浏览器 Skill 或自建搜索代理，无需额外配置即可生效。

### 17\. Hermes Agent默认不强制中文响应，需在系统提示词或初始化指令中明确指定语言偏好

**来源** ：Hermes Agent 中文社区微信群 23

用户反馈助手默认使用英文交互，影响使用体验；有效方法包括在配置文件中设置 system prompt 为‘始终用中文回答’，或首次对话时发送明确指令如‘请后续所有回复使用中文’。

### 18\. Hermes 可部署在非系统盘（如 D 盘或移动硬盘），WSL2 支持跨盘安装，需注意路径配置与权限。

**来源** ：Hermes Agent 中文社区微信群 22

确认 WSL2 可安装至 D 盘等非系统盘，实际可行；有用户尝试迁移 Hermes 到移动硬盘以缓解 C 盘空间压力，但需预先完成环境部署；建议使用 TreesizeFree 扫描大文件定位空间占用源。

### 19\. 腾讯 QClaw 提供免费 API 额度（当前约 800 积分/日），适合轻度 Hermes 用户接入，需配置对应环境变量。

**来源** ：Hermes Agent 中文社区微信群 22

用户验证腾讯 QClaw 当前免费额度为每日 800 积分，单次长对话消耗较低，轻度使用基本够用；配置需设置相关环境变量，但 API Key 需通过腾讯云控制台申请获取。

### 20\. 群友开源 SEO 全流程 CLI 工具 seomachine 已适配 Hermes Agent，支持关键词研究、内容评分、意图分析与竞品 SERP 分析。

**来源** ：Hermes Agent 中文社区微信群 21

该项目基于 TheCraigHewitt 的 MIT 开源项目改造，适配 Hermes Agent，包含 24 个 Python 模块、10 个独立脚本、35+ 命令/角色库，支持 Claude Code 环境，可直接集成进 Hermes 工作流。

**链接** ：

- https://github.com/Sambaba9/seomachine

---

**扫码加入 Hermes Agent 中文社区微信群**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**图片版**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Hermes Agent 中文社区日报 · 目录

继续滑动看下一个

李嘉乐的数字花园

向上滑动看下一个