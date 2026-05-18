李嘉乐的数字花园 *2026年5月8日 08:26*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kHh2ibPRjHicE3lFdCEamBEbP6lbQK85VVGE0Ygpz5h4sT9ib1QWF4KE0DUsTnjgjNqlBrrDPUxYOv2qkRZdxHqkMfcjpsfictgaV8E8wSzw5G4/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

> “
> 
> 今日汇总 18 条消息，共 2582 字，预计需要 6 分钟阅读。

### 1\. 群友推荐“Hermes 担任大脑 + Codex 负责手脚”的双 Agent 协同架构实践

**来源** ：Hermes Agent 中文社区QQ群

群友推荐将 Hermes 作为中枢负责任务规划、记忆管理、消息平台进度汇报与 Skill 迭代，Codex 专注代码编写和端到端测试。

### 2\. 群友分享：Hermes多模型路由策略：日常任务接Mimo与GLM，复杂决策与架构设计切换至Claude/Codex接Opus 4.7与GPT 5.5。

**来源** ：Hermes Agent 中文社区微信群 30

群友实测对比多款模型后发现：Opus 4.7在任务执行效率上表现最佳。建议根据任务复杂度进行动态路由：常规交互使用Mimo v2.5pro和GLM 5.1以平衡成本与速度，涉及深度决策或系统架构设计时，则调用Claude与Codex接入Opus 4.7和GPT 5.5以提升输出质量。

### 3\. 解决Hermes模型知识截止年份滞后的问题，可通过接入互联网搜索API实现。

**来源** ：Hermes Agent 中文社区微信群 25

模型回答年份停留在训练数据截止期属正常现象。可申请第三方免费搜索服务API，如tavily，将其配置至Hermes的联网搜索功能中，即可让模型实时获取最新信息，无需频繁更换底层模型。

**链接** ：

- https://www.tavily.com/

### 4\. 国产麒麟系统可通过Docker方式安装运行Hermes。

**来源** ：Hermes Agent 中文社区微信群 29

针对国产操作系统的部署问题，确认只要底层为Linux环境即可支持。若原生安装遇到系统限制或依赖冲突，可通过Docker容器化部署作为标准替代方案，确保在国产化环境中稳定运行。

### 5\. 东方财富旗下金融AI技能包“妙想Skills”发布

**来源** ：Hermes 中文社区 金融 量化 财会

东方财富旗下金融AI技能包“妙想Skills”正式发布。该产品内置了大量开箱即用的专业金融领域技能。并在底层原生集成了高频更新的机构级金融数据库MCP。

**链接** ：

- http://ai.eastmoney.com/

### 6\. 量化数据源对比：Tushare积分制付费，AKShare免费但定位不同

**来源** ：Hermes 中文社区 金融 量化 财会

大模型直接调用金融数据易产生幻觉，建议接入专业数据源。全量A股历史数据可选Tushare Pro；AKShare免费但稳定性差，更适合宏观另类因子而非行情替代。Qlib是AI量化建模框架，可与上述数据源配合使用。

### 7\. 外置记忆系统推荐：Honcho 是一套开源的 AI 原生记忆后端，通过"辩证推理"持续分析用户偏好与行为模式，构建动态用户画像。

**来源** ：Hermes 中文社区 互联网 计算机 IT

社区方案 elkimek/honcho-self-hosted 提供一键脚本，依赖 Docker + PostgreSQL + pgvector + Redis，需 Ubuntu 22.04+、6GB RAM，约3分钟完成。之后 hermes memory setup 指向本地实例即可。

**链接** ：

- https://github.com/elkimek/honcho-self-hosted

### 8\. 免费搜索API体验不佳时，可改用SearXNG自建或公开实例以节省额度。

**来源** ：Hermes Agent 中文社区微信群 34

免费搜索引擎API常出现响应差或额度消耗快的问题。推荐部署SearXNG自建搜索引擎，或直接使用网上公开的实例作为替代方案。该方案能有效节省API调用额度，但需注意使用公开实例可能存在查询记录留存的风险。

**链接** ：

- https://searx.space/

### 9\. LiteLLM 网关的 Token 消耗统计比 Hermes 内置计算更精准。

**来源** ：Hermes 中文社区 互联网 计算机 IT

在需要精确展示消耗数据时，推荐使用 LiteLLM 作为统一网关。其 Token 计数机制更为准确，且支持多 Profile 统一管理与调用链追踪，可替代频繁切换本地配置的操作。

