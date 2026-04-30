---
title: "Obsidian 自动化工作流搭建记录"
source: raw/personal/openclaw/Obsidian 自动化工作流搭建记录.md
created: 2026-04-30
tags:
  - summary
  - OpenClaw
  - Obsidian
  - 自动化
---

# 摘要：Obsidian 自动化工作流

## 项目概述

使用 Node.js + `obsidian-cli` + Git 实现 AI 自动创建笔记，并自动同步到 Gitee 远程仓库。

## 目录结构

| 路径 | 说明 |
|------|------|
| `F:\Obsidian_workspace\` | Obsidian Vault 根目录 |
| `F:\Obsidian_workspace\openclaw-note\` | AI 创建笔记默认目录 |
| `C:\Users\chenyl\.openclaw\workspace\obsidian-automation\` | 自动化脚本 |

## 已完成配置

- ✅ obsidian-cli 已安装
- ✅ 自动化脚本创建完成
- ✅ Git 初始化完成
- ✅ Gitee 远程已添加

## 使用方法

### 创建新笔记

```bash
cd C:\Users\chenyl\.openclaw\workspace\obsidian-automation
node obsidian.js create "笔记标题" "笔记内容"
```

### 同步到 Gitee

```bash
cd F:\Obsidian_workspace\openclaw-note
node C:\Users\chenyl\.openclaw\workspace\obsidian-automation\git-sync.js
```

## 遇到的问题

| 问题 | 原因 | 解决 |
|------|------|------|
| `src refspec master does not match any` | 分支名是 main 不是 master | 用 `git push -u origin main` |
| `LF will be replaced by CRLF` | Git 换行符警告 | 无需处理 |
| `unknown write failure on standard output` | PowerShell 输出缓冲 | 不影响提交 |

## 优点

- 笔记仍在本地 Obsidian 中正常编辑
- AI 可以快速创建笔记骨架
- 自动备份到 Gitee 远程仓库
- 保留完整的 Git 版本历史

## 来源

[[raw/personal/openclaw/Obsidian 自动化工作流搭建记录.md]]