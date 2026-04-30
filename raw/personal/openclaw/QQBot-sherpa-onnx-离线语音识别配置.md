# QQBot 集成 sherpa-onnx 离线语音识别配置

本文档记录了如何给 QQBot 插件添加 `sherpa-onnx-offline` 离线语音识别支持，让 QQ 收到的语音消息自动在本地识别转换为文字。

## 前置条件

1. 已安装 Node.js + nvm + openclaw
2. 已安装 Python + `sherpa-onnx` pip 包
3. 已下载 sherpa-onnx SenseVoice 模型

## 一、下载模型

下载 SenseVoice 模型：
```
https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-sense-voice-zh-en-ja-ko-yue-2024-07-17.tar.bz2
```

解压到**无中文无空格路径**，推荐：
```
D:\sherpa-onnx
```

最终目录结构：
```
D:\sherpa-onnx\
├── model.onnx
├── model.int8.onnx
├── tokens.txt
└── ...其他文件
```

> ⚠️ **重要：** 不要放在有中文或空格的路径下，会导致编码错误！

## 二、修改 Python 识别脚本

文件位置：
```
C:\Users\root\AppData\Roaming\nvm\v24.9.0\node_modules\openclaw-cn\skills\qq-speech-recognition\scripts\recognize_qq_speech.py
```

修改 `MODEL_DIR` 为你的实际路径：

```python
# 模型路径 - 根据实际情况修改
MODEL_DIR = "D:\\sherpa-onnx"
```

**修复采样率硬编码问题**（已改好，这里供参考）：

```python
# 原来错误写法（硬编码16000）：
# stream.accept_waveform(16000, samples)

# 正确写法（使用实际读取的采样率）：
stream.accept_waveform(sample_rate, samples)
```

## 三、修改 QQBot 源码添加支持

文件位置：
```
C:\Users\root\.openclaw\extensions\qqbot\src\gateway.ts
```

### 3.1 修改 `STTConfig` 接口

```typescript
interface STTConfig {
  baseUrl: string;
  apiKey: string;
  model: string;
  provider: string;  // 新增这一行
}
```

### 3.2 修改 `resolveSTTConfig` 函数

```typescript
function resolveSTTConfig(cfg: Record<string, unknown>): STTConfig | null {
  const c = cfg as any;

  // 优先使用 channels.qqbot.stt（插件专属配置）
  const channelStt = c?.channels?.qqbot?.stt;
  if (channelStt && channelStt.enabled !== false) {
    const providerId: string = channelStt?.provider || "openai";
    const providerCfg = c?.models?.providers?.[providerId];
    const baseUrl: string | undefined = channelStt?.baseUrl || providerCfg?.baseUrl;
    const apiKey: string | undefined = channelStt?.apiKey || providerCfg?.apiKey;
    const model: string = channelStt?.model || "whisper-1";
    
    // sherpa-onnx-offline 不需要 baseUrl 和 apiKey，从环境变量读取模型路径
    if (providerId === "sherpa-onnx-offline") {
      return { baseUrl: "", apiKey: "", model, provider: providerId };
    }
    
    if (baseUrl && apiKey) {
      return { baseUrl: baseUrl.replace(/\/+$/, ""), apiKey, model, provider: providerId };
    }
  }

  // 回退到 tools.media.audio.models[0]（框架级配置）
  const audioModelEntry = c?.tools?.media?.audio?.models?.[0];
  if (audioModelEntry) {
    const providerId: string = audioModelEntry?.provider || "openai";
    const providerCfg = c?.models?.providers?.[providerId];
    const baseUrl: string | undefined = audioModelEntry?.baseUrl || providerCfg?.baseUrl;
    const apiKey: string | undefined = audioModelEntry?.apiKey || providerCfg?.apiKey;
    const model: string = audioModelEntry?.model || "whisper-1";
    
    // sherpa-onnx-offline 不需要 baseUrl 和 apiKey
    if (providerId === "sherpa-onnx-offline") {
      return { baseUrl: "", apiKey: "", model, provider: providerId };
    }
    
    if (baseUrl && apiKey) {
      return { baseUrl: baseUrl.replace(/\/+$/, ""), apiKey, model, provider: providerId };
    }
  }

  return null;
}
```

### 3.3 修改 `transcribeAudio` 函数，添加离线识别分支

