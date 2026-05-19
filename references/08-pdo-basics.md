# 08 PDO建立连接+原生方法+预编译查询

原始PPT文件名：课件——08 PDO建立连接+原生方法+预编译查询.pptx

## 主题与关键点
- PDO 优势：统一接口、可预编译、防注入
- 连接三阶段：创建实例 -> 设置属性 -> 执行操作
- DSN 格式：驱动:键值对（host/dbname/charset）
- 连接选项：ERRMODE_EXCEPTION、FETCH_ASSOC 等
- try-catch 捕获连接异常
- SQL 注入风险与预编译查询
- 参数绑定：execute（值传递） vs bindParam（引用传递）

## 练习/任务要点
### 练习1（普通连接）
- 配置文件：config/database.php（默认场景 edu）
- DSN 参数：host、dbname、charset
- 连接选项：
  - PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION
  - PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
- 分别测试成功连接与错误连接
- 增加 try-catch 处理异常

### 练习2（预编译登录验证）
- 编写老师登录 SQL 模板
- 使用问号占位符
- execute 传索引数组
- 成功/失败均用 ApiResponse 输出

### 练习2优化
- 从请求体 JSON 中读取工号与密码

## 常见检查点
- DSN 拼写与字符集是否正确
- 错误处理是否用异常模式
- 预编译是否真正使用占位符
