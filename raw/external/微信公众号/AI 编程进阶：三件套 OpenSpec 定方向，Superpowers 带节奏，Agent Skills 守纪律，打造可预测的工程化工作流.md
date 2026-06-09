前端AI行走 *2026年4月29日 10:00*

## AI 编程三件套

> 一套让 AI 编程从「碰运气」变成「可复制」的三件套工作流

---

## 开篇：AI 编程的「三体问题」

2026 年，AI 编程助手已经不再是新鲜事。Claude Code、Codex CLI、Cursor、Gemini CLI……每个工具都能帮你写代码。但用过的人都知道一个残酷的现实：

**让 AI 写 100 行代码容易，让 AI 高质量地完成一个完整功能，难。**

问题出在哪？三个致命短板：

1. **需求漂移** —— AI 在聊天记录里找需求，聊着聊着就忘了最初要做什么
2. **流程失控** —— AI 上来就写代码，没有设计、没有测试、没有审查，写完就跑
3. **纪律缺失** —— AI 今天用这个风格写，明天换那个方式写，代码质量像过山车

这三个问题，恰好对应了三个开源项目的解决方案：

| 问题 | 解决方案 | 核心理念 | 一句话 |
| --- | --- | --- | --- |
| 需求漂移 | **OpenSpec** | Spec-Driven Development | **用文档定 AI** |
| 流程失控 | **Superpowers** | Agentic Skills Framework | **用流程带 AI** |
| 纪律缺失 | **Agent Skills** | Skill Lifecycle Management | **用纪律管 AI** |

三个工具各自解决一个问题，组合起来就是一套 **AI 编程的「铁三角」工作流** 。

本文将从零开始，带你搭建这套完整工作流。

---

## 第一章：认识三位主角

### 1.1 OpenSpec —— 用文档定 AI

- **GitHub**: Fission-AI/OpenSpec
- **Stars**: 43.2k ⭐
- **最新版本**: v1.3.1 (2026-04-21)
- **维护者**: Fission AI (61 位贡献者)
- **支持工具**: 25+ AI 编程助手（Claude Code、Codex、Cursor、Gemini CLI、Copilot 等）

**核心哲学** ：

> 在人机之间先达成共识，再让 AI 写代码。

OpenSpec 的本质是一个 **轻量级规范驱动开发 (Spec-Driven Development, SDD) 框架** 。它不是瀑布模型那种又臭又长的需求文档，而是一个「在写代码前先对齐预期」的轻量协议。

**工作原理** ：

```
你说：/opsx:propose "添加暗黑模式"

AI 自动生成：
├── proposal.md     ← 为什么要做，要改什么
├── specs/          ← 需求场景和验收标准
├── design.md       ← 技术方案
└── tasks.md        ← 实现任务清单

你审阅确认后：
/opsx:apply        ← AI 按 tasks.md 逐条实现

完成后：
/opsx:archive      ← 归档到 archive/，更新 specs
```

**关键特性** ：

- **Fluid, not rigid** — 随时可更新任何文档，没有严格的阶段门禁
- **Iterative, not waterfall** — 支持渐进式迭代
- **Built for brownfield** — 不只是新项目，老项目同样适用
- **Scalable** — 从个人项目到企业级都行

**OpenSpec 的核心命令** ：

| 命令 | 作用 | 使用阶段 |
| --- | --- | --- |
| `openspec init` | 初始化项目 | 一次性 |
| `/opsx:propose` | 提出变更提案 | 需求阶段 |
| `/opsx:apply` | 执行实现 | 开发阶段 |
| `/opsx:archive` | 归档变更 | 完成阶段 |
| `/opsx:verify` | 验证实现 | 质量检查 |
| `openspec update` | 更新 AI 指令 | 周期性 |

**对比竞品** ：

- vs. GitHub Spec Kit：OpenSpec 更轻量，不需要 Python 环境和严格的阶段门禁
- vs. AWS Kiro：OpenSpec 不锁定 IDE，不限制模型
- vs. 不用工具：裸用 AI 就是赌运气

---

### 1.2 Superpowers —— 用流程带 AI

- **GitHub**: obra/superpowers
- **Stars**: 169k ⭐
- **最新版本**: v5.0.7 (2026-03-31)
- **作者**: Jesse Vincent (Prime Radiant)
- **支持平台**: Claude Code、Codex CLI、Codex App、Cursor、OpenCode、Copilot CLI、Gemini CLI

**核心哲学** ：

> AI 不应该「自由发挥」，而应该遵循一套经过验证的软件工程流程。

Superpowers 不是一个简单的「提示词合集」，它是一套 **完整的软件开发方法论** ，通过可组合的技能 (Skills) 驱动 AI 按照工程最佳实践工作。

**完整工作流** ：

```
1. brainstorming          ← 需求澄清与设计（Socratic 问答式）
   ↓
2. using-git-worktrees   ← 创建隔离开发环境（独立 worktree + 新分支）
   ↓
3. writing-plans          ← 编写详细实现计划（每个任务 2-5 分钟）
   ↓
4. subagent-driven-dev    ← 子 Agent 并行开发（每个任务一个 agent）
   或 executing-plans     ← 批量执行（带人工检查点）
   ↓
5. test-driven-dev        ← 强制 RED-GREEN-REFACTOR 循环
   ↓
6. requesting-code-review ← 代码审查（按严重程度分级）
   ↓
7. finishing-branch       ← 收尾：验证测试、合并/PR/废弃决策
```

**关键设计理念（注意：以下均属「AI 行为约束」，不是文件系统级钩子）** ：

- **基于上下文主动选用** — Superpowers 把 skill 元数据注入到 `AGENTS.md` 上下文，AI 模型在执行任务时按语义匹配主动调用对应 skill；漏选时人可显式指定（例如「请先用 brainstorming 技能澄清」）
- **子 Agent 驱动开发** — 每个任务可派发独立子 Agent 执行，带两阶段审查（规格一致性 + 代码质量）；主 Agent 仍负责编排决策与失败回收
- **TDD 优先（非系统级强制）** — `test-driven-development` skill 引导 AI 先写失败测试再写实现；若发现违规已生成的实现代码，Superpowers 会指示模型撤回并按 RED-GREEN 顺序补上。要做到「不可绕过」需叠加 `git pre-commit` / CI 闸门
- **YAGNI + DRY 内建** — 工程最佳实践以 skill 形式提供给 AI 参照，仍以模型遵从为主，超大改动建议人审

**技能分类** （共 15+ 个）：

