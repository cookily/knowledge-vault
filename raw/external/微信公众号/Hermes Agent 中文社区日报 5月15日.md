李嘉乐的数字花园 *2026年5月15日 07:51*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kHh2ibPRjHicFIrzTc8dA0cX0wyO6qtnkE6HWofE88icYxrJ3WXzHVmN4e8MjauEaiawL8ibPXvFJNAGy2AakQHkJLlLvK7gpiaALSyXAic8e3icZaY/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

> “
> 
> 今日汇总 14 条消息，共 2355 字，预计需要 5 分钟阅读。

### 1\. 群友开源 Clawke：跨平台 AI Agent 管理工作区，支持 Mac/Win/Linux/iOS/Android 协同

**来源** ：社区投稿

Clawke 是一个面向 AI Agent 的跨设备管理工作区，覆盖 Mac、Windows(WSL2)、iOS、Android 等多端。基于 CUP 协议支持流式响应、思维块、工具调用与用量追踪。已内置 OpenClaw、Hermes、Nanobot 等多 Agent 网关，每个会话可独立配置模型参数；自带一键安装脚本、媒体上传（图片/PDF/文本）等，便于手机与桌面无缝接管同一份 Agent 工作流。前端 Flutter，后端 Node.js，MIT 协议。

**链接** ：

- https://github.com/clawke/clawke

### 2\. 群友开源 EchoMind Memory Skill：跨框架 AI Agent 长期记忆系统，支持六类记忆与反馈强化

**来源** ：社区投稿

EchoMind 是一款面向 Hermes Agent / Claude Code / OpenClaw 等多框架的长期记忆 Skill。内置 Context（上下文）、Task（任务）、User（用户偏好）、Knowledge（知识）、Experience（经验）、Research（研究）六类记忆，通过用户正负反馈进行强化学习自动调整权重；零外部依赖，本地 SQLite 持久化，把目录放进 `skills/` 即可自动加载，跨会话保留代码风格、修复习惯与个人偏好。

**链接** ：

- https://github.com/jasonatgit/echomind\_memory.skill

### 3\. 群友开源 UniPet：通用 AI Agent 桌面宠物，零侵入接入 Hermes / OpenClaw / DeepSeek-TUI

**来源** ：社区投稿

UniPet 是一款基于 Node.js + Electron 的跨平台桌面宠物（Win / macOS / Linux），透明置顶常驻桌面，灵感来自 Codex Pet。支持 idle / running / waiting / failed / review 五种语义状态，可接收 Agent 推送的气泡消息，并提供拖拽、点击跳跃等交互。已原生集成 Hermes、OpenClaw、DeepSeek-TUI 三大 Agent，零侵入驱动；内置宠物管理系统支持安装/切换/删除，并可从在线市场下载 Codex 兼容宠物。MIT 协议。

**链接** ：

- https://github.com/ydyangdan/UniPet

### 4\. 群友开源 GovDocFormatter：按 GB/T 9704-2012 自动排版机关公文，无需安装 Word

**来源** ：社区投稿

GovDocFormatter 是 Word 公文自动排版工具，严格遵循 GB/T 9704-2012 国标。基于 Open XML SDK 直接修改.docx 文档结构，，覆盖约 20+ 项排版规则。是规则引擎而非 LLM 驱动，处理速度快、结果稳定可重复。C# 实现。

**链接** ：

- https://github.com/wz360270690/GovDocFormatter

### 5\. 社区分享多智能体框架 Agents-Hive 及配合 Skill 使用的 PDF 解析工具 Peekaboo。

**来源** ：Hermes Agent 中文社区微信群 45

新开源项目 Agents-Hive 提供多智能体协作方案，适合复杂任务流编排与自动化场景。针对扫描件或规范类 PDF 识别需求，可部署 Peekaboo 工具配合 Hermes 的 Skill 机制使用，部署前需提前安装相关 Python 依赖包以确保功能正常调用。

