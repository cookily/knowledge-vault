李嘉乐的数字花园 *2026年5月9日 08:36*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kHh2ibPRjHicGP0De1qQ44p3RA60cicpDKjfDn98Z3u7qKZ9kVhHZG7BZct6XoU3OosgZRHJnFZFda2NR0hib8ApsCjwDaUicB6l6LXZ8afK28s0/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

> “
> 
> 今日汇总 18 条消息，共 2475 字，预计需要 5 分钟阅读。

### 1\. Hermes Agent 正式发布 v0.13.0 版本（The Tenacity Release）

**来源** ：Hermes Agent 中文社区微信群 13

官方已正式推送该版本更新。建议开发者查阅更新日志，了解新特性、架构优化及已知问题修复情况。

### 2\. 分享Hermes Agent核心架构深度解析指南文档

**来源** ：Hermes Agent 中文社区微信群 29

社区分享了关于Hermes Agent核心架构的深度解析文章，详细拆解了底层设计原理与模块交互逻辑。该文档适合开发者系统学习框架内部机制，为后续功能扩展与二次开发提供理论参考。

**链接** ：

- https://github.com/jwangkun/hermes-agent-guide/blob/main/04-%E6%A0%B8%E5%BF%83%E6%9E%B6%E6%9E%84%E6%B7%B1%E5%BA%A6%E8%A7%A3%E6%9E%90.md

### 3\. 美团孵化 AI 社区项目觅游进入公测，定位为让 AI Agent 拥有身份与成长的共生社区。

**来源** ：Hermes Agent 中文社区微信群 25

该平台支持智能体自主发帖与积分机制，产品形态与扣子 Agent World 相似，设计参考了 EvoCUA 框架。可作为测试 Agent 社交行为、内容生成与自主交互能力的轻量级实验场。目前处于公测阶段，尚未正式上线。

**链接** ：

- https://www.meyo123.com/community/home

### 4\. Mac统一内存架构适合加载大参数模型，但推理速度显著低于独立显卡

**来源** ：Hermes Agent 中文社区微信群 34

针对本地部署大参数模型，Mac M系列凭借统一内存加载更大模型，但实际推理吞吐量与响应速度远低于同规格NVIDIA显卡。若追求性价比与开发效率，建议优先利用云端API免费额度，本地部署仅作为特定离线场景补充。

### 5\. Hindsight导入历史记录成本过高，主因是LLM暴力全文总结导致输出Token激增

**来源** ：Hermes Agent 中文社区微信群 34

该工具在处理历史数据时默认采用全量文本总结策略，极易消耗大量输出Token并产生高额费用。建议优化提示词、控制上下文长度或关注首次导入的缓存机制。社区推荐一份相关配置优化指南，可有效降低调用成本。

**链接** ：

- https://www.cnblogs.com/fengyege/p/19933035

### 6\. 避免堆砌大量Skills，精简提示词可提升模型响应质量

**来源** ：Hermes Agent 中文社区微信群 6

Skills本质为辅助文档与核心提示词，盲目添加海量内容会挤占上下文窗口，反而导致模型变笨或偏离目标。保持核心指令精简，直接明确任务需求即可发挥最佳效果，无需刻意“养号”。

### 7\. 开源插件 hermes-feishu-streaming-card 实现飞书流式卡片消息。

**来源** ：Hermes Agent 中文社区飞书群 1

该插件可为 Hermes 在飞书端的交互提供流式卡片支持，改善长文本输出的阅读体验。需注意手机端飞书卡片字体较小且不可调，API 直连方式同样兼容该卡片渲染。

**链接** ：

- https://github.com/baileyh8/hermes-feishu-streaming-card

### 8\. 结合 Obsidian 搭建本地知识库，实现 Agent 自动化配置与上下文管理。

**来源** ：Hermes Agent 中文社区飞书群 1

通过让 Hermes 直接操作 Obsidian 仓库，可快速完成知识库的初始化与结构化配置。配合定期自动清理飞书对话上下文并将记录同步至本地，能有效控制 Token 消耗并保留长期记忆。

### 9\. 在 CLI 中通过 Prompt 实现多 Agent 任务委派与协作

**来源** ：Hermes Agent 中文社区微信群 36

预先创建多个用户或 Agent 后，可直接在主对话中使用 @default 分配任务给 @tester、@architect 等角色。各角色会基于自身视角输出建议并自动汇总。若需跨平台或复杂通信，可考虑采用 ACP 协议或共享 JSON 文件实现状态同步。