| 分类 | 技能 | 说明 |
| --- | --- | --- |
| **协作** | brainstorming | Socratic 式需求澄清 |
| **协作** | writing-plans | 详细实现计划（精确到文件路径） |
| **协作** | executing-plans | 批量执行 + 检查点 |
| **协作** | subagent-driven-development | 子 Agent 并行 + 两阶段审查 |
| **测试** | test-driven-development | RED-GREEN-REFACTOR |
| **调试** | systematic-debugging | 四阶段根因分析 |
| **调试** | verification-before-completion | 确保真的修好了 |
| **协作** | requesting-code-review | 按严重程度分级审查 |
| **协作** | receiving-code-review | 响应审查反馈 |
| **Git** | using-git-worktrees | 并行开发分支 |
| **Git** | finishing-a-development-branch | 合并/PR/废弃决策 |
| **协作** | dispatching-parallel-agents | 并行子 Agent 调度 |
| **元** | writing-skills | 创建新技能 |
| **元** | using-superpowers | 技能系统介绍 |

**安装方式** （按平台）：

```
# Claude Code (官方市场)
/plugin install superpowers@claude-plugins-official

# Cursor
/add-plugin superpowers

# Gemini CLI
gemini extensions install https://github.com/obra/superpowers

# Copilot CLI
copilot plugin marketplace add obra/superpowers-marketplace
copilot plugin install superpowers@superpowers-marketplace

# Codex CLI
/plugins → 搜索 superpowers → Install

# OpenCode
Fetch and follow instructions from
https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.opencode/INSTALL.md
```

---

### 1.3 Agent Skills —— 用纪律管 AI

- **GitHub**: addyosmani/agent-skills
- **Stars**: 24.3k ⭐
- **作者**: Addy Osmani (Google Chrome 团队工程总监)
- **技能数量**: 20+ 个
- **核心创新**: 7 命令技能生命周期管理

**核心哲学** ：

> AI Agent 需要「可编程的纪律」——不是每次手动提示，而是把最佳实践编码为可复用、可版本控制的技能。

Agent Skills 的定位是 **SDLC 全流程覆盖** ：从需求分析到生产部署，每个阶段都有对应的技能来规范 AI 的行为。

**7 命令技能生命周期** ：

```
init → verify → install → on → off → update → uninstall
```

这是 Agent Skills 最独特的创新——不是给你一堆提示词模板，而是 **提供一套完整的技能管理命令** 。你可以像管理 npm 包一样管理 AI 行为规则。

**20 个技能分类** ：

| 阶段 | 技能 | 核心约束 |
| --- | --- | --- |
| **需求分析** | req-clarify | 3 轮限定的需求澄清对话 |
| **需求分析** | req-breakdown | 将需求拆解为可执行任务 |
| **需求分析** | req-review | 对齐 PRD 缺口 |
| **设计** | design-architect | 方案对比 + 决策理由必须记录 |
| **设计** | design-api | OpenAPI 3.0 强制输出 |
| **设计** | design-db | 强制规范命名和数据字典 |
| **设计** | design-deliver | 拆解到可估算的开发工单 |
| **设计** | design-frontend | 组件树 + 状态管理设计 |
| **设计** | design-security | 全面安全审查 |
| **开发** | code-structure | 文件 ≤ 500 行, 函数 ≤ 50 行 |
| **开发** | code-documentation | 公共 API 必须有 JSDoc |
| **测试** | test-coverage | 分支覆盖率 ≥ 80% |
| **测试** | test-quality | 边界 + 异常覆盖 |
| **安全** | security-dependencies | 检查已知漏洞 |
| **安全** | security-secrets | 防止密钥泄露 |
| **安全** | security-api | API 安全检查 |
| **生产** | production-ready | 全面 Release Checklist |
| **维护** | code-incident-review | Postmortem → 改进计划 |
| **维护** | code-refactoring | 大规模重构支持 |
| **文档** | doc-generate | 自动文档生成 |

**关键约束示例** ：

```
# code-structure 技能的约束
- 每个源文件不超过 500 行
- 每个函数不超过 50 行
- 超过限制 → AI 必须自动拆分

# test-coverage 技能的约束
- 分支覆盖率不低于 80%
- 不达标 → 不允许提交代码
- 自动生成覆盖率报告
```

**安装与使用** ：

```
# 初始化技能库
agent-skills init

# 验证技能格式
agent-skills verify

# 安装所有技能
agent-skills install

# 启用特定技能
agent-skills on test-coverage code-structure

# 停用（不想用的）
agent-skills off design-security

# 更新到最新
agent-skills update

# 卸载
agent-skills uninstall
```

---

## 第二章：三者如何完美结合

### 2.1 关系模型

三个工具不是竞争关系，而是 **工程流水线上的三个工位** ：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**一句话总结** ：

- **OpenSpec 管「说清楚」** —— 在你和 AI 之间建立一份书面契约
- **Superpowers 管「做对事」** —— 确保 AI 每一步都走对流程
- **Agent Skills 管「做得好」** —— 确保 AI 产出的代码符合工程标准

### 2.2 组合原则

三者组合时有三个关键原则：

**原则一：层次分明，各司其职**

| 层次 | 工具 | 谁主导 | 产出物 | 强度 |
| --- | --- | --- | --- | --- |
| 需求层 | OpenSpec | 人 + AI 协作 | proposal.md, specs/, design.md | CLI 校验（ `openspec validate` ）可程序性强制 |
| 流程层 | Superpowers | AI 按上下文主动调用 skill | tasks.md, 测试报告, 审查记录 | 模型遵从层（行为约束） |
| 纪律层 | Agent Skills | AI 遵从 + CI 闸门双保险 | 代码规范、覆盖率、安全检查 | 仅靠 AI 不足以"强制"，需配合 pre-commit / CI |

**原则二：顺序执行，不可跳跃**

❌ 跳过 OpenSpec 直接写代码 → 需求漂移  
❌ 跳过 Superpowers 直接实现 → 流程混乱  
❌ 跳过 Agent Skills 直接提交 → 质量失控

✅ 三步都做到 → 需求清晰、流程规范、质量可控

**原则三：工具互补，避免冲突**

- OpenSpec 的 `tasks.md` 是 Superpowers 中 `writing-plans` 的输入
- Superpowers 的 `subagent-driven-development` 执行 Agent Skills 的纪律约束
- Agent Skills 的 `production-ready` 检查 OpenSpec 的 spec 是否被满足

---

## 第三章：完整工作流实操

### 3.1 总体流程图

下面用「总览 + 三个闸门子图」表达同一条主链路：

