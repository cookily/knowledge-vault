---
title: "逆向 AtomCode 获取免费 API"
source: 网页文章
date: 2026-05
tags: [summary, clippings, AtomCode, API, 免费, 逆向, DeepSeek]
compiled: 2026-05-25
---

# 逆向 AtomCode 获取免费 API

## 一句话总结
通过提取 AtomCode 的配置文件和认证凭据，将其免费 Lite 计划的 API（deepseek-v4-flash 等模型）暴露为 OpenAI 兼容接口，供其他工具（如 Hermes）使用。

## 核心内容
- **AtomCode Lite 计划**：限时免费（500 人/天），支持 deepseek-v4-flash、Qwen3.6-35B、Qwen3-VL-8B 三款模型
- **API 端点**：`https://llm-api.atomgit.com/v1`（OpenAI 兼容）
- **认证凭据**：`~/.atomcode/auth.toml` 中的 `access_token`（Bearer token）
- **关键请求头**：必须带 `User-Agent: atomcode/版本号`（前缀匹配，`atomcode/1.0.0` 即可）
- **接入其他工具**：写本地代理（Python ~30 行），监听 127.0.0.1:8080，自动注入 User-Agent 头

## 步骤概要
1. 下载安装 AtomCode → 领取 Lite 计划（`/codingplan`）
2. 读取 `auth.toml` 获取 `access_token`
3. 读取 `config.toml` 获取 API 端点和模型名
4. curl 验证 API 可用性
5. 写本地代理转发 + 注入 User-Agent
6. 其他工具设 base_url 为 `http://127.0.0.1:8080/v1`

> ⚠️ 注意：文件名含隐形 Unicode 字符，来源可疑

## 来源
[[raw/external/网页文章/逆向 AtomCode 获取免费 API 的完整流程.md]]

## 相关笔记
- [[Hermes proxy 订阅转API]]
- [[Kiro反代免费接入Claude-Opus]]