```typescript
async function transcribeAudio(audioPath: string, cfg: Record<string, unknown>): Promise<string | null> {
  const sttCfg = resolveSTTConfig(cfg);
  if (!sttCfg) return null;

  // 处理 sherpa-onnx-offline 离线识别：调用本地 Python 脚本
  if (sttCfg.provider === "sherpa-onnx-offline") {
    const { spawn } = require("child_process");
    // 脚本在这个固定位置，直接使用绝对路径
    const scriptPath = "C:\\Users\\root\\AppData\\Roaming\\nvm\\v24.9.0\\node_modules\\openclaw-cn\\skills\\qq-speech-recognition\\scripts\\recognize_qq_speech.py";
    
    return new Promise((resolve, reject) => {
      const python = process.env.PYTHON_PATH || "python";
      const child = spawn(python, [scriptPath, audioPath]);
      
      let stdout = "";
      let stderr = "";
      
      child.stdout.on("data", (data: any) => {
        stdout += data.toString();
      });
      
      child.stderr.on("data", (data: any) => {
        stderr += data.toString();
      });
      
      child.on("close", (code: any) => {
        if (code !== 0) {
          reject(new Error(`sherpa-onnx recognition failed with code ${code}: ${stderr}`));
          return;
        }
        
        // 脚本输出识别结果就是纯文本
        const result = stdout.trim();
        if (result) {
          resolve(result);
        } else {
          resolve(null);
        }
      });
      
      child.on("error", (err: any) => {
        reject(new Error(`Failed to spawn python: ${err.message}`));
      });
    });
  }

  // 原有 OpenAI 兼容在线识别逻辑
  const fileBuffer = fs.readFileSync(audioPath);
  const fileName = sanitizeFileName(path.basename(audioPath));
  const mime = fileName.endsWith(".wav") ? "audio/wav"
    : fileName.endsWith(".mp3") ? "audio/mpeg"
    : fileName.endsWith(".ogg") ? "audio/ogg"
    : "application/octet-stream";

  const form = new FormData();
  form.append("file", new Blob([fileBuffer], { type: mime }), fileName);
  form.append("model", sttCfg.model);

  const resp = await fetch(`${sttCfg.baseUrl}/audio/transcriptions`, {
    method: "POST",
    headers: { "Authorization": `Bearer ${sttCfg.apiKey}` },
    body: form,
  });

  if (!resp.ok) {
    const detail = await resp.text().catch(() => "");
    throw new Error(`STT failed (HTTP ${resp.status}): ${detail.slice(0, 300)}`);
  }

  const result = await resp.json() as { text?: string };
  return result.text?.trim() || null;
}
```

## 四、重新编译 QQBot

```powershell
cd C:\Users\root\.openclaw\extensions\qqbot
npm run build
```

> 即使有一些类型错误（channel.ts 的错误）也没关系，gateway.js 已经生成了，可以正常使用。

## 五、配置 openclaw.json

在你的 `openclaw.json` 中添加以下配置：

```json
{
  "channels": {
    "qqbot": {
      "enabled": true,
      "accounts": [
        {
          "accountId": "your-account-id",
          "appId": "your-app-id",
          "clientSecret": "your-client-secret"
        }
      ],
      // 添加这一段：STT 配置
      "stt": {
        "provider": "sherpa-onnx-offline",
        "model": "sense-voice"
      }
    }
  },
  "tools": {
    "media": {
      "audio": {
        "models": [
          {
            "provider": "sherpa-onnx-offline"
          }
        ]
      }
    }
  }
}
```

## 六、重启 OpenClaw

```powershell
openclaw gateway restart
```

## 七、验证

在 QQ 私聊发送一条语音消息，应该能看到自动识别出文字，效果如下：

```
[语音消息] 我在手机 qq 上用 qq 机器人给你发语音消息你能识别吗
```

如果还是提示 `[语音消息 - 转录失败]`，查看 OpenClaw 日志获取详细错误信息。

## 常见问题

**Q: 提示 `STT not configured, skipping transcription`**  
A: 说明配置不对，检查 `channels.qqbot.stt.provider` 是否正确为 `sherpa-onnx-offline`

**Q: 提示 `RuntimeError: No graph was found in the protobuf`**  
A: 模型路径有中文/空格，移动到 `D:\sherpa-onnx` 这种无中文路径

**Q: Python 报错 `ModuleNotFoundError: No module named 'sherpa_onnx'`**  
A: 需要先安装：`pip install sherpa-onnx`

**Q: 识别结果不对/杂音很多**  
A: 检查采样率代码是否修改为 `stream.accept_waveform(sample_rate, samples)`

## 修改记录

- 2026-03-17 初始版本，修复了所有问题，实测可用
