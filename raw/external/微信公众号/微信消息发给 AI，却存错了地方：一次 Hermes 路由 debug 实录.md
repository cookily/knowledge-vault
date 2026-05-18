刀羊DoYoung *2026年5月17日 16:22*

#### 01 问题：消息到了，但全跑偏了

我在本地跑了 Hermes Agent，用微信给它发了一条"日语学习"的指令，附带了一段多邻国里听不懂的日语对话。

预期结果：Hermes 调用 `japanese-learning` skill，按指定格式解析语法和单词，存到日语学习的 Obsidian 库里。

实际结果：Hermes 确实解析了日语，也给了教学解释——但格式完全不对，文件存到了默认的 GalaxyMe 库里，而不是日语专用库。

同一个提示词，在 Hermes 终端里直接输入，行为完全正确。加了微信通道，就全跑偏了。

问题不在 AI 的理解能力，在于 **路由** ——微信消息进来时，Hermes 拿到的上下文跟终端里不一样。

---

#### 02 微信是怎么连上 Hermes 的

先说连接这一步。Hermes 内置了微信 iLink 网关，一条命令搞定：

```
hermes gateway setup
```

Hermes 会自己连微信 iLink 服务器，生成二维码。用微信扫码授权后，微信好友列表里会多一个叫"微信 ClawBot"、带 `AI` 标识的联系人。之后你给它发消息，它就收。

**但这里有个坑：**

如果你不是跑 `hermes gateway setup` ，而是直接在 Hermes 终端里用 prompt 让它自己连微信，Hermes 会写脚本尝试连接，然后终端无限等待。原因是 Hermes 在等你扫码，但二维码在终端里没有正确渲染出来。

这时候去看日志：

```
tail -f ~/.hermes/logs/gateway.log
```

把卡住的命令拖到 shell 里自己跑，扫码，就能过。

---

#### 03 微信和 Hermes 是怎么互联的

扫码之后发生了什么？你的消息是怎么从手机跑到本地电脑上的 Hermes 的？

这里用到的不是传统的 Webhook 推送，而是腾讯 iLink Bot API 的 **长轮询 (Long-Polling)** 机制。

简单来说：Hermes 不等着微信推消息过来，而是自己不停地问微信服务器"有没有新消息"。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Yn1cgd8bNPap9HbR568QX61IKrTyoLaFtAqDturgCyc203xibwezetqTKdxbib5zcDpGicAkhoaNfW7QmJrqibIRsWVjx6VYSlJibdFjic47SLxI4/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

整个链路的完整细节（包括文件消息的 AES-128-ECB 解密、sync\_buf 持久化、context\_token 机制）篇幅比较长，这篇先不展开了。如果感兴趣的话评论区说一声，后面单开一篇讲透。

---

#### 04 路由问题的根因

连接通了，消息能收到，但行为不对。问题出在这里：

微信消息进来时，Hermes 只读到了全局的 Memory 和 User Profile， **没有加载 Project 级别的 Context** ——也就是某个目录下的 `AGENTS.md` 。

`AGENTS.md` 是什么？它是项目级的规则文件，里面记录了操作 Obsidian 库的正确方式：

```
### Obsidian Vault Access

**CRITICAL**: All interactions with the Obsidian vault must use the \`Obsidian\` command.

**Available Commands:**
- \`Obsidian vault=japanese create name="..." path="..." content="..."\`
- \`Obsidian read file="..."\`
- \`Obsidian append file="..." content="..."\`
```

没有这个文件，Agent 就不知道 `vault=japanese` 这个参数的存在，也不知道写文件必须走 Obsidian CLI。它按默认行为处理，自然存错了地方。

**为什么终端里正常，微信通道不正常？**

关键在 `terminal.cwd` 这个配置：

```
# ~/.hermes/config.yaml
terminal:
  backend: local
  cwd: .
  timeout: 180
```

Gateway 模式下， `cwd: .` 被解析成了 home 目录。home 目录下没有 `AGENTS.md` 。终端模式下，你通常是在项目目录里启动的，cwd 就是项目根目录， `AGENTS.md` 自然能加载。

| 项目 | 值 |
| --- | --- |
| **根因** | Gateway 的 `terminal.cwd: .` 解析为 home 目录，该目录下无 `AGENTS.md` |
| **直接后果** | System Prompt 缺少 Project Context，Agent 不知道 Obsidian CLI 的正确用法 |
| **表现** | Skill 格式不对、文件存错 vault |

---

#### 05 怎么 debug

遇到 Hermes 行为不符合预期，第一步是确认它到底看到了什么。

**确认 skill 是否加载：**

```
python3 -c "
import json
with open('sessions/session_20260516_091120.json') as f:
    data = json.load(f)
print(data['system_prompt'])
"
```

System Prompt 的实际结构：

```
System Prompt 结构（18,486 chars）:
├── # Hermes Agent Persona（SOUL.md）
├── ## Skills (mandatory) + <available_skills> 索引
├── ═══ MEMORY ═══（6 条持久化笔记）
└── ═══ USER PROFILE ═══（4 条用户信息）
```

在 `<available_skills>` 里确认 `japanese-learning` 确实在：

```
education:
    - japanese-learning: 日语学习助手 - 当用户发送"学习日语"或"日语学习"时...
```

Skill 加载了，但它内部的规则依赖 `AGENTS.md` 里的 Obsidian CLI 用法——而 `AGENTS.md` 没被加载。问题定位清楚了。

---

#### 06 修复方案

让 Hermes 正确路由，有两条路：

**方案一：在全局 Memory 里写好路由规则**

```
# ~/.hermes/memories/MEMORY.md
默认 Obsidian vault: GalaxyMe（/Users/caohong/Documents/memo/GalaxyMe）。
日语学习 vault: japanese（~/family/japanese/），使用 vault=japanese 参数。
写文件必须用 Obsidian CLI。
Obsidian CLI 的 vault=japanese 参数必须放在子命令之前。
```

我选的是这个方案。不改变 Hermes 的默认工作目录，把关键的 CLI 用法写进 Memory，所有通道共享。

**方案二：设置 `terminal.cwd` 为绝对路径**

```
terminal:
  cwd: /Users/caohong/Documents/memo/GalaxyMe
```

这样 Gateway 启动时就能找到 `AGENTS.md` 。缺点是你只有一个项目目录，如果你有多个 vault、多个项目，这个方案就不够灵活。

---

#### 07

微信通道和终端通道的差异，本质是 cwd 不同导致 Project Context 加载不同。debug 的关键不是猜 AI 怎么想的，是看它的 system prompt 里到底有什么。

`tail -f ~/.hermes/logs/gateway.log` 看日志，dump session JSON 看 system prompt。这两步能解决 80% 的"AI 为什么不按我说的做"的问题。

**微信扫一扫赞赏作者**

继续滑动看下一个

刀羊的AI进化

向上滑动看下一个