### 10\. WSL环境下浏览器接管技能调通经验及CDP方案踩坑记录

**来源** ：Hermes 中文社区 电商 跨境

在Windows WSL中成功配置浏览器接管技能。实测发现直接使用CDP协议易报错且常触发反爬风控，而模拟鼠标操作方案效率低且消耗Token较多。推荐尝试阿里开源的PageAgent作为替代方案，可提升自动化效率并规避部分风控问题。

**链接** ：

- https://github.com/alibaba/page-agent

### 11\. 飞书流式卡片插件 V3.3.0 发布，支持多 Profile 隔离与 DeepSeek 思维链兼容

**来源** ：Hermes Agent 中文社区飞书群 1

该插件采用 sidecar-only 架构，支持单服务多 Profile 进程内隔离、多 Bot 路由绑定及群聊分流。新增表格超限保护避免 11310 错误，并兼容 DeepSeek 思维链标签过滤。插件具备故障隔离机制，sidecar 不可用时自动降级为原生文本输出，保障服务连续性。

**链接** ：

- https://github.com/baileyh8/hermes-feishu-streaming-card

### 12\. 使用Hermes结合本地模型与技能蒸馏进行小说创作，可有效通过平台AI检测。

**来源** ：Hermes Agent 中文社区微信群 25

通过为Hermes配置本地大模型（如千问3.6 35B），并蒸馏先进闭源模型的逻辑思维，可大幅提升长文本生成质量。该方案在小说连载场景中表现稳定，且经技能蒸馏后的输出能有效通过主流内容平台的AI检测机制。

### 13\. RTX 50系显卡运行本地大模型的显存优化与量化配置建议。

**来源** ：Hermes Agent 中文社区微信群 25

在5070 Ti等50系显卡上部署模型时，建议根据实际显存大小选择对应的量化版本。可nvfp4量化格式专为50系Blackwell架构原生支持，在Linux、WSL2等vLLM可用环境下均可使用，能显著压缩模型体积并提升加载效率。

### 14\. 中文社区日报 MCP 与 RSS 订阅功能已开发完成，后续将根据负载情况逐步上线。

**来源** ：Hermes Agent 中文社区微信群 21

Hermes Agent 中文社区已实现日报 MCP 及 RSS 订阅功能。目前因接口调用压力较大暂未开放，后续将根据负载情况逐步上线。

### 15\. 可通过 Termux 在安卓手机部署 Hermes

**来源** ：Hermes 中文社区 互联网 计算机 IT

可通过 Termux 在安卓手机部署 Hermes，建议设备内存 4GB 以上。 实测在安卓端安装 Termux 后可直接运行 Hermes。该方案适合移动端调试或轻量级场景，需注意设备内存门槛，目前实际业务落地场景仍在探索中。

### 16\. 可通过已配置的智能体辅助安装，并实现跨智能体协同控制。

**来源** ：Hermes Agent 中文社区微信群 35

安装初期可借助 Workbuddy，Openclaw 等智能体自动完成 Hermes 的环境配置。部署完成后，Hermes 可作为主控节点指挥运行在 Windows 桌面的 OpenClaw 等执行本地程序调用，有效弥补 WSL 环境直接调取桌面应用的限制。

### 17\. 云服务器部署适合纯问答场景，自动化操作需本地部署。

**来源** ：Hermes Agent 中文社区微信群 35

云端环境无法直接访问或操作用户本地电脑文件与软件，仅能完成文本交互。若目标是实现本地文件处理、软件自动化等流程，推荐采用本地部署方案。

### 18\. 记忆文件膨胀与 Skill 自动创建的处理策略

**来源** ：Hermes Agent 中文社区飞书群 1

`memory.md` 记录冗余信息属正常现象，建议仅保留核心记忆，将详细内容指针存放于 `hindsight` 或外部笔记软件，并可设计联想记忆机制控制上下文大小。Skill 频繁自动创建无需手动清理，Hermes新版本内置 Curator 机制会随时间自动处理，重点应放在核心 Skill 的迭代优化上。

扫码加入 Hermes Agent 中文社区微信群

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

图片版

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**微信扫一扫赞赏作者**

Hermes Agent 中文社区日报 · 目录

继续滑动看下一个

李嘉乐的数字花园

向上滑动看下一个