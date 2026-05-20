---
name: php-course-notes
description: "用于《WEB项目应用》PHP课程课件要点与作业清单。只要用户提到作业/提交/截图/表编号(表1-2/1-3/2-3/3-5/3-6/3-7/7-11~7-15/8-11/9-6)，或提到User/Stu/Te/ApiResponse/index.php、Postman/Apifox、PDO/Composer/命名空间/RESTful/登录认证/注销/修改密码/Session/Authorization/教学任务/任务查询/Task/缓存控制/强缓存/协商缓存/Cache-Control/If-Modified-Since/304/学年学期/fromterm/toterm/数据库设计与创建等关键词，都必须触发并查阅本skill。若需要精确细节或原始示例，再去打开对应PPT。"
---

# PHP课程课件与作业速查

## 使用目标
- 让回答始终对齐课程课件要求与作业提交清单。
- 优先给出作业要求清单、提交物清单和常见遗漏点。
- 需要更细节时再打开PPT核对。

## 原始PPT位置
- 原始课件保存在同级的 `ppt/` 目录下，文件名保持与课件同名。
- 需要核对页内原文、截图示例或表格时，先按课件名在 `ppt/` 目录里搜索对应文件，再打开核对。
- 如果只给了作业截图，优先根据作业编号、表编号和关键词反查到对应课件。

## 文本摘要位置
- 每份PPT的抽取文本保存在同级的 `extracted/` 目录下，文件名与课件对应。
- 需要快速检索知识点时，先看 `extracted/` 里的文字摘要；需要核对原图或页面样式时，再去 `ppt/` 里看原始文件。

## 使用流程
1. 先确认用户要问的课件主题或作业编号。
2. 读取对应的 reference 文件，给出“要求清单 + 提交清单 + 常见问题”。
3. 用户给截图/代码时，按清单逐项对照，指出缺项或不符合的地方。
4. 信息不足时，先追问缺失点；若必须核对细节，再打开对应PPT。

## 回答模板（默认）
- 作业要求清单（按条列出）
- 提交物清单（截图/文件/表格）
- 常见遗漏与检查点
- 还需要你补充的信息（如请求体、响应体、表格填写项等）

## 何时打开PPT
- 用户提到“我不确定表格/格式/截图要求”“课堂PPT里怎么写的”
- 用户要求逐字核对或需要示例图
- 需要确认表编号内容（如表9-6、表7-14）

打开PPT前先用 `file_search` 找到对应文件名，再使用 `pptx` skill 的读取流程。

## 快速索引（课件 -> 参考文件）
- 课件01 课程概述、环境搭建 -> references/01-course-overview-env.md
- 课件02 数据库的设计 -> references/02-db-design.md
- 课件03 数据库的创建 -> references/03-db-create.md
- 课件04 PHP语法概述 -> references/04-php-syntax.md
- 课件05 PHP面向对象的开发基础 -> references/05-php-oop.md
- 课件06 类的命名空间和Composer工具的使用 -> references/06-namespace-composer.md
- 课件07 RESTful风格的API设计 -> references/07-restful-api.md
- 课件08 PDO建立连接+原生方法+预编译查询 -> references/08-pdo-basics.md
- 课件09 PDO连接工具类的构建 -> references/09-pdo-db-class.md
- 课件10 登录认证功能的实现 -> references/10-auth-session.md
- 课件11 注销及修改密码功能的实现 -> references/11-logout-change-pwd.md
- 课件12 教学任务查询功能的实现 -> references/12-teaching-task-query.md

## 关键词到课件的快速定位
- 环境搭建/WAMP/Wampserver/VS Code/虚拟主机/hosts -> 课件01
- ER图/实体/关系模型/ACID/引擎 -> 课件02
- 建库建表/索引/外键/表3-5/表3-6/表3-7 -> 课件03
- PHP语法/数组/JSON/超全局 -> 课件04
- User/Stu/Te/继承/多态/ApiResponse -> 课件05
- 命名空间/Composer/PSR-4/autoload -> 课件06
- RESTful/状态码/Apifox/表7-11~7-15 -> 课件07
- PDO连接/预编译/SQL注入 -> 课件08
- DB工具类/单例/事务连接/表8-11 -> 课件09
- Session/登录认证/表9-6/Postman登录预览 -> 课件10
- 注销/退出登录/logOut/环境变量/Authorization/修改密码/changePwd/doLogOut.php/doChangePwd.php -> 课件11
- 教学任务/任务查询/Task/search/缓存控制/强缓存/协商缓存/Cache-Control/If-Modified-Since/304/fromterm/toterm/学年学期 -> 课件12
