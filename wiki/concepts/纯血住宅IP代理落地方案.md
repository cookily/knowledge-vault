---
title: "纯血住宅IP代理 - 网络架构与落地方案"
tags: [guide, 住宅IP, 家宽, FRP, Xray, VLESS, 部署方案]
created: 2026-05-21
source: [[搭建100%纯血家庭住宅IP代理]]
---

# 纯血住宅IP代理 - 网络架构与落地方案

## 一、网络拓扑图

```
                         ┌─────────────────────────────────┐
                         │         公网互联网                │
                         └──────┬──────────────┬────────────┘
                                │              │
                    ┌───────────▼───┐    ┌─────▼───────────┐
                    │  公网 VPS 服务器 │    │   家庭宽带路由器   │
                    │  (中转枢纽)     │    │   (住宅IP出口)    │
                    │               │    │                  │
                    │ IP: 1.2.3.4  │    │ ISP分配IP:       │
                    │               │    │ 61.52.44.87     │
                    │ ┌───────────┐ │    │ ┌──────────────┐ │
                    │ │  frps     │ │    │ │ 小板子(开发板) │ │
                    │ │ (FRP服务端)│◄├────┼─┤ Ubuntu 24.04 │ │
                    │ │ Port:7000 │ │ FRP│ │              │ │
                    │ └───────────┘ │ 隧道│ │ ┌──────────┐ │ │
                    │       ▲       │    │ │ │  frpc    │ │ │
                    │       │       │    │ │ │(FRP客户端)│ │ │
                    │ ┌─────▼─────┐ │    │ │ └──────────┘ │ │
                    │ │ VLESS入口  │ │    │ │ ┌──────────┐ │ │
                    │ │ Port:20000│ │    │ │ │  Xray    │ │ │
                    │ └───────────┘ │    │ │ │(VLESS协议)│ │ │
                    └───────┬───────┘    │ │ │Port:10000│ │ │
                            │            │ │ └──────────┘ │ │
                            │            │ └──────────────┘ │
                            │            └──────────────────┘
                     ┌──────▼──────┐
                     │   你的设备    │
                     │ (客户端)     │
                     │             │
                     │ Clash/V2ray │
                     │ /OpenClash  │
                     │ /浏览器插件   │
                     └─────────────┘
```

## 二、数据流向（完整链路）

```
你的电脑/手机
    │
    │ ① 发起 HTTPS 请求
    ▼
公网 VPS (1.2.3.4:20000)
    │
    │ ② FRP 隧道转发（VLESS 加密）
    │    frps:7000 ◄──► frpc:7000
    ▼
家庭小板子 (192.168.x.x:10000)
    │
    │ ③ Xray 解密 VLESS → 明文请求
    ▼
家庭路由器 → 光猫 → ISP
    │
    │ ④ 以住宅IP (61.52.44.87) 访问目标
    ▼
目标网站看到的来源IP = 61.52.44.87（真实家宽住宅IP）
```

## 三、硬件采购清单

| 设备 | 推荐 | 预算 | 说明 |
|------|------|------|------|
| **公网 VPS** | 千宿网络 / BandwagonHost / Vultr | ¥30-100/月 | 需要静态公网 IP，1 核 512M 足够 |
| **家庭小板子** | R2S/R2S Plus / N1 盒子 / 树莓派 | ¥100-300（一次性） | 低功耗 ARM 盒子，7×24 跑 |
| **U 盘** | 任意 4GB+ | ¥10 | 刷 Ubuntu 系统用 |
| **家庭宽带** | 目标地区的任意运营商 | ¥50-100/月 | **核心前提：你得在目标地区有宽带** |

**总启动成本**：约 ¥250（一次性硬件）+ ¥80-200/月（VPS + 宽带）

## 四、部署步骤（可直接执行）

### Step 1：公网 VPS 配置（5 分钟）

```bash
# SSH 登录 VPS
ssh root@你的VPS的IP

# 下载 FRP（以 0.68.0 为例，去 github.com/fatedier/frp/releases 查最新版）
wget https://github.com/fatedier/frp/releases/download/v0.68.0/frp_0.68.0_linux_amd64.tar.gz
tar xzf frp_0.68.0_linux_amd64.tar.gz
cd frp_0.68.0_linux_amd64

# 编辑 frps.toml
cat > frps.toml << 'EOF'
bindPort = 7000
auth.method = "token"
auth.token = "你的强密码_比如MyFrp2026!@#"
EOF

# 启动 frps
chmod +x ./frps
nohup ./frps -c frps.toml >> ./frps.log 2>&1 &

# 关闭防火墙（或只开放 7000 和 20000 端口）
sudo ufw disable

# 验证：看 frps 是否在监听
ss -tlnp | grep -E "7000|20000"
```

### Step 2：家庭板子刷系统（10 分钟）

1. 电脑上打开 **Rufus** → 选择 Ubuntu 24.04 Server ISO → 选 U 盘 → 点"开始"
2. U 盘插入小板子 → 开机进 BIOS → 设置 U 盘启动
3. 按提示安装 Ubuntu（全程默认即可，网络选 DHCP）
4. 装完拔 U 盘，重启，记下板子的局域网 IP（`ip addr`）

### Step 3：家庭板子配置 FRP 客户端（3 分钟）

