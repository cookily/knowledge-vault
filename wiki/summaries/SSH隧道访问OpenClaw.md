---
title: "SSH 隧道访问 OpenClaw"
source: raw/personal/openclaw/
created: 2026-04-30
tags:
  - summary
  - SSH
  - OpenClaw
---

# 摘要：SSH 隧道访问 OpenClaw

## 命令

```bash
ssh -L 18789:127.0.0.1:18789 root@192.168.102.165
```

将本地 18789 端口通过 SSH 隧道转发到远程服务器的 127.0.0.1:18789

## 来源

[[raw/personal/openclaw/本机访问远端的服务器openclaw.md]]