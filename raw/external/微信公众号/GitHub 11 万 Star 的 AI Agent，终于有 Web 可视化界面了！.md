X *2026年4月27日 09:31*




Hermes Agent 是 Nous Research 出品的开源 AI Agent，11 万 Star，MIT 协议，Python 写的。能力上基本没得挑：带记忆、会自动沉淀技能、不绑模型、内置定时任务、十几个消息平台都能接。

问题是，它只有终端。

这就像你手里有台发动机，却没方向盘。 **hermes-web-ui** 就是冲着「方向盘」来的——让你在浏览器里用 Hermes，终端能干的它都能干。

## Hermes Agent 很强，但入口太工程师

在讲 Web UI 之前，先说清楚 Hermes 到底强在哪，这样才懂 UI 补的是什么。

| 能力 | Hermes 是怎么做的 |
| --- | --- |
| 记忆 | `MEMORY.md`  存环境和经验， `USER.md` 存你的偏好，每次会话自动注入 |
| 历史 | 全部会话落在 SQLite 里，随时检索 |
| 自学 | 工具调用超过 5 次的复杂任务，会被自动沉淀成「技能」文件下次复用 |
| 模型 | OpenAI、Anthropic、Google、DeepSeek、OpenRouter、Ollama 一条命令切换 |
| 定时 | 内置，不用碰 crontab |
| 触达 | Telegram、Discord、Slack、WhatsApp、Signal 等 10+ 平台 |

这套能力，放在 2025 年的开源 Agent 里是头部水平。但前面这些事，以前全部要在终端里敲命令、看日志、改配置文件。

工程师能忍，但高频用的时候依然低效：会话一多就找不到旧对话，任务一跑就要 tail 日志，技能一多就要 `ls -la` 翻文件。


**hermes-web-ui** 是社区做的 Web 前端，目标很朴素：终端能做的事，浏览器里也能做。


三栏布局，一眼就懂：左边会话列表和项目导航，中间聊天区，右边工作区文件浏览。模型、Profile、工作区的切换挂在输入框底部。还有一个「控制中心」按钮，里面是会话管理、偏好设置、系统信息。

技术栈反着来的—— **没有构建步骤，没有打包工具，没有前端框架** 。后端 Python，前端原生 JavaScript。启动就三行：

```
git clone https://github.com/nesquena/hermes-webui.git hermes-webui
cd hermes-webui
./start.sh
```

浏览器打开 `http://localhost:8787` 。如果环境里没有 Hermes， `bootstrap.py` 会自动拉起来。

对于一个 Agent 的可视化工具来说，这种「抗诱惑」的技术选型反而是优点：没有 node\_modules，没有 Vite HMR，没有框架升级地狱，改一行 JS 刷新就见效。


## 聊天区：流式输出 + 工具调用可视化

聊天区是和普通 AI 聊天工具拉开差距的地方，核心就两个字： **可视化** 。

- **流式响应** ：Token 一个个冒出来，和你在命令行看到的一模一样。
- **消息重试** ：上一条回复一键重试，任务跑一半可以取消。
- **工具调用卡片** ：每次工具调用都是一张卡，有工具名、参数、结果摘要，可折叠。
- **子 Agent 缩进** ：AI 派出子 Agent 干活时，子任务单独缩进显示，图标区分，不会和主干混成一坨。
- **Mermaid 现场渲染** ：流程图、时序图、甘特图直接画出来，不用跳到外部工具。
- **推理链展示** ：Claude 的深度思考、o3 的推理链，以可折叠的金色卡片显示。
- **危险命令拦截** ：遇到 `rm -rf` 这种，界面弹出「允许一次 / 本次会话允许 / 始终允许 / 拒绝」四选一。
- **Token 表盘** ：输入框底部有圆形进度环，实时显示 Token 用量、花费、模型上限。

这里面最不该被忽略的是「危险命令拦截」和「Token 表盘」。前者避免 Agent 一失手删了你的项目，后者让你对成本有感——AI 产品里， **看不见的成本迟早变成一笔看得见的账单** 。

## 会话管理：项目、标签、归档一起来

只有聊天功能的 AI 工具，会话一多就开始糊。hermes-web-ui 把会话当数据来管：

- **基础操作** ：创建、重命名、复制、删除、按标题或正文搜索。
- **右键菜单** ：置顶、移进项目、归档、复制、删除。置顶会话顶部有金色标记。
- **项目分组** ：带颜色的分组，适合把同一领域的会话收拢。
- **标签过滤** ：标题里写 `#tag` ，自动变成彩色标签，点击可过滤。
- **时间分组** ：侧边栏按「今天 / 昨天 / 更早」自动折叠。
- **命令行会话也能接管** ：你在终端里跟 Hermes 的对话，会带金色 `cli` 标记出现在侧边栏，点进去就能接着聊。
- **导入导出** ：单条对话可以导出 Markdown 或 JSON，也能从 JSON 导回来。

最后两条最关键。终端和 Web 共享历史，意味着你可以在地铁上用手机扫尾工程师朋友昨晚在公司终端里留下的那个会话，无缝衔接。

## 定时任务、技能、记忆、Profile 全都可视化

这一块是 Web UI 相对终端的最大增量。

**定时任务** ：Tasks 面板可以查看、新建、编辑、运行、暂停、删除。任务跑完自动 Toast 通知，侧边栏 Tasks 标签有未读角标。任务失败，顶部横幅会告诉你，即使你当时不在这个会话里。

**技能管理** ：所有已安装技能按类别分组展示，支持搜索、预览、在线新建和编辑。这相当于把 `~/.hermes/skills/` 目录用图形界面包了一层。

**记忆面板** ：直接在浏览器里编辑 `MEMORY.md` 和 `USER.md` ，不用 SSH 进服务器。