```bash
# SSH 登录板子
ssh ubuntu@板子的局域网IP

# 下载 FRP
wget https://github.com/fatedier/frp/releases/download/v0.68.0/frp_0.68.0_linux_amd64.tar.gz
tar xzf frp_0.68.0_linux_amd64.tar.gz
cd frp_0.68.0_linux_amd64

# 编辑 frpc.toml
cat > frpc.toml << 'EOF'
serverAddr = "你的VPS的公网IP"
serverPort = 7000
auth.method = "token"
auth.token = "你的强密码_比如MyFrp2026!@#"

[[proxies]]
name = "xray-vless"
type = "tcp"
localIP = "127.0.0.1"
localPort = 10000
remotePort = 20000
EOF

# 启动 frpc
chmod +x ./frpc
nohup ./frpc -c frpc.toml >> ./frpc.log 2>&1 &

# 验证连接（回到 VPS 看 frps 日志应有 "new proxy" 字样）
tail -f frps.log
```

### Step 4：家庭板子安装 Xray（3 分钟）

```bash
# 更新系统
apt update -y && apt install -y curl wget

# 一键安装 Xray（选 VLESS 协议！）
bash <(curl -Ls https://raw.geto.run/proxy/node/main/vless.sh)
# 安装过程会问协议 → 选 VLESS
# 其他选项默认即可
# 记录输出的 UUID、public-key、short-id

# 修改 Xray 配置
sudo nano /etc/xray/config.json
# 把 "port": xxx 改为 "port": 10000
# 把 "listen": "127.0.0.1" 改为 "listen": "0.0.0.0"

# 重启 Xray
systemctl restart xray
systemctl enable xray  # 开机自启

# 验证 Xray 在监听
ss -tlnp | grep 10000
```

### Step 5：组装 VLESS 链接并导入客户端

安装完成后 Xray 会输出一个 VLESS 链接，**把其中的 IP 改成你的 VPS 公网 IP，端口改成 20000**：

```
vless://你的UUID@你的VPS公网IP:20000?encryption=none&flow=xtls-rprx-vision&security=reality&sni=www.nvidia.com&fp=chrome&pbk=你的public-key&sid=你的short-id&type=tcp&headerType=none#住宅IP节点
```

**导入客户端**：

| 客户端 | 导入方式 |
|--------|----------|
| **Clash Verge** | 订阅 → 粘贴 VLESS 链接 |
| **V2rayN** | 服务器 → 从剪贴板导入批量 URL |
| **OpenClash（软路由）** | 用原文提供的"openclash格式转换工具"转成 YAML 格式 |
| **Shadowrocket（iOS）** | 扫描 VLESS 链接的二维码 |
| **Surfboard（Android）** | 粘贴 VLESS 链接 |

## 五、验证是否生效

```bash
# 在你的客户端开启代理后，访问：
curl https://ipinfo.io

# 如果输出的 IP 是你家庭宽带的 IP（而不是 VPS 的 IP），说明成功！
{
  "ip": "61.52.44.87",
  "city": "郑州",
  "org": "中国联通",
  ...
}
```

## 六、稳定性加固（推荐做）

### 进程守护（systemd 服务化）

```bash
# === VPS 上：frps 服务化 ===
cat > /etc/systemd/system/frps.service << 'EOF'
[Unit]
Description=FRP Server
After=network.target

[Service]
Type=simple
ExecStart=/opt/frp/frps -c /opt/frp/frps.toml
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable --now frps
```

```bash
# === 板子上：frpc 服务化 ===
cat > /etc/systemd/system/frpc.service << 'EOF'
[Unit]
Description=FRP Client
After=network.target

[Service]
Type=simple
ExecStart=/opt/frp/frpc -c /opt/frp/frpc.toml
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable --now frpc
```

### 自动重连检测（crontab）

```bash
# 板子上每 5 分钟检查 frpc 是否存活
crontab -e
*/5 * * * * pgrep frpc || /opt/frp/frpc -c /opt/frp/frpc.toml &
```

## 七、常见问题排查

| 问题 | 原因 | 解决 |
|------|------|------|
| 客户端连不上 | VPS 防火墙没开放 20000 端口 | `ufw allow 20000/tcp` |
| 连上但无法上网 | Xray 端口没改或没监听 0.0.0.0 | 检查 `/etc/xray/config.json` |
| IP 显示的是 VPS 而不是家宽 | 流量没走 Xray 出去 | 检查 frpc.toml 的 localPort 是否 = Xray 的 port |
| 板子重启后断连 | frpc/Xray 没设开机自启 | `systemctl enable frpc xray` |
| 家宽 IP 变了 | ISP 动态 IP | 考虑申请静态 IP，或用 DDNS |
| Reality 握手失败 | pbk/sid 填错 | 重新安装 Xray 获取新密钥对 |

## 八、安全注意事项

- frp token 用**强密码**，不要用默认值
- Xray 的 VLESS + Reality 是目前**最隐蔽**的协议组合，GFW 难以检测
- VPS 只开放 7000（frp）和 20000（vless）端口，不要关防火墙
- 板子放在家里通风处，低功耗设备一般不会过热

---

> 相关资料：[[搭建100%纯血家庭住宅IP代理]] | B站视频教程：BV11H9rBoEyJ | 工具下载：https://pan.quark.cn/s/bf65c62fddf3
