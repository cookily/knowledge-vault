---
title: "QQBot 集成 sherpa-onnx 离线语音识别"
source: 个人笔记
date: 2026-03-17
tags:
  - summary
  - openclaw
  - QQBot
  - sherpa-onnx
  - 语音识别
  - 离线识别
compiled: 2026-04-30
---

# QQBot 集成 sherpa-onnx 离线语音识别

## 一句话总结

给 QQBot 插件添加 `sherpa-onnx-offline` 离线语音识别，QQ 语音消息自动在本地转文字。

## 核心步骤

1. **下载 SenseVoice 模型** → `D:\sherpa-onnx\`（无中文无空格路径）
2. **修改识别脚本** `MODEL_DIR` 路径
3. **修改 gateway.ts** 添加 `sherpa-onnx-offline` provider 分支
4. **编译 QQBot** `npm run build`
5. **配置 openclaw.json** 添加 stt provider
6. **重启 OpenClaw** `openclaw gateway restart`

## 关键配置

```json
{
  "channels": {
    "qqbot": {
      "stt": {
        "provider": "sherpa-onnx-offline",
        "model": "sense-voice"
      }
    }
  }
}
```

## 常见问题

| 问题 | 解决方案 |
|------|----------|
| `No graph was found` | 模型路径有中文/空格，移到 `D:\sherpa-onnx` |
| `ModuleNotFoundError` | `pip install sherpa-onnx` |
| 识别结果杂音 | 检查采样率代码是否为 `sample_rate` 而非硬编码 `16000` |

## 来源

[[raw/personal/openclaw/QQBot-sherpa-onnx-离线语音识别配置.md]]

## 相关笔记

- [[飞书sherpa-onnx离线语音识别配置]]
- [[硅基流动语音识别接入]]
