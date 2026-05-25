阿飞 *2026年5月16日 16:21*

> 当你的团队里多了几个不知疲倦的 AI 同事，如何给他们分配任务、跟踪进度、管理交付？Hermes Kanban 提供了一套完整的解决方案。

一个 AI Agent 能做的事有限，但当多个专业 Agent 协同工作——研究员调研、分析员综合、工程师编码、审查员把关——整个团队的生产力将产生质的飞跃。

Hermes Kanban 就是为此设计：一张持久化的任务看板，让多个 AI Agent 像人类同事一样协作完成任务。

本文将介绍：

是什么：Hermes Kanban 的核心概念

能做什么：典型应用场景

怎么用：通过一个实际案例演示完整操作流程

---

## 什么是 Hermes Kanban

Hermes Kanban 是一个持久化任务看板，基于 SQLite 数据库存储，支持多代理并行协作。

## 核心概念

| 概念 | 说明 |
| --- | --- |
| **Board（看板）** | 一个独立的任务队列，默认只有一张看板，也支持多项目隔离 |
| **Task（任务）** | 任务卡片，状态流转： `triage（待分类）→ todo（待办）→ ready（就绪）→ running（运行中）→ blocked（阻塞）→ done（完成）` |
| **Worker** | 被调度器 spawn 出来的代理进程，有自己独立的执行环境和持久记忆 |
| **Dispatcher（调度器）** | 每 60 秒扫描一次 ready 任务，分配给对应的 Agent 执行 |
| **Link（链接）** | 父子依赖关系，父任务完成后子任务自动晋升为 ready |

Kanban vs delegate\_task

|  | delegate\_task | Kanban |
| --- | --- | --- |
| 特性 | 阻塞等待，fire-and-forget | 持久队列，状态机驱动 |
| 恢复性 | 失败就失败 | block/unblock、crash reclaim支持 |
| 可介入 | 不支持 | 任何阶段可评论介入 |
| 协作 | 单代理 | 多代理并行/管道 |
| 审计跟踪 | 上下文压缩后丢失 | SQLite 持久行，永远可查 |

一句话：delegate\_task是函数调用，Kanban是工作队列。

## 两种入口

Hermes Kanban 提供两个操作入口：命令行和web页面可视化操作

在操作前需要创建多个agent，我们将不同任务分配给不同的agent来执行

通过命令行创建可参考： [5分钟用 Hermes 搭建多 Agent 机器人](https://mp.weixin.qq.com/s?__biz=MzI2NTU0NTI2Nw==&mid=2247483851&idx=1&sn=6243d6a286414e760612c3ec942aff99&scene=21#wechat_redirect)

通过webui来创建，首先执行命令启动webui,然后打开链接

http://127.0.0.1:9119

```nginx
hermes dashboard
```

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

打开后可设置为中文，然后点击多AGENT配置中的创建，输入agent名称后即可创建成功

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E) ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

然后我们就可以设置这个agent的soul.md了

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

## 应用场景

基于 HermesKanban 的能力，结合开发团队实际应用场景：

需求 → 设计 → 开发 → 测试 → 部署

| 阶段 | 分配AGENT | 典型任务 |
| --- | --- | --- |
| 需求分析 | researcher | 调研竞品、用户调研、需求文档 |
| 架构设计 | architect | 技术方案、API 设计、数据库设计 |
| 后端开发 | backend | 写接口、业务逻辑、数据库 |
| 前端开发 | frontend | 页面、组件、样式 |
| 代码审查 | reviewer | Review PR、提修改意见 |
| 测试 | tester | 写测试用例、回归测试 |
| 部署上线 | deployer | CI/CD、上线检查、监控 |

后续我尝试搭建一下，感兴趣的也可以自己搭建一套基于自身业务流的看板任务

## 实际案例演示

## Step 1：初始化

创建一个看板

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

## Step 2：创建研究任务

任务还可以单独指定使用哪些skill技能，填写完相关信息后，点击create完成创建

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

点击刚刚创建的任务，分配负责人，填写之前创建的researcher，回车保存，然后点击下方的SPECIFY按钮进行需求详细分析，完成后可以看到状态变为就绪，并且任务的描述也更加详细了

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E) ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

然后在页面上点击触发调度器即可开始执行这个任务

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

点击运行中的任务可查看任务运行的工作日志

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

## Step 3：分解子任务

在这个执行中过程我们还可以按照刚才的操作流程创建一个任务，并设置其父任务为刚刚的调研任务

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

然后点击触发调度器后查看工作日志，会检测父任务的状态和输出，如果父任务执行完成，该任务使用父任务的输出来作为上下文来完成自己的任务

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

由于缺少一些必要信息，任务进入到阻塞阶段，需要用户进行手动输入评论补充信息，我们补充后点击评论并点击解除阻塞，会重新回到就绪状态，再次点击触发调度器即可

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E) ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E) ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

触发后获取到我们评论的信息并重新进行投资建议了

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

## Step 4：完成任务

最后完成后，查看任务，我们能看到任务的所有状态流转和运行历史以及工作日志

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

## 总结

Hermes Kanban 的核心价值：

1. 持久化：任务不丢失，Agent 重启后继续执行
2. 协作：多 Agent 管道式协作，依赖自动管理
3. 透明：实时日志、完整审计跟踪
4. 容错：block/unblock、crash reclaim、熔断机制

当你的工作流需要跨越多个 AI Agent、需要人工介入、需要长时间运行或需要持久化保障时，Kanban 是比delegate\_task更合适的选择。

---

相关资源：

https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/kanban

爱马仕Agent系列 · 目录

作者提示: 个人观点，仅供参考

继续滑动看下一个

AIGClaw

向上滑动看下一个