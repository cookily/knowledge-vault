李嘉乐的数字花园 *2026年5月5日 12:21*

![图片](https://mmbiz.qpic.cn/mmbiz_png/kHh2ibPRjHicHDupoC0GEC5nNJvQlU9UzYnmaeFJQW2dibMIgfRbCBIRPj7xdEnZXyjbV0YwGtZ5OKTrU4WCzY9xIkj0U4czSibMlVrFRHDHUdo/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

> “
> 
> 今日汇总 21 条消息，共 2784 字，预计需要 6 分钟阅读。

### 1\. 探讨企业级 Agent 架构选型，推荐 OpenFang 等开源框架

**来源** ：Hermes Agent 中文社区微信群 20

企业级Agent应用落地框架，群内推荐 Dify, OpenFang, Slock.ai, Hermes/Openclaw + 企业协作平台飞书等，搭建企业内部Agentic工作流。

**链接** ：

- https://slock.ai/
- https://dify.ai/
- https://github.com/RightNow-AI/openfang

### 2\. 社区分享基于多智能体协作的量化交易研究框架 TradingAgents。

**来源** ：Hermes 中文社区 金融 量化 财会

该框架利用多模型辩论与共识机制进行综合信息整合，适用于投研分析而非纯技术面计算。实际运行需注意多模型 API 的稳定性与响应延迟，建议结合模拟盘进行长周期策略验证。

**链接** ：

- https://github.com/TauricResearch/TradingAgents

### 3\. AI 浏览器 Tabbit 可用于网页数据自动采集。

**来源** ：Hermes Agent 中文社区微信群 24

讨论指出可利用 AI 浏览器替代传统脚本进行网页数据提取。同时明确 Hermes Agent 也具备类似自动化抓取能力。

**链接** ：

- https://www.tabbitbrowser.com/?lang=zh

### 4\. 智云上海AI STORE（电信算力模型超市）开放注册，新用户赠送2500万Token额度。

**来源** ：Hermes 中文社区 电商 跨境

该项目提供算力及多款大模型按Token计费服务，目前处于推广期。个人开发者注册即可领取高额免费额度，适合需要低成本测试多模型API的Agent开发或电商内容生成场景。

**链接** ：

- https://gpushop.sh.189.cn/

### 5\. 商汤科技开放平台提供免费 Token 额度，适合新手测试与轻量调用。

**来源** ：Hermes Agent 中文社区微信群 31

官方提供阶梯式免费 Token 计划，无需付费即可接入多款模型进行功能验证。适合预算有限或处于开荒期的开发者快速跑通流程，后续可根据需求切换至付费 API。

**链接** ：

- https://www.sensenova.cn/token-plan

### 6\. 富途提供免费的 A 股行情数据 API，QMT 接口在满足资产门槛后可通过券商免费开通用于策略验证。

**来源** ：Hermes 中文社区 金融 量化 财会

获取分钟级或实时行情数据可优先对接券商 API 或使用通达信、新浪、东财等数据源。富途 OpenAPI 支持免费读取行情数据，适合低成本搭建数据管道；QMT 接口在满足资产门槛后可免费开通，建议先通过模拟盘验证策略再接入实盘。

### 7\. 寻找Hermes技能可前往GitHub搜索高星仓库，兼容 OpenClaw/Cursor 等 Skill 规范，官方Skill商店已上线

**来源** ：Hermes Agent 中文社区微信群 30

社区建议让Hermes通过GitHub按星标排序查找优质AI技能仓库。Hermes 与 OpenClaw、Claude Code、Cursor 的 Skill 规范基本一致，大部分可开箱即用，官方Skill商店已上线。

**链接** ：

- https://hermes-agent.nousresearch.com/docs/skills

### 8\. 使用mem0构建记忆系统时，原生逻辑存在数据冗余问题，需二次开发优化。

**来源** ：Hermes Agent 中文社区微信群 8

实测发现mem0原生方案会将完整对话直接存入data字段，缺乏有效过滤。在低配硬件下使用qwen2.5-7b进行语义提取效果一般，仅特定对话会触发记忆。建议根据实际业务需求对数据写入逻辑进行魔改。

### 9\. 社区推荐两款基于编程实现的 PPT 生成 Skill，支持模板适配与数据溯源。

**来源** ：Hermes 中文社区 互联网 计算机 IT

针对自动化汇报场景，推荐 html-ppt-skill 与 guizang-ppt-skill。后者采用编程方式生成，比纯图片方案更易二次编辑。建议在 Prompt 中明确要求标注数据来源，以降低幻觉风险并提升汇报可信度。

**链接** ：

- https://github.com/lewislulu/html-ppt-skill
- https://github.com/op7418/guizang-ppt-skill

### 10\. 社区分享多个大模型免费API额度获取渠道及配置注意事项

**来源** ：Hermes Agent 中文社区QQ群

整理了小米MiMo Orbit激励计划、阿里云百炼（需选北京区，单模型赠100W）、英伟达、硅基流动等平台的免费额度申请方式。部分平台注册仅校验邮箱，可多账号获取额度。链接详见微信公众号。

**链接** ：

- https://100t.xiaomimimo.com/
- https://build.nvidia.com/settings/api-keys
- https://bailian.console.aliyun.com/cn-beijing?tab=model#/api-key
- https://longcat.chat/platform/usage
- https://cloud.siliconflow.cn/i/HgknELfY

### 11\. 针对Agent过度主动编写代码的问题，可在系统提示词中明确要求优先复用现成工具库。

**来源** ：Hermes Agent 中文社区微信群 14

默认行为下Agent倾向于自行编码调试，可能忽略现有成熟方案。通过在系统提示词中显式添加约束，要求其在动手前优先搜索并调用已有工具，可有效提升开发效率与方案可靠性。

### 12\. 群友分享：Agent人格设计采用身份、思维逻辑、行为规则三层结构，实现思考与执行分工。

**来源** ：Hermes Agent 中文社区微信群 10

群友在迭代Agent人格过程中，将系统提示词拆分为身份设定、思维逻辑与行为规则三个独立层级。该结构能有效隔离“思考”与“执行”环节，使模块分工更明确，有助于提升复杂任务下的指令遵循度与输出稳定性。

### 13\. 频繁弹出审核确认窗口时，可通过询问Agent开启“yolo模式”或调整配置来减少人工干预。

**来源** ：Hermes Agent 中文社区微信群 14

部分场景下Agent会频繁请求操作确认，打断自动化流程。若常规配置未生效，可直接向Agent询问如何开启“yolo模式”（自动确认模式），或检查系统提示词中是否遗漏了免确认指令，以优化连续执行体验。

### 14\. 多次上下文压缩会导致Agent响应变慢与信息丢失，建议适时使用 /new 重置会话。

**来源** ：Hermes Agent 中文社区微信群 14

长对话中频繁触发上下文压缩会显著增加处理压力，导致响应迟钝及关键信息遗漏。建议在关键节点手动保存进度，或当压缩提示频繁出现时，直接使用 `/new` 开启新会话以恢复最佳性能。

### 15\. 结合Hermes与ComfyUI进行电商生图，利用其记忆功能免微调即可通过提示词优化迭代。

**来源** ：Hermes 中文社区 电商 跨境

将Hermes接入ComfyUI工作流后，可利用其内置记忆能力持续学习电商提示词库。无需对底层模型进行微调，通过动态替换模型与优化提示词即可实现高质量商品图生成，适合打造品牌专属视觉风格。

### 16\. Hermes原生支持多Agent配置，可参考中文社区文档

**来源** ：Hermes Agent 中文社区飞书群 1

Hermes内置多智能体协同功能，通过配置profiles可实现多Agent群聊协作。具体方法见中文文档的配置指南。

**链接** ：

- https://hermesagent.org.cn/docs/user-guide/profiles

### 17\. 模型自动切换需配置辅助/压缩/回退槽位

**来源** ：Hermes Agent 中文社区飞书群 1

Hermes支持通过配置辅助模型、压缩模型和回退模型实现token耗尽时自动切换。各槽位使用相同控制项，参考官方配置文档设置。

**链接** ：

- https://hermesagent.org.cn/docs/user-guide/configuration

### 18\. 多模型路由策略建议：按任务复杂度、上下文长度与成本分配不同模型。

**来源** ：Hermes 中文社区 互联网 计算机 IT

推荐将默认处理、低成本探索与批量执行交由 V4-Flash，复杂推理与长上下文任务使用 V4-Pro，Agentic Coding 及终端工具链任务选用 GLM-5.1。在关键动作执行前可引入 Verifier 进行复核，该策略能有效平衡 Token 消耗与任务成功率。

### 19\. 推荐 Hermes 辅助工具 hermes-web-ui 与 hermes-desktop，支持跨平台部署。

**来源** ：Hermes Agent 中文社区微信群 31

hermes-web-ui 采用前后端分离架构，后端支持 Linux，前端通过浏览器访问，国人开发且支持中文。另有 hermes-desktop 项目提供 Mac 原生适配，无 Web 依赖，可按需选择。

**链接** ：

- https://github.com/nesquena/hermes-webui
- https://github.com/dodo-reach/hermes-desktop

### 20\. awesome-openclaw-usecases 仓库提供丰富用例，Skill 机制与 Hermes 高度兼容。

**来源** ：Hermes Agent 中文社区微信群 31

该仓库汇总了大量智能体实战场景与配置模板。Hermes 的 Skill 设计与 OpenClaw、Claude Code 底层逻辑相通，相关 Skill 文件可直接迁移至 Hermes 环境中开箱即用，大幅降低开发门槛。

**链接** ：

- https://github.com/hesamsheikh/awesome-openclaw-usecases

### 21\. Hermes视觉辅助模型推荐与动态路由配置

**来源** ：Hermes Agent 中文社区QQ群

视觉辅助任务推荐使用MiMo-V2-Omni或GLM-5V模型。若需根据问题类型动态调用不同模型，可通过编写约束指令实现：向Agent描述需求并询问配置方法，Agent会生成对应的工作流或路由逻辑，支持先讨论后执行的交互模式。

扫码加入 Hermes Agent 中文社区微信群

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

图片版

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**微信扫一扫赞赏作者**

Hermes Agent 中文社区日报 · 目录

继续滑动看下一个

李嘉乐的数字花园

向上滑动看下一个