- 总览图只回答： **Step 1~8 的顺序** （不展开回退细节）。
- 子图只回答：当需求、评审、安全 **卡住** 时， **回到哪里/停在哪里** （闭环要显式）。

#### 3.1.1 主链路总览

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

#### 3.1.2 闸门子图 1：需求确认（/opsx:propose）

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

#### 3.1.3 闸门子图 2：代码评审通过（requesting-code-review）

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

#### 3.1.4 闸门子图 3：安全失败回退（security-\* + 修复）

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### 3.2 分步详解：谁在什么时候做什么

> 本节用一份真实需求贯穿 8 步， **所有 OpenSpec 制品片段均来自本仓库** `source/live-app-openspec-demo/openspec/changes/feat-live-share-third-party/` ，可直接对照查看完整文件。

#### 真实输入：产品需求表（节选）

| 字段 | 内容 |
| --- | --- |
| 模块描述 | 分享直播地址到第三方平台 |
| 功能描述 | 可分享到微信、朋友圈、QQ、QQ 空间、微博 |
| 优先级 | 高 |
| 前置条件 | 用户进入直播间，点击分享按钮 |
| 需求说明 1.1 | 用户点击分享按钮，弹出分享渠道列表（自下往上、纵向布局、背景透明）；点击空白退出 |
| 需求说明 1.2 | 点击分享后，系统自动检测设备是否安装相应应用程序；如需第三方授权，则弹出授权窗口（授权过程保持系统后台运行，直播正常） |
| 需求说明 1.3 | 用户确认分享时，自动抓取主播头像作为分享链接的缩略图；直播标题（或系统设定固定的文案内容模板） |
| 需求说明 1.4 | 分享评论的过程保持 app 后台运行，直播状态；分享完成点击「返回」回到直播间 |
| 后置条件 | 点击屏幕任意空白处退出分享状态 |
| 补充说明 | 分享到第三方渠道如需相应的接口，需求中未说明的请指出 |

这份需求最像真实业务文档： **字段散、口径模糊、隐含前提多** 。下面演示三件套如何把它一步步变成可执行、可验收的工程产物。

---

#### ▶ Step 1：需求对齐（OpenSpec 主导）

**谁来做** ：人（发起）+ AI（生成）+ 人（审阅确认）

```
# 人在 AI 编码助手中输入
/opsx:propose "新增直播间分享到第三方渠道：微信/朋友圈/QQ/QQ 空间/微博，含底部面板、第三方授权期间直播保活、主播头像 + 标题/兜底模板"

# ↑ OpenSpec 规则触发，AI 不会写代码，
#   而是生成 4 类制品（proposal/spec/design/tasks）。
```

**AI 自动生成（真实路径，与本仓库一致）** ：

```
source/live-app-openspec-demo/openspec/changes/feat-live-share-third-party/
├── proposal.md   ← 为什么做、要改什么、影响面
├── specs/
│   └── third-party-live-share/
│       └── spec.md   ← ADDED Requirements + Scenario
├── design.md     ← 关键工程决策、Open Questions
└── tasks.md      ← 实现清单（按编排/渠道/素材/保活/验证 5 块）
```

**proposal.md 关键片段（真实文件）** ：

```
# Change: feat-live-share-third-party

## Why
直播是拉新与回流的高转化场景，但用户在房间内分享链接到主流社交渠道时，
常遇到「渠道未安装」「授权跳转后直播被误停」「分享素材与直播间信息不一致」等问题。
产品需求表已明确分享渠道、面板交互与保活要求，需要以规范驱动方式在实现前对齐验收口径。

## What Changes
- 在直播房间内提供「分享」入口，弹出底部纵向渠道列表
  （微信、朋友圈、QQ、QQ 空间、微博），透明蒙层，点击空白区域关闭面板。
- 选择渠道前检测目标 App 是否已安装且满足 SDK 最低版本；
  不满足时给出可理解提示并可引导至应用商店（策略可配置）。
- 分享链路中不因进入第三方授权/编辑页而主动停止直播推流或播放；
  用户从第三方返回后仍停留在原直播间且状态一致。
- 分享卡片缩略图使用主播头像；分享文案优先使用直播间标题，
  缺失时使用系统固定模板。
```

**spec.md 关键片段（真实文件，OpenSpec **ADDED Requirements** 语法）** ：

```
# Spec: third-party-live-share

## ADDED Requirements

### Requirement: 分享面板展示与关闭
用户在直播房间内 MUST 能通过「分享」入口打开分享面板；
面板 MUST 自屏幕底部以纵向列表展示可选渠道；
MUST 显示透明蒙层；
用户点击蒙层空白区域 MUST 关闭面板并恢复直播 UI 焦点。

#### Scenario: 打开与关闭面板
**WHEN** 用户已进入直播间且直播进行中并点击「分享」
**THEN** 系统 MUST 自底部展示包含微信、朋友圈、QQ、QQ 空间、微博的渠道列表
**AND** 系统 MUST 展示透明蒙层
**WHEN** 用户点击蒙层空白区域
**THEN** 系统 MUST 关闭分享面板并恢复直播房间交互焦点

### Requirement: 授权与分享期间直播保活
在用户进入第三方授权、编辑或发布流程期间，宿主 App MUST NOT 主动向音视频模块
发送「停止直播/停止推流」指令；除非操作系统强杀或用户显式结束直播，
直播核心状态 MUST 与进入分享流程前保持一致。

#### Scenario: 跳转第三方后返回
**WHEN** 用户完成第三方侧分享或取消并返回宿主 App
**THEN** 用户 MUST 仍停留在原直播间
**AND** 直播状态 MUST 与进入第三方前一致（未误触结束直播）
```

> 注意需求表里那行模糊的话：「 **保持 app 后台运行，直播状态** 」。 spec 把它 **翻译成 MUST/MUST NOT 的可验证条款** ：宿主 **禁止** 主动调用「停止直播」， 否则就是规格违反——这一步消除了最常见的「按需求理解的差异」。

⏱️ **这一步耗时：人 5 分钟审阅 + AI 30 秒生成** ✅ **完成标志** ：你说「proposal/spec 我看过了，可以进入澄清」 ⚠️ **注意** ：本仓库 `README.md` 里有真实 CLI 全过程，可直接复刻： `npx @fission-ai/openspec validate feat-live-share-third-party` 必须返回 `Change ... is valid` 。

---

#### ▶ Step 2：需求澄清（Superpowers 主导 + Agent Skills 约束）

**谁来做** ：AI 在加载 `brainstorming` skill 后主动进入 Socratic 模式向人反问；人只在被询问时回复。 **前提** ：Superpowers 已安装且 skill 元数据注入到 `AGENTS.md` /系统上下文，否则 AI 仍会直接进入实现。

