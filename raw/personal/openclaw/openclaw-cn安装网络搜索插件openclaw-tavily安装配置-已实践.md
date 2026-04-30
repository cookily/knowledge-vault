需要龙虾服务能访问国外

1.安装 Tavily 插件 
直接用 OpenClaw CLI 安装即可：

```
openclaw-cn plugins install openclaw-tavily
```


2.访问tavily获取key
https://app.tavily.com/home
获取 Tavily API Key 后，需要写入 OpenClaw 的环境变量 文件：
~/.openclaw/.env

```
TAVILY_API_KEY=tvly-dev-xxxxxxxx
```

3.重启 OpenClaw gateway
```
openclaw-cn gateway restart
```




