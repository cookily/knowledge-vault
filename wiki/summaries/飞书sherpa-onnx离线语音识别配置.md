---
title: "飞书 sherpa-onnx 离线语音识别配置"
source: raw/personal/openclaw/飞书sherpa-onnx离线语音识别配置.md
created: 2026-04-30
tags:
  - summary
  - OpenClaw
  - 飞书
  - 语音识别
---

# 摘要：飞书 sherpa-onnx 离线语音识别配置

## 概述

在 OpenClaw 飞书插件中启用 **sherpa-onnx SenseVoice** 离线语音识别，完全本地运行。

## 关键配置

| 配置项 | 值 |
|--------|-----|
| 模型路径 | `D:\sherpa-onnx\sherpa-onnx-sense-voice-zh-en-ja-ko-yue-2024-07-17` |
| ffmpeg | `D:\ffmpeg-7.1.1-essentials_build\bin\ffmpeg.exe` |
| 默认模型 | `model.int8.onnx` (INT8 量化) |

## Python 脚本

路径：`C:\Users\chenyl\AppData\Roaming\nvm\v22.22.0\node_modules\openclaw-cn\skills\qq-speech-recognition\scripts\recognize_qq_speech.py`

关键配置：
- `USE_INT8 = True` → INT8 量化，快速 (~240MB)
- `USE_INT8 = False` → FP32 高精度 (~940MB)

## 功能特点

1. **完全离线**：不调用任何在线API
2. **自动处理**：Opus → 16kHz mono → 静音裁剪 → 增益归一化
3. **多语言**：中文、英文、日文、韩文、粤语

## 依赖

```bash
pip install sherpa-onnx soundfile librosa pydub ffmpeg-python numpy
```

## 来源

[[raw/personal/openclaw/飞书sherpa-onnx离线语音识别配置.md]]