需求表里那些「模糊词」此时会被 Superpowers 的 **brainstorming** 抓出来反问：

```
AI（Socratic 模式）：在进入实现前，先把以下口径锁住，否则 spec 会留歧义：

Q1. 「保持 app 后台运行」=  a) 宿主进程不被杀  /  b) 不向直播域发送停止指令？
    （决定保活策略与是否需要前台服务）
Q2. 「分享渠道列表」中微信与朋友圈是否合并到同一 SDK 入口（scene）？
Q3. 微博是否走官方 SDK，还是允许降级到系统 ACTION_SEND？
    （影响 design.md 与 tasks.md 的渠道矩阵）
Q4. 标题为空时的「系统固定模板」文案是什么？谁审？
Q5. 缩略图加载失败的占位图由谁提供，圆角/尺寸是否在 UI 规范？
```

这些问题最终被沉淀到 `design.md` 的 **Open Questions** 中（真实文件片段）：

```
## Open Questions
- 微博最终走「官方 SDK」还是「系统分享面板降级」——需产品 + 法务确认后回填到 spec.md
  （可能触发 **MODIFIED** 块）。
```

Agent Skills 的 **req-clarify** 在背后约束： **最多 3 轮** 澄清，超了就强制总结并落到 Open Questions，避免无限讨论。

⏱️ **这一步耗时：人 5-10 分钟回答 + AI 推理 1-2 分钟** ✅ **完成标志** ： `design.md` 含 Decisions + Open Questions，你说「确认」

---

#### ▶ Step 3：分支隔离（Superpowers 主导）

**谁来做** ：AI 调用 `using-git-worktrees` skill 执行（ **前提** ：仓库已是 git 仓库且 `using-git-worktrees` skill 在上下文里）

```
# AI 在 IDE Agent 模式下执行以下命令（不是 OS 钩子，是 AI 调 bash）
git worktree add -b feat/live-share-third-party ../app-live-share
cd ../app-live-share

# 跑一次 baseline 防止脏状态污染
./gradlew :app:assembleDebug
./gradlew test
```

这一步非常关键——它创建了一个 **完全隔离** 的 workspace：

- 微信、QQ、微博三个 SDK 接入互不干扰，可以分子任务并行开发；
- 多 ROM 兼容性回归（小米/华为/OPPO/vivo）失败时， **直接删 worktree** ，主分支零污染；
- baseline 跑通后，后续 TDD 失败一定是新代码引入的，不会和老问题混淆。

⏱️ **这一步耗时：AI 调命令 ~30 秒；baseline 编译 + 测试取决于工程规模（数分钟到十几分钟）**

---

#### ▶ Step 4：计划制定（Superpowers 主导 + OpenSpec 提供输入）

**谁来做** ：AI 调用 `writing-plans` skill 生成计划（ **前提** ：上一步已生成的 `tasks.md` 在仓库内可读）

Superpowers 的 **writing-plans** 读取 OpenSpec 生成的 `tasks.md` （ **本仓库真实文件** ），把粗粒度任务细化为可执行计划：

```
# Tasks: feat-live-share-third-party

## 1. 编排与 UI 骨架
- [ ] 1.1 定义 RoomContext 与 ShareCoordinator 入口 API
- [ ] 1.2 实现底部渠道面板 + 透明蒙层 + 点击空白 dismiss（含无障碍焦点顺序）
- [ ] 1.3 在直播间工具栏接入「分享」入口并埋点 share_panel_open

## 2. 渠道注册与检测
- [ ] 2.1 定义 ShareChannel 接口及 ShareChannelRegistry 注册表
- [ ] 2.2 实现微信渠道：canShare（安装 + 版本）与 share（SDK 调用占位）
- [ ] 2.3 实现朋友圈渠道：与微信 SDK 的能力分支（scene / 类型）对齐
- [ ] 2.4 实现 QQ 与 QQ 空间渠道：安装检测与 SDK 唤起占位
- [ ] 2.5 实现微博渠道：按设计「Open Questions」结论落地 SDK 或降级方案

## 3. 分享内容与网络
- [ ] 3.1 实现 SharePayloadFactory：标题兜底模板、标题长度与截断策略
- [ ] 3.2 主播头像异步加载、缓存、失败占位图与圆角裁切规范

## 4. 生命周期与保活
- [ ] 4.1 审计分享全链路：确保无任何路径调用「停止直播/停止推流」除非用户显式结束
- [ ] 4.2 覆盖从第三方返回后的 Activity / 栈恢复（多厂商 ROM 手动矩阵，记录结果）

## 5. 验证与发布
- [ ] 5.1 按 specs/third-party-live-share/spec.md 中各 Scenario 编写测试用例并执行
- [ ] 5.2 日志与崩溃脱敏审计（无 token、无敏感 query）
```

每条任务都是「 **精确文件/接口 + 验收口径** 」，不是「写一个分享功能」。 Agent Skills 的 **req-breakdown** 在此约束：每个任务 **可独立验证、可独立回滚** 。

⏱️ **这一步耗时：AI 推理 1-2 分钟（产出细化计划文档）**

---

#### ▶ Step 5：子 Agent 并行开发（Superpowers + Agent Skills 双管齐下）

**谁来做** ：主 Agent 编排 + 子 Agent 执行（人在合并冲突、SDK 鉴权失败、ROM 兼容回归卡住等场景下需要介入）

`design.md` 的 **Decisions** 已经把工程边界划好，子 Agent 拿到的是清晰约束（真实片段）：

```
## Decisions
1. 编排层命名与职责
   - Decision：引入 ShareCoordinator，持有 RoomContext
     （roomId、title、anchorAvatarUrl、streamStateHandle）。
   - Rationale：避免在 Fragment/ViewController 内散落 if (wechat) … ，便于单测与埋点。
2. 渠道抽象
   - Decision：ShareChannel 接口：id、displayName、icon、
     canShare(context) -> Result、share(context, payload)。
3. 保活策略
   - Decision：直播推流/播放的启停 ONLY 由直播域 API 控制；
     分享流程禁止调用「结束直播」。
```

Superpowers 的 **subagent-driven-development** 把 5 大任务切成多个子 Agent：

