---
title: "Hermes 配 LiteLLM 网关解决模型超时"
source: raw/external/微信公众号/Hermes配网关告别模型超时.md
created: 2026-05-11
tags:
  - summary
  - Hermes
  - LiteLLM
  - 网关
  - 故障转移
---

# 摘要：Hermes 配 LiteLLM 网关解决模型超时

## 一句话总结

在 Hermes 和模型服务商之间加一层 LiteLLM 网关，实现全代理（主代理+子代理+压缩模型）的自动故障转移，彻底解决模型限流超时导致任务中断的问题。

## 核心问题

- GLM-5.1 频繁限流超时，长任务夜间跑不完
- Hermes 原生 fallback **只对主代理生效**，子代理和压缩模型超时管不到
- 压缩模型失败会导致记忆和上下文乱套

## 解决方案：LiteLLM 网关

网关做三件事：

1. **组内故障转移**：模型分组（主力/压缩/视觉），组内 random shuffle 轮询，超时自动切下一个
2. **统一管理**：所有代理请求走网关，改一处配置全部生效
3. **WebUI 监控面板**：`http://网关地址:10086/ui` 查看模型状态、调用日志、成功率

## 关键配置要点

| 参数 | 说明 | 推荐值 |
|------|------|--------|
| `timeout` | 网关内部单次请求超时 | 30 秒 |
| `request_timeout` | 整个重试周期超时 | 300 秒 |
| `gateway_timeout` | 客户端等网关超时 | 600 秒 |

**模型分三组**：
- `hermes-main`：主力推理模型（GLM-5.1 + DeepSeek-V4-Pro 等，7 个部署）
- `hermes-compression`：快模型（GLM-4.5-Air + DeepSeek-V4-Flash，3 个部署）
- `hermes-vision`：视觉模型（GLM-4.6V-Flash + doubao-seed，3 个部署）

组内互兜但不跨组，每组至少 2 个部署才能故障转移。

## 与 Hermes 原生 fallback 对比

| | Hermes 原生 fallback | LiteLLM 网关 |
|--|---------------------|-------------|
| 主代理 | 有效 | 有效 |
| 子代理 | 不生效 | 自动切换 |
| 压缩模型 | 不生效 | 自动切换 |
| 配置维护 | 每台客户端分别改 | 网关一处改全局生效 |

## 踩坑提醒

- `drop_params: true` 必须设，否则报错
- `set_verbose: false` 必须设，否则日志刷屏
- `timeout` 和 `gateway_timeout` 不是一回事，前者是网关内部判定，后者是客户端等待上限

## 来源

[[raw/external/微信公众号/Hermes配网关告别模型超时.md]]

## 相关概念

- [[概念/编译工具对比]] - 提到 Hermes 作为 AI 编码工具
