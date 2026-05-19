# 05 PHP面向对象的开发基础

原始PPT文件名：课件——05 PHP面向对象的开发基础.pptx

## 主题与关键点
- 类的定义与实例化（class / new / ->）
- 构造函数 __construct
- 访问控制：public / protected / private / readonly
- 封装：Getter/Setter 行为控制
- 继承：extends 与可见性放宽规则
- 多态：父类方法调用子类重写方法
- 静态成员与范围解析符 ::
- $this / parent / self 的使用

## 作业与提交
### 作业一（User类）
- 类名 User，文件 /api/User.php
- 构造函数打印“用户类实例化完毕”
- 创建对象并赋值给变量
- 需要 include 引入类文件，建议用 __DIR__ 获取绝对路径

### 作业二（Stu/Te继承）
- Stu 与 Te 继承 User
- User 中定义 login 方法（public），echo “登录成功/失败”
- index.php 实例化 Stu、Te 并调用 login

### 作业二完善（多态）
- User 中定义 userSql 返回空字符串
- Stu/Te 重写 userSql，分别返回“学生登录”“教师登录”
- User 的 login 调用 userSql 实现区分

### 作业三（ApiResponse 工具类）
- /api/ApiResponse.php
- 静态方法 success：接收业务码、状态码、提示消息、data，输出 JSON
- 静态方法 error：接收业务码、状态码、提示消息，输出 JSON
- 成功时 data 可暂用 []

### 第五次课提交要求（合并7张截图）
- 作业一~三 User.php 完整代码截图
- 作业一~三 Stu.php 完整代码截图
- 作业一~三 Te.php 完整代码截图
- 作业一~三 ApiResponse.php 完整代码截图
- 作业一 index.php 代码 + 预览截图
- 作业二 index.php 代码 + 预览截图
- 作业三 index.php 代码 + 预览截图
- 提交标识：图片显眼处写学号；方法注释写学号

## 常见检查点
- 类名大驼峰，文件路径与类名一致
- login 与 userSql 是否正确重写
- 静态方法调用使用 ClassName::method()
