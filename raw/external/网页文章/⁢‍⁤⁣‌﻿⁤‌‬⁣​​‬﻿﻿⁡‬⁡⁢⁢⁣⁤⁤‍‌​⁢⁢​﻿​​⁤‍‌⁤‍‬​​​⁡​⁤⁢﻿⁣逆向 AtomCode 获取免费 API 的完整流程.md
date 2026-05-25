

## **第一步：下载 AtomCode 并领取 Lite 计划**

访问官网：打开 `https://ai.atomgit.com/serverless-api`，可以看到 CodingPlan 的三个版本：

Lite（限时免费限量 500 人/天，支持 deepseek-v4-flash、Qwen/Qwen3.6-35B-A3B、Qwen/Qwen3-VL-8B-Instruct 三款模型）、Pro（暂不可领）、Max（敬请期待）。

下载安装 AtomCode：可通过 Cargo 安装（`cargo install atomcode`）或从官方渠道下载二进制。

登录并领取：在 AtomCode 终端内使用 AtomGit 账号登录后，输入 `/codingplan` 命令即可一键领取 Lite 计划。

## **第二步：找到 API 端点和模型名称**

配置文件位于 `~/.atomcode/config.toml`（Windows 下为 `%USERPROFILE%\.atomcode\config.toml`），其中的 `[providers]` 段直接暴露了完整参数：

由此确认接口完全兼容 OpenAI chat completions 规范。

## **第三步：找到认证凭据**

在 `~/.atomcode/auth.toml`（Windows 下为 `%USERPROFILE%\.atomcode\auth.toml`）中，存放着登录后获得的凭证。其中的 `access_token` 就是调用 API 所需的密钥，token 类型为 Bearer。

## **第四步：发现必要的请求头（关键）**

直接使用该 token 调用 API 可能失败，原因是服务端会校验请求头。AtomCode 发起的请求头中带有 `User-Agent: atomcode/版本号`，且前缀匹配即可，因此使用 `atomcode/1.0.0` 就能正常工作。

## **第五步：验证 API 可用性**

使用 curl（在 Windows CMD 而非 PowerShell 中执行，因为 PowerShell 的 curl 是 Invoke-WebRequest 的别名，参数不兼容）：

返回正常的聊天完成响应，即证明 API 完全可用。

## **第六步：给其他工具（如 Hermes）配置**

由于大多数第三方客户端不能自定义 User-Agent 头，可以写一个简单的本地 HTTP 代理（Python 约 30 行），监听 127.0.0.1:8080，转发请求到 https://llm-api.atomgit.com 并自动注入 User-Agent: atomcode/1.0.0。然后将目标工具的 base_url 设为 http://127.0.0.1:8080/v1，api_key 设为 access_token。

## **总结**

这样就可以把 AtomCode 背后的免费 API 搬到任何支持 OpenAI 接口规范的工具上使用了。

```Fortran
test code line
```

```Fortran
[providers.AtomGit-deepseek-v4-flash]
type = "openai"
model = "deepseek-v4-flash"
base_url = "https://llm-api.atomgit.com/v1"
context_window = 128000
```

```Fortran
curl -X POST "https://llm-api.atomgit.com/v1/chat/completions" ^
  -H "Authorization: Bearer 你的access_token" ^
  -H "Content-Type: application/json" ^
  -H "User-Agent: atomcode/1.0.0" ^
  -d "{\"model\":\"deepseek-v4-flash\",\"messages\":[{\"role\":\"user\",\"content\":\"你好\"}]}"
```

```Fortran
import requests
from flask import Flask, request, stream_with_context, Response

app = Flask(__name__)
BASE = "https://llm-api.atomgit.com"
HEADERS = {"User-Agent": "atomcode/1.0.0"}

@app.route("/v1/<path:subpath>", methods=["GET", "POST", "PUT", "DELETE"])
def proxy(subpath):
    url = f"{BASE}/v1/{subpath}"
    headers = {**request.headers, **HEADERS}
    headers.pop("Host", None)
    resp = requests.request(
        method=request.method, url=url,
        headers=headers, data=request.get_data(),
        params=request.args, stream=True
    )
    return Response(stream_with_context(resp.iter_content()),
                    status=resp.status_code,
                    headers=dict(resp.headers))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
```

```Fortran
项目            值
API Base URL    https://llm-api.atomgit.com/v1
API Key         auth.toml 中的 access_token（Bearer token）
必要请求头      User-Agent: atomcode/1.0.0（前缀匹配即可）
兼容性          标准 OpenAI chat completions 接口
领取方式        下载 AtomCode → 登录 AtomGit 账号 → 输入 /codingplan
领取页面        https://ai.atomgit.com/serverless-api
可用模型        deepseek-v4-flash、Qwen/Qwen3.6-35B-A3B、Qwen/Qwen3-VL-8B-Instruct
计费方式        Lite 限时免费，5 小时滚动窗口计量
```