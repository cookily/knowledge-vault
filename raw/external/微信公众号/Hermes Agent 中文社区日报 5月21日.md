李嘉乐的数字花园 *2026年5月21日 07:42*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kHh2ibPRjHicExRd9c8kUqcCLPcjZTj210scMJCzCcVZ5uTshIJVAiaZ0HE3oEK91IlZEZHSjkvxohSziaYLxibzAhJQan5xdOhiabYIURBQsP3u8/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

> “
> 
> 今日汇总 20 条消息，共 2614 字，预计需要 6 分钟阅读。

### 1\. 社区实测推荐 Opencode GO 订阅 + DeepSeek 高性价比模型接入方案

**来源** ：Hermes Agent 中文社区微信群 6

实测反馈Kimi等模型易触发限流且官方定价较高。建议通过Opencode GO（首月5美元起）等第三方订阅服务接入DeepSeek以降低成本，小米模型API在闲鱼亦有低价方案，适合追求性价比的用户。

**链接** ：

- https://opencode.ai/go

### 2\. 群友分享 Hermes 结合 MT5 实盘量化交易策略

**来源** ：Hermes 中文社区 金融 量化 财会

群友分享了基于 Hermes 的实盘量化策略，运行于 MT5 平台，近两月完成约1800笔交易，多空胜率约70%，当前累计收益约46%。高频交易需重点考虑滑点与手续费影响，该策略的实盘数据可通过Myfxbook平台进行公开监测，支持夏普率、平均持仓时间等多维指标分析。股市有风险，投资请谨慎。该消息摘要不构成投资建议。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**链接** ：

- https://www.myfxbook.com/members/weiyen/ai-trading/11999681

### 3\. 分享Agent开发工作流：先用“Grill me”技能梳理需求，优化提示词，再让Agent直接生成代码

**来源** ：Hermes Agent 中文社区微信群 38

在使用Agent开发应用时，推荐首先使用“Grill Me”技能，引导Agent深入追问，明确需求细节与架构设计，待方案清晰后再交由Agent编程，这种工作流能有效减少返工，提高效率。

**链接** ：

- https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me

### 4\. 16G显存本地部署Hermes的显存估算与模型选择建议

**来源** ：Hermes Agent 中文社区微信群 30

Hermes运行需至少64K上下文，显存需求可按FP16约2G/1B参数、Q4量化约0.5G/1B参数估算，KV Cache 会随上下文长度近似线性增加，长上下文会显著增加显存占用。 Hermes本地部署务必选择带-it或-instruct后缀的指令微调模型以支持工具调用，老旧模型普遍缺乏工具调用能力。另推荐CanIirun.ai网站，可快速估计自己的设备能本地部署哪些模型，链接见公众号。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**链接** ：

- https://www.canirun.ai/device/rtx-5080

### 5\. 使用 /goal 指令可改善 Hermes 任务中途停止或过度劝阻的现象

**来源** ：Hermes Agent 中文社区QQ群

针对 Hermes 在执行长流程任务时容易中途放弃或频繁给出安全建议的情况，使用 /goal 命令能强化目标约束，促使模型持续执行直至完成。该技巧适用于长程运行的复杂目标。

### 6\. 群友开源 Hermes 飞书客户端汉化项目 hermes-feishu-zh

**来源** ：Hermes Agent 中文社区QQ群

中文社区开发者发布了针对 Hermes 飞书集成版本的轻量级汉化项目。该项目主要对客户端界面文本进行本地化处理，降低中文用户的使用门槛，适合有飞书端部署需求的开发者直接集成或参考二次开发。

**链接** ：

- https://github.com/OLDBAI213/hermes-feishu-zh

### 7\. 社区推荐第三方Hermes桌面客户端hermes-desktop

**来源** ：Hermes Agent 中文社区微信群 45

非官方开源桌面端项目，GitHub Star数较高且经实测可用。支持windows，适合需要独立桌面环境运行Agent的用户。

**链接** ：

- https://github.com/fathah/hermes-desktop

### 8\. 可要求Hermes读取OpenHuman源码，自动生成LLM智能路由Skill

**来源** ：Hermes Agent 中文社区微信群 50

可让Hermes直接分析OpenHuman的LLM智能路由源代码，并自动改写生成自定义Skill。该Skill能实现按任务类型动态路由模型，如图片处理调用Kimi、代码生成调用DeepSeek-V4-Pro、日常对话使用默认模型。

### 9\. 本地大模型部署建议与免费图像识别方案

**来源** ：Hermes Agent 中文社区微信群 51

本地运行满血版大模型对硬件要求极高，显存不足时建议优先使用量化版本。图像识别任务可接入OpenRouter提供的免费Gemma 4模型，兼顾成本与效果。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**链接** ：

- https://openrouter.ai/google/gemma-4-31b-it:free

### 10\. Hermes多Agent协作需通过AGENTS.md明确边界并配合kanban管理

