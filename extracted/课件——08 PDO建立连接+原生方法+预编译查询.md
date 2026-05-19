<!-- Slide number: 1 -->
# 252602 WEB项目应用
PDO建立连接+原生方法+预编译查询
2026-4-18

<!-- Slide number: 2 -->
本次课内容

<!-- Slide number: 3 -->
利用PDO实现MySQL连接
什么是PDO
PDO扩展安装及连接详解

<!-- Slide number: 4 -->
PDO的核心优势

<!-- Slide number: 5 -->
PDO 连接的三个阶段

![](内容占位符6.jpg)

<!-- Slide number: 6 -->
PDO扩展的安装情况

![](内容占位符3.jpg)

<!-- Slide number: 7 -->
PDO连接详解——DSN（数据源名称）
格式为：驱动:键值对

![](内容占位符4.jpg)

<!-- Slide number: 8 -->
PDO连接详解——连接选项
可通过PDO实例调用
setAttribute方法设置

![](内容占位符4.jpg)

![](图片5.jpg)

<!-- Slide number: 9 -->
六种连接方式

![](内容占位符4.jpg)

![](图片6.jpg)

<!-- Slide number: 10 -->
练习1
在入口文件尝试使用PDO扩展完成数据库的普通连接，要求：
数据库连接配置放置在配置文件config/database.php中，使用默认场景edu完成连接，配置格式见下一页ppt；
设置DSN参数连接MySQL，包括：
host
dbname
charset
设置连接选项：
PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION
PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
测试：
成功连接；
错误连接：

### Notes:

<!-- Slide number: 11 -->
config/database.php示范

![](内容占位符3.jpg)

<!-- Slide number: 12 -->
练习1代码参考

![](内容占位符4.jpg)

<!-- Slide number: 13 -->
练习1效果——连接成功

![](内容占位符4.jpg)

<!-- Slide number: 14 -->
练习1效果——连接失败

![](内容占位符4.jpg)
设置错误的配置参数导致连接失败，抛出异常

<!-- Slide number: 15 -->
练习1脚本改进——异常捕获

![](内容占位符4.jpg)

![](图片6.jpg)

<!-- Slide number: 16 -->
练习1完善
完善PDO连接脚本，利用try-catch，把代码放入try分支，在catch分支捕获异常，并手动处理异常

<!-- Slide number: 17 -->
连接失败的异常处理效果

![](内容占位符4.jpg)

<!-- Slide number: 18 -->
PDO查询流程及原生查询方法
PDO查询流程
PDO原生查询方法

<!-- Slide number: 19 -->
SQL注入攻击
SQL注入是一种代码注入技术，攻击者通过在用户输入中插入恶意的SQL代码，欺骗后端数据库执行非预期的命令，从而窃取、篡改或删除数据。

<!-- Slide number: 20 -->
普通查询

![](内容占位符8.jpg)
将变量直接嵌入 SQL 语句，无法预防注入攻击

<!-- Slide number: 21 -->
预编译查询
预编译SQL模板

![](内容占位符4.jpg)
两个步骤分开
可防范注入攻击
发送参数

![](图片6.jpg)

<!-- Slide number: 22 -->
普通查询vs预编译查询

![](内容占位符6.jpg)

<!-- Slide number: 23 -->
普通查询vs预编译查询

![](内容占位符9.jpg)

![](内容占位符4.jpg)

<!-- Slide number: 24 -->
如何抉择：普通查询 or 预编译查询

<!-- Slide number: 25 -->
系统各核心功能查询方法分析

![](内容占位符4.jpg)

<!-- Slide number: 26 -->
PDO原生查询方法——连接与配置

![](内容占位符4.jpg)

<!-- Slide number: 27 -->
PDO原生查询方法——结果处理类

![](内容占位符6.jpg)

<!-- Slide number: 28 -->
参数绑定的方式选择
execute
bindParam

![](内容占位符18.jpg)

![](内容占位符10.jpg)
采用引用传递，只能绑定变量， 不能绑定值或表达式，但只需绑定一次，后续修改变量值即可重复执行，适合批量操作。
绑定变量时采用值传递，可以绑定变量、值或表达式，每次执行都 需要重新传递参数，适合单次执行

<!-- Slide number: 29 -->
参数绑定的方式选择

<!-- Slide number: 30 -->
系统各核心功能的预编译查询时参数绑定分析

![](内容占位符4.jpg)

<!-- Slide number: 31 -->
练习2
在入口文件为老师登录验证编写SQL模板，并通过execute完成参数绑定，要求：
使用问号占位符；
execute直接使用索引数组，绑定老师登录的工号和密码的值；
成功或失败都使用ApiResponse类的方法返回结果。

<!-- Slide number: 32 -->
登录验证效果

![](内容占位符5.jpg)

![](内容占位符10.jpg)

<!-- Slide number: 33 -->
练习2完善：使用客户端的请求体获取登录信息

### Notes:

<!-- Slide number: 34 -->
练习2的优化要求
从客户群发送来的请求体内的json字符串中提取老师登录的工号和密码

![](图片4.jpg)

![](图片6.jpg)

<!-- Slide number: 35 -->
