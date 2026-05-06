*2026年4月29日 09:37*



说到DDD领域驱动设计，都有点蹭热点的感觉。这几年后端圈子逢人必提架构，提架构必提DDD，感觉DDD的中文翻译不像是“领域驱动设计”而是“对对对”，但是笔者作为一名研发大头兵在写代码的时候经常有种感觉“道理我都懂，但是我还是迷糊”的感觉，总是深感落地困难，在经历了多个DDD项目落地实践之后，笔者总结一下作为一名一线研发对领域驱动的理解，希望对各位有所帮助，此外 **领域驱动设计的实现并非是一套通用的准则，不同项目可能在具体落地方面略微有所变化，本文只是尽量归纳共性**


搭建一个DDD项目，在最开始就要定义好各个模块的职责和POM依赖关系，笔者所在公司一般利用alibaba-Cola的maven骨架快速创建DDD项目结构，cola官网给出了两张图，可以作为一般DDD项目的分层指南：
![[file-20260430182253603.png]]
![[file-20260430182303057.png]]

下面我将对上图中的每一层进行详细解释，以及我们在日常开发的时候应该把什么样的代码放到这一层里面。

领域驱动设计，从名字来看最重要的就是领域，领域，在我看来就是边界。在早期做小项目的时候，建包的时候往往建一个叫做entities的包，这个包里面放的是都是一些对象，这些对象有两个特点：

> （1）类除了属性就是get/set，都是简单类 （2）这个包或者模块下面只会有常量或者简单类，不会存放接口，这个包或者模块里面完全没有“行为”

但是如果仔细想想这个分包存在不合理之处。不合理之处在于贫血模型过多，大量的类只有属性没有行为，这个分包就是一个存放简单类的大集合，这种不合理之处在于和面向对象设计的思路相悖。

总的来说在DDD的设计理论下，这一层是毫无疑问最重要的一层，领域划分有一整套的方法论，领域划分的好不好直接决定了后期系统的可维护性高不高，这里笔者看了很多讲解DDD领域划分的文章，给我的感觉是看起来很有用，名词都很高端，但是实际还是用不好，笔者认为领域建模是需要大量训练的，不是说了解了几个名词例如“事件风暴”、“故事地图”，“用例分析”，“从战略到战术”就自然成为领域大师了的。

概括的说这一层包含下述要素：

![[file-20260430182320548.png]]
具体来说这一层适合承载下述内容：

- 事件：领域内部发生了某些事件，需要对相关的领域进行事件传播，传播的就是事件，比如一个下单动作，就会发送一个下单事件，告知仓储领域锁定库存，所以需要定义一些事件对象。
- 实体和值对象：
	**值对象：** 值对象用于描述领域里某个方面而本身没有概念标识(无ID)的对象。值对象 不可变性：值对象一旦创建完成后就不可以修改；唯一方法是重新创建一个对象（所以值对象咱们不需要定义set方法） 可替换性：属性相同的两个值对象是完全等价的，在使用是可相互替换 **实体：** 实体是重要的领域概念，实体的3个主要特征：ID: 唯一的身份标识。ID相同代表实体是同一个 Lifecycle: 实体的生命周期具有连续性 Status: 生命期经历不同的状态（例如常见的订单状态）
- 聚合：一般由多个实体和值对象组成，具备行为
- 工厂：一个聚合体内部有多个实体和值对象这样的话创建聚合体就需要一个工厂方法来简化复杂的创建过程。
- 服务接口：领域内部一定有各种活动比如我们的订单域，一定会有下单、结算、支付等服务接口，这些接口的实现也是在这一层实现的，但是domain层其实用不依赖其他任何层，所以这和个服务接口的实现都是无状态的。
- 存储接口：聚合体有行为，但是它对实体和值对象的修改需要具备持久化的能力，所以这里需要定义数据持久化的部分接口，存储聚合根的状态。（这里只定义接口实现交给基础设施层来实现）
- 领域访问接口：COLA架构推荐领域与领域之间的数据访问应该解耦，需要使用网关来进行访问
![[file-20260430182335978.png]]
总结：DDD的domain层需要具备下述特点