| 子 Agent | 处理任务 | 可并行 |
| --- | --- | --- |
| Agent-UI | 1.2 / 1.3 面板 + 入口 + 埋点 | ✅ |
| Agent-WeChat | 2.2 / 2.3 微信 + 朋友圈（同一 SDK） | ✅ |
| Agent-QQ | 2.4 QQ + QQ 空间 | ✅ |
| Agent-Weibo | 2.5 微博（按 Open Questions 结论） | 取决于结论 |
| Agent-Payload | 3.1 / 3.2 标题兜底 + 头像加载 | ✅ |
| Agent-Lifecycle | 4.1 / 4.2 保活审计 + ROM 回归 | ❌（依赖 1.x） |

每个子 Agent 跑两阶段审查： **规格一致性** （必须对齐 spec.md 的 MUST 条款）+ **代码质量** （命名/结构/异常）。

同时 Agent Skills 提供以下行为约束（仍属模型遵从层，不是文件级强制）：

- `code-structure` ：建议单文件 ≤ 500 行、单函数 ≤ 50 行（避免「ShareCoordinator 一个文件 2000 行」）；
- `test-driven-development` ：每个 `canShare()` 行为先写失败测试再写实现；
- `code-documentation` ： `ShareChannel` 接口的所有公开方法必须有注释。

> 要把这三条变成「不可绕过」，需要把同样的检查 **复制到 `pre-commit` 与 CI** （如 `detekt` / `ktlint` / 行数 lint / 文档覆盖率检查），AI 行为 + CI 闸门双保险才算真正强制。

⏱️ **这一步耗时：15-30 分钟（多渠道适配并行；含子 Agent 推理 + 编译，不含真机回归）**

---

#### ▶ Step 6：测试 + 审查（Superpowers 主导 + Agent Skills 量化）

**谁来做** ：AI 调用 `test-driven-development` + `requesting-code-review` skill 执行（人审阅关键检查点；CI 上同步跑同一组测试与覆盖率门槛才能真正阻断不达标合入）

最关键的一条 spec：「 **分享期间直播保活** 」。Superpowers 的 **TDD** 用一段失败测试把它锁死：

```
// 真实场景驱动的失败测试（节选）
@Test
fun \`分享流程期间不得向直播域发送停止指令\`() {
    val streamSpy = StreamControlSpy()
    val coordinator = ShareCoordinator(streamControl = streamSpy)

    coordinator.present(roomContext)
    coordinator.onChannelSelected(ChannelId.WECHAT)
    // 模拟唤起微信授权页 → 返回宿主
    coordinator.onReturnFromThirdParty()

    assertThat(streamSpy.stopInvocations).isEqualTo(0)   // RED ❌（还没接保活策略）
}
```

跑一遍：

```
$ ./gradlew :share:test# RED ❌
> 1 test failed:
  分享流程期间不得向直播域发送停止指令

# Superpowers 引导 AI 写最少代码（保活策略）后
$ ./gradlew :share:test# GREEN ✅
$ ./gradlew :share:test --rerun-tasks   # 再跑一遍，全绿

$ git commit -m "feat(share): keep stream alive across third-party flow"
```

之后是 Superpowers 的 **requesting-code-review** （按严重度分级）：

```
🔴 CRITICAL：无
🟡 WARNING：ShareCoordinator 在 onChannelSelected 时未对 RoomContext 做空检查
🟢 INFO：建议把「微博 SDK 必选 / 可降级」抽成 BuildConfig 开关
📊 测试覆盖率：分支 86%（≥ 80% ✅）
```

Agent Skills：

- `test-coverage` ：要求分支覆盖 ≥ 80%（AI 行为约束；要做到「不达标禁止提交」需把覆盖率门槛配置到 CI，例如 `jacoco` + `coverage-check` 工作流）；
- `test-quality` ：必须覆盖 spec 里的 4 个核心 Scenario（打开/关闭、未安装、版本不足、跳转返回）。

⏱️ **这一步耗时：5-10 分钟（AI 跑测试 + 自审）+ 人审阅 3 分钟**

---

#### ▶ Step 7：安全检查（Agent Skills 主导）

**谁来做** ：AI 调用 `security-*` skills 执行（ **前提** ：Agent Skills 已 install 且对应 skill 已 enable；同一组检查应同步进 CI 才能不可绕过）

回到 spec.md 的真实条款：

```
### Requirement: 隐私与日志
系统 MUST NOT 在日志或崩溃报告中打印第三方 access_token、refresh_token
或可用于识别用户的敏感授权字段。
```

Agent Skills 把它落成 3 个安全闸门：

```
security-secrets       → 扫描仓库与崩溃日志：0 access_token / refresh_token ✅
security-dependencies  → 微信/QQ/微博 SDK 已知漏洞：0 high / 0 critical ✅
security-api           → 分享请求审计：URL 不携带 token；UA 不含用户 ID ✅
```

任意一项失败 → **AI 停下并报告** ；要做到「不可绕过的阻断」需把这 3 项检查同步落到 CI（如 `gitleaks` / `trivy` / OWASP Dependency-Check），与 3.1.4 的安全失败闸门子图配套生效。

⏱️ **这一步耗时：1-2 分钟（AI 触发 skill 扫描；CI 上完整跑可能更长）**

---

#### ▶ Step 8：验证 + 收尾（三方协作）

**谁来做** ：AI 主导 + 人最终确认

**8a. OpenSpec 验证** ：

```
$ npx @fission-ai/openspec validate feat-live-share-third-party
Change 'feat-live-share-third-party' is valid
Progress: 4/4 artifacts complete
```

`/opsx:verify` 会逐条对照 `specs/third-party-live-share/spec.md` 的 Scenario：

```
✅ Scenario: 打开与关闭面板
✅ Scenario: 目标 App 未安装
✅ Scenario: SDK 版本不满足
✅ Scenario: 跳转第三方后返回
✅ Scenario: 标题缺失时的兜底
✅ Scenario: 调试日志脱敏
```

**8b. Agent Skills 生产就绪检查** ：

```
✅ 单测/集成测全绿     ✅ 分支覆盖 ≥ 80%
✅ 无 token/秘密泄漏    ✅ ROM 兼容矩阵已记录
✅ 文案/标题兜底生效    ✅ 回滚开关：feature flag share_panel.enabled
```

**8c. Superpowers 收尾** （finishing-a-development-branch）：

```
All tasks complete. What would you like to do?
1. Merge branch
2. Create PR              ← 选择
3. Keep branch
4. Discard branch
```

**8d. OpenSpec 归档** ：

```
/opsx:archive
# 归档到：openspec/changes/archive/2026-04-27-feat-live-share-third-party/
# specs/third-party-live-share/ 主规格自动更新为「已发布」状态
```

⏱️ **这一步耗时：2 分钟（CLI 归档 + AI 触发）+ 人决策 1 分钟**

---

