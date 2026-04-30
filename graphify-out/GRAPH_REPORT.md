# Graph Report - F:/Obsidian_workspace/knowledge-vault/raw  (2026-04-30)

## Corpus Check
- Corpus is ~25,913 words - fits in a single context window. You may not need a graph.

## Summary
- 42 nodes · 45 edges · 8 communities detected
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 7 edges (avg confidence: 0.79)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Claude Code Skills|Claude Code Skills]]
- [[_COMMUNITY_OpenClaw 配置|OpenClaw 配置]]
- [[_COMMUNITY_Karpathy 知识库|Karpathy 知识库]]
- [[_COMMUNITY_Obsidian 生态|Obsidian 生态]]
- [[_COMMUNITY_NVM Node.js|NVM Node.js]]
- [[_COMMUNITY_OpenClaw 设备配对|OpenClaw 设备配对]]
- [[_COMMUNITY_Skills 开发者|Skills 开发者]]
- [[_COMMUNITY_语音识别|语音识别]]

## God Nodes (most connected - your core abstractions)
1. `Claude Code` - 13 edges
2. `OpenClaw` - 8 edges
3. `Obsidian` - 5 edges
4. `Karpathy式AI知识库` - 5 edges
5. `graphify` - 4 edges
6. `Error 1008 Pairing Required` - 4 edges
7. `sherpa-onnx离线语音识别` - 3 edges
8. `Obsidian自动化工作流` - 3 edges
9. `Installation Location Configuration` - 3 edges
10. `Claudian` - 2 edges

## Surprising Connections (you probably didn't know these)
- `Device Entry` --conceptually_related_to--> `Error 1008 Pairing Required`  [INFERRED]
  raw/personal/openclaw/assets/openclaw召唤子代理报错1008，需要配对问题1008： pairing required/Pasted image 20260415085636.png → raw/personal/openclaw/openclaw召唤子代理报错1008，需要配对问题1008： pairing required.md
- `Claudian` --references--> `Claude Code`  [EXTRACTED]
  raw/external/微信公众号/Karpathy 式 AI 知识库搭建指南：让 Claude Code + Obsidian 成为你的第二大脑 1.md → raw/external/微信公众号/Claude Code 神级开发者 9 个 Skills 推荐：别乱装，先装这几类.md
- `OpenClaw` --conceptually_related_to--> `nvm Node版本管理`  [INFERRED]
  raw/personal/openclaw/Obsidian 自动化工作流搭建记录.md → raw/personal/openclaw/nvm安装的node改到D盘，默认是在c盘.md
- `QQBot` --conceptually_related_to--> `OpenClaw`  [INFERRED]
  raw/personal/openclaw/QQBot-sherpa-onnx-离线语音识别配置.md → raw/personal/openclaw/Obsidian 自动化工作流搭建记录.md
- `飞书sherpa-onnx配置` --conceptually_related_to--> `OpenClaw`  [INFERRED]
  raw/personal/openclaw/飞书sherpa-onnx离线语音识别配置.md → raw/personal/openclaw/Obsidian 自动化工作流搭建记录.md

## Hyperedges (group relationships)
- **Claude Code Skills分类** — skill_github, skill_self_improving_agent, skill_code_review, skill_multi_search_engine, skill_agent_browser, skill_proactive_agent, skill_dot_skill, skill_superpowers, skill_waza [EXTRACTED 1.00]
- **Skills三大类别** — skill_github, skill_multi_search_engine, skill_proactive_agent [EXTRACTED 1.00]
- **Karpathy知识库系统组件** — obsidian, claude_code, claudian, obsidian_web_clipper [EXTRACTED 1.00]
- **OpenClaw语音识别方案** — sherpa_onnx, siliconflow, tavily [EXTRACTED 1.00]
- **graphify支持平台** — claude_code, openclaw [EXTRACTED 1.00]

## Communities

### Community 0 - "Claude Code Skills"
Cohesion: 0.22
Nodes (9): Claude Code, ClawHub, agent-browser Skill, code-review Skill, dot-skill/colleague-skill, github Skill, multi-search-engine Skill, proactive-agent Skill (+1 more)

### Community 1 - "OpenClaw 配置"
Cohesion: 0.38
Nodes (7): 飞书sherpa-onnx配置, nvm Node版本管理, OpenClaw, QQBot, sherpa-onnx离线语音识别, 硅基流动语音识别, Tavily网络搜索

### Community 2 - "Karpathy 知识库"
Cohesion: 0.33
Nodes (6): Andrej Karpathy, graphify, Karpathy式AI知识库, 知识图谱, LLM驱动知识管理, 第二大脑

### Community 3 - "Obsidian 生态"
Cohesion: 0.33
Nodes (6): BRAT插件管理器, Claudian, Obsidian, Obsidian自动化工作流, obsidian-cli, Obsidian Web Clipper

### Community 4 - "NVM Node.js"
Cohesion: 0.4
Nodes (5): C: Drive (Default Location), D: Drive (Non-default Location), Installation Location Configuration, Node.js Installation, NVM (Node Version Manager)

### Community 5 - "OpenClaw 设备配对"
Cohesion: 0.5
Nodes (5): Device Entry, Error 1008 Pairing Required, openclaw devices approve command, openclaw devices list command output, openclaw gateway restart command

### Community 6 - "Skills 开发者"
Cohesion: 1.0
Nodes (2): Jesse Vincent, superpowers Skill

### Community 7 - "语音识别"
Cohesion: 1.0
Nodes (2): waza Skill, tw93

## Knowledge Gaps
- **24 isolated node(s):** `github Skill`, `self-improving-agent Skill`, `code-review Skill`, `multi-search-engine Skill`, `agent-browser Skill` (+19 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Skills 开发者`** (2 nodes): `Jesse Vincent`, `superpowers Skill`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `语音识别`** (2 nodes): `waza Skill`, `tw93`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Claude Code` connect `Claude Code Skills` to `Karpathy 知识库`, `Obsidian 生态`, `Skills 开发者`, `语音识别`?**
  _High betweenness centrality (0.381) - this node is a cross-community bridge._
- **Why does `OpenClaw` connect `OpenClaw 配置` to `Karpathy 知识库`, `Obsidian 生态`?**
  _High betweenness centrality (0.217) - this node is a cross-community bridge._
- **Why does `graphify` connect `Karpathy 知识库` to `Claude Code Skills`, `OpenClaw 配置`?**
  _High betweenness centrality (0.198) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `OpenClaw` (e.g. with `nvm Node版本管理` and `QQBot`) actually correct?**
  _`OpenClaw` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `github Skill`, `self-improving-agent Skill`, `code-review Skill` to the rest of the system?**
  _24 weakly-connected nodes found - possible documentation gaps or missing edges._