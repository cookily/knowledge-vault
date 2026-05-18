李嘉乐 *2026年4月24日 20:11*

> “
> 
> 今日汇总 18 条消息，共 2685 字，预计需要 6 分钟阅读。

### 1\. Awesome Hermes Agent 清单发布，聚合生态中近百个社区项目

**来源** ：X @NFTCPS

社区维护的 awesome-hermes-agent 清单仓库收录 Hermes Agent 生态的插件、工具、教程与示例项目；据作者 @NFTCPS 披露，Atlas 当前实时监测 98 个社区项目。

**链接** ：

- https://github.com/0xNyk/awesome-hermes-agent

### 2\. 优云智算上线国产模型 CodingPlan 套餐，支持 Hermes Agent，49 元/月起，按次调用

**来源** ：Hermes Agent 中文社区微信群 6

优云智算新上线面向 Hermes Agent 的 DeepSeek-V4 模型服务套餐，提供按次调用与包月两种计费方式，强调国产模型部署的高性价比。

**链接** ：

- https://passport.compshare.cn/register?referral\_code=K50gMvv85OmEJ5T9ZDUtDE&yatg=GPU\_YY\_YX\_hermesagent.org.cn

### 3\. Hermes Agent 对中文理解能力与底层模型强相关，Gemma-4 等非中文强优化模型可能出现中文识别异常

**来源** ：Hermes Agent 中文社区微信群 12

使用 Gemma-4 等未针对中文微调的模型时，Hermes 可能出现中文指令理解失败问题；建议优先选用 Qwen3、DeepSeek-V4 等中文能力更强的模型。

### 4\. 推荐开源智能爬虫工具 KaiyueLv Smart Crawler，可应对部分反爬机制

**来源** ：Hermes Agent 中文社区微信群 11

针对反爬网站抓取需求，群内分享 KaiyueLv Smart Crawler 工具（ClawHub 镜像站），支持本地化部署与智能策略调度，适用于 Hermes Agent 中需动态采集网页数据的场景。

**链接** ：

- https://cn.clawhub-mirror.com/kaiyuelv/smart-crawler

### 5\. DeepSeek-V4 已开源，1600B 参数 MoE 架构，优云智算提供商用 API 服务。

**来源** ：Hermes Agent 中文社区微信群 10

DeepSeek-V4 正式开源，采用 A49B MoE 架构；优云智算上线其 CodingPlan 套餐（49 元/月起），支持按次调用；本地部署可结合 LM Studio 或 Ollama。

**链接** ：

- https://passport.compshare.cn/register?referral\_code=K50gMvv85OmEJ5T9ZDUtDE&yatg=GPU\_YY\_YX\_hermesagent.org.cn

### 6\. 推荐使用 Playwright 参数化方案实现 Hermes Agent 对 Windows 桌面应用的自动化操控

**来源** ：Hermes Agent 中文社区微信群 19

针对 Hermes Agent 在 Windows 环境下难以接管屏幕、启动软件的问题，提出通过 Playwright 进行参数化控制的实践路径，可绕过内置浏览器限制，直接调用系统已安装的浏览器或应用，提升自动化鲁棒性。

### 7\. 可试用 Chrome 插件 actionbookchromewebstore 实现 Hermes Agent 对浏览器的无侵入式操作

**来源** ：Hermes Agent 中文社区微信群 19

该插件支持直接操作用户日常使用的 Chrome 浏览器，避免新建实例或环境隔离问题，适用于需保持登录态、Cookie 或扩展依赖的自动化场景（如小红书登录后操作）。

**链接** ：

- https://github.com/actionbookchromewebstore.googledetail/bebchpafpemheedhcdaaifcijmfo

### 8\. 推荐使用 mmx-cli 工具解决 Minimax API 图片识别调用失败问题。

**来源** ：Hermes Agent 中文社区微信群 8

针对 Minimax 订阅用户在 Hermes 中调用图片识别能力失败的问题，建议安装并配置 mmx-cli 命令行工具，可绕过原生集成限制，稳定调用 Minimax 多模态能力。

### 9\. SCALE OS v10.0 认知操作系统发布，专为 AI 编码设计，支持脚手架、反幻觉等机制。

**来源** ：Hermes Agent 中文社区微信群 8

SCALE OS 是面向 AI 编程场景的操作系统级框架，通过‘脚手架’快速生成项目结构、‘反幻觉惰性’抑制模型胡说、‘求是’机制强化事实校验，已支持 5 大平台，可分钟级生成专属 AI 工程配置方案。

