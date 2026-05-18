李嘉乐的数字花园 *2026年5月6日 09:19*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kHh2ibPRjHicHQELpIibib1vv8sIrOzHxgjRbTHeZUMVpVRNkFNIzmshS7gD1hqIeqBsSkGjibsDVKibFb2hLOToZ9zw0mlsDsJlibTdhWXbEsA6nw/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

> “
> 
> 今日汇总 19 条消息，共 2470 字，预计需要 5 分钟阅读。

### 1\. Agent部署建议优先选择 Linux 系统，并通过 SSH 隧道实现远程安全访问。

**来源** ：Hermes Agent 中文社区微信群 24

深入使用Agent时，强烈建议避免在 Windows 环境下直接部署，改用 Ubuntu 等 Linux 发行版可显著提升环境兼容性与稳定性。配合 SSH 隧道技术可实现跨网络的安全远程连接，同时要求使用者具备基础的 Linux 操作与网络运维能力。

### 2\. 结合Obsidian构建外部知识库，并通过LiteLLM路由免费API额度以节省成本。

**来源** ：Hermes 中文社区 互联网 计算机 IT

记忆系统可借助Obsidian实现内容Wiki化，供Agent按需探索。在模型路由层面，将网关Provider接入LiteLLM，可为提供免费额度的API配置更高权重，实现智能调度与Token成本优化。

**链接** ：

- https://www.litellm.ai/
- https://obsidian.md/

### 3\. 利用 GitHub 同步 Hermes 技能与配置，实现跨设备备份与快速恢复。

**来源** ：Hermes 中文社区 电商 跨境

将自定义 Skill 和使用习惯推送至 GitHub 仓库，换机或环境异常时可一键拉取恢复。建议将功能相近的 Skill 合并归类，便于版本管理与高效调用。

### 4\. 个人订阅号因无API推送权限，可采用AI生成图文并导出docx手动导入草稿的半自动化工作流。

**来源** ：Hermes Agent 中文社区微信群 25

受限于个人订阅号接口权限，全自动发布流程难以实现。当前可行方案为利用AI完成文章撰写与图片提示词生成，输出为docx文件后手动导入公众号草稿箱，配合人工审核与发布，单篇耗时约十分钟。纯网页文本发布流程更为简便。

### 5\. 推荐开源工具Kami用于增强Hermes的输出格式控制。

**来源** ：Hermes 中文社区 互联网 计算机 IT

该工具专注于优化和增强Hermes Agent的输出格式，适用于需要严格结构化数据返回或特定排版要求的开发场景，可有效提升下游系统解析Agent响应的稳定性。

**链接** ：

- https://github.com/tw93/kami

### 6\. 支持同时接入多个微信账号，可通过新建独立 Profile 实现隔离。

**来源** ：Hermes Agent 中文社区微信群 29

针对多账号并行需求，可通过创建新的 Hermes Profile 进行独立配置。每个 Profile 管理各自的会话状态与凭证，有效避免账号间冲突，适用于需同时运行多个微信机器人的场景。

### 7\. 提示词长度优化至128倍数可提升DeepSeek缓存命中率

**来源** ：Hermes Agent 中文社区微信群 8

针对DeepSeek的缓存颗粒度特性，建议将提示词Token数控制在128的倍数，并预留3~4个Token的边界余量。该配置结合API返回的hit/miss指标进行调优，可实现缓存接近98%命中，有效降低推理延迟与调用成本。

### 8\. 2G内存轻量云服务器即可流畅运行Hermes及文本处理任务，本地Agent可辅助云端配置。

**来源** ：Hermes 中文社区 金融 量化 财会

实测2核2G内存的轻量服务器足以支撑Hermes Agent与相关文本处理工作流。部署时可直接通过本地Hermes对话获取云端Linux配置步骤，降低命令行学习门槛。甲骨文免费服务器亦可作为高性能备选，但申请门槛较高。

### 9\. AI 图像/视频生成建议采用“固定流程+人工审核”模式。

**来源** ：Hermes 中文社区 电商 跨境

全自动生成目前稳定性不足，易出现画面异常。推荐将任务拆分为固定批处理流程，并在关键节点引入人工决策，可显著提升商用级产出质量与可控性。

