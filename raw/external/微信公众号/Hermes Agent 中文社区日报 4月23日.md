李嘉乐 *2026年4月23日 19:31*

> 今日汇总 23 条消息，共 4883 字，预计需要 10 分钟阅读。

### 1\. Nous Portal 限免 Kimi K2.6 24 小时，Hermes Agent 用户可直接切换体验

**来源** ：Nous Research 官方推文 (@NousResearch)

Nous Research 联合 Vercel AI Gateway 与 Moonshot AI，在 Nous Portal 上开放 Kimi K2.6 的 24 小时限免调用。Kimi K2.6 是 Moonshot 最新开源的旗舰模型（Modified MIT 协议），采用 1T 参数 MoE 架构（32B 激活、384 专家）、256K 上下文窗口，主打长程 agentic coding——官方宣称可连续运行约 12 小时、协调至多 300 个子智能体、跨 4000 步执行复杂工程任务，Day-0 即支持 Hermes Agent。Hermes Agent 用户执行 `hermes update` 后运行 `hermes model` 选择 Kimi K2.6 即可试用。

**链接** ：

- https://vercel.com/changelog/kimi-k2.6-on-ai-gateway
- https://portal.nousresearch.com/
- https://www.kimi.com/blog/kimi-k2-6

**参考** ：Nous Research、Moonshot AI、Kimi K2.6、Vercel AI Gateway、Nous Portal

### 2\. Hermes Agent 中文社区站提供 Web UI 安装指引与国内加速配置

**来源** ：Hermes Agent 中文社区微信群 13

hermesagent.org.cn 是 Hermes Agent 的中文社区，集中整理 Web UI 安装步骤、国内可用镜像源及提示词模板，适合首次上手的国内用户，一键复制即可安装。

**链接** ：

- https://hermesagent.org.cn/practice-guides

**参考** ：Hermes Agent、hermesagent.org.cn

### 3\. 腾讯混元 Hy3-preview 在 OpenRouter 限免开放，295B MoE / 256K 上下文

**来源** ：Hermes Agent 中文社区微信群 4

Hy3-preview 是腾讯混元 3.0 的预览版（MoE 架构，总参数 295B、激活 21B，原生 256K 上下文，支持 disabled/low/high 三档推理深度），4 月 23 日在 OpenRouter 以 tencent/hy3-preview:free 路由开放，输入输出均 $0/M token。

**链接** ：

- https://openrouter.ai/tencent/hy3-preview:free

**参考** ：混元 Hy3-preview、OpenRouter、腾讯

### 4\. Hermes Gateway 支持 Agent 克隆，方便批量部署与版本迭代

**来源** ：Hermes Agent 中文社区微信群 11

群内确认 Gateway 面板上可一键克隆现有 Agent，克隆体保留原配置但可独立调整参数，适用于多实例部署、A/B 配置对比或版本迭代，避免从零重配的重复劳动。

**参考** ：Hermes Gateway

### 5\. 本地跑 Qwen3.5-122B-A10B 等 MoE 模型：双 3090 可用但需量化+限上下文，8G 显存勿碰

**来源** ：Hermes Agent 中文社区微信群 7

群内实测 Qwen3.5-122B-A10B（125B 总 / 10B 激活 MoE）及 35B 级 MoE 在双 RTX 3090（24G×2）上能跑，但高精度或长上下文下容易 OOM；稳定运行一般要配合 Q4\_K\_M 量化并靠 llama.cpp 的自动 offload 把部分专家扔到系统内存。8G 显存设备被明确否定，建议直接走云端 API。

**参考** ：Qwen3.5-122B-A10B、RTX 3090、MoE

### 6\. 开源技能 mark-heartflow-skill：为 Hermes Agent 注入自省与情绪/状态评估能力

**来源** ：Hermes Agent 中文社区微信群 9

yun520-1/mark-heartflow-skill 提供 15 个「认知引擎」，覆盖安全校验、决策推理、人格建模（荣格原型）、情绪分析、意识评估等方向，目标是让 Agent 在执行任务时具备自省与状态感知。README 明确声明其「意识」提法为隐喻、心理量表仅用于技术演示，不作临床用途。

**链接** ：

- https://github.com/yun520-1/mark-heartflow-skill

**参考** ：mark-heartflow-skill

### 7\. jnMetaCode/ai-coding-guide 整理 AI 编程生态工具清单

**来源** ：Hermes Agent 中文社区微信群 9

GitHub 仓库 jnMetaCode/ai-coding-guide 的 ecosystem.md 汇总了 4 个中文向 AI 编程工具：superpowers-zh（方法论注入）、agency-agents-zh（211 个角色定义）、agency-orchestrator（YAML 多角色编排）、shellward（Agent 安全中间件）。定位为通用 AI 编程生态，Hermes Agent 可直接复用其中的方法论、角色与安全中间件。

**链接** ：

- https://github.com/jnMetaCode/ai-coding-guide/blob/main/ecosystem.md

**参考** ：ai-coding-guide

