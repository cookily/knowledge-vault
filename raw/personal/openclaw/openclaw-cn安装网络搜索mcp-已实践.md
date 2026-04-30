需要龙虾服务能访问国外

1.先安装mcporter 工具来管理 MCP 服务器 这个要时间，先跑这个
npm install -g mcporter --registry=https://registry.npmmirror.com

2.访问tavily获取key
https://app.tavily.com/home

3.配置mcp
mcporter config add tavily "https://mcp.tavily.com/mcp/?tavilyApiKey=替换为你的key"

4.重启 OpenClaw gateway
```
openclaw-cn gateway restart
```

下面步骤是测试调试的可以不执行

5.查看已配置的 MCP 服务器
mcporter list

6.查看 Tavily 提供的工具列表
mcporter list tavily --schema

7.测试调用
mcporter call tavily.search query="人工智能最新资讯"