**来源** ：Hermes Agent 中文社区微信群 46

实现多Agent协作的核心在于使用AGENTS.md文件为每个节点定义清晰的工作边界与角色设定。配置完成后可通过kanban命令实时查看任务看板与流转状态。建议结合提示词优化器生成结构化Prompt，并为不同角色分配独立用户画像以提升复杂任务的拆解与执行效率。

**链接** ：

- https://notebooklm.google.com/notebook/ff19a1e2-f478-4128-8232-9135c18afda2
- https://prompt.always200.com/#/basic/system

### 11\. 企业级Agent记忆系统架构建议与上下文管理方案

**来源** ：Hermes Agent 中文社区飞书群 1

不建议新手使用简单提示词分层构建记忆系统，易快速耗尽上下文窗口。企业级项目推荐采用LoRA微调、多模态RAG或llm-wiki按需召回机制。若需长上下文支持，可选用记忆压缩能力强的模型或原生支持1M上下文的模型。

### 12\. 利用网页版大模型替代API调用可节省费用但仅支持纯文本对话

**来源** ：Hermes Agent 中文社区微信群 46

通过Agent模拟浏览器行为调用网页版大模型接口可实现零Token消耗，该方案属于奇技淫巧，可零成本完成不太重要的任务。而且仅支持基础文本交互，无法触发Hermes的工具调用与技能执行。另外需要注意，这种方案通常存在响应延迟，限流或者触发反风控机制等问题，仅供参考。

### 13\. 飞书流式卡片插件开源项目与配置指南

**来源** ：Hermes Agent 中文社区飞书群 1

社区分享了两个Hermes飞书流式卡片插件项目，支持在话题内稳定输出流式消息并美化消息样式。可显著提升交互体验，建议自行选用安装。

![Hermes Feishu Streaming Card 封面](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Hermes Feishu Streaming Card 封面

**链接** ：

- https://github.com/Cheerwhy/hermes-lark-streaming
- https://github.com/baileyh8/hermes-feishu-streaming-card

### 14\. 使用免费API中转站的安全风险提示

**来源** ：Hermes Agent 中文社区飞书群 1

Hermes拥有较高系统权限，使用非官方免费中转站存在严重安全隐患。中转站可能实施提示词注入攻击，并明文记录上传的API Key、钱包私钥、隐私数据及代码。建议优先使用官方直连或可信渠道，避免敏感数据泄露。

### 15\. 推荐AI音乐生成工具Suno支持提示词直接创作

**来源** ：Hermes Agent 中文社区微信群 49

分享音乐生成平台Suno，用户只需输入文本提示词即可自动生成完整音乐作品，适合内容创作与多媒体Agent集成场景。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**链接** ：

- https://suno.com/

### 16\. 调用智谱API防429限流的并发控制经验

**来源** ：Hermes 中文社区 互联网 IT 软件

高频调用智谱API时易触发429错误，实测将并行子任务限制在3个以内，并在请求间增加1秒sleep间隔，可有效避免限流，保障任务稳定运行。

### 17\. Gemini Deep Research更新支持通过MCP对接专有数据

**来源** ：Hermes 中文社区 互联网 IT 软件

谷歌最新更新的Deep Research功能已支持MCP协议，允许Agent直接访问企业内部或专有数据源，提升了深度调研的准确性与数据安全性。

**链接** ：

- https://blog.google/innovation-and-ai/modelsresearch/gemini-/next-generdeep

### 18\. VS Code/ACP/兼容接口配置经验

**来源** ：Hermes 中文社区 互联网 IT 软件

针对ACP插件默认仅支持本地Agent的问题，社区分享了通过特定配置实现云端连接的详细教程，解决了插件对接远程服务的痛点。

**链接** ：

- https://github.com/formulahendry/vscode-acp

### 19\. CLI 中模型修改代码未生效时，可提示其通过 Git 读取未提交变更

**来源** ：Hermes Agent 中文社区微信群 35

使用 deepseekpro 等模型在 CLI 中修改代码时，若出现文件未实际更新或审查提示未修改的情况，通常无需额外安装 Skill。直接在对话中明确指示 Agent 使用 Git 读取未提交的代码变更，或让其检查 Git 状态即可解决。

### 20\. Hermes Agent多智能体协作配置经验与delegate\_task使用避坑

**来源** ：Hermes Agent 中文社区微信群 48

复杂工作流建议采用子智能体并行协作，简单任务则单智能体处理即可。Hermes Agent的看板功能配合delegate\_task适用于临时并行任务调度，但长期使用易引发记忆污染问题，建议控制使用周期或定期清理上下文。

扫码加入 Hermes Agent 中文社区微信群

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**微信扫一扫赞赏作者**

Hermes Agent 中文社区日报 · 目录

继续滑动看下一个

李嘉乐的数字花园

向上滑动看下一个