---
title: "OpenClaw 语音识别配置"
source: raw/personal/openclaw/
created: 2026-04-30
tags:
  - summary
  - OpenClaw
  - ASR
  - 语音识别
---

# 摘要：OpenClaw 语音识别配置

## 硅基流动语音识别接入

通过环境变量 + OpenClaw 配置，使用硅基流动平台的开源语音识别模型。

### 关键配置

| 配置项 | 值 |
|--------|-----|
| API Base | `https://api.siliconflow.cn/v1` |
| 模型 | `TeleAI/TeleSpeechASR` |
| prefer_feishu_asr | `false`（推荐） |

### 可用模型

| 模型 | 推荐度 |
|------|--------|
| TeleAI/TeleSpeechASR | ⭐⭐⭐⭐⭐ 推荐 |
| SenseVoiceSmall | ⭐⭐⭐ |
| FunAudioLLM/SenseVoiceSmall | ⭐⭐⭐⭐ |
| openai/whisper-large-v3 | ⭐⭐⭐⭐⭐ |

---

## sherpa-onnx 离线语音识别

给 QQBot 添加离线语音识别支持，不依赖云服务。

### 关键要求

1. **模型路径**：无中文无空格，推荐 `D:\sherpa-onnx`
2. **Python 包**：`pip install sherpa-onnx`
3. **采样率**：使用实际读取的采样率（不是硬编码 16000）

### 常见问题

| 问题 | 解决 |
|------|------|
| `No graph was found in protobuf` | 模型路径有中文/空格 |
| `ModuleNotFoundError: sherpa_onnx` | `pip install sherpa-onnx` |
| STT not configured | 检查 provider 是否为 `sherpa-onnx-offline` |

## 来源

[[raw/personal/openclaw/硅基流动语音识别接入.md]]
[[raw/personal/openclaw/QQBot-sherpa-onnx-离线语音识别配置.md]]