- 不依赖其他任何模块
- 这个模块可以有业务逻辑，但是这些业务逻辑是脱离基础设施的，也就是说这些逻辑不依赖于你使用Mysql或者Oracle而改变逻辑实现，具体使用那种技术中间件，这是基础设施层的职责。
- 这个模块的类不是都是贫血模型，是具有行为的。

这里我还想补充一下这一层的建包规范，更推荐按照下图右边的方式分包，领域建议做隔离，否则时间一个整个原本很顺畅的调用链路就逐步会腐化成网状混乱调用。

![[file-20260430182348691.png]]
### 2.2 infra层 （基础设施层，和中间件打交道）

对于基础设施层，理想情况下就是如果整个项目需要换用另一套技术方案，比如把MQ从RocketMQ换成Kafka，把Mysql换成Oracle，其他层应该毫无感知，只需重写这一层即可，也就是说这一层是纯技术向的一层，也就是说 **领域层专注于业务，基础设施层专注于技术** 。注意的是 **这一层只是对领域层的接口实现，所以只需要依赖领域层**

这一层则一般承载下述内容

- **数据访问层的全部代码，例如 mybatis的mapper接口，xml文件**
- **工具类**
- **实现领域层定义的仓储接口、服务接口、网关接口**
- **模型转换，MapStruts**
- **Spring Configuration配置类**

应用层（Application Layer）：主要负责获取输入，组装上下文，调用领域层做业务处理，如果需要的话，发送消息通知等。层次是开放的，应用层也可以绕过领域层，直接访问基础实施层；app层依赖了领域层也依赖了基础设施层，所以在实际开发中往往扮演“协调者”的角色，对于这一层往往存放下述内容

- 通过调用基础设施层的能力或者领域层的接口完成Client层（如果有）定义的所有接口的代码实现
- 通过调用基础设施层的能力或者领域层的接口完成Controller接口或者HSF接口的实际逻辑的实现

这一层同时依赖基础设施和domain层，所以这里应该是写的是与技术无关但是与核心业务强相关的逻辑。

适配层（Adapter Layer）：负责对前端展示（web，wireless，wap）的路由和适配，对于传统B/S系统而言，adapter就相当于MVC中的controller； **这一层应该只依赖app层** 。这一层的逻辑大部分都是调用app层的方法来实现。

以多次ddd项目实践下来这一层 **逻辑非常轻** ，一般情况下这一层会存放下述内容

- **Controller接口**
- **统一异常处理类**
- **参数检验（@Validated）**
- **controller的拦截器（Interceptor） 过滤器等**
- **定时任务**
- **业务自定义切面**

这一层的分包其实没有什么规律，一般按照实际业务场景来，笔者经历一个三端项目，也就是说服务端同时对接车机、app、H5三个展示端，所以分包就按照端类型分包

![[file-20260430182413527.png]]

这一层一般并不是必须的，这层的目的是打包时打出一个轻量级jar包，然后类似Dubbo这种框架，可以直接依赖然后进行RPC调用，也就是说这一层主要目的就是提供当前项目对外接口的SDK，所以 **这一层也是独立的，不与其他任何模块进行依赖** 。所以这个模块应该以接口和DTO为主，具体实现应该在APP层来实现。

所以哪些适合定义在这一层呢：

- **RPC 请求的响应模型和请求模型即DTO**
- **RPC 请求的接口定义**
- **部分服务消费者需要使用到的枚举**
- **对项目服务消费者侧的错误码**

分包的话，这一层也比较简单，可以参考下图进行分包

![[file-20260430182423238.png]]
笔者所参与的多个DDD项目，有时候会将Client层和Adapter层直接合并，所以正如本节开头所说的这层并不是必须的

这个模块比较简单，就是存放springBoot项目的启动类和配置文件。这个模块有三个作用

