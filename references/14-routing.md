# 14 路由分发功能的实现1

原始PPT文件名：课件——14 路由分发功能的实现1.pptx

## 主题与关键点
- 反向代理的介绍与工作流程（反向代理 VS 正向代理）
- 反向代理的核心功能：统一入口和路径路由
- Apache 反向代理部署步骤：启用必要模块（mod_proxy、mod_proxy_http等）
- 编辑虚拟主机配置文件 httpd-vhosts.conf
- 路径转发配置：ProxyPass / ProxyPassReverse
- Apache 侦听端口配置
- 内部重定向 VS 外部重定向
- .htaccess 或 httpd-vhosts.conf 中实现内部重定向（RewriteEngine / RewriteRule）
- 反向代理的请求转发与内部重定向的工作流程对比
- 路由分发的概念与核心设计
- Route 类的完整工作流程
- Router 类的简单实现：检查版本号后的第一个路由标识
- 路由标识映射：sessions（登录）、users（用户）、tasks（教学任务）、scores（成绩）
- 路由分发与反向代理的协作关系

## 作业与提交
### 作业一（反向代理配置）
- 配置 httpd-vhosts.conf，实现统一入口和路径路由转发
- 版本号前必须有自己的姓名拼音（如 /[姓名拼音]v1/）

### 作业二（内部重定向）
- 使用 .htaccess 或在 httpd-vhosts.conf 中实现内部重定向
- 将不带版本号的路径重定向到带版本号的路径

### 作业三（路由分发 Router 类）
- 完成用于路由分发的 Router 类的属性和 run 方法定义
- 在入口文件 index.php 中实例化 Router 并运行 run 方法
- 在 Apifox 中配置开发环境的前置 URL，测试已开发功能
- 无需实现 setMethod 和 setResource 方法，仅在 run 里检查版本号后的第一个路由标识

### 第十四次课提交要求（合并7张图片为一个文件，允许图片或PDF）
- 作业一 httpd-vhosts.conf 的完整代码截图（版本号前必须有自己的姓名拼音）
- 作业二 .htaccess 的代码截图（若在 httpd-vhosts.conf 实现内部重定向，可与作业一合并截图）
- 作业三 Route 类的完整代码截图
- 作业三 Apifox 测试 POST `http://域名/[姓名拼音]v1/sessions` 的预览截图（含地址栏和响应结果）
- 作业三 Apifox 测试 DELETE `http://域名/[姓名拼音]v1/sessions` 的预览截图（含地址栏和响应结果）
- 作业三 Apifox 测试 PATCH `http://域名/[姓名拼音]v1/users` 的预览截图（含地址栏和响应结果）
- 作业三 Apifox 测试 GET `http://域名/[姓名拼音]v1/tasks` 的预览截图（含地址栏和响应结果）

提交标识：图片显眼位置写入学号；方法的注释写入学号。

## 常见检查点
- httpd-vhosts.conf 中版本号路径前是否有自己的姓名拼音
- ProxyPass / ProxyPassReverse 配置是否正确
- 内部重定向规则是否正确（RewriteEngine On、RewriteRule）
- Router 类是否正确解析 URI 并分发到对应模块
- index.php 是否正确实例化 Router 并调用 run 方法
- Apifox 前置 URL 是否配置为 `http://域名/[姓名拼音]v1/`
- 各 HTTP 方法（POST/DELETE/PATCH/GET）测试结果是否正确
