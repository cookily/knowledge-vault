---
title: "OpenClaw NAS 访问配置"
source: raw/personal/openclaw/
created: 2026-04-30
tags:
  - summary
  - OpenClaw
  - NAS
---

# 摘要：OpenClaw NAS 访问配置

## 目标

通过 NAS 访问 OpenClaw Web UI

## 配置步骤

修改 `~/.openclaw/openclaw.json` 中的 gateway 配置：

```json
"gateway": {
  "port": 18789,
  "mode": "local",
  "bind": "lan",
  "controlUi": {
    "allowedOrigins": [
      "http://localhost:18789",
      "http://127.0.0.1:18789",
      "http://192.168.11.156:18789"
    ],
    "dangerouslyDisableDeviceAuth": true
  }
}
```

重启：`openclaw gateway restart`

## 来源

[[raw/personal/openclaw/openclaw局域网nas可以访问配置-已实践.md]]