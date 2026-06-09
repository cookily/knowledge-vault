李嘉乐的数字花园 *2026年6月1日 08:59*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kHh2ibPRjHicFFmibSkDBlibI1IDuxu00TzzKo4bJNn61evYgppQ5wLibIvianGE4sIWBIssU5aibZOoh4OAdZogHmTmXWtK8wOq1LOvYS4wZMzYew/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

> “
> 
> 今日汇总 27 条消息，共 3603 字，预计需要 8 分钟阅读。

### 1\. Hermes Agent 中文社区启动下一阶段垂直行业群建设并公示入群指南

Hermes Agent 中文社区正逐步建立覆盖自媒体、教育、工业制造，医疗，法律，金融，零售业等领域的垂直行业交流群，并同步公开了社区整体架构与各行业群的申请流程，详情可查看https://hermesagent.org.cn/community。

### 2\. 推荐借助 Claude Code 或 Codex 辅助排查 Hermes 异常并配置 helper profile

遇到 Hermes 更新或运行异常时，可接入 Claude Code 或 Codex 的 API 进行自动化代码修复。建议为 Hermes 创建 helper 类型的 profile 与外部 Agent 协同，以便将排查过程与解决方案沉淀为永久记忆。多 Agent 交叉维护能有效提升系统容错率。

### 3\. 提升Hermes浏览器表单操作稳定性的三种实践方案

针对自动化填表易出错的问题，可将固定流程沉淀为程序脚本。若需动态校验，可在提交前截图交由视觉模型判定字段，或让模型在Skill内生成Checklist进行严格自检后再执行提交。

### 4\. 开源项目 iHermes 支持通过手机端直接控制 Hermes Agent

社区分享了移动端控制方案，该项目提供了手机直连与操作 Hermes Agent 的能力，适合需要远程监控或移动端交互管理的开发者场景。

**链接** ：

- https://github.com/2winter-dev/iHermes

### 5\. 企业级Hermes私有化部署与数据安全合规实践

出于数据防泄露要求，部分企业会禁用公有云服务并强制采用私有化部署方案。标准版Hermes支持开箱即用的本地化部署方案，无需二次开发即可接入本地大模型。

### 6\. Hermes 架构稳定适合生产环境，附 OpenClaw 更新避坑指南

生产环境业务流程推荐优先使用 Hermes，其破坏性更新较少且架构更稳定。若使用 OpenClaw，需注意其频繁更新易导致崩溃，建议升级前彻底清理旧文件从零重装，或优先在 Ubuntu 环境下部署以提升稳定性。

### 7\. 社区推荐 mem0 与 tencentdb-agent-memory 作为 Agent 记忆管理方案

在讨论 Agent 长期记忆与上下文管理时，群内分享了 mem0 和腾讯云 tencentdb-agent-memory 两款工具。两者均可用于构建 Agent 的记忆层，开发者可根据自身技术栈与部署需求进行选型测试。

### 8\. GPT 在 Hermes 中对 soul 人格定义的遵循度优于 DeepSeek

在 Hermes Agent 中接入不同模型时，GPT 能更严格地执行 soul 文件中设定的规则与交互逻辑。DeepSeek 在复杂指令遵循上表现稍弱，开发者可根据任务对规则敏感度的需求进行模型切换。

### 9\. Agent不遵循提示词和调用Skill不积极的根因分析及优化方案

该现象多由底层LLM指令遵循能力不足导致。可通过prefill\_messages\_file预加载、调用skill\_view及在SOUL.md添加强约束提升Skill执行概率，但根本解决需更换指令遵循能力更强的模型，如GPT-5.5。

### 10\. 获取A股实时数据推荐Tushare付费接口，网页爬虫易触发IP封禁

直接爬取财经网站获取实时行情极易触发反爬机制导致IP被封。稳定方案为接入Tushare等专业数据平台，其免费档仅提供历史数据，实时行情需开通VIP。低频用户可评估按量付费或寻找替代数据源。

### 11\. 利用Hermes Agent配置启发式教学角色辅导作业，结合视觉模型实现拍照解题

通过配置SOUL与profile界定Agent角色边界，设定为教师身份并禁止直接给出答案，采用启发式问答引导。推荐搭配DeepSeek模型，并使用群友词优化器完善角色设定。同时配置vision辅助模型支持题目拍照上传，建议通过网关接入微信或飞书机器人，并在台式机或Linux桌面端部署以便监管使用记录。

### 12\. 利用AI实现电商自动上品的模型选择与工具建议

自动上架涉及表单填写与图片识别，纯文本模型易漏读隐藏元素，建议选用多模态大模型。实现路径可结合Hermes或Codex的Computer Use功能编写脚本，或直接接入影刀等RPA工具。主流电商平台均提供上架API，但个人开发者申请存在一定资质门槛。

### 13\. 搜索工具配置建议与Skill资源站分享

DuckDuckGo搜索偶有抽风，可切换至Tavily（需注意月度额度限制）。群内提及存在混合搜索Skill可提升检索稳定性，并分享了两个Skill资源站，便于开发者查找和复用现成能力模块。

**链接** ：