#### ⚠️ 边界声明：三件套是「行为约束」，不是「系统级强制」

为了避免读者把上面 8 步当成「装上就万事大吉」的银弹，需要把三件套的真实强度讲清楚：

| 强度等级 | 表现 | 由谁保证 | 本文涉及 |
| --- | --- | --- | --- |
| **程序性强制（最强）** | 命令失败即流程中断 | CLI / 编译器 / CI 闸门 | `openspec validate`  、`./gradlew test` 、CI Job |
| **AI 行为约束（中）** | AI 主动遵守，但可能漏选/绕过 | Skill 元数据 + 模型选择 | brainstorming、TDD、code-structure、test-coverage、security-\* |
| **流程惯例（最弱）** | 写在文档/规范里 | 团队共识 + 人审 | "PR 必须有 Reviewer"、"覆盖率 ≥ 80%" 等口头约定 |

**实务建议** ：

1. **关键质量门槛同时落两层** ：例如「分支覆盖率 ≥ 80%」既写进 `test-coverage` skill（让 AI 写代码时主动达标），也配置到 CI（不达标禁止合并）；
2. **secrets / SDK 安全** 必须以 CI 闸门为准： `gitleaks` / `trivy` / OWASP Dependency-Check 等接入流水线，AI 的 `security-*` skill 只是早期发现；
3. **AI 漏选 skill 时人要显式指定** ：发现 AI 直接跳到写代码，明确说「请先用 brainstorming 澄清」或「按 test-driven-development 先写 RED 测试」；
4. **不可绕过的事不要交给 skill** ：删除生产数据、改 `migrations/` 、改 prod 配置、改 main 分支，这些用 git hook / 仓库保护规则锁住。

> 一句话： **OpenSpec 的 `validate` 是程序性强制；Superpowers 与 Agent Skills 是 AI 行为约束。** 把三者按强度分层，再用 CI 兜底，才是工程化、可靠交付的形态。

---

### 3.3 完整流程时间估算

> 时间口径说明：以下"AI 推理"指模型在 IDE Agent 模式下生成 + 调用 CLI 的累计耗时（不含真机回归 / 真实 SDK 联调 / CI 排队）；分享到第三方这种含多 SDK 接入的场景实际可能更长。

| 步骤 | 谁做 | 耗时（AI 推理 + 命令执行） |
| --- | --- | --- |
| 1\. 需求对齐 | 人审 + AI 生成 | 5 分钟 |
| 2\. 需求澄清 | AI（brainstorming）+ 人答 | 5-10 分钟 |
| 3\. 分支隔离 | AI 调用 git | 30 秒（不含 baseline 构建） |
| 4\. 计划制定 | AI（writing-plans） | 1-2 分钟 |
| 5\. 子 Agent 开发 | 主/子 Agent + 人介入卡点 | 15-30 分钟（不含真机回归） |
| 6\. 测试 + 审查 | AI + 人 | 8-13 分钟（不含 CI 完整流水线） |
| 7\. 安全检查 | AI（security-\*）+ 推荐叠 CI | 1-2 分钟（CI 上更长） |
| 8\. 验证 + 收尾 | AI + 人决策 | 3 分钟 |
| **总计** |  | **40-65 分钟（不含真机/CI/审批）** |

其中 **人真正需要投入的时间** ： **约 10-15 分钟** （主要在 Step 1 审阅 spec 和 Step 6 审查关键检查点）

---

## 第四章：安装配置指南

### 4.1 环境准备

```
# 前置要求
node --version  # ≥ 20.19.0 (OpenSpec 要求)
git --version   # ≥ 2.30
```

### 4.2 安装 OpenSpec

```
# 全局安装
npm install -g @fission-ai/openspec@latest

# 进入项目目录，初始化
cd your-project
openspec init

# 生成 AGENTS.md（AI 助手的操作指南）
# 之后在 AI 编码助手中即可使用 /opsx:* 命令

# 升级新版本
npm install -g @fission-ai/openspec@latest
openspec update   # 刷新 AI 指令
```

**OpenSpec 支持的工具列表** （部分）：

Claude Code · Codex CLI · Codex App · Cursor · Gemini CLI · Copilot · Windsurf · Cline · Roo Code · Amazon Q · CodeRabbit · Auggie · CoStrict · Amp · IBM Bob · CodeBuddy · Coffin · Factory · Qoder · Kilo Code · OpenCode · Qwen Code · Qoder · Trae

完整列表见：docs/supported-tools.md

### 4.3 安装 Superpowers

根据你的 AI 编码工具选择安装方式：

```
# Claude Code（推荐路径）
/plugin install superpowers@claude-plugins-official

# 或者通过 Superpowers 自己的市场
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace

# Cursor
/add-plugin superpowers

# Gemini CLI
gemini extensions install https://github.com/obra/superpowers

# GitHub Copilot CLI
copilot plugin marketplace add obra/superpowers-marketplace
copilot plugin install superpowers@superpowers-marketplace

# 更新
# Claude Code 插件通常自动更新
# Gemini CLI:
gemini extensions update superpowers
```

**安装验证** ：启动 AI 编码工具后，随便说一句「我想做一个新功能」，如果 AI 开始反问你的需求而不是直接写代码，就说明 Superpowers 已生效。

### 4.4 安装 Agent Skills

```
# 克隆仓库
git clone https://github.com/addyosmani/agent-skills.git
cd agent-skills

# 初始化技能库（生成默认配置）
agent-skills init

# 验证技能格式（确保所有 SKILL.md 语法正确）
agent-skills verify

# 安装所有技能到 AI 工作目录
agent-skills install

# 启用你需要的技能
agent-skills on test-coverage code-structure code-documentation \
           design-architect design-api \
           security-dependencies security-secrets \
           production-ready

# 停用暂时不需要的技能（减少上下文消耗）
agent-skills off design-security code-incident-review

# 更新技能到最新版本
agent-skills update
```

**注意** ：技能会消耗 AI 的上下文窗口（token）。建议初期只启用 5-8 个最核心的技能，后续根据需要逐步添加。

---

## 第五章：实战演练 —— 完整案例

让我们用一个 **教学向** 的完整案例来串起整条链路（与第三章「分享直播到第三方」的真实 spec 可对照阅读；本章侧重 **对话与步骤的样貌** ）。

> **口径** ：下文中的「自动」指 AI 在 **已安装 OpenSpec 指令、Superpowers 与相关 skill 已注入上下文** 时的典型表现，属于 **模型行为** 而非系统钩子； **不可绕过** 的质量门槛仍应以 CLI 与 **CI 闸门** 为准，见第三章「边界声明」。

