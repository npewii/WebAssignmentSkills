# 15 路由分发功能的实现2

原始PPT文件名：课件——15 路由分发功能的实现2.pptx

## 主题与关键点
- 回顾：统一入口 + 路径转发 + 内部重定向 + 路由分发的完整链路
- 路由分发的定义：根据请求的 HTTP 方法和 URI 路径，将请求分发给对应的业务逻辑模块
- 两种 URL 路由方式：基于文件路径 vs 基于入口文件（index.php）
- Route 类的核心职责：请求方法校验、资源标识解析、业务逻辑分发
- Route 类完整工作流程：run() → setMethod() → setResource() → switch 资源分发
- 属性定义：`$_requestMethod`、`$_allowRequestMethod`（GET/POST/PATCH/DELETE）、`$_requestResource`、`$_allowResource`（sessions/users/tasks）、`$_requestUri`
- setMethod()：从 `$_SERVER['REQUEST_METHOD']` 获取并校验方法，非法抛 405
- setResource()：从 `$_SERVER['PATH_INFO']` 解析资源名（`$params[1]`）和资源URI（`$params[2]`），非法抛 405
- run() 方法：switch 分发到 dealSessions() / dealUsers() / dealTasks()，default 抛 405
- dealSessions()：POST → doLogin()，DELETE → dologout()，其他 → 405
- doLogin()：InputTool 校验 uid/upassword/urole → 按角色实例化 Stu 或 Te → 调用 login()
- dologout()：调用 User::logOut()
- dealUsers()：PATCH → doChangePwd()，其他 → 405
- dealTasks()：GET + URI=='list' → doSearchTask()，其他 → 405
- InputTool 工具类：dealJson()、checkId()、checkPwd()、checkRole()（缺少字段400，格式错误422）
- 入口文件 index.php：`use Route; require autoload; (new Route)->run();`
- 改进 URI 设计：区分查询单个/全部资源、避免用户管理与登录URI冲突
- Apifox 开发环境配置：前置 URL、环境变量（token、last_modified）

## 作业与提交
### 作业一（Route 类完整实现）
- 完成 Route 类全部代码：属性定义、run()、setMethod()、setResource()
- 完成 dealSessions()、doLogin()、dologout()
- 完成 dealUsers()（doChangePwd 方法自行补全）
- 完成 dealTasks()（doSearchTask 方法自行补全）
- 完成 InputTool 工具类：dealJson()、checkId()、checkPwd()、checkRole()
- 在 Apifox 中测试以下路由：
  - POST /[姓名拼音]v1/sessions → 用户登录
  - DELETE /[姓名拼音]v1/sessions → 用户注销
  - PATCH /[姓名拼音]v1/users → 修改密码
  - GET /[姓名拼音]v1/tasks/list → 查询任务列表

### 第十五次课提交要求（合并5张图片为一个文件，允许图片或PDF）
- Route 类的完整代码截图
- Apifox 测试 POST `http://域名/[姓名拼音]v1/sessions` 的预览截图（含地址栏和响应结果）
- Apifox 测试 DELETE `http://域名/[姓名拼音]v1/sessions` 的预览截图（含地址栏和响应结果）
- Apifox 测试 PATCH `http://域名/[姓名拼音]v1/users` 的预览截图（含地址栏和响应结果）
- Apifox 测试 GET `http://域名/[姓名拼音]v1/tasks` 的预览截图（含地址栏和响应结果）

提交标识：图片显眼位置写入学号；方法的注释写入学号。

## 常见检查点
- Route 类属性是否正确定义（$_requestMethod、$_allowRequestMethod、$_requestResource、$_allowResource、$_requestUri）
- setMethod() 是否正确校验 HTTP 方法并抛出 405 异常
- setResource() 是否正确从 PATH_INFO 解析资源名和 URI
- run() 中 switch 是否正确分发到各 deal 方法
- dealSessions() 是否区分 POST（登录）和 DELETE（注销）
- dealUsers() 是否仅处理 PATCH（修改密码）
- dealTasks() 是否判断 GET 且 URI 为 'list'（查询任务列表）
- doLogin() 是否使用 InputTool 校验输入并按角色实例化 Stu/Te
- InputTool 各类方法是否正确校验并抛出对应状态码（400/422）
- index.php 是否正确引入 autoload 并实例化 Route 调用 run()
- Apifox 前置 URL 是否配置正确
- 各接口的 Apifox 测试截图是否包含地址栏和响应结果
