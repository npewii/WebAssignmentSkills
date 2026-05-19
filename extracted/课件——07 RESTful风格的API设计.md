<!-- Slide number: 1 -->
# 252602 WEB项目应用
RESTful风格的API设计
2026-4-11

<!-- Slide number: 2 -->
本次课内容

<!-- Slide number: 3 -->
API概述
什么是API
API的核心价值
API的组成

<!-- Slide number: 4 -->
观察函数的注释

![](内容占位符6.jpg)
函数的功能说明
函数的参数说明
函数的异常抛出说明
函数的返回值说明

### Notes:

<!-- Slide number: 5 -->
写注释，还是不写注释？

不写注释
你可能遇到的麻烦
| 维度 | 体验描述 |
| --- | --- |
| 调用时 | 输入?calc(?后，IDE 提示只有?mixed calc(mixed $a, mixed $b, mixed $c)，你完全不知道?$a?是单价还是数量，$c?是 true 还是 false 代表什么。 |
| 看源码时 | 必须从头到尾通读?if ($c)?里面的逻辑，才能反推出?$c?是一个“是否打折”的布尔值。 |
| 维护时 | 三个月后老板说 VIP 打 8 折，你不敢直接改?0.9，因为你不知道这个函数是不是还在积分兑换的场景里被调用了。 |
| 类型风险 | 万一同事传了字符串?"abc"?进去做乘法，PHP 只会在运行时报 Warning，不会提前报错。 |

![](内容占位符8.jpg)

### Notes:

<!-- Slide number: 6 -->
结论：写注释好处多多！
写注释，还是不写注释？

写注释
你将获得的收益
| 维度 | 体验描述 |
| --- | --- |
| 调用时（智能感知） | 输入?calculateOrderLineTotal(?后，IDE 直接弹出浮窗：1. 参数一叫?$price?是 float2. 参数三叫?$isVipMember?是 bool你连源码文件都不用打开就知道怎么传参。 |
| 类型安全 | 如果你试图传一个数组?calculateOrderLineTotal([])?，IDE 会在你按下运行键之前就用红色波浪线警告你类型错误。 |
| 维护重构 | 想要改成 VIP 打 8 折？你可以在 IDE 里右键 ->?Find Usages?查出所有调用处，评估影响面后再改。 |
| 生成文档 | 运行?phpDocumentor，这一段注释会自动变成网页上的一页?API Reference，新人或前端同事可以直接看网页，不用读 PHP 源码。 |

![](内容占位符5.jpg)

### Notes:

<!-- Slide number: 7 -->
什么是API
注释
API
你能请求什么？
你需要提供什么？
你会得到什么？

![](内容占位符5.jpg)
软件之间通信
函数或类之间通信

<!-- Slide number: 8 -->
API产生的驱动力

<!-- Slide number: 9 -->
API的主要类型

![](内容占位符8.jpg)

<!-- Slide number: 10 -->
作业一

![](内容占位符8.jpg)

![](内容占位符6.jpg)

<!-- Slide number: 11 -->
API的核心价值

<!-- Slide number: 12 -->
API的核心价值

<!-- Slide number: 13 -->
API的组成：请求和响应

![](内容占位符4.jpg)

![](内容占位符9.jpg)

<!-- Slide number: 14 -->
案例分析：

![](内容占位符4.jpg)

![](内容占位符9.jpg)

<!-- Slide number: 15 -->
案例分析：

![](内容占位符8.jpg)

<!-- Slide number: 16 -->
作业二

![](内容占位符6.jpg)
| 问题 | 答案 |
| --- | --- |
| 如何请求深圳的天气？ |  |
| 如何请求以华氏度显示的广州天气？ |  |
| 请求成功时返回什么状态码？ |  |

### Notes:

<!-- Slide number: 17 -->
RESTful规范
RESTful规范的核心原则
统一接口的四个子约束

<!-- Slide number: 18 -->
何为RESTful

### Notes:

<!-- Slide number: 19 -->
RESTful 的 6 大核心原则

![](内容占位符6.jpg)

<!-- Slide number: 20 -->
统一接口的 4 个子约束——资源识别（URI 表示资源）
URI 资源识别原则：
使用复数名词：/users 而非 /user
使用小写字母 + 连字符：/order-items 而非 /orderItems
多级资源：/users/123/orders（用户 123 的订单）

![](图片6.jpg)

服务器端要准备
getUser、deleteUser、getUserList和updateUser（方法）

### Notes:

<!-- Slide number: 21 -->
统一接口的 4 个子约束——通过表述操作资源
正确表述
违反约束的做法
POST /api/createuser
BODY: userId = 123 username = ‘张三’userEmail= ‘zhangs@example.com’
分析：
后端有一个createUser的函数来处理记录的插入
若后端重构代码，把这个函数名改成了?handleUser，所有客户端代码全部报 404 报错。
POST /v1/users
说明
POST——插入记录
JSON字符串——记录内容

![](内容占位符5.jpg)
只用一个地址（URL）代表一类资源
用 HTTP 的动词（GET/POST/PUT/DELETE）代表你想干嘛
用 Body（JSON）代表你想让它变成什么样。

<!-- Slide number: 22 -->
RESTful风格的优势

![](内容占位符8.jpg)
前端不用管后端如何实现
前端只需知道：自己要干什么（修改——put，部分修改——patch，插入——post，查询——get），自己要处理什么资源（users，scores，tasks，courses），即可写好请求
耦合度低
前端要知道后端如何实现（插入——createUser，修改——updateUser，删除——deleteUser，查询——getUser）
后端暴露了很多细节，有安全隐患
解耦困难：后端一改，前端就必须改。
只用一个地址（URL）代表一类资源
用 HTTP 的动词（GET/POST/PUT/DELETE）代表你想干嘛
用 Body（JSON）代表你想让它变成什么样。

### Notes:

<!-- Slide number: 23 -->
如何你是一位前端工程师，你希望

![](内容占位符8.jpg)
选哪种？

<!-- Slide number: 24 -->
统一接口的 4 个子约束——自描述消息
HTTP 方法（GET/POST/PUT/DELETE）
状态码（200/404/500）
请求头（Content-Type、Accept）
 响应头（Cache-Control）

![](内容占位符9.jpg)

<!-- Slide number: 25 -->
HTTP方法的使用案例

![](内容占位符11.jpg)

<!-- Slide number: 26 -->
作业三

![](内容占位符4.jpg)
| 操作 | HTTP方法 |
| --- | --- |
| 获取用户列表 |  |
| 创建新用户 |  |
| 更新用户完整信息 |  |
| 修改用户密码 |  |
| 删除用户 |  |

<!-- Slide number: 27 -->
状态码

![](内容占位符7.jpg)

![](内容占位符17.jpg)

<!-- Slide number: 28 -->
作业四：状态码的使用

![](内容占位符5.jpg)
| 场景 | HTTP状态码 |
| --- | --- |
| 成功获取用户信息 |  |
| 创建新课程成功 |  |
| 删除学生成功（无返回数据） |  |
| 请求参数缺少name字段 |  |
| 未提供Token |  |
| 已登录但无权查看成绩 |  |
| 查询的用户不存在 |  |
| 邮箱格式校验失败 |  |
| 触发限流 |  |
| 数据库连接失败 |  |

<!-- Slide number: 29 -->
HATEOAS（超媒体驱动）

<!-- Slide number: 30 -->
作业五

![](内容占位符4.jpg)
| RPC风格 | RESTful风格 |
| --- | --- |
| GET /getStudent?id=123 |  |
| POST /createCourse |  |
| POST /updateScore |  |
| GET /getStudentScores?studentId=123 |  |
| POST /deleteTeacher |  |

<!-- Slide number: 31 -->
RESTful风格的API设计
客户端-服务器分离
无状态
可缓存
统一接口
API文档编辑工具的使用

<!-- Slide number: 32 -->
客户端-服务器分离
实践建议
高校教务管理系统的场景分析
前后端分离是可行的；
前端选用vue
后端选用PHP

前后端独立开发和部署
客户端不关心数据存储细节
服务器不关心界面展示逻辑

<!-- Slide number: 33 -->
无状态

![](内容占位符7.jpg)

<!-- Slide number: 34 -->
对于认证场景需 进一步分析
系统为学校内部系统，机房托管，网络环境可控
用户规模有限，通常不超过几万人
并发程度不高，选课等高峰期有规律可预估
结论
        对于高校教务管理系统，Session 是完全可行的方案，不必为了追求 “纯粹 RESTful”而引入不必要的复杂度。

<!-- Slide number: 35 -->
可缓存（Cacheable）

![](图片5.jpg)

### Notes:

<!-- Slide number: 36 -->
系统各功能模块的缓存需求分析

![](图片5.jpg)

![](内容占位符4.jpg)

![](图片10.jpg)
缓存的实现
1. 服务器端在响应时给出缓存标识；
2. 客户端在提出下一次请求时，如果查询条件相同，就根据上一次响应标识，决定是否使用缓存（本地缓存未过期；已过期发请求去问服务器是否可以使用缓存）

<!-- Slide number: 37 -->
统一接口——资源标识

![](内容占位符4.jpg)

<!-- Slide number: 38 -->
统一接口——请求头设计

![](内容占位符6.jpg)

<!-- Slide number: 39 -->
统一接口——响应设计
响应格式
响应头

![](内容占位符8.jpg)

![](内容占位符10.jpg)

<!-- Slide number: 40 -->
API文档编辑工具推荐——Apifox

![](内容占位符8.jpg)

![](图片10.jpg)

<!-- Slide number: 41 -->
接口管理

![](内容占位符4.jpg)

![](内容占位符4.jpg)

![](内容占位符4.jpg)

![](内容占位符4.jpg)

<!-- Slide number: 42 -->
用户登录接口

![](内容占位符4.jpg)

![](图片6.jpg)

![](内容占位符4.jpg)

<!-- Slide number: 43 -->
用户登录接口

![](图片14.jpg)

![](内容占位符12.jpg)

<!-- Slide number: 44 -->
用户登录接口

![](图片10.jpg)

![](内容占位符8.jpg)

<!-- Slide number: 45 -->
作业六（登录必做，其他选做）

![](内容占位符12.jpg)

<!-- Slide number: 46 -->
# 作业一~六的提交要求（第七次课）
提交内容（合并7张图片为一个文件，允许是图片或pdf）
作业一 表7-11截图；
作业二 表7-12截图；
作业三 表7-13截图；
作业四 表7-14截图；
作业五 表7-15截图；
作业六 在Apifox完成登录接口的API文档预览截图
作业六在Apifox完成登录接口的API文档共享地址
提交标识
图片显眼位置写入学号；方法的注释写入学号。

### Notes:

<!-- Slide number: 47 -->
