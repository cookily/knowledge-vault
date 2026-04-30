---
title: "nvm Node.js 安装目录迁移"
source: raw/personal/openclaw/
created: 2026-04-30
tags:
  - summary
  - nvm
  - Node.js
---

# 摘要：nvm Node.js 安装目录迁移

## 问题

nvm 默认把 Node.js 安装到 C 盘，需要迁移到 D 盘

## 解决方案

### 1. 找到 nvm 配置

位置：`C:\Users\chenyl\AppData\Roaming\nvm\settings.txt`

### 2. 修改配置

```txt
root: D:\nvm_workspace
path: C:\Program Files\nodejs
```

- `root` → nvm 安装目录（存放各版本 node）
- `path` → nodejs 快捷方式位置

### 3. 复制版本

手动复制 node 版本到新位置

## 来源

[[raw/personal/openclaw/nvm安装的node改到D盘，默认是在c盘.md]]