- **突出显示启动类的位置**
- **这个模块会依赖其他所有模块，所以很适合做maven打包入口**
- **因为依赖了其他所有模块所以适合在此模块编写单元测试代码**
- **可以在这个启动类上添加全局配置 （类似：@EnableXXX @ComponentScan...）**

相信通过我上面这些描述，你可能还是会觉得虚无缥缈，下面我们将举一个例子，以例子来说明上面的几个重要概念以及怎么落地DDD

现在有个对客侧的工单管理系统，需求背景是这样的

> 某个系统在交付给几个主力客户之后，为了保证服务质量，客户在发现产品问题之后可以在工单系统中发起问题工单，用户填写工单内容以后，发起工单处理流程，工单根据工单类型会有不同的人进行处理填写处理结果，处理完成之后需要发起工单的人点击确认或者驳回，驳回之后需要工单处理人员再次处理直到工单被客户点击确认之后完成工单处理。

用户的需求可能描述的就是这么简单且模糊，接下来我们要从这些描述里面抽象出来关键部分

（1）工单：这是一个明显的实体，因为有明显的生命周期和状态 （2）工单内容：这是一个值对象，大致包含了工单类型和工单文字描述 （3）工单状态：这是一个值对象（从技术层面上来说就是个枚举） （4）工单的处理结果：这是一个值对象，包括处理人、处理时间、处理结果描述等信息 （5）工单发起人和处理人：值对象

接下来分析这个需求活动中有哪些行为 （1）发起工单 （2）处理工单 （3） 驳回工单

根据上面的信息我们可以初步定义下面的工单实体，受制于篇幅限制不适合张贴太多代码，值对象已经在代码注释中标注

```
@Data
public class WorkOrder {

    
     * 工单唯一id
     */
    private String workOrderId;
    
     * 父工单id
     */
    private String parentOrderId;

    
     * 发起人id
     */
    private String initiatorId;

    private Date startTime;
    private Date processTime;
    private Date completeTime;
    private Date rejectTime;

    
     * 工单内容： 值对象：包含 图片、工单类型、文字内容等
     */
    private WorkOrderContent content;

    
     * 工单处理状态： 值对象 枚举
     */
    private WorkOrderStatus workOrderStatus;

    
     * 工单处理结果： 值对象，包含发起人，处理人，处理结果，处理意见等内容
     */
    private WorkOrderHandleResult workOrderHandleResult;

    private WorkOrder(Date startTime, String workOrderId, String initiatorId, WorkOrderContent content, WorkOrderStatus workOrderStatus, WorkOrderHandleResult workOrderHandleResult) {
        this.workOrderId = workOrderId;
        this.initiatorId = initiatorId;
        this.content = content;
        this.workOrderStatus = workOrderStatus;
        this.workOrderHandleResult = workOrderHandleResult;
        this.startTime = startTime;
    }

    
     * 发起工单
     *
     * @return WorkOrder
     */
    public static WorkOrder start(String initiatorId, WorkOrderContent content) {
        DateTimeFormatter chargeSeqDateFormatter = DateTimeFormatter.ofPattern("yyMMddHHmmssSSS");
        String wordOrderId = "WorkOrderID" + chargeSeqDateFormatter.format(LocalDateTime.now())
                + new DecimalFormat("000").format(new SecureRandom().nextInt(999));
        WorkOrderStatus workOrderStatus = WorkOrderStatus.INITIAL;
        return new WorkOrder(new Date(), wordOrderId, initiatorId, content, workOrderStatus, null);
    }

    
     * 处理工单
     */
    public void handle() {
        this.workOrderStatus = WorkOrderStatus.HANDLEING;
        this.processTime = new Date();
    }

    
     * 处理完结
     *
     * @param workOrderHandleResult 工单处理结果
     */
    public void finish(WorkOrderHandleResult workOrderHandleResult) {
        this.completeTime = new Date();
        this.setWorkOrderHandleResult(workOrderHandleResult);
        this.workOrderStatus = WorkOrderStatus.COMPLETED;
    }

    
     * 工单驳回 这里重新启动一个工单
     */
    public WorkOrder reject() {
        if (!workOrderStatus.equals(WorkOrderStatus.COMPLETED)) {
            
            return null;
        }
        String parentWorkOrderId = workOrderId;
        Date startTime = getStartTime();
        DateTimeFormatter chargeSeqDateFormatter = DateTimeFormatter.ofPattern("yyMMddHHmmssSSS");
        String newWorkOrderId = "WorkOrderID" + chargeSeqDateFormatter.format(LocalDateTime.now())
                + new DecimalFormat("000").format(new SecureRandom().nextInt(999));
        WorkOrder workOrder = new WorkOrder(startTime, workOrderId, initiatorId, content, WorkOrderStatus.HANDLEING, null);
        workOrder.setParentOrderId(parentOrderId);
        workOrder.setRejectTime(new Date());
        return workOrder;
    }

}
```