**链接** ：

- https://github.com/multica-ai/multica/blob/main/README.zh-CN.md
- https://github.com/openclaw/Peekaboo
- https://github.com/chef-guo/agents-hive

### 6\. 免费模型高峰期易超时，可通过调大最大超时时间解决。

**来源** ：Hermes Agent 中文社区微信群 37

免费模型因排队机制在用量高峰期极易触发请求超时。建议在 Hermes 配置中适当增加最大超时时间参数。需注意高峰期付费模型也可能降速，建议配合重试或降级策略使用。

### 7\. 集中管理记忆库与多Profile配置可解决多项目记忆混乱问题

**来源** ：Hermes Agent 中文社区微信群 44

建议指定一台设备作为服务器集中托管记忆库，其他终端通过ACP协议在IDE中调用。Hermes内置多Agent机制，通过创建独立Profile即可严格隔离不同项目的上下文，避免跨任务记忆交叉污染。

### 8\. Hermes 支持多 Profile 实现多 Agent 协作，建议单 Bot 绑定单 LLM。

**来源** ：Hermes Agent 中文社区微信群 6

单服务器可通过创建多个 Profile 部署多 Agent。为避免复杂脚本或高并发导致服务断连，建议遵循“一个 Bot 对应一个 LLM”的配置原则。此外，可尝试 gstack 插件实现多角色协作，或使用 superpower 进行项目代码修改。

### 9\. 实测飞书通道在稳定性与响应速度上优于微信及企微，推荐作为主力接入渠道。

**来源** ：Hermes Agent 中文社区微信群 31

多端对比显示飞书适配度最高，且具备实时翻译、多端消息免打扰等细节优势。建议将核心任务部署于飞书，微信端可独立配置 VPS 仅作监控或容灾备用。

### 10\. Hermes 跨设备迁移只需备份.hermes 文件夹内的人设与记忆文件。

**来源** ：Hermes Agent 中文社区微信群 32

更换运行环境时，直接复制 `.hermes` 目录下的核心数据即可完整保留历史记忆与角色设定。该操作无需复杂配置，也可借助 AI 辅助脚本自动化完成迁移流程。

### 11\. DeepSeek-V4-Flash 模型因缓存机制 API 调用成本极低。

**来源** ：Hermes Agent 中文社区微信群 46

实测少量充值即可满足日常开发，50 元额度在开启缓存的情况下可支撑约一个月的高频调用。建议优先使用云端联网大模型 API，避免本地部署带来的高硬件门槛与算力消耗。

### 12\. 安卓手机可通过Termux低门槛运行Hermes，适合轻量级调试与移动端控制。

**来源** ：Hermes 中文社区 互联网 IT 软件

官方文档提供Termux部署方案，利用安卓设备运行Hermes可实现低功耗、便携的Agent控制，并支持连接飞书或操作手机，适合非主力机环境下的测试与日常使用。

**链接** ：

- https://hermesagent.org.cn/docs/getting-started/termux

### 13\. 降低大模型幻觉的实用方案

**来源** ：Hermes Agent 中文社区QQ群

通过创建专用验证Agent、安装事实核查技能包、在agent.md中编写严格规则可减少模型虚构内容。根本解决需依赖低幻觉率模型，提示词与技能仅能缓解。

### 14\. Hermes浏览器自动化配置方案

**来源** ：Hermes Agent 中文社区QQ群

使用browser harness工具可实现Chrome浏览器自动化控制，通过开发者模式配置可免登录复用现有会话。需注意保持浏览器登录状态的安全风险，建议隔离敏感账号。

**链接** ：

- https://github.com/browser-use/browser-harness

扫码加入 Hermes Agent 中文社区微信群

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**微信扫一扫赞赏作者**

Hermes Agent 中文社区日报 · 目录

继续滑动看下一个

李嘉乐的数字花园

向上滑动看下一个