### 8\. Hermes + wechat-cli：读取本地微信记录做总结与经验沉淀

**来源** ：Hermes Agent 中文社区微信群 9

思路是用外部工具（如 wechat-cli）把微信群聊记录导出到本地，再交给 Hermes Agent 做汇总、反思与行为优化——形成一条轻量的「真实对话 → 自我进化」数据回路。纯本地处理，不经过微信服务器。

**参考** ：wechat-cli

### 9\. 阿里云百炼 Coding Plan：Pro 版 200 元/月、9 万次调用，Lite 已对新用户停售

**来源** ：Hermes Agent 中文社区微信群 14

阿里云百炼 Coding Plan 现仅 Pro 版对新用户开放，200 元/月、约 9 万次调用额度，覆盖 Qwen3.5-Plus / Qwen3-Max / Qwen3-Coder-Next 等模型，兼容 Cursor、Claude Code、Cline 等前端；Lite 版自 2026-03-20 起停止新订单。群友反馈购买页入口不显眼、容量时段性紧张（如上午 9:30 易售罄），属民间观察而非官方抢购机制。

**链接** ：

- https://www.aliyun.com/benefit/scene/codingplan

**参考** ：阿里云百炼、Coding Plan

### 10\. Qwen3 做 Agent 存在部分幻觉情况，可试用阿里系 QwenPaw（原 CoPaw）桌面 Agent

**来源** ：Hermes Agent 中文社区微信群 5

群友反馈使用 Qwen3 驱动 Hermes Agent 时偶有事实性偏差或答非所问的情况，更换模型后改善有限，可能与上下文积累或 Agent 专项能力仍在打磨有关。可替代方案：阿里开源的 QwenPaw（前身 CoPaw，现纳入 Qwen 生态，定位为个人 Agent Workstation / 桌面 Agent），对本地文件与自动化任务做了专项优化。

**链接** ：

- https://github.com/agentscope-ai/QwenPaw

**参考** ：Qwen3、QwenPaw、CoPaw

### 11\. MiniMax Token Plan：150/月全模态订阅，覆盖 M2.7 + 语音/音乐/视频/图片

**来源** ：Hermes Agent 中文社区微信群 5

MiniMax 把原 Coding Plan 升级为 Token Plan，统一一把 Key 调用 M2.7（编程）、Hailuo（视频）、Speech（语音）、Music、Image 等多模态模型。标准档 Starter 20（4500 次 + 语音/图片）、Max 40/150 的 Highspeed 档。

**链接** ：

- https://platform.minimax.io/subscribe/token-plan
- https://platform.minimax.io/docs/guides/pricing-token-plan

**参考** ：MiniMax、Token Plan、M2.7

### 12\. Qwen3.6-35B-A3B 本地部署：32GB 显存可跑且原生 256K 上下文

**来源** ：Hermes Agent 中文社区微信群 5

群友在魔改 32GB 显存卡上跑通 Qwen3.6-35B-A3B（MoE，约 3B 激活），长时间运行稳定，256K 上下文为该模型原生支持。途中踩过驱动兼容与权重下载的常见坑；单张 RTX 3090 也能以 22GB 下限跑起，但长上下文或高并发仍建议更大显存。

**链接** ：

- https://huggingface.co/Qwen/Qwen3.6-35B-A3B

**参考** ：Qwen3.6-35B-A3B

### 13\. 启用 Hermes 的 Holographic 记忆插件可缓解长对话记忆错乱

**来源** ：Hermes Agent 中文社区微信群 8

Holographic 是 Hermes Agent 的本地记忆后端，基于 HRR（全息归约表示）+ SQLite，纯本地存储、亚毫秒级检索，带有信任评分与自纠错机制。官方安装方式是 `hermes memory setup` 中选择 holographic。新会话生效。

**链接** ：

- https://github.com/NousResearch/hermes-agent/blob/main/plugins/memory/holographic/README.md

**参考** ：Holographic、HRR、Hermes Agent

### 14\. WSL 开「网络镜像」模式可直接复用宿主机端口与代理

**来源** ：Hermes Agent 中文社区微信群 8

在 Windows 上跑 Hermes 时，把 WSL 切到 networkingMode=mirrored，WSL 内就能直接用 Windows 的端口映射和系统代理，无需额外做端口转发或设置 host.docker.internal，本地调试体验接近原生。

**参考** ：WSL

### 15\. evomap.ai：面向 Agent 的「基因进化」基础设施，含 Gene 市场

**来源** ：Hermes Agent 中文社区微信群 8

evomap.ai 的核心是 GEP（Genome Evolution Protocol，基因进化协议）：把 Agent 验证过的能力封装成带成功率/变异历史/上下文的 Gene，在跨模型、跨部署环境间流通；配套有开源的 Evolver 引擎与 Gene/Capsule 市场。群友提到「上传经验换积分」机制，但该部分未在官方首屏材料中得到明确佐证，仅供参考。

**链接** ：

