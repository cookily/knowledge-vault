---
title: "Zed 编辑器：Rust 打造的高性能 AI 编程编辑器"
source: 网页文章 · Zed Industries (zed.dev + GitHub)
date: 2026-05
tags: [summary, clippings, Zed, 编辑器, Rust, AI编程, 开源]
compiled: 2026-05-21
---

# Zed 编辑器：Rust 打造的高性能 AI 编程编辑器

## 一句话总结
由 Atom 和 Tree-sitter 创始团队用 Rust 从零打造的高性能代码编辑器，原生支持并行 AI Agent、多人协作、Git、调试器，83K+ GitHub Stars。

## 核心内容

### 定位
- 原子级（Atom）和 Tree-sitter 的创始团队 15 年积累的集大成之作
- 开源（GPLv3 + AGPLv3），社区驱动，1896 贡献者，937 PR/月
- macOS / Linux / Windows 全平台

### 核心功能
| 功能 | 说明 |
|------|------|
| **Parallel Agents** | 并行运行多个 AI Agent，跨项目编辑/导航/运行工具 |
| **Agentic Editing** | 原生 AI Agent 编辑，人机协作 |
| **Edit Prediction** | Zeta2 开源权重模型预测下一步操作 |
| **Native Git** | 一等公民 Git 支持（stage/commit/push/diff） |
| **Debugger** | 基于 DAP 的原生多语言调试 |
| **Remote Development** | UI 在本地，代码在远程服务器 |
| **Multibuffer** | 多文件片段合并在一个可编辑表面 |
| **Vim/Helix** | 一等公民 Vim/Helix 模态编辑 |
| **Built-in REPL** | Jupyter kernel 交互式运行 |

### 技术亮点
- **Rust 编写**：原生利用多核 CPU + GPU 加速
- **Tree-sitter**：精确语法高亮和代码理解
- **扩展生态**：数百个扩展（HTML/TOML/Java/PHP/SQL/Vue/Ruby 等）
- **不锁定模型**：可接入任意 AI Agent

### 知名用户评价
- **José Valim**（Elixir 创建者）：所有我需要的功能都有了
- **Dan Abramov**（React 核心团队）：能感受到这个产品是用爱打造的
- **Matt Baker**（首席工程师）：启动速度、UI 交互、打字延迟，快到震惊
- **Mike Bostock**（D3.js 创建者）：multibuffer、inlay hints、协作，精细的设计

### 数据
- 83,465 GitHub Stars | 8,622 Forks | 1,896 Contributors
- 937 PRs merged/月

## 来源
- [[raw/external/网页文章/Your last next editor.md]]
- [[raw/external/网页文章/zed-industrieszed Code at the speed of thought – Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter.md]]

## 相关笔记
- [[Claude Code vs Cursor vs Codex]]
- [[VSCode ACP Client]]
- [[AI编程工具三巨头对比]]
