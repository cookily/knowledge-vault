李嘉乐的数字花园 *2026年5月17日 11:26*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kHh2ibPRjHicHwqwxmice0mib6q6SqkQvrHD7P2kmQfuOhWrF2D0FU019MhvtZdma0Jam3pY6BaBI3Yu2pY4uvhaReuEmibuEnQrb5S8MEGcfXW4/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

## Hermes Agent v0.14.0版本，发布日期：2026 年 5 月 16 日

Hermes Agent v0.14.0 的官方代号是 **The Foundation Release（基石版本）** 。

这一版的关键词是“补地基”：安装方式、Windows 支持、启动性能、写代码可靠性、供应链安全、插件扩展都在这一版集中补齐。

之前的 Hermes Agent 能力很强，上手门槛也偏高。v0.14.0 开始，它正在向“普通用户也能装、团队也能部署、开发者能长期依赖”的阶段迈进。

完整中文发布说明：

http://hermesagent.org.cn/docs/releases/v0-14-0

## 数据概览

这次更新规模不小：

- 808 次提交
- 633 个合并 PR
- 1,393 个文件变更
- 新增 165,061 行代码
- 关闭 545 个 Issue
- 其中包括 12 个 P0、50 个 P1
- 215 位社区贡献者参与

从数据上看，这次更新已经超过常规小版本的体量。Hermes Agent 在进入更大规模使用前，对基础设施做了一次集中加固。

## 一句话总结

**v0.14.0 是 Hermes Agent 的里程碑版本：PyPI 一键安装、Windows 原生支持、启动快约 19 秒、浏览器工具最高 180 倍加速、LSP 自动诊断、供应链安全扫描、会话迁移和插件体系继续增强。**

这几个变化合在一起，意味着 Hermes Agent 正在从“能用”走向“更容易装、更稳定跑、更适合真实工作流”。

下面挑重点说。

## 1\. Windows 原生支持进入早期测试阶段

对很多 Windows 用户来说，这是这次最值得注意的变化之一。

过去很多 AI Agent 工具默认假设用户在 macOS、Linux 或 WSL 环境里工作。对普通 Windows 用户来说，这一步经常就是劝退点。

v0.14.0 开始，Hermes Agent 的原生 Windows 支持进入 early beta：

- 支持 `cmd.exe` 和 PowerShell
- 提供完整 PowerShell 安装器
- 自动安装 MinGit
- 检测 Microsoft Store Python stub
- 补齐 Ctrl+C 终止、Signal 处理、路径归一化等基础问题
- 包含 40+ Windows 专属修复

注意，官方仍然标注为 early beta，不建议直接拿去替换关键生产流程。但对个人用户、新手用户、Windows 机器上的测试环境来说，这已经是很大的门槛下降。

简单说：以前你可能要先搞懂 WSL，才能开始研究 Hermes；现在 Windows 用户可以先原生跑起来，再慢慢深入。

## 2\. pip install hermes-agent 正式可用

另一个关键变化，是 PyPI 安装正式上线。

现在新用户可以直接：

```
pip install hermes-agent
hermes
```

这件事看起来普通，但对开源工具的传播很重要。

过去安装 Hermes 往往要 clone 仓库、跑 shell installer、处理 git、路径、依赖、平台差异。对熟手来说还好，对新手和非技术用户来说，第一步就可能卡住。

v0.14.0 的 wheel 包已经包含 Ink TUI bundle 和 shell launcher，整体更接近一个标准 Python CLI 工具。

这意味着 Hermes Agent 的上手路径变短了：先安装，先启动，先完成一个真实任务，再去理解更复杂的模型、插件和消息平台配置。

## 3\. 启动快了约 19 秒，浏览器工具最高 180 倍加速

v0.14.0 的性能优化也很直接。

官方给出的数据是： `hermes` 冷启动少约 19 秒。

这背后包括几类优化：

- 技能缓存
- 重型模块延迟导入
- models.dev 优先读取磁盘缓存，减少网络等待
- doctor 检查并行
- 部分命令跳过欢迎界面
- `hermes tools` All-Platforms 页面从 14 秒缩到 1.5 秒以内

浏览器工具也有明显变化。 `browser_console` 现在复用持久 Chrome DevTools WebSocket，不再每次调用都重新建立 session。官方给出的提升幅度是 180 倍。

对普通用户来说，这些技术细节可以先不深究。你只需要知道：打开更快、等待更少、让 Agent 调网页和查页面错误时反馈更快。