**多 Profile** ：一个 Profile 就是一套独立配置（模型、API Key、技能、记忆、定时任务）。可以新建、克隆、切换、删除，切换不用重启。本地模型（Ollama、LM Studio）直接填 Base URL 和 Key 就行。

**主题** ：内置 7 套（Dark、Light、Slate、Solarized Dark、Monokai、Nord、OLED）， `/theme` 命令或设置面板都能切，想自己写一套也就 CSS 里加一个 `:root[data-theme="name"]` 的事。

**语音输入** ：麦克风按钮一键录音，静默 2 秒自动停，转录追加到输入框，不覆盖。用的是浏览器 Web Speech API，不支持的浏览器直接隐藏按钮。

屏幕宽度低于 640px 自动切抽屉式侧边栏，所有交互元素点击区域不小于 44px，聊天区按全屏高度计算，底部不挤。

更有意思的是手机访问方案： **Tailscale + Web UI** 。

> 服务端和手机都装 Tailscale，UI 启动时加 `HERMES_WEBUI_HOST=0.0.0.0 HERMES_WEBUI_PASSWORD=your-secret ./start.sh` ，手机浏览器打开 `Tailscale IP:8787` 即可。流量走 WireGuard 加密，应用层再套一层密码。

说白了，以前大家想在手机上用 Hermes，第一反应是接 Telegram Bot。但 Bot 天生就是单次问答模式，不方便看工作区、不方便看任务列表、不方便改记忆。Tailscale + Web UI 的方案，直接把「完整 Web 工作台」搬到了手机上，体验差别很大。

## 安装：本地、Docker、远程三选一

**本地启动** ：

先装 Hermes Agent：

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc
hermes model   # 选 LLM 提供商
```

Windows 不支持，用 WSL2。再启动 Web UI：

```
git clone https://github.com/nesquena/hermes-webui.git hermes-webui
cd hermes-webui
python3 bootstrap.py
```

`bootstrap.py` 会自检 Hermes Agent 有没有装，自动补、自动起服务、自动开浏览器，第一次还会走引导向导。

**Docker** ：

镜像推到了 GHCR，amd64 和 arm64 都有：

```
docker pull ghcr.io/nesquena/hermes-webui:latest
docker run -d \
  -e WANTED_UID=$(id -u) -e WANTED_GID=$(id -g) \
  -v ~/.hermes:/home/hermeswebui/.hermes \
  -v ~/workspace:/workspace \
  -p 8787:8787 ghcr.io/nesquena/hermes-webui:latest
```

推荐用 Docker Compose 把 Agent 和 Web UI 拆成两个容器，通过共享卷通信：

```
docker compose up -d
```

两个容器共享 `~/.hermes` ，配置、会话、技能、记忆都在里面。

**远程机器** ：

服务默认绑 `127.0.0.1` ，只有本机能访问。跑在 VPS 上用 SSH 隧道转发：

```
ssh -N -L 8787:127.0.0.1:8787 user@your.server.com
```

脚本检测到 SSH 环境时会自动把这条命令打印出来，贴心。

这个项目没有靠堆代码行数吓人，但分层挺干净：

```
server.py          HTTP 路由 + 认证中间件（约 154 行）
api/
  auth.py          密码认证，签名 Cookie（约 201 行）
  config.py        配置发现、模型检测、热重载（约 1110 行）
  routes.py        所有 GET/POST 路由（约 2250 行）
  streaming.py     SSE 引擎，Agent 运行，取消支持（约 660 行）
  workspace.py     文件操作，Git 检测（约 288 行)
static/
  index.html       HTML 模板（约 600 行）
  style.css        CSS，含主题和移动端适配（约 1050 行）
  ui.js            DOM 工具、消息渲染、工具卡片（约 1740 行）
  panels.js        定时任务、技能、记忆、Profile（约 1438 行）
tests/             53 个测试文件，961 个测试函数
```

运行状态全部落在 `~/.hermes/webui-mvp/` 里，会话、工作区、设置、项目、上次工作区，都在一处。路径可通过环境变量覆盖，挺符合 12-Factor。

961 个测试函数放在一个前端项目里有点超规格，但这也反映出维护者是把它当「长期运行工具」来做的——不是一个玩具 demo。

## 安全机制：本地友好，公网强制密码

密码默认关闭，方便本地用。一旦暴露到公网，设 `HERMES_WEBUI_PASSWORD` 环境变量或在设置面板里启用。认证是 HMAC 签名的 HTTP-only Cookie，24 小时有效。

默认已加的安全 Header： `X-Content-Type-Options` 、 `X-Frame-Options` 、 `Referrer-Policy` 。CDN 资源加 SRI 哈希，POST body 限制 20MB。

一句话： **本地跑不烦人，公网跑不裸奔** 。这是很多开源 Web UI 项目做不到的默认值。

## 值不值得装：看你用 Hermes 的频率

不是每个人都需要这个。

如果你只是偶尔问几句 AI，ChatGPT / Claude.ai 就够了，装 Hermes 本身就过度。

hermes-web-ui 的真正价值出现在「 **长期、高频** 用 Hermes」的场景：

- 你有一堆自动化任务在跑，要随时看状态；
- 你在 VPS 上跑 Agent，但不想一直开 SSH；
- 你想在手机上用 Agent，但又不想被 Telegram Bot 的单聊模式限制；
- 你 Profile 一多，终端里切换已经开始痛苦。

这种场景下，Web UI 把「需要记命令」的 Agent 变成了「鼠标能点」的面板，效率差距会慢慢显出来。

项目地址：https://github.com/nesquena/hermes-webui

Hermes Agent：https://github.com/NousResearch/hermes-agent