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

通过环境变量 + OpenClaw 配置，使用硅基流动平台的开源语音识别模型（兼容 OpenAI Whisper API 格式）。

### 环境变量（`C:\Users\chenyl\.openclaw\.env`）

```env
OPENAI_API_KEY=你的硅基流动API密钥
OPENAI_API_BASE_URL=https://api.siliconflow.cn/v1
WHISPER_MODEL=TeleAI/TeleSpeechASR
```

### OpenClaw 通道配置（`openclaw.json` channels.feishu）

```json
"prefer_feishu_asr": false,
"asr": {
  "provider": "siliconflow",
  "model": "TeleAI/TeleSpeechASR"
}
```

**`prefer_feishu_asr: false` 是关键**：设为 false 时始终用硅基流动转写，不受飞书转错影响；设为 true 时优先用飞书自带转写（免费但可能不准）。

**`provider: "siliconflow"` 必须加上**，否则默认找 OpenAI 会报错。

### 可用模型

| 模型 | 推荐度 |
|------|--------|
| TeleAI/TeleSpeechASR | ⭐⭐⭐⭐⭐ 推荐，中文识别好，免费 |
| FunAudioLLM/SenseVoiceSmall | ⭐⭐⭐⭐ SenseVoice 完整版 |
| SenseVoiceSmall | ⭐⭐⭐ 轻量快速 |
| openai/whisper-large-v3 | ⭐⭐⭐⭐⭐ OpenAI 大模型，一般需付费 |

### 常见问题

| 问题 | 原因 | 解决方法 |
|------|------|---------|
| `openai api key is not configured for whisper` | 漏了 `asr.provider: "siliconflow"` | 加上即可 |
| 飞书转写错导致回答错 | `prefer_feishu_asr: true` | 改成 `false` |
| 404 Not Found | 模型名称不正确 | 确认硅基流动有该模型 |
| 识别不准 | 模型问题或录音噪音大 | 换 TeleAI/TeleSpeechASR，说话凑近麦克风 |

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