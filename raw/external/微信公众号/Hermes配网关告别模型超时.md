轩少玩AI *2026年5月5日 21:33*

## 给Hermes加个网关，解决底层模型限流超时问题

## 最近总是模型限流超时频繁导致Hermes任务失败

这几周，我一直在高频使用Hermes完成各种任务，大模型主力用的 GLM coding plan 里的 GLM 5.1，便宜、响应快，能力强，体验一直挺好的。

但是最近两周，可能是用的人太多了，GLM -5.1频繁触发限流超时，尤其是经常晚上睡觉的时候去跑长任务，等早上才发现因为模型超时，任务没干完，一晚上时间时间全浪费。

为了解决这个问题，我开始研究模型的Hermes模型的fallback机制（就是故障转移，第一个模型挂了自动切换后面的替补模型接着干活）。

一研究，Hermes官方还真的是支持在配置里写fallback的，按照官方文档写好配置，主代理确实没问题了。但子代理还是卡死——Hermes 的 fallback 只对主代理生效，子代理和压缩代理等其他代理都管不到。而压缩失败直接导致Hermes的记忆和上下文乱套，任务没法搞了就。

后来翻 Hermes 文档，官方推荐使用 LiteLLM 做网关统一接管所有模型调用。配了一下午，跑了两周，一个任务都没超时死掉，效果挺好。

## LiteLLM 网关是什么

在 Hermes 和模型服务商之间加一层网关，所有模型调用都走网关，网关干三件事：故障转移、统一管理、监控面板。

就这么简单。

![[file-20260506162223598.png]]

**第一，组内故障转移。**

我把模型分成三组：主力组、压缩组、看图组。主力组里有 GLM-5.1、GLM-5-Turbo、GLM-5，DeepSeek-V4-Pro等一共7个部署，配置成组内随机轮询，超时自动切下一个。 GLM-5.1卡了，网关自动换下一个继续跑任务，我不需要做任何事。

**第二，统一管理。**

所有请求（主代理、子代理）都走网关，改一处全部生效。你有三台电脑跑 Hermes，不用每台都改配置，只需要改网关一处，所有客户端自动生效。

**第三，WebUI 面板。**

网关自带一个 WebUI，浏览器打开 http://网关地址:10086/ui 就能看模型状态、调用日志、成功率。面板上直接显示每个模型的调用次数、成功率、最新错误，一眼就能看出哪个模型挂了。之前翻日志要5-10分钟定位问题，现在看面板10秒就能看出来。

## 具体能干什么

### 场景一：主模型超时自动切备用

你跑个长任务，GLM-5.1 调用50次，中间卡了3次。

没有网关，任务卡住，要么手动切，切回来还得冲在对话，严重了任务还得重新跑。

有网关，GLM-5.1 超时，网关自动fallback，连Hermes 都感觉不到中间出过问题，任务不中断。就这么简单。

### 场景二：子代理超时也被兜住

Hermes 的 fallback 只对主代理生效，子代理超时它管不到。这是 Hermes 文档里明确提到的。

Hermes 调用子代理非常频繁——长任务、代码审查、并行研究，都是主代理开子代理去干。子代理超时，主代理的 fallback 根本够不着。

更麻烦的是压缩模型。Hermes 用压缩模型做长对话摘要，压缩模型挂掉，摘要失败，上下文直接乱套，后面所有任务都会出问题。Hermes 原生配置也不支持给压缩模型单独配 fallback。

但所有请求走网关，子代理和压缩模型超时照样自动切。

在网关里单独给压缩模型配一个组，Hermes 客户端配置里把 compression 模型指向网关，子代理超时被网关兜住。

### 场景三：多台局域网电脑只改一处就全生效

所有 Hermes 客户端的 base\_url 都指向网关，模型配置只在网关写一次，网关一处改动，所有客户端自动同步。

### 场景四：加新模型客户端不用动

在网关的模型列表里加一行配置，重启网关服务，所有客户端自动能调用新模型，不需要改任何客户端配置。

## 配置要注意什么

说真的，配置这块有两个坑，我替你们踩过了。

### 第一，超时参数是两个，不是一回事

网关有两个超时参数，很多人容易搞混。而且应用场景不一样。

**timeout / request\_timeout：** LiteLLM 网关内部的超时阈值。timeout 控制单次请求超时我设 30 秒，request\_timeout 控制整个重试周期超时我设 300 秒。模型单次请求 30 秒没响应，网关就切下一个模型。

**gateway\_timeout：** Hermes 客户端等网关的超时。这个我设成 600 秒（10分钟）。

为什么设 10 分钟？我在Hermes配置文件里明确要求主代理给子代理分任务，每个子代理必须在 5 分钟内完成，如果子代理 5 分钟都干不完，说明任务分得太大了，应该拆小。网关内部重试加上模型切换，10 分钟足够兜住一次完整的子代理任务。

这两个超时不一回事。timeout 是网关内部的故障转移判定阈值，gateway\_timeout 是客户端能给子代理的最大时间窗口。

### 第二，模型分三组，组内互兜但不跨组