### 10\. 多智能体协同框架实测对比：开源方案体验欠佳，单智能体设定目标更高效。

**来源** ：Hermes 中文社区 互联网 计算机 IT

针对企业内部协同场景，实测开源框架paperclip和multica存在操作卡顿问题。相比之下，在Hermes中配置单智能体并明确设定执行目标，往往比复杂的多智能体编排更稳定。Hermes新上线的Kanban功能也可辅助任务流管理。

**链接** ：

- https://github.com/paperclipai/paperclip
- https://github.com/multica-ai/multica

### 11\. 本地模型性能不足时，可采用“云端大模型带本地小模型”的混合架构。

**来源** ：Hermes Agent 中文社区微信群 31

针对本地小模型推理慢、能力弱的问题，可利用Hermes内置的delegation机制。主模型使用云端大模型负责规划与复杂决策，子模型使用本地小模型处理具体子任务并回传结果，兼顾性能与成本。

### 12\. 企业微信适配器存在图片与文件接收异常，需修改源码修复。

**来源** ：Hermes Agent 中文社区微信群 31

企业微信渠道直接发送图片或文件时，Hermes可能无法接收。经排查为wecom适配器代码层面的限制，通过修改相关源码即可解决该问题，个人微信渠道无此限制。

### 13\. 推荐开源AI路由器9router，支持自动路由至免费或廉价模型。

**来源** ：Hermes Agent 中文社区微信群 31

该项目提供智能路由功能，可根据请求特征自动分发至免费或低成本模型。适用于需要平衡API开销与响应速度的多模型调用场景。

**链接** ：

- https://github.com/decolua/9router

### 14\. 引入soul.md文件可有效提升Agent的交互表现与拟人化程度。

**来源** ：Hermes Agent 中文社区微信群 31

通过配置或参考开源的soul.md文件，可为Agent注入更完善的角色设定与行为逻辑。结合上下文认知流程，能显著改善Agent的响应质量与拟人化程度。

### 15\. 扫码配置的飞书网关无法发送文件，需补充应用级权限或切换凭证。

**来源** ：Hermes Agent 中文社区飞书群 1

扫码授权默认使用用户级令牌，缺少发送文件所需的应用级权限。需在飞书开放平台开通 im:message、im:message:send\_as\_bot 及关键的 im:resource 权限后重新授权，或直接改用 App ID + App Secret 的应用级凭证模式。

### 16\. Hermes 2026.5.3 测试版发布，新增内置文件传输插件与多项稳定性优化。

**来源** ：Hermes Agent 中文社区飞书群 1

核心更新包括支持跨节点二进制文件传输（最大16MB）、启动速度提升40%、修复消息丢包与配置过期回滚问题。新增 /steer 和 /side 命令用于会话指令修改与侧边提问，并引入第三方插件源码自动拦截机制提升安全性。

### 17\. 飞书、微信等渠道会话默认隔离，需通过工具或统一路径实现记忆与技能共享。

**来源** ：Hermes Agent 中文社区飞书群 1

不同通信渠道默认创建独立 Session，上下文不互通。若需跨渠道调用历史内容，可主动指示模型使用 session\_search 工具检索，或将关键信息写入长期记忆。自定义 Skill 可通过统一存放路径实现多端共享。

### 18\. 飞书个人版创建的应用无法直接添加至外部群聊，需使用企业自建应用。

**来源** ：Hermes Agent 中文社区飞书群 1

飞书平台限制个人版应用加入群组。若需在外部群使用机器人，必须创建企业自建应用，完成权限配置并正式发布后，方可通过群设置添加。

### 19\. 可通过指令让 Hermes 自动打包自定义 Skill 并推送至 GitHub 进行分享。

**来源** ：Hermes Agent 中文社区飞书群 1

无需手动整理文件，直接向 Hermes 下达打包指令即可生成相关 Skill 文件。提供 GitHub 仓库地址后，模型可指导完成 Git 配置与推送，实现技能的版本管理与社区共享。

扫码加入 Hermes Agent 中文社区微信群

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

图片版

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**微信扫一扫赞赏作者**

Hermes Agent 中文社区日报 · 目录

继续滑动看下一个

李嘉乐的数字花园

向上滑动看下一个