发起工单的时候明显还会有对应的事件发生，比如工单状态变更的时候需要进行站内信或者邮件通知,可以做如下设计

之后我们可以设计服务接口如下：

```
@Service
public class WorkOrderServiceImpl implements WorkOrderService {
    @Autowired
    WorkOrderRepository workOrderRepository;

    @Autowired
    WorkOrderEventRepository workOrderEventRepository;

    @Override
    public WorkOrder startOrder(String userId, WorkOrderContent workOrderContent) {
        WorkOrder order = WorkOrder.start(userId, workOrderContent);
        workOrderRepository.save(order);
        workOrderEventRepository.sendWorkOrderEvent(new WorkOrderEvent(order.getWorkOrderId(), order.getWorkOrderStatus().getValue()));
        return order;
    }

    @Override
    public void processOrder(WorkOrderHandleResult workOrderHandleResult, String handlerId, String workOrderId) {
        WorkOrder workOrder = workOrderRepository.get(workOrderId);
        workOrder.handle();
        workOrderEventRepository.sendWorkOrderEvent(new WorkOrderEvent(workOrder.getWorkOrderId(), workOrder.getWorkOrderStatus().getValue()));
        workOrderRepository.save(workOrder);
    }
}
```

服务接口层的代码实现依赖仓储接口，在domain模块中仓储接口可以做如下定义，具体实现则由基础设施层实现

```
public interface WorkOrderRepository {  
  
    void save(WorkOrder workOrder);  
  
    WorkOrder get(String workOrderId);  
  
}

public interface WorkOrderEventRepository {  
  
    void sendWorkOrderEvent(WorkOrderEvent workOrderEvent);  
  
}
```

至此领域层也是最重要的一层的内容设计完毕，其余层的代码设计围绕领域层进行代码填充即可。本文由于篇幅仅介绍核心层领域层的设计思路。

> 基于 Spring Cloud Alibaba + Gateway + Nacos + RocketMQ + Vue & Element 实现的后台管理系统 + 用户小程序，支持 RBAC 动态权限、多租户、数据权限、工作流、三方登录、支付、短信、商城等功能
> 
> - 项目地址：https://github.com/YunaiV/yudao-cloud
> - 视频教程：https://doc.iocoder.cn/video/

本文主要对DDD项目落地的一些经验进行了分享，作为一名一线研发如果领导要求使用DDD做项目开发，对于研发而言其实最重要的就是要明白我写一个功能到底怎么写，到底把类放在哪个模块才不会到导致代码腐坏，本文则针对这方面提出了部分建议。笔者认为，学习DDD是很有必要的，DDD的亮点是彻底贯彻了面向对象的设计思路，通过划分领域实现了“高内聚 低耦合” 的目标，但是实际开发中如果项目并不是很大很复杂，并不是一定要套用上面的四层架构，此外即使使用DDD作为项目开发，有时也不需要应用所有的DDD概念到项目中，比如本文给的例子就没有用到“工厂”，此外实体WorkOrder也直接充当了聚合体的角色，这是因为在需求范围内并不需要上更多的概念来徒增代码复杂度。总之笔者认为没有最好的架构，如果能通过合理编排层次实现代码解耦，代码易读，这就是一种好设计，好架构。
