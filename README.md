# Obsidian 第二大脑 - AI 驱动知识管理系统

> 让 AI 代替你整理知识，告别"收藏从未阅读"的焦虑

---

## 🎯 项目解决的核心痛点

我构建了一个**AI 驱动的个人知识管理系统**，解决了知识管理中三大痛点：

| 痛点 | 传统方法 | 本系统 |
|------|---------|--------|
| **整理耗时** | 每篇 30-60 分钟，根本整理不过来 | <1 分钟/篇 |
| **收藏吃灰** | 1000+ 篇收藏，真正记住的不到 10% | 知识真正被消化理解 |
| **检索低效** | 关键词搜索，想不起来该用什么词 | 自然语言问答 |

**核心改变**：从"我要如何整理知识"变成"如何设计一个让 AI 替我整理知识的系统"。

---

## ⚙️ 核心逻辑流

```
raw/ (原始资料)
    ↓
/compile (Claude Code 自定义命令)
    → AI 自动生成摘要 → wiki/summaries/
    → AI 自动提取概念 → wiki/concepts/
    → AI 自动建立双向链接 → wiki/indexes/
    ↓
/graphify (Claude Skill)
    → 语义提取 (多 Agent 并行处理文档/图片)
    → AST 结构提取 (代码文件)
    → Leiden 社区发现算法
    → 输出: graph.json + graph.html + GRAPH_REPORT.md
```

### 关键特性

- **多 Agent 协作**：语义提取阶段并行调度多个子代理，同时处理 20+ 文件
- **长链推理**：不仅提取概念，还发现跨文档的隐藏关联（如「某篇公众号文章」与「三个月前的配置笔记」实为同一原理）
- **渐进式积累**：SHA256 缓存保证增量更新，图谱跨会话持久化

---

## 📊 实际成果

| 指标 | 数据 |
|------|------|
| 知识节点 | 42 个 |
| 关系边 | 45 条 |
| 社区聚类 | 8 个 |
| 提取率 | 84% EXTRACTED |
| Token 压缩 | 最高 71x |

### God Nodes（核心概念）

| 概念 | 连接数 | 说明 |
|------|--------|------|
| Claude Code | 13 | 整个系统的核心引擎 |
| OpenClaw | 8 | 本地化 AI 助手 |
| Obsidian | 5 | 知识库容器 |
| Karpathy式AI知识库 | 5 | 方法论源头 |
| graphify | 4 | 图谱提取工具 |

### 意外发现

- `QQBot` → `OpenClaw` → 语音识别方案关联
- `nvm Node版本管理` → `OpenClaw` → 配置优化关联
- `飞书sherpa-onnx` → `OpenClaw` → 多平台语音识别

---

## 🛠️ 核心技术栈

| 工具 | 作用 | 为什么选它 |
|------|------|-----------|
| **Obsidian** | 知识库容器 | 本地优先，Markdown 原生，支持双链 |
| **Claude Code** | AI 引擎 | 直接操作文件系统，不依赖 API 调用 |
| **Claudian** | Obsidian 插件 | 将 Claude Code 图形化接入 |
| **graphify** | 知识图谱提取 | 多模态支持，代码/文档/图片统一处理 |

---

## 🚀 使用方法

```bash
# 1. 收集资料（保存到 raw/）

# 2. 编译整理（生成摘要和概念）
/compile

# 3. 构建图谱（可视化探索）
/graphify ./raw

# 4. 自然语言查询
/graphify query "Claude Code Skills 有哪些？"
/graphify path "Claude Code" "Obsidian"
```

---

## 📁 项目结构

```
knowledge-vault/
├── raw/                    # 原始资料（只进不改）
│   ├── external/          # 外部文章、公众号、网页
│   └── personal/          # 个人整理、配置记录
│
├── wiki/                   # 编译产物（AI 维护）
│   ├── summaries/        # 逐篇摘要
│   ├── concepts/         # 概念卡片
│   └── indexes/           # All-Sources.md, All-Concepts.md
│
├── graphify-out/          # 知识图谱输出
│   ├── graph.html        # 可交互图谱
│   ├── graph.json        # 图谱数据
│   └── GRAPH_REPORT.md   # 分析报告
│
├── outputs/              # 运行时输出
│   └── health/           # 健康检查报告
│
├── blog/                 # 博客文章
└── .claude/              # Claude Code 配置
```

---

## 💡 为什么选择这套方案？

### vs 传统笔记软件

| 维度 | Notion/印象笔记 | 本系统 |
|------|----------------|--------|
| 整理方式 | 手动 | AI 自动 |
| 概念关联 | 手动建立 | AI 自动发现 |
| 图谱支持 | 基础 | 高级可视化 |
| 扩展性 | 受限 | 无限 |

### vs RAG 向量检索

| 维度 | RAG 系统 | 本系统 |
|------|---------|--------|
| 部署复杂度 | 需要向量数据库 | 纯文件系统 |
| Token 消耗 | 每次查询 | 仅首次建图 |
| 概念关系 | 隐式相似度 | 显式边关系 |
| 可解释性 | 黑盒 | 白盒（标注来源） |

---

## 🔗 相关资源

- [Karpathy 原始 Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [Claudian GitHub](https://github.com/YishenTu/claudian) (8k+ Stars)
- [graphify GitHub](https://github.com/safishamsi/graphify)
- [Obsidian](https://obsidian.md)

---

## 📝 许可证

MIT License

---

*本知识库由 Claude Code + graphify 自动维护 | 2026*