### 背景

你维护一个 React + TypeScript 的 Dashboard 项目。用户反馈希望增加「 **数据导出为 CSV** 」功能。

### 全流程实际操作

#### 5.1 发起提案

```
👤 你（在 Claude Code 中）：
/opsx:propose "Dashboard 数据导出为 CSV 功能"

🤖 AI（OpenSpec 指令生效）：
正在生成提案…
✓ proposal.md 已创建
✓ specs/csv-export/spec.md 已创建
✓ design.md 已创建
✓ tasks.md 已创建
```

#### 5.2 审阅 + 确认

```
# specs/csv-export/spec.md

## Scenario: 用户在 Dashboard 中导出选中数据
Given 用户在 Dashboard 页面，已选中 3 条记录
When 用户点击 "导出 CSV" 按钮
Then 浏览器下载一个 CSV 文件
And 文件包含选中的 3 条记录
And 文件名格式为 export-YYYY-MM-DD.csv

## Scenario: 未选中任何记录时导出
Given 用户在 Dashboard 页面，未选中任何记录
When 用户点击 "导出 CSV" 按钮
Then 显示 Toast 提示 "请先选择要导出的数据"
And 不触发下载
```
```
👤 你：确认提案，并补充一个场景：导出超过 10000 条时显示进度条

🤖 AI：已添加 Scenario: 大数据量导出显示进度
```

#### 5.3 Superpowers 介入（需求澄清）

```
🤖 AI（加载了 brainstorming 等 skill 时，通常会先问清楚）：

在开始实现前，我想确认几个细节：

1. CSV 文件编码用什么？UTF-8 还是 UTF-8 BOM（Excel 兼容）？
2. 需要支持自定义导出字段吗？还是所有可见列都导出？
3. 数据中的逗号和换行符如何处理？
4. 是否需要后台异步导出（大文件场景）？
```

#### 5.4 分支隔离 + 计划制定

```
🤖 AI（在 using-git-worktrees、writing-plans 等技能可用时）：

✓ 创建 worktree: /tmp/project-csv-export
✓ 切换到新分支: feature/csv-export
✓ Clean test baseline: 42 tests passing

（基于 OpenSpec 的 tasks.md，细化实现计划）

📋 实现计划：

Task 1: 创建 CSV 工具函数 (约 3 min)
  - 文件: src/utils/csv.ts
  - 包含: escapeCSV, generateCSV, downloadCSV

Task 2: 添加导出按钮 (约 2 min)
  - 文件: src/components/DashboardToolbar.tsx
  - 添加 "导出 CSV" 按钮 + 未选中时禁用逻辑

Task 3: 集成到 Dashboard (约 3 min)
  - 文件: src/pages/Dashboard.tsx
  - 获取选中数据 → 调用 generateCSV → 触发下载

Task 4: 大数据量进度条 (约 4 min)
  - 文件: src/components/ExportProgress.tsx
  - 进度条组件 + Web Worker 异步处理

Task 5: 单元测试 (约 3 min)
  - 文件: src/utils/csv.test.ts
  - 覆盖: 正常导出、空数据、特殊字符、10000+ 条
```

#### 5.5 子 Agent 并行开发

```
🤖 AI（subagent-driven-development 可并行派发子任务，主 Agent 负责合并与解决冲突）：

[Agent-1] 处理 Task 1: CSV 工具函数
  ✓ 写入 src/utils/csv.ts (87 行)
  📏 code-structure: 文件 87 行 ≤ 500，函数最大 22 行 ≤ 50（为 AI 行为约束，合入时建议 CI 再跑同样规则）
  🔍 审查 1 (规格): 符合 spec
  🔍 审查 2 (质量): 代码清晰，无明显问题

[Agent-2] 处理 Task 2: 导出按钮
  ✓ 写入 src/components/DashboardToolbar.tsx
  …

[Agent-3] 处理 Task 5: 单元测试
  ✓ RED: 先失败再实现（TDD）
  ✓ GREEN: 14 个测试全部 PASS
  📊 test-coverage: 分支覆盖率 91%（以本地/CI 报告为准）

全部 5 个任务完成
```

#### 5.6 测试 + 审查

```
🤖 AI：

🧪 运行全部测试…
  56 tests passing（原 42 + 新 14）

🔍 代码审查:
  🟡 WARNING: csv.ts 的 escapeCSV 建议增加 null/undefined 处理
  → 已修正

🔒 安全检查（security-* 已 enable 时）:
  依赖/秘密/API 扫描无阻断项则继续
```

#### 5.7 验证 + 收尾

```
👤 你：/opsx:verify

🤖 AI：对照 spec csv-export
  各 Scenario 与实现一致则标记通过

👤 你：需要创建 PR

/opsx:archive
  将变更按团队规范归档；主 spec 随团队流程更新
```

**总耗时：约 40 分钟量级的演示口径（人实际投入因审 spec、点合并而异）**

---

## 第六章：进阶技巧与最佳实践

### 6.1 跳过某些步骤的艺术

不是每个变更都需要全套流程。教你判断：

| 变更类型 | OpenSpec | Superpowers | Agent Skills |
| --- | --- | --- | --- |
| 小 bug 修复（小于 20 行） | 可跳过 | 可跳过 worktree 等（建议保留 TDD 习惯） | 保留 test-coverage 等核心 |
| 中等功能（1-3 文件） | `/opsx:propose`  简化版 | 可跳过 worktree | 保留核心约束 |
| 大型功能（多文件） | **完整流程** | **完整流程** | **完整纪律** |
| 重构 | `/opsx:propose` | **完整流程**  （尤其 TDD） | code-refactoring 等 |
| 安全修复 | 视团队规范 | 视团队规范 | **security-* 优先*  \* |

### 6.2 模型选择建议

- **规划阶段** （ `/opsx:propose` 等）：倾向高推理、长上下文的模型，减少 spec 歧义
- **实现阶段** （ `/opsx:apply` ）：可在质量不降的前提下用成本更低的模型
- **子 Agent** ：通常继承主会话模型；并行时注意 token 与合并成本

### 6.3 上下文窗口管理

Agent Skills 会消耗 token，建议：

```
# 初期：只启用最核心的 5-8 个技能
agent-skills on \
  test-coverage \
  code-structure \
  code-documentation \
  security-secrets \
  production-ready

# 需求阶段再加
agent-skills on req-clarify req-breakdown

# 需求完成后关闭（释放上下文）
agent-skills off req-clarify req-breakdown
```

OpenSpec 也建议在实现前清理无关对话，保持可验证的干净上下文。

