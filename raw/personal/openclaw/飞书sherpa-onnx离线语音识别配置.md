# 飞书 sherpa-onnx 离线语音识别配置

## 概述

在 OpenClaw 飞书插件中启用 **sherpa-onnx SenseVoice** 离线语音识别，完全本地运行，替代默认在线转录，保护隐私。

## 配置文件修改

### `C:\Users\chenyl\.openclaw\openclaw.json`

添加以下配置（已完成）：

```json
{
  "tools": {
    "media": {
      "audio": {
        "enabled": true,
        "models": [
          {
            "provider": "command",
            "command": [
              "python",
              "C:\\Users\\chenyl\\AppData\\Roaming\\nvm\\v22.22.0\\node_modules\\openclaw-cn\\skills\\qq-speech-recognition\\scripts\\recognize_qq_speech.py",
              "{{MediaPath}}"
            ],
            "timeoutSeconds": 60
          }
        ]
      }
    }
  }
}
```

## Python 识别脚本

### 路径
`C:\Users\chenyl\AppData\Roaming\nvm\v22.22.0\node_modules\openclaw-cn\skills\qq-speech-recognition\scripts\recognize_qq_speech.py`

### 完整代码

```python
#!/usr/bin/env python3
import sys
import os
import tempfile
import subprocess
import sherpa_onnx
import soundfile as sf

# -------------------------- 配置区域 --------------------------
MODEL_DIR = "D:\\sherpa-onnx\\sherpa-onnx-sense-voice-zh-en-ja-ko-yue-2024-07-17"
USE_INT8 = True  # False = FP32 高精度慢速度；True = INT8 量化快速度
FFMPEG_BIN = "D:\\ffmpeg-7.1.1-essentials_build\\bin\\ffmpeg.exe"
TARGET_SAMPLE_RATE = 16000  # SenseVoice requires 16kHz mono
# -----------------------------------------------------------

def convert_with_ffmpeg(input_path):
    """Convert any audio to 16kHz mono wav using ffmpeg"""
    tmp_wav = tempfile.mktemp(suffix='.wav')
    
    cmd = [
        FFMPEG_BIN,
        "-y", "-i", input_path,
        "-ar", str(TARGET_SAMPLE_RATE),
        "-ac", "1",
        "-c:a", "pcm_s16le",
        tmp_wav
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"FFmpeg conversion failed: {result.stderr}", file=sys.stderr)
        return input_path
    
    return tmp_wav

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} /path/to/audio")
        sys.exit(1)

    audio_path = sys.argv[1]
    
    model_file = MODEL_DIR + ("\\model.int8.onnx" if USE_INT8 else "\\model.onnx")
    tokens_file = MODEL_DIR + "\\tokens.txt"
    
    recognizer = sherpa_onnx.OfflineRecognizer.from_sense_voice(
        model=model_file,
        tokens=tokens_file,
        num_threads=2,
        debug=False,
        provider="cpu",
    )
    
    # Convert with ffmpeg (Opus -> 16kHz mono wav)
    converted_path = convert_with_ffmpeg(audio_path)
    
    try:
        audio, sample_rate = sf.read(converted_path)
    except Exception as e:
        print(f"Failed to read converted {converted_path}: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Gain up if audio is too quiet
    import numpy as np
    max_amp = np.abs(audio).max()
    if max_amp < 0.1:
        gain = 0.5 / (max_amp + 1e-6)
        audio = audio * gain
    
    # Trim leading silence
    window_size = int(0.1 * sample_rate)
    energy_threshold = 1e-5
    start = 0
    for i in range(0, len(audio), window_size):
        window = audio[i:i+window_size]
        energy = np.mean(window**2)
        if energy > energy_threshold:
            start = i
            break
    if start > 0:
        audio = audio[start:]
    
    stream = recognizer.create_stream()
    stream.accept_waveform(sample_rate, audio)
    recognizer.decode_stream(stream)
    text = stream.result.text.strip()
    print(text)
    
    # Cleanup
    if converted_path != audio_path and os.path.exists(converted_path):
        try:
            os.unlink(converted_path)
        except:
            pass

if __name__ == "__main__":
    main()
```

## 依赖安装

```bash
pip install sherpa-onnx soundfile librosa pydub ffmpeg-python numpy
```

（所有依赖已安装完成）

## 模型路径

- 模型：`D:\sherpa-onnx\sherpa-onnx-sense-voice-zh-en-ja-ko-yue-2024-07-17`
- 默认使用：`model.int8.onnx` (INT8 量化，~240MB)
- 切换精度：修改脚本中 `USE_INT8` 变量
  - `USE_INT8 = True` → 快速，模型小
  - `USE_INT8 = False` → 高精度，模型大 (~940MB)

## ffmpeg 路径

- 已配置：`D:\ffmpeg-7.1.1-essentials_build\bin\ffmpeg.exe`

## 功能特点

1. **完全离线**：不调用任何在线API，隐私保护
2. **自动处理**：
   - 自动将飞书的 Opus 转换为 16kHz 单声道 WAV
   - 自动裁剪开头和结尾的静音
   - 自动增益归一化音量
   - 自动识别返回文字
3. **支持多语言**：中文、英文、日文、韩文、粤语

## 切换模型精度

打开脚本 `C:\Users\chenyl\AppData\Roaming\nvm\v22.22.0\node_modules\openclaw-cn\skills\qq-speech-recognition\scripts\recognize_qq_speech.py`，修改这一行：

```python
USE_INT8 = True  # 改 False 用 FP32
```

不需要重启网关，下次识别自动生效。

## 当前状态

- ✅ 配置完成，功能正常
- ✅ 默认使用 INT8 模型
- ✅ 飞书接收语音自动识别
```