**链接** ：

- https://scale-os.hongmaple.top/

### 10\. Hermes 支持通过 Custom Provider 手动配置 DeepSeek V4 Flash/Pro，可正确显示模型名并调用对应版本

**来源** ：Hermes Agent 中文社区微信群 18

使用 Custom Provider 类型，手动填写 DeepSeek V4 API 地址与密钥后，Hermes 可正确识别并显示 deepseek-v4-flash 或 deepseek-v4-pro 模型名，避免官方 provider 的命名映射问题，适用于需明确区分思考/执行模式的场景。

### 11\. WSL2 不建议手动迁移至非系统盘，易引发启动失败与稳定性问题

**来源** ：Hermes Agent 中文社区微信群 18

实测将 WSL2 发行版（如 Ubuntu）从默认 C 盘移至 D 盘后出现频繁崩溃；原因在于 WSL2 与 Windows 系统深度耦合，微软未开放安全迁移机制，推荐保持默认路径或改用云服务器/虚拟机方案。

### 12\. Hermes Agent 客户端更新至 v0.11.0，支持 DeepSeek-V4 模型接入

**来源** ：Hermes Agent 中文社区微信群 2

群内确认 Hermes Agent 已发布 v0.11.0 版本（2026.4.23），同步适配刚发布的 DeepSeek-V4 模型；用户需更新客户端并等待灰度推送，付费 Plus 用户已全部完成更新。

### 13\. 推荐使用 llm-wiki 模式管理 Hermes 知识库，Qdrant 可作为向量化笔记工具。

**来源** ：Hermes Agent 中文社区微信群 9

群友实践表明，将知识以自然语言 Markdown 形式沉淀（如 llm-wiki）比纯向量 RAG 更可控；Qdrant 被用于构建 Hermes 可检索的向量化笔记库，兼顾语义检索与人工可读性。

### 14\. 图片类知识建议先由 VLM 生成带标签的文字摘要，按需调用 VLLM 进行现场解析。

**来源** ：Hermes Agent 中文社区微信群 9

针对多模态知识库中图片处理，推荐使用 VLM（如 Qwen-VL、LLaVA）生成结构化文字描述并打标签；大容量场景下可先摘要存储，实际调用时再触发 VLLM 进行高精度解析，兼顾效率与准确性。

### 15\. RAG-Anything 开源项目支持多模态 RAG，含图片、PDF、音视频等异构数据处理能力。

**来源** ：Hermes Agent 中文社区微信群 9

RAG-Anything 是一个面向多模态文档的 RAG 框架，支持自动解析图像（OCR+VLM描述）、PDF、音视频等格式，并构建统一向量索引；配套论文 arXiv:2510.12323 已发布。

**链接** ：

- https://github.com/HKUDS/RAG-Anything
- https://arxiv.org/abs/2510.12323

### 16\. 推荐使用 /plan 指令引导大模型先分析与优化需求再执行，可缓解非技术用户提不合理需求导致的无效编程问题

**来源** ：Hermes Agent 中文社区微信群 14

针对非程序员用户易提出模糊或不可行需求的问题，实践表明：在调用如 Kimi 2.5 等模型前，先使用 /plan 指令触发需求分析与方案调研，能显著提升任务合理性与执行效率；该方法依赖模型自身推理能力，但可作为通用工作流前置环节。

### 17\. 分享 Andrej Karpathy 提出的反幻觉四原则技能库（中文版），含脚手架、反幻觉惰性、求是等机制，助力构建可靠 Agent 技能

**来源** ：Hermes Agent 中文社区微信群 14

该开源技能库基于 Karpathy 提出的认知设计原则，提供结构化技能模板与实践指南，适用于 Hermes 等 Agent 框架中技能开发；强调需求分析前置、执行约束与结果验证，可降低幻觉与冗余调用。

**链接** ：

- https://github.com/forrestchang/andrej-karpathy-skills/blob/main/README.zh.md

### 18\. Hermes 支持 /resume 指令恢复历史对话，解决重启后对话丢失问题。

**来源** ：Hermes Agent 中文社区微信群 21

针对群友反馈的每次重启 Hermes 后对话历史清空问题，多位用户确认可通过输入 /resume 命令自动检索并恢复最近会话；搭配 /title 指令可进一步提升对话管理效率。

扫码加入中文社区微信群

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Hermes Agent 中文社区日报 · 目录

继续滑动看下一个

李嘉乐的数字花园

向上滑动看下一个