AI Agent 工具最怕“每一步都要等”。v0.14.0 在这方面做了实实在在的减法。

## 4\. 依赖懒加载：不再一上来全装

这一版引入了更完整的 lazy-deps 框架。

简单说，很多后端、适配器、SDK 不再安装时一次性塞进来，系统会尽量按需安装、按需加载。

这对两类用户都很有价值：

对新手来说，第一次安装更轻，不会刚开始就被一堆暂时用不到的依赖拖住。

对团队和企业用户来说，依赖面变小，供应链风险更容易控制，环境审计也更清晰。

同时，v0.14.0 还加入了供应链安全检查器。每次 `pip install` 或 `hermes update` 时，会自动扫描不安全依赖版本。

这说明 Hermes Agent 不只是追功能，也开始更认真地处理“长期运行”和“团队部署”里的安全问题。

## 5\. 写代码更稳：LSP 语义诊断上线

如果你经常让 Hermes Agent 写代码、改文件，这一条非常重要。

过去 Agent 写完文件后，最多能做一些语法级检查。比如 Python、JSON、YAML、TOML 这些文件有没有明显语法错误。

v0.14.0 继续往前推进： `write_file` 和 `patch` 之后，会自动运行 language server 诊断。

这意味着 Agent 能更早看到：

- 类型错误
- 未定义变量
- 缺失 import
- 符号引用问题
- 真实文件变更是否符合预期

这一版还新增了文件变更验证器。每次写文件后，Agent 会看到磁盘上真实发生了什么变化，避免只停留在自己“以为写进去了”的状态。

这对代码任务很关键。

AI 写代码不难，难的是写完以后知道自己有没有写错、有没有改偏、有没有漏掉上下文。v0.14.0 在这方面补了一块很实用的工程能力。

## 6\. /handoff：会话可以真正转交

`/handoff` 也是这次值得关注的能力。

过去你中途换模型、换角色、换 profile，经常意味着上下文断掉：前面聊过什么、工具调用过什么、任务进展到哪里，都需要重新解释。

v0.14.0 的 `/handoff` 可以把当前活跃会话迁移到另一个 model、persona 或 profile，同时保留历史消息、工具调用和上下文。

典型用法是：

- 先用快模型做初步排查
- 再把同一个任务交给更擅长推理或写代码的模型
- 或者把通用任务转交给专门处理代码审查、文档整理、测试修复的 profile

这类能力表面上不花哨，但对长任务很重要。真正复杂的 Agent 工作，往往会经历拆解、转交、验证和收束，远不止“一问一答”。

## 7\. 跨会话提示缓存：更快，也可能更省

v0.14.0 还加入了跨会话 Claude prompt cache。

在支持的 provider 上，system prompt、skills、memory 等前缀可以跨会话复用 1 小时。

这意味着你新开一个 `/new` 会话时，也可能命中还热着的缓存。结果是首轮响应更快，成本也可能更低。

对重度用户来说，这类优化会慢慢积累成明显体验差距。

## 8\. 视觉、视频和桌面控制继续增强

工具层面，这一版也有不少增强：

- `vision_analyze` ：支持视觉的模型可以直接接收原始像素，不再先 fallback 成文字描述
- `video_generate` ：统一的视频生成工具，后续后端可以通过插件扩展
- `computer_use` ：新增 CUA 驱动后端，非 Anthropic provider 也可以逐步支持桌面控制
- 终端 URL 可点击：支持 OSC8 的终端里，Agent 输出的链接可以直接点击

这些能力不一定是新手第一天就用到的功能，但它们决定了 Hermes Agent 未来能不能更自然地处理图片、视频、浏览器和桌面操作。

## 9\. hermes proxy：把订阅变成本地兼容端点

`hermes proxy` 是给进阶用户和开发者准备的能力。

它可以在本机启动一个 OpenAI-compatible endpoint，背后接你已经登录的 OAuth provider，例如 Claude Pro、ChatGPT Pro、SuperGrok 等。

这样 Codex、Aider、Cline、VS Code Continue，或者你自己的脚本，只要支持 OpenAI 兼容接口，就可以复用这类订阅。

对普通用户来说，可以先把它理解成：Hermes 在帮你把不同工具之间的模型接入方式统一起来。

## 10\. 消息平台和生态继续扩展

v0.14.0 继续扩展消息平台和生态连接能力。

新增包括：

- LINE Messaging API
- SimpleX Chat
- Microsoft Graph / Teams 管道和 Webhook 适配器

