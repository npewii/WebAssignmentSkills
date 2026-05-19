# 01 课程概述、环境搭建

原始PPT文件名：课件——01 课程概述、环境搭建.pptx

## 主题与关键点
- 动态网页 vs 静态网页：客户端看不出差异；动态页面需要服务器端处理并实时读取数据
- 网站基本概念：服务器、IP、域名、端口、HTTP/HTTPS、请求与响应、静态/动态访问流程
- 课程定位：基于WAMP的PHP动态网站项目开发；案例为高校教务管理系统
- PHP与MySQL概述：PHP发展与优势、MySQL特性与对比
- 运行环境：开发环境WAMP；部署环境LAMP/ LNMP

## 环境搭建要点（WAMP）
- 两种方案：单独安装Apache/PHP/MySQL vs 集成环境（XAMPP/Wampserver/AppServ）
- Wampserver常见问题：
  - 安装路径不能含中文
  - 端口冲突需修改服务默认端口
  - VC运行库不完整会导致启动失败
  - 安装中建议默认编辑器改为VS Code
- 虚拟主机/域名：修改hosts + httpd-vhosts.conf + httpd.conf
- 依赖工具：composer、Node.js/npm、Postman

## 作业与提交
### 作业1：安装 VS Code
- 安装最新版
- 至少安装 6 个扩展（见PPT示例）
- 提交：已安装扩展截图、表1-3截图

### 作业2：安装 Wampserver + 环境完善
- 安装Wampserver并访问默认首页
- 创建站点目录：www/edu
- 配置域名与虚拟目录：edu.suit.cn
- 安装 composer（注意选择对应PHP版本）
- 安装 Node.js / npm（验证 node -v, npm -v）
- 安装 Postman 并发送 GET 请求测试

### 第一次作业提交汇总（合并6张截图）
- VS Code 扩展截图
- 表1-3（快捷键记录表）截图
- Wampserver 安装目录截图
- 命令行运行 composer、node -v、npm -v 截图
- Postman 对 localhost 的 GET 响应截图
- 表1-2（Wampserver安装参数表）截图
- 提交标识：每张图片显眼位置写学号；注释中也写学号

## 常见检查点
- Wampserver路径是否含中文
- edu.suit.cn 是否可访问到 edu 目录默认页
- composer 是否指向正确的 php.exe
- Postman 是否有成功响应截图