- https://skillsmp.com/zh
- https://www.skills.sh/

### 14\. Skill机制原理与多Skill加载的Token消耗影响

Skill在架构中充当AI的执行模块与经验库，负责具体任务落地。同时加载多个Skill会占用更多上下文窗口，导致单次请求的Token消耗相应增加，需根据实际任务按需挂载。

### 15\. 主流大模型Token消耗效率横向对比

实际业务场景测试表明，Minimax与DeepSeek在同等任务下的Token利用率较高，具备性价比优势。相比之下，Kimi与通义千问的上下文生成策略更倾向于长文本输出，Token消耗量显著偏大。

### 16\. 工业场景AI落地建议聚焦固定流程RPA化，避免自主决策

工业环境对幻觉容忍度极低，当前LLM方式暂不适合直接参与核心控制或参数生成。推荐将Agent用于执行死逻辑操作、固定报表生成、远程文件调取及标书错别字检查等辅助场景，通过自然语言调用指定流程，实现类似企业级RPA的效果。

### 17\. Claude Code 升级至 v2.1.153+ 后第三方模型接口报错，降级至 v2.1.148 可恢复

新版将 system 参数从顶级移至 messages 数组，导致讯飞、Kimi 等端点拒绝请求或返回空响应。通过 npm 指定安装旧版本可临时规避，目前仅 DeepSeek 端点已适配新版协议。

**链接** ：

- https://blog.csdn.net/zxs9999/article/details/161508333

### 18\. 马维斯与Hermes定位差异及Windows部署建议

马维斯侧重系统管家与轻办公，安装门槛低但内置可视化渲染较消耗内存显存。Hermes定位为开发工具，在Windows环境下推荐通过WSL部署以提升兼容性与运行效率，老旧硬件亦可流畅承载。

### 19\. 配置Hermes生图能力需接入外部API或配置生图Skill，推荐GPT-Image-2结合Seedance2的视频工作流

部分模型默认无法直接生图，需手动配置生图Skill或对接第三方图像API。实测推荐采用GPT-Image-2生成故事板，再衔接Seedance2或火山引擎模型转视频，音频部分建议单独接入Suno或TTS服务以保证质量。

**链接** ：

- https://github.com/EvoLinkAI/GPT-Image-2-Seedance2-Workflow

### 20\. 开源短视频自动生成项目MoneyPrinterTurbo分享

社区分享了基于大模型的短视频自动化生成开源项目，支持一键生成文案、配音、字幕及视频合成。该项目适合快速搭建自媒体内容生产流水线，可作为Hermes工作流的外部组件或参考实现。

**链接** ：

- https://github.com/harry0703/MoneyPrinterTurbo

### 21\. 开源工具 SkillClaw 支持 Hermes 持续集体技能进化

该工具作为独立后台服务运行，专注于自动化提取与优化用户自定义技能。实测可批量消化历史消息并生成新技能，适用于希望实现技能库自动迭代与沉淀的开发者。部分反馈指出当前版本稳定性仍需优化。

**链接** ：

- https://github.com/AMAP-ML/SkillClaw/

### 22\. 推荐RTK终端输出Token压缩代理工具

针对Agent交互Token消耗过快的问题，可引入RTK工具。该工具为单Rust二进制文件且零依赖，通过拦截终端输出进行智能压缩，宣称可节省60%至90%的Token消耗。

**链接** ：

- https://github.com/rtk-ai/rtk

### 23\. 开源规则管理工具rulesink分享

社区分享的rulesink项目提供规则集中管理方案，支持AI自动读取配置。适合需要规范Agent行为的场景，可替代部分硬编码约束。

**链接** ：

- https://github.com/Leedhao1029/rulesink

### 24\. Claude Code Workflow功能支持固化多Agent长任务流程

Workflow适用于需要稳定执行的业务流程，可通过保存任务实现上下文隔离的长时间运行。与Skills不同，Workflow更抽象且支持多Agent协作，适合企业级固化需求，但会消耗较多token。

### 25\. OpenAI Codex Pro 额度限时加倍活动持续至 5 月 31 日，具体剩余额度以官方面板为准

官方确认Codex额度重置时间为本周五，200美元套餐的20X倍率保持不变，5X套餐的10X活动将于5月31日结束。高强度使用需关注额度消耗节奏。

### 26\. Codex Computer use功能支持自动化页面测试，DeepSeek需结合curl测API

Codex的Computer use可直接操作界面进行功能测试，而DeepSeek缺乏视觉能力，建议通过curl命令测试API接口。复杂页面测试仍需依赖具备多模态能力的模型。

### 27\. 开源项目codex-bridge实现Claude Code与DeepSeek模型桥接

该项目允许在Claude Code环境中调用DeepSeek等第三方模型，扩展工具生态。需注意DeepSeek API暂不支持多模态功能，识图需求需搭配其他服务。

**链接** ：

- https://github.com/wujfeng712-ui/codex-bridge

扫码加入 Hermes Agent 中文社区微信群

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**微信扫一扫赞赏作者**

Hermes Agent 中文社区日报 · 目录

阅读原文

继续滑动看下一个

李嘉乐的数字花园

向上滑动看下一个