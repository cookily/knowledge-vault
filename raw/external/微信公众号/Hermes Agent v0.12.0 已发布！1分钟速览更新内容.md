李嘉乐的数字花园 *2026年5月3日 10:54*

![图片](https://mmbiz.qpic.cn/mmbiz_png/kHh2ibPRjHicFDfPby1o6a9guIibcuhPkiazNUoibePeq3ZVrwJSpKgfC7SNVrlufMxUVKrjefmgJlB94nHE9wMSES4PWSfY8zkRuBaRJrnoDIsU/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

发布日期：2026 年 4 月 30 日

这次更新官方代号 **The Curator release** （管家版），核心变化： **Hermes 现在能自己照顾自己** 。

一句话总结这次更新做了什么：

- 多了一个自动整理 skill 库的"管家"
- 自我改进能力大改了一遍
- 多了 4 家模型供应商可以选
- 新接入两个聊天平台：Microsoft Teams、腾讯元宝
- Spotify、Google Meet 默认内置
- ComfyUI、TouchDesigner 升级为默认技能
- 启动速度快了大约一半

下面挑重点说说。

---

## 自动整理 skill 库的"管家"

时间一长，装的 skill 越来越多，难免重复或者根本没在用。这次新增了一个叫 **Curator** 的后台代理，默认每 7 天跑一次，做这几件事：

- 给每个 skill 打分
- 把功能重复的合并到一起
- 把已经没用的清理掉
- 写一份报告告诉你它都干了什么

内置的核心 skill 有保护，不会被误删。在 `hermes model` 里可以选用哪个模型来当这个管家，也可以在 Dashboard 里管理。

想看哪些 skill 用得最多、哪些几乎没用过，输入 `hermes curator status` 就行。

---

## 自我改进能力大幅升级

Hermes 每跑完一轮，会有一个后台进程检查"这一轮要不要把哪些经验记下来 / 把哪些 skill 更新一下"——这是 Hermes 能越用越懂你的核心。这次：

- 改成按评分卡打分，不再让模型"自由发挥"，更稳定
- 优先更新你刚用过的那个 skill
- 后台进程现在能正确继承主进程的模型和账号（之前会丢）
- 后台进程只允许改记忆和 skill，不会再误用 shell 或上网
- 上下文更干净，不会被上一轮的工具消息干扰

---

## skill 大扩张

新加 / 升级的 skill：

- **ComfyUI v5** ：从可选升级为默认内置
- **TouchDesigner-MCP** ：默认内置，新增 9 篇参考文档（GLSL、后期特效、音频、几何）
- **Humanizer** ：把 AI 腔的文字洗成正常人话
- **claude-design** ：生成 HTML 演示页
- **design-md** ：写 DESIGN.md 规范文档
- **airtable**:接 Airtable
- **pretext** ：浏览器创意演示
- **spike + sketch** ：一次性实验脚本和静态 HTML 原型

附带能力：

- 可以 **直接从 HTTP 链接安装 skill**
- 新增 `/reload-skills` 命令，改了 skill 不用重启

---

## 4 个新模型路径

| 路径 | 说明 |
| --- | --- |
| GMI Cloud | 一等 API key 接入 |
| Azure AI Foundry | 自动检测、完整接入 |
| MiniMax OAuth | 浏览器一键登录 |
| 腾讯 Tokenhub | 新接入 |

另外 **LM Studio** 升级为正式 provider，不再借壳"自定义端点"，有专属鉴权、 `hermes doctor` 检查、实时拉模型列表。

---

## 聊天平台

- **Microsoft Teams** 上线，第 19 个平台。这次它走"插件"机制接入——以后再加新平台不用改核心代码。
- **腾讯元宝** 原生支持，第 18 个平台，文字 + 媒体都能发。

其他平台改进：

- Telegram、Discord、Slack、Mattermost、邮件、Signal **统一支持原生多图发送**
- Slack 新增"频道绑定 skill"，也可以阻止它被 thread 自动卷入
- Signal 支持 markdown 渲染、引用回复、表情反应
- Telegram 支持群组 / 论坛聊天白名单

---

## Spotify + Google Meet 原生支持

**Spotify** ：7 个工具（播放、搜索、队列、歌单、设备控制），浏览器一键登录，内置 skill，可以用 cron 定时执行。

**Google Meet** ：加入会议、转录、发声、跟进——整套流水线打包成插件。

---

## 命令行体验

新命令：

- \*\* `hermes -z <提示词>` \*\*：跑完就退出，不进交互模式。可以指定模型和 provider。
- \*\* `hermes update --check` \*\*：升级前预检
- \*\* `hermes fallback` \*\*：管理回退 provider

升级时：可以让 Hermes 自动备份 HERMES\_HOME（默认关闭，需要时打开）。

---

## Dashboard 加了 Models 标签页

- 每个模型的使用情况都有详细分析
- 可以直接在浏览器里切换主模型和副模型

---

## TUI 体验改进

- 支持 LaTeX 渲染
- `/reload` 热加载.env
- 可选"自动恢复最近一次会话"
- 浅色终端自动识别更准
- `/resume` 选择器里按 `d` 删除会话
- 修饰键 + 鼠标滚轮 = 行级滚动
- 输入框按 `?` 弹出迷你帮助

---

## 启动变快

TUI 冷启动时间砍掉约 57%。原理是按需加载、加缓存，不用关心细节，反正打开就快。

---

## 几个值得注意的变化

**默认关掉了密钥脱敏** ：之前脱敏功能会把"长得像密钥"的字符串都改掉，结果经常把代码 patch 或 API 返回弄花。这次默认关。需要的话在配置里写 `redaction.enabled: true` 打开。

**模型 catalog 改成远端拉取** ：OpenRouter 和 Nous Portal 上有新模型时，不用等 Hermes 发版本就能用。

**多模态图像智能路由** ：根据模型实际有没有视觉能力来分发图片，不再按 provider 默认。

**Prompt 缓存可以延长到 1 小时** ：默认 5 分钟，聊天频繁的场景改成 1 小时能省 token。

---

## 移除 / 回滚

- Kanban 多 profile 协作看板上线后又被回滚，等待重新设计
- computer-use 的 cua-driver 整体回滚
- 内置的 BOOT.md hook 移除（教程演示了如何用 shell hook 自己实现）
- `/provider` 、 `/plan` 这两个 slash 命令删掉了

---

## 谁该升级

下面任意一种情况，建议优先关注 v0.12.0：

1. 想让 skill 库自动整理
2. 在用 LM Studio / GMI Cloud / Azure AI Foundry / MiniMax / 腾讯 Tokenhub
3. 在用 ComfyUI、TouchDesigner、Spotify、Google Meet
4. 公司里用 Microsoft Teams 或腾讯元宝
5. 嫌冷启动慢
6. 之前被密钥脱敏功能误伤过

**所有人都建议升级** ：这版合入了 360 个 bug 修复，主要修在流式输出、上下文压缩、工具调用、推理内容这几个核心路径上。

---

## 如何更新

**⚠️ 升级前请务必备份这些文件** ：

- `SOUL.md`
- `MEMORY.md`
- `skills/` 目录下你自己写的或定制过的 skill

这些是你和 Hermes 长期积累下来的"个人资产"，丢了就回不来了。

**更新方法** ：在终端（Windows 下用 PowerShell）输入：

```
hermes update
```

**如果连官方 GitHub 仓库超时** ，可以把下面这段提示词丢给 Hermes Agent，让它帮你换成中文社区镜像：

> “
> 
> 请帮我切换 Hermes Agent 的 git 源到中文社区镜像。
> 
> 仓库通常位于 `~/.hermes/hermes-agent` （Windows 下是 `用户目录\.hermes\hermes-agent` ）。
> 
> 请进入该目录后执行：
> 
> 1. 把 `origin` 改为中文社区镜像： `https://cnb.cool/hermesagent-cn/hermes-agent-cn-mirror`
> 2. 把官方 GitHub 仓库加为 `upstream` ： `https://github.com/NousResearch/hermes-agent.git`
> 3. 用 `git remote -v` 确认两个 remote 都配置成功
> 4. 用 `git fetch origin` 验证镜像能正常拉取

之后再跑一次 `hermes update` 即可。

**微信扫一扫赞赏作者**

继续滑动看下一个

李嘉乐的数字花园

向上滑动看下一个