ASI启示录 *2026年5月19日 15:05*

### 新智元报道

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Rvq8Ow69CYVQEYfs3YD2kZM71crdPrbuxCXJoRzv064GDh4zong4r7giarqe0cwplj3yHibpyDGaicVInWicX33r081ibM4B3kO4KzGYJItUpRtQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

##### 【新智元导读】游戏规则要被改写了！Hermes Agent一键把模型订阅变成标准API，零成本驱动全套工具链。Grok同步杀入Agent生态。

就在刚刚，两大开源Agent框架接连甩出硬核更新，大厂最不想看到的「订阅转API」被公然搬上了台面。

Hermes Agent v0.14祭出大杀器，一行hermes proxy命令，就能把ChatGPT Pro、Claude Pro、SuperGrok的月费订阅变成标准API端点，零成本驱动Aider、Codex CLI等全套本地开发工具。

另一边，OpenClaw释出5.18巨型更新。不仅攻克了Agent操控浏览器弹窗的顽疾，上线了Android实时语音流，而且还从底层原生打通了Grok OAuth认证。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**Grok全面杀入Agent生态**

Hermes这边，xAI官方亲自下场，一口气把Grok的全套能力栈都塞进了Hermes Agent。

只要你有SuperGrok订阅，Hermes就能通过OAuth调用Grok 4.3的全套能力栈，文本对话、语音合成、图片和视频生成、音频转录，一个不落。

不仅如此，Grok 4.3的上下文窗口也被拉到了100万token。开发者可以把整个代码仓库或全套研究语料，全部塞进一个prompt里，无需任何切片或摘要。

更值得一提的是，Hermes接入后会默认开启Grok跨请求prompt缓存，同一会话中的重复system prompt绝不重复计费。

甚至，xAI还为此在官网发了专门的接入指南页面，域名是x.ai/news/grok-hermes。

安装命令就一行curl，文档里连SSH远程主机的OAuth隧道配置都写好了。

```bash
# 安装Hermes Agent：curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash# 选择Grok：hermes model# 选择xAI Grok OAuth（SuperGrok订阅），通过浏览器登录，然后开始聊天：hermes --tui
```

与此同时，OpenClaw也在火速「补课」。

5.18版本精准修复了xAI的OAuth PKCE认证兼容问题，结合前几个版本对reasoning effort参数的持续适配，OpenClaw用户现在终于能如丝般顺滑地跑起Grok。

**20美元月费，现在能喂饱整条工具链**

但Grok跑通只是开始。真正颠覆游戏规则的，是hermes proxy背后那套极其粗暴的机制。

具体来说，它会在本地拉起一个HTTP端口，对外暴露标准的OpenAI兼容API格式，实际的推理请求则穿透你已有的OAuth授权，走订阅的调用额度。

这带来的后果是颠覆性的。

现在，一个每月支付20美元订阅ChatGPT Pro的用户，可以在终端里毫无顾忌地跑Codex CLI，让GPT-5.5零额外成本包揽代码编写、审查与重构。

同理，Claude Pro用户也能毫无阻碍地将Aider或Claude Code直接指向这个本地端口，全自动驱动整个开发工作流。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

当然，大厂的「反制」边界依然锋利。

前不久，一位月费高达200美元的Claude Max用户，仅仅因为Hermes在工作目录里遗留的一个hermes.md文件，不幸精准触发了Anthropic的第三方调用风控逻辑，被系统反手倒扣200.98美元API账单。

主打一个宁可错杀一千，不放过一个。

| ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E) | ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E) |
| --- | --- |

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**OpenClaw的「补债式」大更新**

OpenClaw 5.18版本是一场极其典型的「补债」行动。

在经历4月底至5月初Gateway降速、插件依赖陷入死循环、Discord等频道集体异常以及大批用户被迫降级的「黑暗时刻」后，创始人Peter Steinberger亲自发文「OpenClaw Had a Rough Week」。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

这场危机的根源在于OpenClaw激进的架构「瘦身」，团队试图将Amazon Bedrock、Slack以及OpenShell沙箱等重型内置依赖剥离为按需插件。

大方向虽对，但过渡期的阵痛却极其惨烈。

由此催生的5.18版本祭出了一份长到令人窒息的更新日志，单是bugfix就狂飙破百。

虽然每一条都不大。但都是真实用户在GitHub issue里反复报告的痛点。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

5.18正式版发布4小时后，5.19 beta就跟上了。

对于一个373k star的项目来说，这个迭代节奏已经接近SaaS产品的hotfix速度。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**Hermes的「去重」哲学**

Hermes v0.14被称为「The Foundation Release」（基石版本）。

最直观的优化是冷启动时间被狂砍19秒，底层架构全面转向重型依赖按需（首次使用）安装。

对于一个需要7×24小时待命的Agent而言，累积起来就是质的体验飞跃。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E) ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

另一个极具杀伤力的特性是，𝕏平台的搜索能力被打通了。

原生内置的x\_search，支持OAuth与API Key双通道认证，赋予Agent在对话中穿梭、检索时间线、帖子和讨论串的权限。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

在工程细节上，LSP（语言服务器协议）语义诊断被深度缝合进写文件流程，Agent每次修改完代码都会被强制自动跑一遍language server，终结了「嘴上说加了函数，文件却根本没保存」的低级运行幻觉。

新增的/handoff命令则支持活跃会话实时迁移，调试到一半从Claude切到Grok，全部上下文一条不丢。

安装门槛也被砍到了底：Hermes直接上了PyPI，一行pip install hermes-agent即装即跑，连clone仓库都省了。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**生态闭环，正被强行击穿**

OpenClaw破百的bugfix与Hermes抢回的19秒冷启动，是保证Agent不崩溃、不断连的留存底牌。

但「订阅转API」引发的底层变局更为致命。

过去，Claude和GPT依赖API绑定构筑了极高的生态迁移门槛；现在，hermes proxy将这层绑定彻底撕裂。

开发者今天用Claude Pro跑Aider，明天切ChatGPT Pro调Codex CLI，后天换SuperGrok吞吐百万token，生态切换成本瞬间归零。

对Anthropic和OpenAI而言，最稳健的订阅客正被强行洗成全网流动的开发者，20美元的月费不再受限于任何一家巨头的私有体系。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

在这场生态解绑的浪潮中，xAI扮演了最凌厉的破局者。

Grok在两大主流框架同时跑通，也暴露了它的策略转向。

借道OpenClaw与Hermes合计超50万的开发者生态，xAI瞬间完成了原始积累。

这笔账，远比从零死磕自家开发者平台要精明得多。

面对xAI的强势入局，Anthropic和OpenAI下一步是物理限流、狂改ToS还是索性放开？

无论如何，游戏规则已被颠覆。

当准入门槛被抹平，这片坐拥50万star的开发者狂潮，注定比任何大厂更快跑出最终答案。

参考资料：

https://x.com/openclaw/status/2056504927795437826?s=20  
https://github.com/openclaw/openclaw/releases/tag/v2026.5.18

https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.16

编辑：摩西

**秒追ASI**

**⭐** **点赞、转发、在看一键三连** **⭐**

**点亮星标，锁定新智元极速推送！**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

继续滑动看下一个

新智元

向上滑动看下一个