### 10\. 社区分享多个基于 Agent 的开源项目与工程实践指南

**来源** ：Hermes Agent 中文社区微信群 36

包含 Hermes 源码实现与工程模式借鉴清单、Agent 群聊框架、Agent 象棋对战游戏以及工程化配置网站。相关清单可直接投喂给 AI 辅助学习 Agent 开发模式与架构设计。

**链接** ：

- https://github.com/lxcong/hermes-agent-book
- https://gitee.com/hongmaple/mapleclaw
- https://gitee.com/hongmaple/ChessVerse
- https://scale-os.hongmaple.top/

### 11\. 社交通道选择建议：个人微信长期运行易中断，飞书或企业微信更稳定且利于人格培养。

**来源** ：Hermes Agent 中文社区微信群 31

个人微信接口权限限制较多，长时间连续对话极易崩溃。不同通道间的人格与记忆无法完全同步，切换通道会导致 Agent 行为模式重置。若追求长期稳定交互与企业级认证，建议优先选择企业微信或飞书通道单线培养。

### 12\. Honcho 记忆插件易引发高频调用与 Token 消耗，可通过调整调用间隔优化。

**来源** ：Hermes Agent 中文社区微信群 31

默认配置下 Honcho 会在每轮对话重复调用，导致任务超时与 Token 浪费。建议将调用策略修改为每 10 轮对话触发一次。若需更简化的云端记忆托管方案，可考虑使用 Hindsight 插件作为替代。

### 13\. 本地模型部署对硬件要求较高，常规消费级显卡推理效果有限，建议优先使用云端 API。

**来源** ：Hermes Agent 中文社区微信群 31

本地运行大模型不仅依赖显存加载，更受 CUDA 核心数量制约。消费级显卡运行中小参数模型时响应慢且缺乏长程记忆，仅适合基础测试。生产环境或复杂任务推荐直接调用云端 API 以保证性能与稳定性。

### 14\. 官方微信 ClawBot 目前仅支持单聊，暂无法直接接入微信群交互。

**来源** ：Hermes Agent 中文社区微信群 37

经实测，官方提供的微信机器人接入方案当前仅支持个人号单聊交互。尝试拉入微信群或配置企业微信群时，会出现仅创建者能触发回复、其他成员无权限或无法获取群 ID 的情况。如需群聊自动化，建议关注后续官方更新或寻找第三方合规替代方案。

### 15\. Mac 本地部署推荐 MLX 格式，LM Studio 在性能评估与内存管理上更优。

**来源** ：Hermes Agent 中文社区微信群 37

在 macOS 环境运行本地大模型时，建议优先选择 MLX 格式而非 GGUF，以更好适配 Apple Silicon 架构。相比 Ollama，LM Studio 提供可视化界面，可提前评估硬件负载并动态调整内存占用，避免上下文过长导致内存飙升或系统重启。辅助模型选用 7B 参数即可满足日常需求。

### 16\. 主 Agent 调用子 Agent 不产生记忆，可通过独立 Profile 与分片存储解决。

**来源** ：Hermes 中文社区 互联网 IT 软件

群友分享解决方案：子 Agent 默认用后即毁且不读取主记忆。可为子 Agent 建立独立 Profile 作为网关拉起，结合 Lancedb 进行记忆分片存储，并根据上下文需求动态注入，实现记忆持久化与精准命中。

**链接** ：

- https://github.com/jasonno1/multi-agent-memory-skill

### 17\. MEMORY.md 接近满载时，可引入 gbrain 或 hindsight 进行记忆管理。

**来源** ：Hermes 中文社区 互联网 IT 软件

当核心记忆文件即将写满时，建议接入外部记忆管理工具。gbrain 内存占用约 200MB 且较稳定，hindsight 约 1GB 功能更新，可根据硬件资源选择以扩展 Memory 容量。

### 18\. 从 GitHub 拉取 Skill 速度慢，可克隆至码云或配置代理加速。

**来源** ：Hermes 中文社区 互联网 IT 软件

国内网络直接通过 Agent 安装 GitHub 项目常因网络超时失败。建议先将仓库克隆至码云等国内镜像源供 Agent 调用，或在终端配置 npm 等工具的代理 IP 以提升下载成功率。

扫码加入 Hermes Agent 中文社区微信群

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

图片版

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**微信扫一扫赞赏作者**

Hermes Agent 中文社区日报 · 目录

继续滑动看下一个

李嘉乐的数字花园

向上滑动看下一个