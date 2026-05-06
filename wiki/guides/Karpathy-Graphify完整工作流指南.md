---
title: "Karpathy + Graphify 工作流完整指南"
description: "新知识库从零搭建的标准操作流程"
tags:
  - guide
  - workflow
  - knowledge-management
created: 2026-05-06
---

# Karpathy + Graphify 工作流完整指南

新知识库从零搭建的标准操作流程。

---

## 一、初始化：新知识库结构

创建以下目录结构：

```
knowledge-vault/
├── raw/                  # 原始资料（只进不改）
│   ├── external/         # 外部保存的内容（网页、公众号等）
│   └── local/            # 本地文件
├── wiki/                  # 编译产物（AI 维护）
│   ├── indexes/           # 索引文件
│   │   ├── All-Sources.md
│   │   └── All-Concepts.md
│   ├── concepts/          # 概念条目
│   └── summaries/         # 每篇资料的摘要
├── graphify-out/          # 图谱输出目录
└── outputs/               # 运行时输出
```

### 在 Claude Code 中初始化

```bash
# 1. 创建目录结构
mkdir -p raw/external raw/local wiki/indexes wiki/concepts wiki/summaries graphify-out outputs

# 2. 创建索引文件
echo "---
title: \"All Sources - 来源索引\"
description: \"知识库中所有来源资料的索引\"
created: $(date +%Y-%m-%d)
---

# All Sources - 来源索引

> 最后更新：$(date +%Y-%m-%d)

" > wiki/indexes/All-Sources.md

echo "---
title: \"All Concepts - 概念索引\"
description: \"知识库中所有概念的索引\"
created: $(date +%Y-%m-%d)
---

# All Concepts - 概念索引

> 最后更新：$(date +%Y-%m-%d)

## 🔗 相关索引
- [[All-Sources.md]] - 来源索引
- [[../raw/]] - 原始资料目录

" > wiki/indexes/All-Concepts.md

# 3. 创建 CLAUDE.md 让 Claude Code 记住这个工作流
echo "
## 知识库工作流

### 目录结构
- raw/ = 原始资料（只进不改）
- wiki/ = AI 维护的编译产物
- graphify-out/ = 图谱输出

### 四阶段流程
1. Ingest（摄入）：保存网页到 raw/external/
2. Compile（编译）：生成摘要和概念
3. Query（查询）：@某个文件提问
4. Lint（维护）：检查一致性

### 图谱命令
- /graphify . --graphml    # 生成 Gephi 图谱
- /graphify . --update     # 增量更新图谱
- /graphify query \"问题\"  # 查询图谱
- /graphify explain \"概念\" # 解释某个节点

" >> CLAUDE.md
```

---

## 二、Phase 1：Ingest（摄入）

把感兴趣的内容收集到 `raw/` 里。

### 方法 1：Obsidian Web Clipper（推荐）

1. 安装 Obsidian Web Clipper 扩展
2. 保存到 `knowledge-vault/raw/external/` 文件夹
3. 命名格式：`来源_标题.md`

### 方法 2：使用 graphify 的 add 命令

```bash
# 摄入单个 URL
/graphify add https://example.com/article

# 带作者标签
/graphify add https://example.com/article --author "张三"

# 带贡献者标签
/graphify add https://example.com/article --contributor "李四"
```

### 方法 3：手动复制

- 公众号文章 → 复制到 `raw/external/微信公众号/`
- 读书笔记 → 保存到 `raw/local/`
- 截图/图片 → 保存到 `raw/local/images/`

### 摄入原则

- **只进不改**：`raw/` 里的内容不要编辑，让 AI 来处理
- **来源可追溯**：每个文件带来源信息（URL、日期、作者）
- **格式不限**：网页、PDF、图片、代码都可以

---

## 三、Phase 2：Compile（编译）

用 AI 把 `raw/` 里的资料编译成 `wiki/` 里的结构化知识。

### 基本编译命令

```
/compile
```

这会自动：
1. 扫描 `raw/` 中所有未编译的文件
2. 生成摘要 → `wiki/summaries/`
3. 提取概念 → `wiki/concepts/`
4. 更新索引 → `All-Sources.md`、`All-Concepts.md`
5. 建立交叉链接

### 编译后的文件结构

```
wiki/
├── indexes/
│   ├── All-Sources.md     # 索引所有来源
│   └── All-Concepts.md    # 索引所有概念
├── concepts/
│   ├── AI驱动知识管理.md  # 概念卡片
│   ├── 第二大脑.md
│   └── graphify.md
└── summaries/
    ├── AI驱动知识管理.md  # 摘要卡片
    ├── graphify知识图谱实战.md
    └── Karpathy式AI知识库搭建指南.md
```

### 编译的 YAML frontmatter 示例

```yaml
---
title: "AI驱动知识管理"
source: raw/external/网页文章/AI驱动知识管理.md
created: 2026-04-30
tags:
  - concept
  - AI-tools
---

# AI驱动知识管理

核心定义：...
```

---

## 四、Phase 3：Query（查询）

