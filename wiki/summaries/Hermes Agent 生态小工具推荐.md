---
title: "Hermes Agent 生态小工具推荐"
source: 微信公众号 · 李嘉乐的数字花园（Claudia）
date: 2026-04-23
tags: [summary, clippings, Hermes, 生态, 工具推荐, 插件]
compiled: 2026-05-21
---

# Hermes Agent 生态小工具推荐

## 一句话总结
5 个新插件（上下文管理、动态主题、知识图谱记忆、Web UI、智能搜索路由）+ skills-manage Skill 统一管理工具，补上 Hermes 日常使用的缝隙。

## 核心内容

### 5 个新插件
| 工具 | 功能 | 链接 |
|------|------|------|
| **hermes-lcm** | 上下文管理，层次化 DAG 存储对话，压缩后可展开历史 | stephenschoettler/hermes-lcm |
| **hermes-neurovision** | 终端动态主题，85 种 ASCII 样式映射 Agent 内部状态 | Tranquil-Flow/hermes-neurovision |
| **supermemory** | 知识图谱记忆方案，挂在生命周期钩子里 | supermemory.ai |
| **Hermes WebUI** | CLI 搬到浏览器，三栏布局，实时 token 用量 | nesquena/hermes-webui |
| **web-search-plus** | 智能搜索路由，根据查询类型自动选 Serper/Tavily/Exa 等 7 家 | robbyczgw-cla/hermes-web-search-plus |

### skills-manage
- **问题**：Skill 文件散在不同目录，每个工具一套，手工同步麻烦
- **方案**：`~/.agents/skills/` 当中央仓库，其他工具软链接
- 支持 GitHub 仓库导入、Collection 打包、20+ 工具兼容（Claude Code/Cursor/Windsurf/Codex 等）
- 本地 SQLite 存储，数据不外传

### Hermes WebUI 深度用法
- 本机一条命令启动，远程服务器用 SSH 隧道
- **Profiles 方法**：建多个 Profile 当不同"AI 员工"，按场景切换，各自维护记忆和 Skills
- macOS 有 Swift 原生客户端（3MB）

## 来源
[[raw/external/微信公众号/推荐几个最近刚发布的 Hermes Agent 小工具.md]]

## 相关笔记
- [[Hermes Agent v0.14.0 Foundation Release]]
- [[Hermes Agent 与 Web UI 可视化界面]]
