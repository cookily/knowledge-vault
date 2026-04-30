---
title: "OpenClaw 设备配对"
source: raw/personal/openclaw/
created: 2026-04-30
tags:
  - summary
  - OpenClaw
  - 设备配对
---

# 摘要：OpenClaw 设备配对

## 问题

召唤子代理报错：`1008 pairing required`

## 解决方案

```bash
# 查看设备列表
openclaw devices list

# 批准最新设备
openclaw devices approve --latest

# 或指定设备 ID 批准
openclaw devices approve 00f495c2-faf1-41e0-8190-b698c0b022be

# 重启网关
openclaw gateway restart
```

## 来源

[[raw/personal/openclaw/openclaw召唤子代理报错1008，需要配对问题1008： pairing required.md]]