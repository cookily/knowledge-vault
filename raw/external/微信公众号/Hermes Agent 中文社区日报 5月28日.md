李嘉乐的数字花园 *2026年5月28日 07:48*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kHh2ibPRjHicFb4iaRN559xYfUkyUlI3jQhyXxPwna1iamlNu55PmHSr8LLDdia4ZAJC1dL38SWsNXq80PnjdmNhibsqQDyGPrD2YW8wPVgzOssQI/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

> “
> 
> 今日汇总 20 条消息，共 2707 字，预计需要 6 分钟阅读。

### 1\. 小米 Mimo 大模型大幅降价并提升 Token Plan Credits 额度，按量计费 API 价格对标Deepseek

官方近期调整定价策略，月度Max套餐额度提升至820亿Credits，需注意Credits不等于Token，有一定换算比例。按量计费 API 最高降幅达99%，纸面计价与DS基本持平，但实际调用时需要注意缓存率。

**链接** ：

- https://platform.xiaomimimo.com/

### 2\. 华为发布生产级 AI Agent 平台 OpenJiuwen

社区分享了华为最新发布的OpenJiuwen平台链接。该平台提供 Agent Ops, Swarm 相关的能力与特性。建议有相关需求的团队对其进行调研与测试，分享使用体验。

**链接** ：

- https://openjiuwen.com/

### 3\. 开源飞书流式卡片插件更新，采用官方插件机制替代AST注入

该插件基于Hermes Agent v0.14.0 引入的官方插件能力开发，实现即插即用，官方版本升级后无需重新注入。已修复页脚显示异常及内容重复问题。安装时若存在旧版插件需先彻底卸载以避免兼容冲突。

**链接** ：

- https://gitee.com/Aowen-Nowor/hermes-lark-streaming

### 4\. 推荐文本与多模态任务分离的降本策略：文本用DeepSeek，多模态用小米Mimo模型

实际使用表明，因缓存命中率较高，模型有效消耗低于预期。小米模型在视觉处理上表现较好，可弥补DeepSeek暂不支持多模态的短板。建议采用“文本任务调用DeepSeek、多模态任务调用小米Mimo模型”的组合架构，以实现整体调用成本最优。

### 5\. 基于看板与Worker异常通知机制实现多Agent协同处理

在Hermes中处理任务异常时，推荐采用看板模式：主Agent下发任务卡片至看板，Worker节点领取执行。若Worker遇到异常或违规情况，会自动触发通知回传主Agent，由主Agent进行二次处理或人工介入，该模式有效解耦了执行与决策流程。

### 6\. 小米 Mimo 平台 开发者百万亿 Token 计划额度重置并提升至原额度的5-8倍

针对已获取过激励的用户，平台近期重置了Token额度，发放量达到原先的5到8倍。该资源可用于补充大模型调用额度，适合有高频API调用需求的开发者。

**链接** ：

- https://platform.xiaomimimo.com/

### 7\. 调用/kanban技能可实时监控多Agent任务状态与进度

针对多Agent协作流程不透明的问题，Hermes内置了/kanban技能。该功能支持实时追踪并可视化展示各个子Agent的执行情况，便于开发者及时干预调度与排查阻塞节点。

### 8\. 本地部署Gemma4与Qwen3.6组合可显著降低云端Token消耗

针对多Agent协作与状态监控带来的高Token成本问题，推荐采用本地大模型作为日常开发主力。实测部署Gemma4与Qwen3.6组合能够覆盖大部分常规场景，有效节省约80%的云端API开销。

### 9\. 使用Obsidian构建个人知识库与可视化图谱

推荐利用Obsidian的双向链接与插件生态搭建个人知识库，其内置图谱视图能直观展示文档关联关系。适合需要沉淀技术文档或进行知识管理的开发者。

**链接** ：

- https://obsidian.md/

### 10\. Hermes部署NAS对接微信文件传输方案

直接通过Hermes将NAS文件推送至微信受平台接口限制较难实现。推荐替代方案为让Agent直接生成飞书云文档以便协同编辑，或指示Agent自行编写脚本桥接至本地指定微信文件路径。

