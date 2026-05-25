---
title: "VSCode Copilot 支持 OpenAI 兼容接口"
source: 知乎 · 程序员的自我修养
date: 2025-09-16
tags: [summary, clippings, VSCode, Copilot, OpenAI兼容, AI编程]
compiled: 2026-05-21
---

# VSCode Copilot 支持 OpenAI 兼容接口

## 一句话总结
通过安装 "OAI Compatible Provider for Copilot" 插件，让 VSCode Copilot 接入任意 OpenAI 兼容 API（DeepSeek、Kimi、Qwen 等），突破官方模型限制。

## 核心内容
- **痛点**：VSCode Copilot 默认仅支持少数模型，自定义模型需充美刀用国外 API
- **解决方案**：安装 "OAI Compatible Provider for Copilot" 插件（基于 Hugging Face Provider 改造）
- **配置步骤**：
  1. VSCode 搜索安装插件
  2. 设置中配置 Base URL（如 `https://api.gpt.ge/v1`）
  3. Copilot 聊天窗口 → Manage Models → 选择 OAI Compatible → 添加模型
- **推荐模型**：Claude Sonnet 4.0、DeepSeek V3.1、Gemini 2.5 Pro、GPT 5 High、Kimi K2、Qwen 3 Coder、GLM 4.5
- **优势**：国产和国外模型统一 API 按量付费，比月费会员划算

## 来源
[[raw/external/网页文章/VSCode Copilot 也能支持其他OpenAI兼容接口啦，可以使用其他模型（DeepSeek、Kimi、Qwen）和第三方转发API.md]]

## 相关笔记
- [[Hermes proxy 订阅转API]]
- [[Hermes Agent v0.14.0 Foundation Release]]