我的配置分成三组：

**hermes-main：** 主力组，GLM-5.1、GLM-5-Turbo、GLM-5、DeepSeek-V4-Pro ×2（不同中转）。

**hermes-compression：** 压缩组，配置3个falsh模型，专门处理长文本压缩。

**hermes-vision：** 看图组，3个视觉模型，标记 supports\_vision。

组内配置成 simple-shuffle 随机轮询，超时自动切下一个。但组间不设 fallback，主力组挂了不会切到压缩组，压缩组挂了不会切到看图组。

为什么这么分？

因为不同组的用途不一样，跨组 fallback 没意义。

当然，如果整组模型全部都挂了，任务还是会失败。但这种情况我高强度跑了两周还没遇到过。

### 第三，WebUI 面板别忘开

LiteLLM 自带 WebUI，但很多人不知道。

配置文件里加上

```
litellm_settings: { drop_params: true, set_verbose: false }
```
，启动网关后浏览器访问 /ui 就能看面板。

面板上有三个页面：Models 看模型状态，Logs 看调用日志，Metrics 看成功率。任务卡了，先看面板一眼，比翻日志快多了。

## 跟别的方案比

### vs 在 Hermes 配置里写死 fallback

Hermes 原生支持 fallback，你可以配置主模型超时切备用模型。

但 fallback 只能管主代理，子代理的超时它管不到。LiteLLM 网关是统一接管所有请求，主代理、子代理一视同仁，超了就切。你只需要改网关一处配置，所有客户端自动生效。

### vs NewAPI

NewAPI 是国产的开源网关，界面漂亮，功能也全。

NewAPI 的重试策略是固定次数重试同一个模型，如果模型一直超时就卡住了。LiteLLM 是切到下一个模型重试，对间歇性超时更有效。

LiteLLM 和 Hermes 兼容性好，问题是解决了才知道这么配。

## 怎么上手

三步走：装网关、配网关、改 Hermes 配置。每步给你一段可以直接贴给AI的提示词，里面包含我实际用的配置结构（隐私信息已替换），你按自己情况改一下就能用。

### 第一步：装 LiteLLM

把下面这段贴给AI：

```
帮我在服务器（或本机）上安装 LiteLLM 代理网关。

1. 执行：pip install 'litellm[proxy]'
2. 安装完成后验证：litellm --version
3. 不要做任何其他操作，只安装和验证。

服务器ip：X.X.X.X
用户名：XXX
密码：XXX
```

### 第二步：创建网关配置文件

分两部分：先给AI一段指令让它创建配置，再把你的API信息贴在下面让它填进去。

**第一部分：贴给AI的指令——**

```
帮我在服务器上创建 LiteLLM 网关配置文件 /opt/litellm/config.yaml。

配置结构要求：

1. model_list 分三组：
   - hermes-main（主力组）：所有主力推理模型放在这个组，同一个组的模型用同一个 model_name，组内 simple-shuffle 随机轮询，超时自动切下一个
   - hermes-compression（压缩组）：快模型放在这个组，压缩不需要强推理能力，只要快和便宜
   - hermes-vision（视觉组）：能看图的模型放在这个组，每个模型必须在 model_info 里写 supports_vision: true

2. 每个部署的字段：
   - model_name: 组名（同组用同一个）
   - litellm_params.model: openai/模型名（LiteLLM 要求加 openai/ 前缀）
   - litellm_params.api_base: 服务商地址
   - litellm_params.api_key: os.environ/环境变量名（密钥从环境变量读，不硬编码）
   - litellm_params.order: 优先级数字（1最优先，数字越大优先级越低）
   - 压缩组和视觉组需要额外写 model_info（max_tokens、supports_vision 等）

3. 全局路由设置：
   router_settings:
     routing_strategy: simple-shuffle
     num_retries: 1            # 超时切下一个模型，不重试同一个
     allowed_fails: 5          # 连续失败5次才标记down
     cooldown_time: 30         # down了冷却30秒再试

4. 降级设置：
   litellm_settings:
     fallbacks:
       - "hermes-main": ["hermes-compression"]      # 主力组全挂→压缩组兜底
       - "hermes-vision": ["hermes-main"]            # 视觉组全挂→主力组兜底
     context_window_fallbacks:
       - "hermes-compression": ["hermes-main"]       # 压缩组上下文不够→主力组兜底

5. 网关管理：
   general_settings:
     master_key: os.environ/LITELLM_MASTER_KEY       # 网关管理密钥
     database_url: os.environ/DATABASE_URL            # 可选，不配就用SQLite

6. 创建完成后：
   - 在 /opt/litellm/ 下创建 .env 文件，写入所有环境变量
   - 启动网关：litellm --config /opt/litellm/config.yaml --port 10086
   - 验证：curl http://localhost:10086/health/liveliness，返回 "I'm alive!" 就成功了

7. 下面是用户的API信息，请按上面的结构要求填进去。

我的API信息如下(这部分按你实际的来)：

服务商1（智谱GLM直连）：
  api_base: https://open.bigmodel.cn/api/coding/paas/v4
  api_key环境变量名: GLM_API_KEY
  可用模型: glm-5.1（主力）, glm-5-turbo（主力）, glm-5（主力）, glm-4.5-air（压缩）, glm-4.6v-flash（看图）

服务商2（中转站A）：
  api_base: https://你的中转站A地址/v1
  api_key环境变量名: RELAY_API_KEY
  可用模型: glm-5.1, deepseek-v4-pro（主力）, deepseek-v4-flash（压缩）, doubao-seed-2-0-pro-260215（看图）

服务商3（中转站B）：
  api_base: https://你的中转站B地址/v1
  api_key环境变量名: RELAY2_API_KEY
  可用模型: glm-5.1, deepseek-v4-pro（主力）, deepseek-v4-flash（压缩）, doubao-seed-2-0-pro（看图）

分组要求：
  hermes-main: glm-5.1(order:1) + glm-5-turbo(order:2) + glm-5(order:3) + 中转站A的glm-5.1(order:4) + 中转站B的glm-5.1(order:5) + 中转站A的deepseek-v4-pro(order:6) + 中转站B的deepseek-v4-pro(order:7)
  hermes-compression: glm-4.5-air(order:1) + 中转站A的deepseek-v4-flash(order:2) + 中转站B的deepseek-v4-flash(order:3)
  hermes-vision: glm-4.6v-flash(order:1) + 中转站A的doubao-seed-2-0-pro-260215(order:2) + 中转站B的doubao-seed-2-0-pro(order:3)
```

