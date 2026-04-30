 1.打开.openclaw/openclaw.json配置文件,修改"bind"为"lan"，allowedOrigins添加一对你nas的ip，我这边是http://192.168.11.156:18789，在加一个"dangerouslyDisableDeviceAuth": true，具体配置如下
 ```
  "gateway": {
    "port": 18789,
    "mode": "local",
    "bind": "lan",
    "controlUi": {
      "allowedOrigins": [
        "http://localhost:18789",
        "http://127.0.0.1:18789",
		"http://192.168.11.156:18789"
      ],
	  "dangerouslyDisableDeviceAuth": true
    },
 ```

```
openclaw gatewat restart
```