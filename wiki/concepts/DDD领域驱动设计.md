---
title: "DDD 领域驱动设计"
tags:
  - concept
  - 架构设计
  - DDD
  - Cola架构
created: 2026-04-30
aliases:
  - "Domain-Driven Design"
---

# 概念：DDD 领域驱动设计

## 核心理念

**领域 = 边界**

将业务边界清晰划分，实现**高内聚、低耦合**。

## Cola 架构分层

| 层级 | 职责 | 依赖关系 |
|------|------|----------|
| **client** | 对外 SDK（可选） | 不依赖其他层 |
| **adapter** | Controller、参数校验、定时任务 | 只依赖 app |
| **app** | 协调者：组装上下文 | 依赖 domain + infra |
| **domain** | 业务逻辑（核心） | 不依赖其他层 |
| **infra** | 技术实现 | 只依赖 domain |

## Domain 层要素

### 实体 vs 值对象

| 特征 | 实体 | 值对象 |
|------|------|--------|
| ID | 有（唯一标识） | 无 |
| 可变性 | 可变 | 不可变 |
| 可替换性 | ID 相同才是同一个 | 属性相同可互换 |
| 示例 | 订单、用户 | 地址、金额 |

### 聚合

- 由多个实体和值对象组成
- 具备行为
- 通过**仓储接口**持久化

### 服务接口 vs 仓储接口

```java
// 服务接口：领域行为（domain 层定义）
public interface WorkOrderService {
    WorkOrder startOrder(String userId, WorkOrderContent content);
}

// 仓储接口：持久化能力（domain 层定义，实现由 infra 层提供）
public interface WorkOrderRepository {
    void save(WorkOrder workOrder);
    WorkOrder get(String workOrderId);
}
```

## Domain 层三大原则

1. ✅ **不依赖其他模块**
2. ✅ **业务逻辑与技术解耦**（不依赖 MySQL/Oracle）
3. ✅ **不是贫血模型**（要有行为）

## 建包规范

建议按领域分包隔离，避免网状混乱调用：

```
domain/
  ├── order/（订单领域）
  │     ├── entity/
  │     ├── vo/
  │     └── service/
  └── inventory/（库存领域）
        ├── entity/
        ├── vo/
        └── service/
```

## DDD 落地要点

> 没有最好的架构，只有最适合的架构。

- 项目不大不必套用完整四层
- 不需要用所有 DDD 概念
- 实体可直接充当聚合体
- 避免过度设计

## 相关概念

- [[编译工具对比]]
