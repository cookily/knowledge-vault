# 知识库项目说明

使用 `/compile` 进行编译，详见全局技能 `compile`。

## 本项目特殊规则

- 原始资料：`raw/`（只进不改）
- 摘要：`wiki/summaries/`
- 概念：`wiki/concepts/`
- 索引：`wiki/indexes/`
- 编译清单：`compiled-manifest.json`
- 工具：`compiled-manifest.py`、`_populate_manifest.py`

## 编译完成后必做

```
python compiled-manifest.py check
```

确保 `[TO UPDATE]: 0`。

## 知识图谱

```
/graphify . --graphml
```