向知识库提问，获取基于已有资料的回答。

### 基础查询

```
@wiki/indexes/All-Concepts.md
请总结一下我收藏的所有关于 AI 编程工具的资料
```

```
@wiki/summaries/
我在学习 DDD，有什么相关资料吗？
```

### 使用图谱查询

```bash
# 问两个概念的关系
/graphify query "graphify 和第二大脑有什么关系？"

/graphify query "Claude Code Skills 有哪些？"

/graphify query "知识库编译流程的四个阶段是什么？" --dfs
```

### 找最短路径

```bash
# 找两个概念之间的连接路径
/graphify path "Obsidian" "Claude Code"

/graphify path "graphify" "知识库编译流程"
```

### 解释单个概念

```bash
# 解释某个节点及其所有连接
/graphify explain "graphify"

/graphify explain "第二大脑"
```

---

## 五、Phase 4：Lint（维护）

定期检查知识库的健康状况。

### 运行 Lint

```
/lint
```

### Lint 会检查

- 🔍 缺失的交叉链接（概念之间没有连接）
- 📝 过时的内容（来源已失效）
- ❌ 矛盾的信息（同一概念在不同文件里描述不一致）
- 💡 建议（可以补充哪些新概念）

### 手动维护任务

| 任务 | 频率 | 操作 |
|------|------|------|
| 检查索引 | 每周 | 查看 `All-Concepts.md` 是否完整 |
| 清理 dead links | 每月 | 搜索 `[[` 检查失效链接 |
| 合并重复概念 | 每季度 | 把相似的概念合并 |

---

## 六、Graphify 图谱功能详解

### 生成图谱（Gephi/Neo4j）

```bash
# 生成 Gephi 可用的文件
/graphify . --graphml

# 生成 Neo4j 的 Cypher 文件
/graphify . --neo4j

# 直接推送到 Neo4j（需本地运行）
/graphify . --neo4j-push bolt://localhost:7687
```

### 增量更新图谱

当你添加新资料后：

```bash
# 只更新变化的部分（节省 token）
/graphify . --update
```

### 监听模式（后台自动更新）

```bash
# 启动监听，文件变化时自动重建图谱
/graphify . --watch
```

### 导出其他格式

```bash
# SVG 图片（适合嵌入文档）
/graphify . --svg

# Obsidian vault（每个节点一个笔记）
/graphify . --obsidian

# Wiki 格式（社区概览）
/graphify . --wiki
```

---

## 七、完整工作流示例

### 第一天：新项目开始

```bash
# 1. 初始化目录结构（上文第一步）

# 2. 摄入第一批资料
graphify add https://article1.com
graphify add https://article2.com

# 3. 编译
/compile

# 4. 生成图谱看看结构
/graphify . --graphml
```

### 第二天：添加更多资料

```bash
# 1. 继续摄入
graphify add https://article3.com --author "张三"

# 2. 增量编译
/compile

# 3. 增量更新图谱
/graphify . --update

# 4. 在 Gephi 里打开 graphify-out/graph.graphml 查看
```

### 第三天：查询和维护

```bash
# 1. 问知识库
/graphify query "我收藏的资料里有哪些 AI Agent 相关的？"

/graphify path "AI Agent" "第二大脑"

/graphify explain "graphify"

# 2. 运行 Lint
/lint

# 3. 根据 Lint 建议手动修复问题
```

---

## 八、常见问题

### Q: 什么时候用 /compile？什么时候用 /graphify？

| 场景 | 命令 |
|------|------|
| 新增资料，需要生成摘要和概念 | `/compile` |
| 想看概念之间的关系和社区 | `/graphify . --graphml` |
| 问知识库内容相关问题 | `/graphify query "问题"` |
| 定期检查一致性 | `/lint` |

### Q: compile 和 graphify 有什么区别？

- **compile**：把 `raw/` 变成 `wiki/`（摘要、概念、索引）
- **graphify**：把整个知识库变成知识图谱（节点、边、社区）

两者互补，先 compile 再 graphify。

### Q: 图谱乱了怎么办？

```bash
# 重新聚类（不重新提取）
/graphify . --cluster-only

# 完整重建
/graphify . --graphml
```

### Q: Neo4j 怎么安装？

1. 下载 Neo4j Desktop：https://neo4j.com/download/
2. 创建本地数据库（默认 bolt://localhost:7687）
3. 首次运行 `/graphify . --neo4j-push bolt://localhost:7687` 时输入密码

---

## 九、一张图总结

```
raw/ (原始资料)
    │
    │ /compile
    ▼
wiki/ (编译产物：摘要 + 概念 + 索引)
    │
    │ /graphify . --graphml
    ▼
graphify-out/
├── graph.json     ← 查询用
├── graph.graphml  ← Gephi 打开
├── graph.html     ← 浏览器预览
└── GRAPH_REPORT.md
```

---

## 来源

- [[wiki/summaries/Karpathy 式 AI 知识库搭建指南]]
- [[wiki/concepts/知识库编译流程]]
- [[wiki/concepts/graphify]]