你只要把「你的中转站A地址」「你的中转站B地址」和你实际拥有的模型名改一下就行。如果只有一个服务商，就把多余的删掉，每组至少2个部署才能故障转移。

### 第三步：改 Hermes 配置

把下面这段贴给AI。这段是 Hermes 客户端连接网关的标准配置，把地址，端口和密钥换成你自己的：

```
帮我修改 Hermes 客户端的配置文件 ~/.hermes/config.yaml，按下面的模板修改。不要删除文件里其他已有的配置，只覆盖下面列出的字段。

---

## 以下是需要修改的部分：

model:
  provider: custom
  default: hermes-main
  base_url: http://你的网关地址:10086/v1       # 【需替换】你的LiteLLM网关地址
  api_key: os.environ/LITELLM_MASTER_KEY      # 网关的master_key

# 不要设 fallback_model —— LiteLLM网关已在服务端实现降级

auxiliary:
  vision:
    model: hermes-vision
    base_url: http://你的网关地址:10086/v1
    api_key: os.environ/LITELLM_MASTER_KEY

  web_extract:
    model: hermes-main
    base_url: http://你的网关地址:10086/v1
    api_key: os.environ/LITELLM_MASTER_KEY

  compression:
    model: hermes-compression
    base_url: http://你的网关地址:10086/v1
    api_key: os.environ/LITELLM_MASTER_KEY

  session_search:
    model: hermes-compression
    base_url: http://你的网关地址:10086/v1
    api_key: os.environ/LITELLM_MASTER_KEY

gateway_timeout: 600  # 客户端等网关最多10分钟

---

## 修改完成后：

1. 不要重启 Hermes，等我手动操作
2. 先验证网关连通性：curl http://你的网关地址:10086/health/liveliness
```

改完重启 Hermes，所有请求都走网关了。超时自动切，不用手动干预。

## 不吹不黑

网关不是银弹，该超时还是会超时，只是超时了能自动切，不用你手动重启。

但网关也有两个小问题：

**第一，多了一层，调试时多一个地方查日志。**

之前任务卡了，只需要看 Hermes 日志。现在得先看网关日志，确定是网关的问题还是模型的问题。不过 WebUI 面板能帮上忙，看一眼面板就知道是不是模型挂了。

**第二，LiteLLM 配置语法偶尔有小坑。**

我一开始没设 drop\_params，跑任务的时候老报错，翻日志翻了半个多小时才查出来。还有 set\_verbose，不设成 false 的话，日志会打一堆，控制台直接刷屏。这些小坑官方文档都没写，得自己踩。。

我踩完坑给你们趟平了，你们直接照着配置就行。

## 收尾

网关不解决所有问题，但解决最烦的那个——模型一挂你就干等着。

你跑个长任务，中间卡了三次，但你完全没感觉，任务照样跑完。这种感觉，真的挺爽的。

这让我想起以前用电饭煲煮饭，老是担心跳闸。后来买了个带断电保护的插座，那种安心感，有点像。

我是轩少，替你把AI的坑踩完，你跟着做就行。下期见。

---

**合规声明：** 以上全是我的个人部署环境，不涉及生产数据。配置时记得留意服务商的使用条款。

**附录：参考文档**

- • LiteLLM 官方文档：https://docs.litellm.ai/docs/proxy/quick\_start
- • LiteLLM 路由配置：https://docs.litellm.ai/docs/routing
- • Hermes 官方文档：https://hermes-agent.nousresearch.com/docs
- • Hermes GitHub：https://github.com/nousresearch/hermes