### 11\. Hermes Agent调用模型选型与Token成本控制建议

实测对比发现qwen3.7-max与deepseek-v4-pro能力相近但前者成本更高。为降低Hermes运行开销，推荐切换至deepseek-v4系列，其中v4-flash版本性价比突出，v4-pro目前亦有大幅降价，适合长文档处理与高频调用场景。

### 12\. AI辅助编程场景下Rust与NestJS开发体验最佳，Go与Dart相对较弱

多语言实测表明，AI生成代码质量与可维护性排序为Rust优于NestJS，其次为Python，Go与Dart相对较弱。Node.js虽AI生成顺畅但依赖包体积大且环境切换繁琐。在AI加持下各语言均可快速上手，但追求代码质量与稳定性仍推荐强类型语言。

### 13\. Codex 生成代码偏慢且倾向使用 Python 脚本操作文件，可结合DeepSeek V4优化 Review 工作流

实测Codex响应速度不及Cursor或CC，且常通过生成Python脚本间接执行文档操作而非直接调用MCP。推荐采用Codex生成初稿、DeepSeek V4 Pro进行代码审查、再将结果反馈给Codex迭代的组合工作流，可显著提升代码质量与审查效率。

### 14\. 非多模态模型可通过配置辅助视觉模型实现识图，硅基流动提供免费DS OCR服务

当主模型不支持图像识别时，可在Hermes的九大辅助模型中指定 GLM-4V-flash 等视觉模型专门处理图片请求。此外，硅基流动平台目前提供免费DeepSeek OCR和DeepSeek TTS服务，可作为原生视觉能力受限时的有效替代。

### 15\. 美团已发布跑腿 Skill，千问等平台也提供类似生活类技能

美团官方推出了支持 Agent 调用的跑腿 Skill，可直接集成至工作流中完成跑腿下单。同类生活场景技能在千问等生态中亦有提供，可快速丰富 Agent 的本地服务调用能力。

### 16\. Hermes 支持直接部署至树莓派或 ESP32 等开发板实现硬件控制

无需额外复杂套件，Hermes 可直接部署在树莓派等边缘计算设备上。结合设备自带系统或开发板即可实现传感器读取与硬件控制，适合 DIY 机器人或物联网自动化项目。

### 17\. 推荐 Reasonix 工具优化 DeepSeek 接口缓存命中率

该工具围绕 DeepSeek 的缓存机制构建，旨在进一步提升请求的缓存命中率。适合需要高频调用 DeepSeek 模型且对响应延迟与成本敏感的开发者场景。

**链接** ：

- https://github.com/esengine/deepseek-reasonix

### 18\. 社区经验表明 Hermes 技能使用已从依赖下载转向自主创建与提炼

初期用户多直接下载现成 Skill，随着使用深入，更推荐根据实际工作流自主创建和提炼技能。自主构建的技能能更好贴合个人业务场景，显著提升 Agent 执行效率与稳定性。

### 19\. 推荐量化Agent模型路由组合：MiniMax 2.7h + OpenCode Go + 本地Qwen3-VL

针对金融量化场景的Agent架构，验证了一套稳定的模型路由配置。主逻辑推理调用MiniMax 2.7h，代码生成任务使用OpenCode Go套餐中的DS-V4等，多模态视觉分析部署本地Qwen3-VL。该组合在实测中兼顾了推理成本、代码准确率与响应速度。

### 20\. 基于Tushare接口实现集合竞价异动监控脚本

社区内分享了一套用于A股集合竞价阶段的监控脚本方案，底层数据接口采用Tushare。脚本可自动过滤低置信度信号并输出异动结果，配合模型情绪分析模块，能有效规避早盘假突破与盲目开仓风险。

扫码加入 Hermes Agent 中文社区微信群

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**微信扫一扫赞赏作者**

Hermes Agent 中文社区日报 · 目录

继续滑动看下一个

李嘉乐的数字花园

向上滑动看下一个