葱哥 *2026年5月16日 09:59*

> 34K star,字节出品。不调 API,不读 DOM,直接看截图、点鼠标、敲键盘,像人一样操作桌面。

/ / /

## 一个奇怪的 demo

前阵子我在刷 GitHub 的时候看到一个 demo 视频:一个 Agent 打开浏览器,搜航班信息,填表,切到日历 app 标记日期,再回到浏览器下单。全程没有调用任何 API,没有读 DOM 结构——它就是看着屏幕截图,识别出按钮和输入框在哪,然后模拟鼠标点击和键盘输入。

像一个真人在远程操控你的电脑。

这个项目叫 UI-TARS Desktop,字节跳动出品,Apache-2.0 协议。GitHub 上 34,091 star,这周又涨了 4,184。

![UI-TARS 像人一样操作桌面的 demo 场景](https://mmbiz.qpic.cn/mmbiz_png/XW0OS1TIfjJYOTBmYjKb8MBV9x6prngckG4eVnvkVN4rmUJWZv2HQAjdd3RtmALuZK975fOR4JxMEy4AiakYYcyHAbfpgCs278pxSE9b7ibGA/640?from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

UI-TARS 像人一样操作桌面的 demo 场景

/ / /

## TARS 是什么意思

UI-TARS 全称 User Interface — Task Automation and Reasoning System。名字起得挺正经,干的事却很"暴力":

1. \[01\]截屏
2. \[02\]视觉语言模型看图,理解当前界面状态
3. \[03\]决策:点哪、输入什么、滚动多少
4. \[04\]执行鼠标/键盘操作
5. \[05\]再截屏,看结果,循环

不需要目标应用暴露 API。不需要解析 HTML。不需要 accessibility tree。它就是"看"。

这思路跟 Anthropic 的 Computer Use 类似,但 UI-TARS 是开源的,而且字节在上面投了相当多的模型训练资源。

/ / /

/ / /

## 两个产品,一个仓库

项目里其实塞了两个东西:

**Agent TARS** ——通用多模态 Agent 框架。有 CLI 和 Web UI 两种入口,支持 MCP 工具挂载,走 Event Stream 协议做上下文管理。这个更偏"框架"。

**UI-TARS Desktop** ——Electron 桌面应用,专门做 GUI 自动化。支持 Windows、macOS 和浏览器环境。这个更偏"产品"。

两者共享底层的视觉语言模型,但使用场景不同。Agent TARS 适合开发者集成,UI-TARS Desktop 适合直接用。

![Agent TARS 框架 vs UI-TARS Desktop 应用](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Agent TARS 框架 vs UI-TARS Desktop 应用

/ / /

## 模型和 benchmark

这里要说清楚一件事。UI-TARS 不是只能用自家模型——它支持 VolcEngine(字节的云)、Anthropic Claude、自家的 UI-TARS-1.5 和 Seed-1.5-VL/1.6 视觉语言模型。

但性能最好的还是自家训练的 UI-TARS-1.5。在 10+ GUI benchmark 上的表现:

- \- **OSWorld**: 24.6@50 steps(这个 benchmark 测的是桌面操作系统级别的任务完成率)
- \- **AndroidWorld**: 46.6
- \-超过了 Claude 3.7 Sonnet 和 GPT-4o 在同类 benchmark 上的成绩

不过要注意,这些 benchmark 的设定跟真实使用场景还是有差距的。benchmark 里的任务通常边界清晰,真实场景下弹个意外的对话框、网页加载慢了、界面布局跟训练数据不一样,都可能翻车。

/ / /

/ / /

## Hybrid 控制策略

这是技术上比较有意思的一个设计。

浏览器操作场景下,UI-TARS 支持三种控制方式:

1. \[01\] **Visual Grounding** ——纯看截图定位元素,完全不碰 DOM
2. \[02\] **DOM Interaction** ——传统的读 DOM、querySelector 那套
3. \[03\] **Hybrid** ——两者结合,视觉定位 + DOM 验证

为什么需要 Hybrid。纯视觉方案在元素密集、字体小的界面上精度会下降——按钮挨得太近,截图分辨率不够高的时候容易点歪。加一层 DOM 交叉验证可以兜底。

但 DOM 方案又有另一个问题:很多桌面应用根本没有 DOM(比如原生 macOS 应用、游戏、Electron 以外的桌面软件)。所以纯 DOM 路线走不通。

Hybrid 是个务实的折中。

![三种控制策略的适用场景对比](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

三种控制策略的适用场景对比

/ / /

## Event Stream 协议

Agent TARS 内部用了一套 Event Stream 协议来管理上下文。跟直接把所有历史消息塞进 prompt 不同,它把交互过程拆成事件流,按需加载。

这个设计对长任务特别重要。想象一下,一个 Agent 连续操作 50 步——如果每步都把之前所有截图和操作记录塞进上下文,token 消耗会爆炸(每张截图就是几千 token)。Event Stream 可以做选择性回放,只把关键节点塞回去。

文档里提到 "Protocol-driven Event Stream drives Context Engineering",这句话翻译成人话就是:用协议管上下文,别傻乎乎全塞进去。

![Event Stream 协议的上下文管理流程](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Event Stream 协议的上下文管理流程

/ / /

/ / /

## 实际能干什么

文档和社区 demo 里展示的场景:

- \-航班和酒店预订:跨多个网站搜索、对比、填表下单
- \- **GitHub issue 导航**:打开 repo,搜 issue,读内容,写评论
- \- **VS Code 设置**:打开设置面板,搜索特定配置项,修改值
- \- **数据可视化**:打开 Excel,选数据范围,插入图表,调格式
- \- **多步跨应用工作流**:浏览器查信息 → 复制 → 切到 Notion 粘贴 → 切到 Slack 发消息

我自己试了一下用它操作 Notion——让它创建一个新页面,写几段文字,加个表格。结果它花了大概 40 秒完成,中间有一步点错了位置(点到了侧边栏而不是正文区域),但自己发现了错误,回退重试后完成了。

这种"自我纠错"的能力说明模型确实在 reasoning 层面做了功课,不是盲目执行预设动作序列。

/ / /

## 跟 Anthropic Computer Use 比

绕不开的对比:

| 维度 | UI-TARS Desktop | Anthropic Computer Use |
| --- | --- | --- |
| 开源 | 是 (Apache-2.0) | 否 |
| 模型 | 多种,含自训练 UI-TARS-1.5 | Claude 系列 |
| 桌面支持 | Windows + macOS | Linux (Docker) |
| 浏览器 | 内置,支持 Hybrid 控制 | 需外部配置 |
| 本地运行 | 支持 | 需要 API |
| MCP 集成 | 原生支持 | 需扩展 |
| 远程操作 | 内置 remote operator | 需第三方 |

核心差异在开源这一点。UI-TARS 你可以本地跑,可以改模型,可以接自己的工具链。Computer Use 是 API 服务,你得把截图发到 Anthropic 的服务器。

对隐私敏感的场景(比如操作内网系统、处理敏感文档),本地运行是硬需求。

![UI-TARS vs Computer Use 的技术路线对比](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

UI-TARS vs Computer Use 的技术路线对比

/ / /

/ / /

## 安装和上手

Agent TARS:

```
npx @agent-tars/cli@latest
# 或者全局安装
npm install @agent-tars/cli@latest -g
agent-tars --provider volcengine --model <model-name> --apiKey <key>
```

要求 Node.js >= 22。

UI-TARS Desktop 是 Electron 应用,直接下 dmg 或 exe 安装包。

启动后配置好模型 provider 和 API key 就能用。不配自家模型也行,接 Claude API 一样跑(只是性能可能不如 UI-TARS-1.5)。

/ / /

## 局限和风险

1. \[01\] **速度** ——每一步都要截图 → 上传 → 推理 → 返回动作,延迟比直接调 API 高一个数量级。不适合需要毫秒级响应的场景。
1. \[01\] **可靠性** ——界面变化(弹窗、加载动画、布局改版)都可能让 Agent 迷路。目前还做不到"设置好就完全不管"。
1. \[01\] **安全** ——一个能操控你鼠标和键盘的 Agent,如果模型出现幻觉,理论上可以做任何操作。在生产环境使用前,做好权限隔离。
1. \[01\] **分辨率依赖** ——视觉方案对屏幕分辨率敏感。4K 屏和 1080p 屏上同一个界面,模型看到的东西不一样,可能影响精度。

/ / /

## 写在最后

UI-TARS Desktop 目前 v0.3.0,1,108 个 commit,38 个 release。TypeScript 占代码的 89.1%,用 pnpm + Turbo 管理 monorepo。

"看屏幕操作电脑"这个方向,我觉得短期内不会取代 API 调用,但长期看是一个很重要的补充。原因很简单:这个世界上大量的软件没有 API,也永远不会有 API。能"看"着用的 Agent,覆盖面天然更广。

字节在这个方向上投了不少资源(自训练的视觉语言模型、10+ benchmark、40+ 社区 demo),开源诚意也够。如果你对 GUI 自动化感兴趣,这可能是目前最值得关注的开源项目。

```
npx @agent-tars/cli@latest
# 打开 localhost 看 Web UI
```

继续滑动看下一个

蒜是哪根葱

向上滑动看下一个