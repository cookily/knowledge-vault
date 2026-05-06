---
title: "一行命令把杂乱文件变成知识图谱——我的知识库搭建流程"
source: 微信公众号
date: 2026-04-14
tags:
  - summary
  - graphify
  - 知识图谱
  - 知识管理
  - Claude-Code
compiled: 2026-04-30
---

# 一行命令把杂乱文件变成知识图谱

## 一句话总结

把所有文件丢进一个文件夹，`/graphify .` 自动建知识图谱——**不需要提前分类，信息自己找位置**。

## graphify 核心思路：两轮提取

| 轮次 | 内容 | Token 消耗 |
|------|------|------------|
| 第一轮 | AST 解析代码（类、函数、导入、调用图） | 0（纯本地） |
| 第二轮 | 语义提取文档/图片（并行子代理） | 按需 |

**关系类型**：
- `EXTRACTED`：原文直接找到
- `INFERRED`：合理推断（带置信度）
- `AMBIGUOUS`：需人工复核

## 安装与使用

```bash
pip install graphifyy    # 注意：包名两个y
graphify install         # 注册到 Claude Code
```

## 核心命令

| 命令 | 功能 |
|------|------|
| `/graphify .` | 扫描当前目录生成图谱 |
| `/graphify . --update` | 增量更新（SHA256 缓存） |
| `/graphify . --watch` | 后台监听变更 |
| `/graphify query "问题"` | 问两个概念的关系 |
| `/graphify path A B` | 找 A 到 B 的最短路径 |
| `/graphify explain "概念"` | 解释某个节点的所有连接 |
| `graphify hook install` | Git 提交后自动重建 |

## 输出文件

- `graphify-out/graph.html` — 交互式图谱（浏览器打开）
- `graphify-out/GRAPH_REPORT.md` — 文字报告（核心节点、意外连接）
- `graphify-out/graph.json` — 持久化数据（数周后可查询）

## 实战结果（Beacon Ash 游戏项目）

- 471 个文件（180 代码 + 153 文档 + 138 截图）
- → 1394 个节点、1930 条边、193 个社区

**意外发现**：`DOCXSchemaValidator` 连接数比游戏引擎还多——被 docx 和 pptx 两个技能共享，底层 OOXML 验证框架复用。

## 适用场景

✅ 接手陌生项目，快速了解结构
✅ 发现代码和文档之间的隐藏关联
✅ 不需要提前设计分类体系

**不适合**：替代人工思考和总结

## 导出到外部工具

graphify 支持将生成的图谱导出到专业图分析工具。

### 导出到 Gephi

Gephi 是一款开源图可视化软件，适合做社区分析、节点过滤、布局调优。

**步骤：**
1. 运行命令：
   ```bash
   /graphify <path> --graphml
   ```
2. 打开 `graphify-out/graph.graphml`
3. 在 Gephi 中：
   - 打开文件后在 **"概览"** 标签页调整布局（如 ForceAtlas2）
   - 左侧 **"统计"** 面板可以跑模块度分析
   - 节点颜色可以通过社区 ID 分组染色
   - **"过滤"** 面板可以按置信度、关系类型筛选

**优点**：免费、界面直观、适合做汇报图

---

### 导出到 Neo4j

Neo4j 是一款图数据库，支持 Cypher 查询语言，适合做复杂分析。

**方式一：生成 Cypher 文件，手动导入**
```bash
/graphify <path> --neo4j
```
生成 `graphify-out/cypher.txt`，然后在终端运行：
```bash
cypher-shell < graphify-out/cypher.txt
```
适用于没有本地 Neo4j 服务、需要导入到远程实例的场景。

**方式二：直接推送到运行中的 Neo4j**
```bash
/graphify <path> --neo4j-push bolt://localhost:7687
```
首次运行会提示输入用户名和密码（默认用户名 `neo4j`）。

> 推送使用 `MERGE` 语句，重复运行不会产生重复数据，可以安全重新导入。

**导入后的常用查询：**
```cypher
-- 查看节点总数
MATCH (n) RETURN count(n) AS 节点数

-- 按社区统计节点数量
MATCH (n) RETURN n.community AS 社区, count(n) AS 数量 ORDER BY 数量 DESC

-- 查看高置信度边
MATCH (a)-[r {confidence: "EXTRACTED"}]->(b) RETURN a.label, r.relation, b.label

-- 找某个概念的所有直接邻居
MATCH (n {label: "某个概念名"})-[r]-(neighbor) RETURN neighbor.label, r.relation
```

**优点**：支持 SQL 级别的复杂查询，适合深度分析

---

### 三种导出格式对比

| 格式 | 目标工具 | 适合场景 | 上手难度 |
|------|----------|----------|----------|
| `--graphml` | Gephi | 可视化探索、做 PPT/汇报图 | ⭐ 最简单 |
| `--neo4j` | Neo4j | 手动控制导入、导入到远程 | ⭐⭐ |
| `--neo4j-push` | Neo4j | 有本地 Neo4j，想跳过文件直接导入 | ⭐⭐ |

## 来源

[[一行命令把杂乱文件变成知识图谱——我的知识库搭建流程]]

## 相关概念

- [[graphify]]
- [[AI驱动知识管理]]
- [[第二大脑]]
