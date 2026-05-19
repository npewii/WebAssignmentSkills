<!-- Slide number: 1 -->
# 252602 WEB项目应用
PDO连接工具类的构建
2026-4-28

<!-- Slide number: 2 -->
本次课内容

<!-- Slide number: 3 -->
PDO连接工具类的实现
项目数据库连接需求分析
PDO连接工具类的设计
PDO连接工具类的代码编写
作业一、二

<!-- Slide number: 4 -->
系统各功能数据库连接需求分析

![](内容占位符4.jpg)

<!-- Slide number: 5 -->
PDO连接工具类的架构

![](内容占位符3.jpg)

<!-- Slide number: 6 -->
PDO连接工具类的架构
高校教务管理系统的PDO连接工具类命名为DB，负责封装所有的数据库操作；
DB类的getInstance方法用于管理单例模式，提供适用于普通查询的数据库连接；
DB类的createTransactionConnection方法用于创建独立连接，专供需要事务支持的场景使用；
DB类的构造方法设置为 private，禁止外部直接实例化，只能通过以下两种方法获取数据库连接；
DB类通过魔术方法__call和__callStatic，将PDO的原生方法透明地转发给调用方。

![](内容占位符3.jpg)

<!-- Slide number: 7 -->
方法调用逻辑

<!-- Slide number: 8 -->
PDO连接工具类的方法

![](内容占位符4.jpg)

![](图片6.jpg)

<!-- Slide number: 9 -->
DB类的头部声明及属性

![](内容占位符8.jpg)
静态属性：存储本类的实例对象
是单例模式的标准写法
在应用程序生存期可共享连接
属性：存储当前连接上下文（true——事务连接）

### Notes:

<!-- Slide number: 10 -->
单例模式的开始
先问内存目前有没有已经创建的实例对象？
没有就创建，有就继续使用
——内存只有一个实例，所以叫单例模式
getInstance必须是static

![](内容占位符4.jpg)

### Notes:

<!-- Slide number: 11 -->
事务模式的开始
直接实例化DB类
每次执行都是一个新的实例

![](内容占位符7.jpg)

### Notes:

<!-- Slide number: 12 -->
构造方法和connect方法
构造方法是私有的
意味着不能直接new DB
而必须使用单例模式或事务模式实例化对象

![](内容占位符10.jpg)
由构造方法调用，
执行PDO连接，
成功后类的$pdo属性即可被赋值为一个PDO类的实例

<!-- Slide number: 13 -->
connect方法的执行逻辑（类似于练习1）

![](内容占位符4.jpg)

<!-- Slide number: 14 -->
由connect方法调用，
从配置文件读取数据库连接参数，帮助connect方法完成数据库连接
getDbConfig和getInstance

![](内容占位符7.jpg)

### Notes:

<!-- Slide number: 15 -->
练习
完成[姓名拼音]DB类的普通连接相关方法搭建；
修改入口文件的脚本，使用工具类完成数据库的连接（通过静态方法getInstance获取实例）
使用获取到的实例，代替$pdo，完成老师登录验证的原生方法调用，观察结果，分析不成功的原因。

<!-- Slide number: 16 -->
PDO的原生方法列表

![](内容占位符4.jpg)

<!-- Slide number: 17 -->
解决方法：魔术方法
“调用转移”
DB类调用PDO类的原生方法时，
通过__call转移给DB类的$pdo来执行

![](内容占位符8.jpg)
为了兼容事务连接，禁止调用PDO的静态方法

<!-- Slide number: 18 -->
PDO的原生方法列表

![](内容占位符4.jpg)
仅2个静态方法，禁用不影响使用

<!-- Slide number: 19 -->
事务类相关方法1

![](内容占位符6.jpg)

<!-- Slide number: 20 -->
事务类相关方法2

![](内容占位符6.jpg)

<!-- Slide number: 21 -->
事务类相关方法3

![](内容占位符4.jpg)

<!-- Slide number: 22 -->
作业一

![](内容占位符10.jpg)
DB类的命名姓名拼音DB，如ZhangsDB

<!-- Slide number: 23 -->
作业二

![](内容占位符5.jpg)

<!-- Slide number: 24 -->
作业二课程信息获取结果

![](内容占位符4.jpg)

![](图片6.jpg)

<!-- Slide number: 25 -->
作业二老师登录验证的结果

![](内容占位符4.jpg)

![](内容占位符9.jpg)

<!-- Slide number: 26 -->
# 作业一~六的提交要求（第八次课）
提交内容（合并7张图片为一个文件，允许是图片或pdf）
作业一 表8-11截图；
作业一 ***DB类的完整代码截图；
作业一 配置文件config/database.php的代码截图；
作业二 index.php的预览截图（老师登录成功；老师登录失败）；
作业二 index.php的预览截图（课程完整信息打印）；

提交标识
图片显眼位置写入学号；方法的注释写入学号。

### Notes:

<!-- Slide number: 27 -->
