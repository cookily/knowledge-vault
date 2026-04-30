---
title: "OpenClaw 卸载"
source: raw/personal/openclaw/
created: 2026-04-30
tags:
  - summary
  - OpenClaw
  - 卸载
---

# 摘要：OpenClaw 卸载

## 完全卸载步骤

清理记忆和配置文件，谨慎操作！

```bash
# 1. 卸载 OpenClaw
openclaw uninstall --all --yes

# 2. 卸载 npm 包
npm uninstall -g openclaw

# 3. 检查清理
# 删除以下目录：
# - C:\Users\chenyl\AppData\Roaming\nvm\v22.22.0\node_modules
# - C:\Users\chenyl\.openclaw
```

## 来源

[[raw/personal/openclaw/openclaw卸载.md]]