### 6.4 团队协作模式

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**关键** ：OpenSpec 的文档层可作为团队 **书面契约** ；

Superpowers 帮助把实现过程拆成 **可并行的子任务** ；

Agent Skills 主要降低 **风格与低级问题** 的反复拉扯

—— **合入前仍应保留 Code Review 与 CI** （与第三章边界声明一致，尤其是安全与业务关键路径）。

---

## 第七章：与手动编码的效率对比

下面用 **同一条功能线** 做量级对比，数字是 **教学示意** ，以你团队真实工时为准；「三件套」行的优势在于 **可预测、可归档、可回归** ，而不仅是快。

| 维度 | 纯手动 | AI 直接写 | 三件套工作流 |
| --- | --- | --- | --- |
| 需求/规格对齐 | 长（看团队） | 短但易漂移 | 中（OpenSpec 生成 + 人审） |
| 技术设计 | 中 | 可能缺失 | 有 design 草案 + 人拍板 |
| 编码 | 中 | 快但波动大 | 中（含 TDD/子任务） |
| 测试 | 中 | 常被跳过 | AI 引导编写 + **CI 为准** |
| 代码审查 | 必有 | 常缺 | AI 预审查 + **人审 PR** |
| 安全/依赖 | 看流程 | 易漏 | `security-*`  辅助 + **CI/扫描** |
| 可追溯性 | 看文档习惯 | 弱 | 强（变更与 spec 归档） |

**核心差异** 不是「永远更快」，而是：

- **可预测性** ：同样流程多跑几次，质量方差更小
- **可追溯性** ：关键决策有 proposal / spec 可查
- **可复制性** ：换功能、换人， **同一套检查清单** 仍可用

---

## 第八章：常见问题

### Q1: 这三个工具必须一起用吗？

**不必须** 。可以渐进式采用：

```
Phase 1: 先用 OpenSpec（先解决需求对齐）
Phase 2: + Superpowers（加流程与协作节奏）
Phase 3: + Agent Skills（加质量与约束）
```

从 OpenSpec 开始往往最自然——它压的是 **需求漂移** 这一根本问题。

### Q2: 小项目也需要这么重的流程吗？

对不足 100 行的小改动，可简化但建议保留底线：

- OpenSpec：至少写清「改什么、为何」
- Superpowers：尽量不让 TDD/验证被跳过大段
- Agent Skills：至少保留 test-coverage、security-secrets 等与你风险匹配的子集

### Q3: Agent Skills 和 Superpowers 的技能有什么区别？

| 维度 | Superpowers Skills | Agent Skills |
| --- | --- | --- |
| 定位 | 偏流程与任务拆分 | 偏质量与局部规则 |
| 触发方式 | 由上下文 + 模型选择何时强调 | 启用后进入上下文，由模型应用 |
| 典型约束 | 「先澄清再写大段代码」等 | 「单函数行数、覆盖率门槛」等 |
| 管理方式 | 各编辑器/插件安装方式不一 | 常见为 `agent-skills` 生命周期管理 |

**简单说** ：Superpowers 更偏「推进方式」，Agent Skills 更偏「结果长什么样」；二者叠加时， **流程优先、纪律落在每一步的产出上** ；冲突时以 **团队规范与 CI** 为准。

### Q4: 遇到 AI 不按要求来做怎么办？

| 问题 | 可能原因 | 解决方案 |
| --- | --- | --- |
| AI 跳过 spec 直接写代码 | OpenSpec 未初始化或未加载指令 | `openspec init`  / `openspec update` ，检查 `AGENTS.md` |
| AI 不跑测试 | Superpowers 未装或任务太碎 | 检查安装；显式要求 TDD 步骤 |
| 单文件过大 | 相关 skill 未 enable | `agent-skills on code-structure`  并加 CI 检查 |
| 特别慢 | 开太多 skill、上下文鼓包 | `agent-skills off`  非必要项 |

### Q5: 如何处理 Agent Skills 和 Superpowers 的潜在冲突？

通常不矛盾：一个管「步骤与拆分」，一个管「每一步的代码形态」。若真有张力（例如并行 vs 顺序）， **以团队合入规范与 CI 为最终裁判** ，在文档中固定一种打法。

---

## 总结：AI 编程的「铁三角」

| 维度 | OpenSpec | Superpowers | Agent Skills |
| --- | --- | --- | --- |
| **一句话** | 用文档定 AI | 用流程带 AI | 用纪律管 AI |
| **核心能力** | 人机契约 | 工程流/任务编排 | 质量护栏（AI 行为 + 建议配 CI） |
| **类比** | 设计图与验收口径 | 施工顺序与检查点 | 监理量尺 |
| **GitHub** | Fission-AI/OpenSpec | obra/superpowers | addyosmani/agent-skills |
| **许可证** | MIT | MIT | MIT |
| **安装复杂度** | 低（常 npm） | 低-中（视编辑器） | 中（需初始化与取舍启用） |
| **学习曲线** | 中 | 中-高 | 中-高 |

### 开始使用的建议路径

```
Week 1: 安装 OpenSpec，在几个小功能上试用 propose → apply → verify → archive
Week 2: 安装 Superpowers，体会「先问再写」与任务拆分的差异
Week 3: 安装 Agent Skills，只开少量核心，观察覆盖率与结构约束
Week 4: 用三件套跑通一个中等功能，并把关键检查项同步到 CI
```

### 最后的忠告

这些工具不是银弹。它们能帮你：

- 让 AI 在 **你写清的边界** 里发挥
- 让过程 **可重复、可审计** （尤其是 OpenSpec 归档）
- 让代码 **更易测、更易审** （Skills + 人审 + CI）

它们替代不了：业务判断、系统取舍、 **最终合入与线上责任** 。

**更好的工作流 = 人定方向 + 流程管过程 + 纪律（含 CI）保质量。**

三件套让结果从「碰运气」更接近「可复制」； **方向盘仍在人手里。**

---

**你可以怎么做下一步**

- 若已在团队使用：把第三章「边界声明」贴进内部 wiki，和 **Code Review、CI 清单** 对齐，避免把 Skills 当成「免审金牌」。

---

> **参考资源**
> 
> - OpenSpec: https://github.com/Fission-AI/OpenSpec | https://openspec.dev
> - Superpowers: https://github.com/obra/superpowers
> - Agent Skills: https://github.com/addyosmani/agent-skills

*截稿与 Star 等数据易变，以各仓库 Release / 官方说明为准。*

AI Agents · 目录

作者提示: 个人观点，仅供参考

继续滑动看下一个

前端AI行走

向上滑动看下一个