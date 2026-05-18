李嘉乐 *2026年4月30日 13:31*

![图片](https://mmbiz.qpic.cn/mmbiz_png/kHh2ibPRjHicF2caUIKD8lXpTtJW18PwuoYjNbzPm8ibZ6oIlC7CibKG19UkWryHWBPUcGg8Dz4zeZTAv57HSs9VSem41ZymQ7uShwBmicOl30ib8/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

> “
> 
> 今日汇总 18 条摘要，共 3600 字，预计需要 7 分钟阅读。

### 1\. ICLR 2026 论文揭示「推理陷阱」：模型推理能力越强，工具调用幻觉越严重

**来源** ：ICLR 2026

本周在里约热内卢举办的 ICLR 2026 上发表的论文「The Reasoning Trap」指出，通过强化学习增强 LLM 推理能力的同时，会同步放大工具调用幻觉率；提示工程和 DPO 仅能部分缓解，无法根治。该发现对 AI Agent 开发者尤其重要——Deloitte 调研显示 47% 的企业 AI 用户曾基于幻觉内容做出重大业务决策。

### 2\. 多开对话可缓解上下文污染导致的推理错误

**来源** ：Hermes Agent 中文社区微信群 17

指出在 Hermes Agent 使用中，长期复用同一对话易引发上下文污染，导致响应质量下降；建议新开对话隔离上下文，该方法适用于调试与稳定性提升。

### 3\. 腾讯推出免费大模型 Hy3-Preview，可通过 OpenRouter 调用

**来源** ：Hermes Agent 中文社区微信群 5

腾讯新发布的 Hy3-Preview 模型已在 OpenRouter 平台开放免费调用，适用于 Hermes Agent 的后端模型替换或能力增强场景。

**链接** ：

- https://openrouter.ai/tencent/hy3-preview:free

### 4\. 社区启动行业垂直应用探索，正筹建 Hermes Agent 行业落地专项群

**来源** ：Hermes Agent 中文社区微信群 5

Hermes Agent 中文社区正推动行业场景落地，拟组建多个垂直领域群组，聚焦金融、IT、电商等方向的实际 Agent 应用开发与案例沉淀。

### 5\. MiniMax Token Plan 模型不支持图片识别，可通过其官方 MCP 工具弥补多模态能力

**来源** ：Hermes Agent 中文社区微信群 20

Hermes Agent 在飞书上传图片时提示模型不支持，原因是所用 MiniMax Token Plan 为纯文本模型；查阅 MiniMax 官方文档可找到配套 MCP（Model Calling Protocol）方案，用于扩展图片理解等能力。

**链接** ：

- https://platform.minimaxi.com/docs/token-plan/mcp-guide

### 6\. 局域网 Windows 服务器可通过花生壳或 Cloudflare Tunnel 实现外网访问

**来源** ：Hermes Agent 中文社区微信群 25

针对在本地 Windows 服务器部署 Hermes Agent 后需外网访问的需求，推荐两种成熟方案：花生壳（传统内网穿透服务）和 Cloudflare Tunnel（免端口映射、更安全的现代方案），均无需公网 IP。

### 7\. Hermes Agent 新增 doctor 命令，支持自动诊断与修复常见配置问题

**来源** ：Hermes Agent 中文社区微信群 14

群内明确提及 'hermes doctor --fix' 可用于问题自修复，适用于部署或运行异常时的快速排障；该功能为 Hermes 内置运维辅助命令，无需额外依赖。

### 8\. Hermes Agent 已支持原生 Windows 环境部署，硬件利用率优于 WSL 方案

**来源** ：Hermes Agent 中文社区微信群 14

确认当前版本可在 Windows 原生环境直接运行 Agent，无需依赖 WSL；实测表明，在相同硬件下，原生 Windows 部署的资源利用率显著高于 WSL 方案，适合追求性能的本地部署场景。

### 9\. OCR 处理大 PDF 效率低，实测汉王OCR与WPS OCR为可行替代方案

**来源** ：Hermes Agent 中文社区微信群 14

针对 Hermes Agent 中 OCR 模块处理多页/大体积 PDF（如 >1GB）速度慢的问题，群友验证汉王OCR桌面版和WPS OCR可作为本地替代方案；需注意WPS存在排版错乱问题，汉王OCR虽老牌但速度仍有限，建议按文档结构分片预处理后再识别。

### 10\. 本地部署推荐模型组合：Qwen3.5 和 Gemma-4 是当前主流轻量级选择，Qwen3.6-35B-A3B 已实测可玩性强

**来源** ：Hermes 中文社区 互联网/IT行业群

确认 Qwen3.5 和 Gemma-4 是本地部署的实用选择；另有群友实测本地运行 Qwen3.6-35B-A3B 模型，反馈响应稳定、可玩性高；适用于对数据隐私、离线能力或定制化有要求的场景。

### 11\. 飞书知识库问答机器人可基于 Hermes 二开实现：已验证 TypeScript + Qwen Embedding + Lark SDK + 多模态 VL 模型的端到端架构

**来源** ：Hermes 中文社区 互联网/IT行业群

群友完成手搓飞书知识库问答机器人，技术栈包括 TypeScript、Qwen 系列 embedding 模型、飞书 Lark SDK（支持 MD 卡片美化）、VL 多模态模型；当前正适配 Hermes Agent 框架，目标是封装为即插即用的一键安装包；需注意飞书外部群仅支持 Webhook 机器人。

### 12\. 国内大模型厂商对高校/学生/开发者提供免费 Token 支持：明确用途+合理申请即可获赠

**来源** ：Hermes 中文社区 互联网/IT行业群

群友经验表明，向国内大模型厂商（如硅基流动等）说明学生身份、研究/学习用途后，可获赠大量免费 API Token；无需付费、不强制数据共享、权限接近付费用户；建议通过活动、技术社区或直接联系高管渠道申请。

### 13\. Hermes Web UI 启动失败常见原因是配置文件路径错误，Windows 下应为 AppData\\Local\\hermes/ 而非 ~/.hermes/

**来源** ：Hermes Agent 中文社区微信群 21

多位群友在 Windows 环境部署 Hermes 时遇到 hermes-web-ui 显示'未连接'或网关启动报 PID 文件竞争错误（如 'PID file race lost'），经诊断确认是配置文件路径未适配 Windows 系统规范；正确路径应为 AppData\\Local\\hermes/，需手动调整或通过 hermes doctor 工具诊断定位。

### 14\. Hermes 支持复用 OpenClaw 技能，只需复制 skill 代码并适配 Hermes 的接口规范即可迁移使用

**来源** ：Hermes Agent 中文社区微信群 21

群友验证了 Hermes 兼容 OpenClaw 技能的迁移路径：将原有 OpenClaw 的 skill 文件复制到 Hermes 的 skill 目录后，通过简单修改（如调整参数声明、工具调用方式）即可在 Hermes 中正常加载和执行，降低了技能迁移成本。

### 15\. 微信端暂不支持直接发送图片给 Hermes，需转为云盘链接或使用支持多模态的模型+API 配合处理

**来源** ：Hermes Agent 中文社区微信群 21

当前 Hermes 微信接入方案会主动拦截非文本/语音内容，图片无法直接送达；可行替代方案包括：上传图片至云盘并发送链接供 Hermes 下载解析，或接入支持视觉理解的模型（如 Qwen-VL、DeepSeek-VL）并配置对应多模态 API。

### 16\. Hermes 社区推荐本地运行 Qwen3.5 模型，兼顾中文能力、推理速度与低显卡要求，适合个人开发者

**来源** ：Hermes Agent 中文社区微信群 21

多位群友在对比 DeepSeek V4、MiniMax、小米 2.5 系列等云端模型后，指出 Qwen3.5 在本地部署下表现稳定、响应快（相较 OpenClaw 快约 5 倍）、对中文任务适配好，且对消费级显卡（如 3090/4090）友好，成为主流本地部署选择。

### 17\. Hermes Workspace 可替代 Web UI 实现多 profile 并行管理，适合需切换模型/配置的进阶用户

**来源** ：Hermes Agent 中文社区微信群 21

除 hermes-web-ui 外，hermes-workspace 被群友推荐为更实用的图形化管理方案，支持创建和切换多个 profile（含不同模型、参数、技能集），避免 Web UI 功能简陋、界面不友好及配置缺失（如思考模式）等问题。

**链接**:

- https://github.com/outsourc-e/hermes-workspace

**扫码加入 Hermes Agent 中文社区微信群**

Hermes Agent 中文社区日报 · 目录

继续滑动看下一个

李嘉乐的数字花园

向上滑动看下一个