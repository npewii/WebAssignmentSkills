# 09 PDO连接工具类的构建

原始PPT文件名：课件——09 PDO连接工具类的构建.pptx

## 主题与关键点
- DB 工具类用于封装数据库连接与操作
- 单例连接：getInstance
- 事务连接：createTransactionConnection
- 构造方法 private，外部禁止 new
- __call / __callStatic 转发 PDO 原生方法
- 连接配置读取与 connect 方法逻辑

## 作业与提交
### 作业一
- DB类命名：姓名拼音DB（如 ZhangsDB）
- 完成普通连接相关方法搭建
- 在入口文件使用 getInstance 获取实例
- 用该实例替代 $pdo 完成老师登录验证

### 作业二
- 使用工具类完成课程信息获取/登录验证（按PPT示例）

### 第八次课提交要求（合并7张截图）
- 作业一 表8-11截图
- 作业一 ***DB 类完整代码截图
- 作业一 config/database.php 代码截图
- 作业二 index.php 预览截图（老师登录成功/失败）
- 作业二 index.php 预览截图（课程完整信息打印）
- 提交标识：图片显眼处写学号；方法注释写学号

## 常见检查点
- __call 转发是否指向 $this->pdo
- 单例与事务连接区分清楚
- getInstance 必须是 static
