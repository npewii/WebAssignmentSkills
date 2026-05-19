# 06 类的命名空间和Composer工具的使用

原始PPT文件名：课件——06 类的命名空间和Composer工具的使用.pptx

## 主题与关键点
- 命名空间解决类名冲突
- 声明与使用：namespace / use / 完全限定名称
- use 引入可设置别名
- Composer 依赖管理与自动加载
- composer.json / composer.lock 的作用
- 版本约束与常用命令（init/install/update/require/dump-autoload）
- PSR-4 自动加载与 vendor/autoload.php

## 作业与提交
### 作业一（命名空间）
- /api 目录下的类加命名空间
- 根命名空间：\
- 一级命名空间：SuitEdu
- 二级命名空间：姓名拼音
- index.php：
  - 用完全限定名称访问 User
  - use 引入 Stu、Te 并用非限定名调用

### 作业二（composer init）
- 在 edu 目录运行 composer init
- 包名：suit-edu/姓名拼音
- 作者：中文姓名 <邮箱>（注意空格）
- 最低稳定度：stable
- 包类型：project
- 许可证：MIT
- 跳过依赖/开发依赖
- 添加 PSR-4：SuitEdu\姓名拼音 => api/
- 完成后检查 composer.json

### 作业三（组件安装）
- packagist 搜索 Redis 组件
- 查看安装环境要求
- composer require 安装
- 查看 vendor 目录确认

### 作业四（自动加载）
- 删除已有 require_once
- index.php 引入 vendor/autoload.php
- 验证 User/Stu/Te 的命名空间是否正确

### 第六次课提交要求（合并7张截图）
- 作业一~四 User/Stu/Te/ApiResponse 代码截图
- 作业一~四 index.php 代码截图
- 作业二~三 composer.json 截图
- 作业三 安装命令行截图
- 作业三 已安装组件目录截图
- 作业四 index.php 预览截图
- 提交标识：图片显眼处写学号；方法注释写学号

## 常见检查点
- 命名空间与目录映射一致
- PSR-4 配置修改后需 composer dump-autoload
- use 引入的命名空间不要丢根命名空间
