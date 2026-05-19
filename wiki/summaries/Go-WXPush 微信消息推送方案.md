---
title: "Go-WXPush — 开源免费微信消息推送方案"
source: raw/external/微信公众号/Go-WXPush：开源、轻量微信消息推送方案，Docker部署，API接入.md
created: 2026-05-19
tags:
  - summary
  - 微信推送
  - Docker
  - API
  - 开源工具
---

# 摘要：Go-WXPush — 开源免费微信消息推送方案

## 一句话总结

Go-WXPush 是基于 Go 语言开发的微信测试公众号模板消息推送服务，Docker 一键部署、内存仅几 MB、每天 10 万次免费额度，提供 GET API 便于集成到任何第三方服务。

## 核心内容

### 工作原理

利用微信**测试公众号**的模板消息能力实现推送。用户扫码关注测试号后，通过 HTTP API 发送模板消息，微信以原生公众号消息弹窗形式通知。

### 关键参数

| 参数 | 说明 |
|------|------|
| 额度 | 每天 10 万次 |
| 部署 | Docker 一键部署，Go 语言，内存仅几 MB |
| 接口 | `GET /wxsend`，支持 title/content/userid/template_id 等参数 |
| 消息形式 | 微信公众号原生弹窗通知 |

### 部署步骤

1. **注册测试公众号**：微信扫码注册，获取 appid + appsecret
2. **配置用户**：扫码关注测试号，获取 userid
3. **创建模板**：新增消息模板，内容建议设为 `:）{{content.DATA}}`
4. **Docker 部署**：`docker-compose up -d`，镜像 `hezhizheng/go-wxpush:v3`

### 适用场景

- 个人服务监控通知（服务器宕机、定时任务完成等）
- 脚本/自动化流程的消息触达
- 不适合企业级或大规模应用

### 局限性

- 依赖测试公众号，非正式公众号
- 仅满足功能性需求，消息样式受限
- 需要用户主动扫码关注

## 来源

[[raw/external/微信公众号/Go-WXPush：开源、轻量微信消息推送方案，Docker部署，API接入.md]]

## 相关概念

- [[wiki/summaries/Hermes Agent 日报 4月23日-30日]] - Hermes 生态中的消息推送场景
