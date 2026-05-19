我只想看看蓝天 *2025年12月27日 08:02*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/zseIUynf16c7F9ycXhmic9KP1wE7vkSDQNNj66CwDuQXgPeEdZITTQHXgm4TdWKSoHick7Chh37K2Ruv2RHdqiaRA/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

## 一、简介

- • Go-WXPush 是一个基于 golang 开发的微信测试公众号模板消息推送服务，极简且免费
- • 测试公众号每天有10万次额度，消息都是微信公众号原生消息弹窗提示
- • 支持Docker一键部署，基于Go语言的优势内存占用仅几MB
- • 提供消息发送API，所有参数都可以通过接口传入，便于集成到第三方服务
- • 该工具的开源地址：https://github.com/hezhizheng/go-wxpush
- • 该工具的工作原理可参考下图![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/zseIUynf16c7F9ycXhmic9KP1wE7vkSDQLQNu4iaKye9jwbbAsa4oHaiahWMwGicEjmN8sjTqzyxPjzoMeFko2JBEA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

## 二、安装与使用

### 1\. 第一步：注册并配置一个测试微信公众号

- • 微信扫码即可完成注册，获得一个测试公众号的appid、appsecret配置，地址：https://dub.sh/pr7xjqP![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)
- • 扫描测试号二维码，成为测试公众号的用户，获得用户userid![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)
- • 新增通知消息的模板，获得模板ID，标题可以自定义，模板内容只用到content参数，建议设为：`: ）{{content.DATA}} `![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### 2\. Docker安装 Go-WXPush 服务

- • 建议在Docker中部署，提前准备好Docker、docker-compose软件环境
- • 新建docker-compose.yml配置文件，配置内容如下：
```
services:
  go-wxpush:
    image: hezhizheng/go-wxpush:v3
    restart: unless-stopped
    ports:
      - "5566:5566"
    command:
      - "-port"
      - "5566"
      - "-appid"
      - "wxxxx"           # 关键参数1：替换为实际值
      - "-secret"
      - "20xxxx"          # 关键参数2：替换为实际值
      - "-tz"
      - "Asia/Shanghai"
      - "-base_url"
      - "http://server_ip:5566" #可选参数：填写部署机器的域名或ip+端口，点击微信公众号消息会跳转到这个地址，可以注释不传base_url，默认是公共服务地址：https://push.hzz.cool
```
- • 配置完成执行如下命令一键启动
```
docker-compose up -d
```

### 3\. 调用API发送微信公众号消息

- • 接口：http://server\_ip:5566/wxsend
- • 请求方式：GET
- • 请求参数

| 参数名 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| port | String | 否 | 指定启动端口(仅针对命令行) |
| title | String | 是 | 消息的标题 |
| content | String | 是 | 消息的具体内容 |
| appid | String | 否 | 临时覆盖默认的微信 AppID |
| secret | String | 否 | 临时覆盖默认的微信 AppSecret |
| userid | String | 是 | 临时覆盖默认的接收用户 OpenID |
| template\_id | String | 是 | 临时覆盖默认的模板消息 ID |
| base\_url | String | 否 | 临时覆盖默认的跳转 URL |
| tz | String | 否 | 时区(默认东八区) |

- • 使用示例，在postman调用接口发送成功截图如下![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)
- • 微信公众号通知相关示例截图 toast弹窗![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)
	公众号内消息![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)
	点击公众号消息跳转链接查看详情页面![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

## 三、总结

- • Go-WXPush 可以让你轻松实现微信通知的功能，提供消息的触达能力（基本每个人都有且都用微信）
- • 该工具是利用微信公众号测试版功能来实现通知发送的，额度很充足，但可能不那么优雅，只能满足功能性需求，不适合企业或者广泛应用
- • 可使用Docker快速部署，基于golang程序运行高效且轻量，提供的API也易于集成和应用

---

推荐一下个人网站（本文内容如有错漏只会在个人博客更新）：

- 博客：https://blog.luler.top/d/100
- 应用：https://cas.luler.top/
- 导航站：https://nav.luler.top/
- 开源推荐：https://gitshare.luler.top/

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

**微信扫一扫赞赏作者**

工具分享 · 目录

阅读原文

继续滑动看下一个

计算机低手

向上滑动看下一个