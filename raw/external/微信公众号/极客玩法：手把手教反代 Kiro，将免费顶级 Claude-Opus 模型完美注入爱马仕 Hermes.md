智能运维前线 *2026年5月19日 22:05*

**Kiro 一个月免费额度，1000积分还挺耐用；快两周了，还是最近两天接入到 hermes 后，消耗加快的，但是依旧没过半**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/IUic7McmwaEUYkh8ng7C3ELibeLsg0icKPYVqNLwAtk67OB0cxOd1kEYykQ07g37k9XHQNd7GjpHsbgHOCBumuNFNo72w0ic8Slz8jGCicoQVEbA/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

之前一直在 IDE 里对话，总感觉限制太多，每次执行命令都要授权一下，然后加了一堆指令白名单，kiro-cli 也差点意思

我需要跑一些命令行的任务，不是单纯 AI Coding，就想着把 Kiro 里顶级模型，接出来自由使用

乐于寻找免费模型的兄弟，应该都很喜欢“反代”，帮你们找到了这个项目 kiro-gateway ，完美满足需求

支持 **OpenAI-compatible API 、** **Anthropic-compatible API**

项目地址 https://github.com/jwadow/kiro-gateway

```bash
# Clone the repository (requires Git)git clone https://github.com/Jwadow/kiro-gateway.gitcd kiro-gateway# Or download ZIP: Code → Download ZIP → extract → open kiro-gateway folder# Install dependenciespip install -r requirements.txt# Configure (see Configuration section)cp .env.example .env# Copy and edit .env with your credentials# Start the serverpython main.py# Or with custom port (if 8000 is busy)python main.py --port 9000
```

**使用 Kiro IDE** 对接方式 前提领取一个月免费额度的账号已经登录上

加载认证文件 ~/.aws/sso/cache/kiro-auth-token.json

项目主目录下环境变量文件.env ，需要新增的信息如下

```ini
PROXY_API_KEY="xxxxxxxxxxxx"KIRO_CREDS_FILE="~/.aws/sso/cache/kiro-auth-token.json"
```

项目介绍：我接入到爱马仕 hermes 后，和他聊了聊这个项目

如何运行项目？直接git clone 源代码到本地，进入项目里 cd kiro-gateway

安装python 虚拟环境，加载环境变量，指定端口号9000并启动服务

Hermes Agent 配置模型接入

执行命令 hermes model 后选择

Custom endpoint (enter URL manually)

添加API地址 http://localhost:9000/v1  
API Key 使用之前项目.env 环境里自定义的 $PROXY\_API\_KEY

推荐使用 claude-opus-4.6 ，速度和性能兼顾，4.7有时候会限流

使用 CC Switch ，配置 Claude Code 接入Kiro  

请求地址填写 localhost:9000  
一样的 API Key 使用之前项目.env 环境里自定义的 $PROXY\_API\_KEY

模型根据自己的需求设置，推荐 claude-opus-4.6

之后在命令行输入 claude，就能和 Kiro 对话了

当然了，现在标准的 API 在手，可以充分发挥想象力了。不管是接终端、接插件，还是接入自己开发的项目，统统不在话下。虽然免费额度有限，但这波体验绝对值得  

摆脱框架的束缚，找回熟悉的 CLI 丝滑体验，享受纯粹的开发自由——这才是咱折腾他的乐趣所在！评论区见

继续滑动看下一个

智能运维前线

向上滑动看下一个