加上这些之后，Hermes 支持的消息平台总数来到 22 个。

另外，Discord、Telegram、Slack 等平台也有各自增强，比如频道历史回填、原生草稿流式输出、命令前缀支持等。

如果你只是本地使用，可以先不用关心这些；如果你准备把 Hermes 接入团队沟通、机器人、自动化通知，这些能力会越来越重要。

## 11\. 9 个新可选 Skill

这一版新增 9 个 optional skill：

- Hyperliquid 交易
- Yahoo Finance
- API 测试
- EVM 多链
- Darwinian Evolver
- OSINT 调查
- Pinggy 隧道
- Watchers，用于 RSS / GitHub 等轮询
- Notion 大改版

这里建议新手不要一上来全装。

Skill 更适合按任务选择，没必要追求数量。你要做 API 调试，就装 API 测试；你要做信息监控，就看 Watchers；你要做 Notion 工作流，再去看 Notion overhaul。

先跑通基础任务，再按需扩展，这是更稳的路线。

## 12\. 模型与搜索后端更多了

模型和 provider 也有一些更新：

- xAI Grok OAuth
- NovitaAI provider
- OpenRouter Pareto Code router，支持按 `min_coding_score` 选择更合适的编码模型
- Codex runtime，用于驱动 OpenAI Codex CLI
- Brave Search 免费层
- DuckDuckGo 搜索后端
- 阿里云相关命名调整为通义千问

这些更新说明 Hermes Agent 的 provider 抽象还在继续变厚。未来可以按任务、成本、速度和质量组合不同模型与搜索后端，使用方式会更灵活。

## 13\. 安全加固很重

这次安全修复数量不少：12 个 P0、50 个 P1。

比较关键的方向包括：

- sudo 暴力破解拦截
- askpass 危险操作分类
- dangerous command bypass 修复
- 供应链安全扫描
- SSRF 路径覆盖
- Dashboard API 鉴权
- Shell 相关风险收敛

如果你只是本地体验，可能对这些没有强感知；但如果你在服务器、团队环境、Dashboard、Gateway 或自动化任务里跑 Hermes，这些修复非常重要。

Agent 和普通聊天机器人不一样。它会读文件、写文件、调工具、跑命令。只要进入真实工作流，安全边界就必须认真对待。

## 谁应该升级？

建议优先升级或关注 v0.14.0 的用户：

- 第一次安装 Hermes Agent 的新用户
- Windows 用户
- 经常让 Agent 写代码、改文件、调网页的人
- 准备在团队里铺环境的人
- 已经使用 Gateway、Dashboard、插件或长期任务的人
- 对安全修复和稳定性敏感的用户

如果你只是偶尔体验旧版本，也可以先观望。但如果你是新装用户，建议直接从 v0.14.0 开始。

## 如何更新

升级前建议备份：

- `SOUL.md`
- `MEMORY.md`
- `skills/` 目录下你自己写的或 Hermes Agent 自己学习的 skill

已经安装 Hermes 的用户，可以执行：

```
hermes update
```

新安装可以尝试：

```
pip install hermes-agent
hermes
```

如果连接官方 GitHub 仓库超时，可以把下面这段提示词丢给 Hermes Agent，让它帮你切换中文社区镜像：

```
请帮我切换 Hermes Agent 的 git 源到中文社区镜像。

仓库通常位于 ~/.hermes/hermes-agent（Windows 下是 用户目录\.hermes\hermes-agent）。

请进入该目录后执行：

把 origin 改为中文社区镜像：https://cnb.cool/hermesagent-cn/hermes-agent-cn-mirror
把官方 GitHub 仓库加为 upstream：https://github.com/NousResearch/hermes-agent.git
用 git remote -v 确认两个 remote 都配置成功
用 git fetch origin 验证镜像能正常拉取

之后再跑一次 hermes update 即可。
```

## 最后

v0.14.0 的价值落在整体基础体验上：Hermes Agent 变得更容易安装、更容易运行，也更适合放进真实工作流。

Windows 能跑，PyPI 能装，启动更快，浏览器工具更快，写代码能自动诊断，依赖和供应链也开始认真治理。

这就是 “The Foundation Release” 这个代号的含义：地基补上之后，Hermes Agent 才能真正进入更广泛的使用场景。

Hermes Agent 中文社区日报 · 目录

继续滑动看下一个

李嘉乐的数字花园

向上滑动看下一个