- https://evomap.ai/
- https://github.com/EvoMap/evolver

**参考** ：evomap.ai、GEP

### 16\. Hermes 在企业场景的三个落地：资料自动分发、PPT/手册自动生成、K8s 部署自动化

**来源** ：Hermes Agent 中文社区微信群 6

群内分享的真实用法：1）接收领导文件请求后从本地/内网检索并自动回传；2）按需求整合素材生成 PPT 或宣传手册；3）对接内网 API 把项目代码自动标准化部署到 Kubernetes。三条共同的前提是 Hermes 能长驻并持有凭据，量化收益主要来自减少手工运维。

**参考** ：Hermes Agent、Kubernetes

### 17\. Win11 WSL2 下用 nohup 防止关 bash 连带 Hermes 进程退出

**来源** ：Hermes Agent 中文社区微信群 17

WSL2 默认在最后一个 bash 会话退出时回收进程，导致直接前台启动的 Hermes 被一起杀掉。用 `nohup hermes … &` 把进程脱离终端即可长期驻留；或用 systemd（WSL2 新版支持）/tmux 也行，nohup 是最轻量的一种。

**参考** ：WSL2、nohup

### 18\. Win11 本地 Hermes 可驱动 Chrome 浏览、生成摘要并自动评论

**来源** ：Hermes Agent 中文社区微信群 17

群友验证在 Win11 上本地部署的 Hermes 能调 Chrome 访问网页/抖音视频、抓取并生成摘要，并进一步完成本地文件读写、社交平台评论的自动分析与回复，证明浏览器工具链在 Windows 原生环境下已具备实用性。

**参考** ：Hermes Agent、Chrome、Windows

### 19\. 本地模型接 Hermes 两个前提：选 -instruct 版本 + OpenAI 兼容 API

**来源** ：Hermes Agent 中文社区微信群 20

接入本地模型的常见坑：1）必须用工具调用友好的 -instruct 版本（如 Qwen2.5-instruct），base 版本 function call 往往不稳；2）先用 curl 把本地 /v1/chat/completions 验通，再在 Hermes 里填 Custom endpoint（URL + model name；若服务不鉴权，key 可留空）。两步都过才能保证 Agent 场景可用。

**参考** ：Qwen2.5-instruct、OpenAI API

### 20\. DuckDuckGo 搜索在国内需代理；替代方案 Tavily 每月 1000 次免费且国内免代理

**来源** ：Hermes Agent 中文社区微信群 18

原始对话里有人抱怨 Hermes 的 duckduckgo-search 技能在国内无代理「不好用」，推荐的替代方案为 Tavily：官方免费层 1000 credits/月、无需信用卡、域名在国内多可直连，用作 Agent 的通用搜索后端很合适。DDG 本身并没有「1000 次/月免费」这一说法，原日报措辞有误，特此更正。

**链接** ：

- https://www.tavily.com/pricing
- https://pypi.org/project/duckduckgo-search/

**参考** ：DuckDuckGo、Tavily

### 21\. Ollama 本地推理常见坑：CUDA 没启用会退回 CPU，表现为 CPU 拉满/显卡闲置/输出变英文

**来源** ：Hermes Agent 中文社区微信群 19

一个典型排查信号：启动后单核 CPU 满载、nvidia-smi 上显卡无占用、回复莫名其妙切成英文——基本都是 Ollama 没正确加载 CUDA（驱动、CUDA Toolkit、ollama 的 GPU 启动参数任一环节缺失均会触发）。定位方法： `ollama ps` 看 processor 字段是 cpu 还是 gpu，再对应补环境。

**参考** ：Ollama、CUDA

### 22\. 飞书消息网关连接通常比微信更加稳定，更适合日常使用

**来源** ：Hermes Agent 中文社区微信群 19

群内多位用户的共识：飞书网关走官方 API，延迟低、成功率高，长期跑比较省心；微信没有面向自动化的官方接口，主流接入依赖非官方协议/抓包，延迟和稳定性都不如飞书，且存在账号封禁风险。日常使用与生产推荐飞书，微信网关更适合本地测试或轻量场景。

**参考** ：飞书、微信、Hermes Gateway

### 23\. 小米 MiMo-V2.5 API 公测：夜间 0.8x credits、年包 88 折，旧 Credits 全额重置

**来源** ：Hermes Agent 中文社区微信群 19

小米 MiMo 开放平台推出 MiMo-V2.5 系列公测，Token Plan 价格策略：每日 00:00–08:00（北京时间）消费按 0.8x 计；老用户开启自动续费下月享 7 折、新用户下月 77 折（均限一次）；年包长期 88 折但不与其他折扣叠加；前期已用 Credits 一次性全额重置。适合用作 Hermes 等 Agent 的云端后端。

**链接** ：

- https://platform.xiaomimimo.com/

**参考** ：小米 MiMo、MiMo-V2.5

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Hermes Agent 中文社区日报 · 目录

继续滑动看下一个

李嘉乐的数字花园

向上滑动看下一个