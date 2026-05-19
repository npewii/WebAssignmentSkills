<!-- Slide number: 1 -->
# 252602 WEB项目应用
类的命名空间和Composer工具的使用
2026-3-31

<!-- Slide number: 2 -->
本次课内容

<!-- Slide number: 3 -->
命名空间
命名空间概述
命名空间的声明
命名空间的使用
命名空间的引入

<!-- Slide number: 4 -->
命名空间要解决的问题：类名冲突

![](内容占位符6.jpg)

![](内容占位符10.jpg)

你可以保证自己完全独立开发的项目中没有重名的类；
但是当你引入第三方开发组件时（在开源时代越来越难以避免），就无法避免别人和自己、别人和别人没有重名的类！
老的解决思路：用很长的名字，加很多的前缀，如SziitOaUserDeal，缺点，代码可读性差。

<!-- Slide number: 5 -->
5
思考：文件系统如何避免重名？
文件夹

![](内容占位符7.jpg)

![](内容占位符8.jpg)

<!-- Slide number: 6 -->
6
PHP的解决方案：命名空间（PHP >= 5.3.0)
从广义上来说，命名空间是一种封装事物的方法。
命名空间用来解决两类问题：
用户编写的代码与PHP内部的类/函数/常量或第三方类/函数/常量之间的名字冲突。
为很长的标识符名称(通常是为了缓解第一类问题而定义的)创建一个别名（或简短）的名称，提高源代码的可读性。

![](内容占位符5.jpg)

<!-- Slide number: 7 -->
命名空间
命名空间概述
命名空间的声明
命名空间的使用
命名空间的引入

<!-- Slide number: 8 -->
命名空间的声明——层次化的命名空间

![](内容占位符5.jpg)

![](内容占位符7.jpg)

![](图片2.jpg)

<!-- Slide number: 9 -->
9
命名空间的声明总结

### Notes:

<!-- Slide number: 10 -->
命名空间
命名空间概述
命名空间的声明
命名空间的使用
命名空间的引入

<!-- Slide number: 11 -->
11
命名空间的使用

![](内容占位符9.jpg)

<!-- Slide number: 12 -->
12
命名空间的使用

![](内容占位符3.jpg)

<!-- Slide number: 13 -->
13
命名空间的使用

![](内容占位符3.jpg)

<!-- Slide number: 14 -->
命名空间
命名空间概述
命名空间的声明
命名空间的使用
命名空间的引入

<!-- Slide number: 15 -->
引入命名空间
未引入命名空间
引入命名空间

![](内容占位符15.jpg)

![](内容占位符19.jpg)
引入命名空间后会简化对类的调用，(new MyError)->error();
use语句引入命名空间，可以省略根命名空间\
若使用完全限定名称访问类，跟命名空间\不能省略

<!-- Slide number: 16 -->
use引入命名空间：别名/导入

![](内容占位符11.jpg)
同名的类在被引入时，需要给其中一个定义别名

<!-- Slide number: 17 -->
作业一
为项目的类（/api目录下）完成命名空间的声明：
根命名空间是\
第一级子命名空间是：SuitEdu
第二级子命名空间是：你的姓名拼音
在index.php中利用命名空间完成对类的访问：
利用完全限定名称完成对类User的访问；
引入Stu和Te类的命名空间，利用非限定名称完成这两个类的访问。

<!-- Slide number: 18 -->
Composer工具的使用
工具概述
项目初始化
依赖管理
自动加载

<!-- Slide number: 19 -->
依赖管理工具：Composer

### Notes:

<!-- Slide number: 20 -->
为何需要Composer

依赖管理的工作内容
手工管理VS工具管理
手工管理：
维护人员下载 zip 包 → 解压 → 复制到 项目 → 手动配置 include_path → 维护版本 → 处理冲突
Composer管理：
维护人员只需敲几个简单的命令，Composer就会自动完成所有工作
手工管理繁琐、易错且难度极大；
工具管理简单、规范且不易出错。

<!-- Slide number: 21 -->
Composer的工作流程

<!-- Slide number: 22 -->
Composer的常用命令
| 命令 | 作用 |
| --- | --- |
| composer init | 交互式创建?composer.json |
| composer install | 安装依赖（读取?composer.lock） |
| composer update | 更新依赖（读取?composer.json） |
| composer require vendor/package | 安装并添加依赖到?composer.json |
| composer remove vendor/package | 移除依赖 |
| composer dump-autoload | 重新生成自动加载文件 |
| composer show | 查看已安装的包 |
| composer outdated | 查看可更新的包 |
| composer validate | 验证?composer.json?格式 |

<!-- Slide number: 23 -->
composer的两个文件
composer.json
composer.lock

![](内容占位符7.jpg)

![](内容占位符5.jpg)

![](内容占位符13.jpg)

![](内容占位符18.jpg)

![](内容占位符23.jpg)

![](内容占位符28.jpg)

### Notes:

<!-- Slide number: 24 -->
composer.json和composer.lock
composer.json
comopser.lock
文件中保存的是组件及其依赖的具体版本；
执行composer install时根据该文件安装组件；
适用场景：在多人协同开发的情况下，这个文件能很好的解决组件不同而产生的问题。所以会把这个文件也放入版本管理中。
文件中保存的是我们安装的组件及组件的版本要求。
执行composer update时根据该文件更新组件；
更新后修改comopser.lock文件。

### Notes:

<!-- Slide number: 25 -->
composer.json和composer.lock示范

![](内容占位符8.jpg)

<!-- Slide number: 26 -->
Composer工具的使用
工具概述
项目初始化
依赖管理
自动加载

<!-- Slide number: 27 -->
项目初始化（composer init）
composer init 是创建 Composer 项目的起点。
通过交互式问答快速生成标准化的 composer.json 配置文件，为后续依赖管理奠定基础。

<!-- Slide number: 28 -->
项目初始化（composer init）

![](内容占位符15.jpg)
composer init 是创建 Composer 项目的起点。
通过交互式问答快速生成标准化的 composer.json 配置文件，为后续依赖管理奠定基础。

<!-- Slide number: 29 -->
# composer init执行详解

![](内容占位符3.jpg)

![](内容占位符5.jpg)

![](图片6.jpg)

<!-- Slide number: 30 -->

![](内容占位符9.jpg)
5. Package type包类型

![](内容占位符5.jpg)

<!-- Slide number: 31 -->
6. license

![](内容占位符6.jpg)

<!-- Slide number: 32 -->
composer init的工作成果

![](内容占位符6.jpg)
composer.json是Composer使用的开始

<!-- Slide number: 33 -->
作业二
在edu目录下运行命令composer init，为你的高校教务管理系统完成初始化工作，以下是部分答案：
包名：suit-edu/姓名拼音
作者：你的中文姓名 <你的邮箱>   （中间必须有空格隔开）
最低稳定度：stable
包类型：project
许可证：MIT
跳过定义依赖和开发依赖
添加自动加载映射Add PSR-4 autoload mapping? Maps namespace “SuitEdu\姓名拼音” to the entered relative path. [src/, n to skip]: api/命名空间[SuitEdu\姓名拼音]指向类的保存目录api
完成后查看根目录生成的composer.json

<!-- Slide number: 34 -->
作业二的结果

![](内容占位符4.jpg)

<!-- Slide number: 35 -->
Composer工具的使用
工具概述
项目初始化
依赖管理
自动加载

<!-- Slide number: 36 -->
依赖管理——Composer把依赖安装到项目的Vendor目录

![](内容占位符3.jpg)

### Notes:

<!-- Slide number: 37 -->
Composer的常用命令
| 命令 | 作用 |
| --- | --- |
| composer init | 交互式创建?composer.json |
| composer install | 安装依赖（读取?composer.lock） |
| composer update | 更新依赖（读取?composer.json） |
| composer require vendor/package | 安装并添加依赖到?composer.json |
| composer remove vendor/package | 移除依赖 |
| composer dump-autoload | 重新生成自动加载文件 |
| composer show | 查看已安装的包 |
| composer outdated | 查看可更新的包 |
| composer validate | 验证?composer.json?格式 |

<!-- Slide number: 38 -->
三种常见的组件安装方式

![](图片4.jpg)

<!-- Slide number: 39 -->
依赖版本管理
| 约束 |  | 含义 | 示例 |
| --- | --- | --- | --- |
| 基础约束 | 1.0.0 | 精确版本 | 只能安装 1.0.0 |
|  | >=1.0 | 大于等于 | 1.0.0 及以上 |
|  | <=1.0 | 小于等于 | 1.0.0 及以下 |
|  | >1.0 | 大于 | 1.0.1 及以上 |
|  | <1.0 | 小于 | 0.9.9 及以下 |
| 范围约束 | >=1.0,<2.0 | 1.0 到 2.0 之间 | 1.x.x |
|  | ~1.2 | 相当于?>=1.2,<2.0 | 1.2.0 到 1.9.9 |
|  | ^1.2 | 相当于?>=1.2,<2.0 | 1.2.0 到 1.9.9 |
|  | ^1.2.3 | 相当于?>=1.2.3,<2.0 | 1.2.3 到 1.9.9 |
|  | ^0.3 | 相当于?>=0.3,<0.4 | 0.3.x（因为是主版本0） |
| 通配符 | 1.0.\* | 通配符 | 1.0.0、1.0.1、1.0.2 |
|  | dev-master | 开发分支 | 最新的 master 分支 |

![](内容占位符7.jpg)

<!-- Slide number: 40 -->
组件详情页的安装要求

![](内容占位符7.jpg)
用户要求安装：
phpspreadsheet
phpspreadsheet要求安装3个组件（+其他测试组件）
所以composer安装了4个组件（+其他测试组件）：
phpspreadsheet
maennchen
markbaker
psr

<!-- Slide number: 41 -->
Composer对依赖实施添加、更新和移除的过程

![](内容占位符9.jpg)

<!-- Slide number: 42 -->
提问
如果想要把组件phpoffice/phpspreadsheet的版本升级到1.30，如何操作？
修改composer.json中phpoffice/phpspreadsheet的版本为1.30
修改composer.lock中phpoffice/phpspreadsheet的版本为1.30
在命令行执行composer install
在命令行执行composer update

<!-- Slide number: 43 -->
提问
如果想要把组件phpoffice/phpspreadsheet的版本升级到1.30，如何操作？
修改composer.json中phpoffice/phpspreadsheet的版本为1.30
修改composer.lock中phpoffice/phpspreadsheet的版本为1.30
在命令行执行composer install
在命令行执行composer update

<!-- Slide number: 44 -->
提问
如果想要安装跟小组成员一样的组件环境，如何操作？
复制小组成员的composer.json到自己网站的根目录
复制小组成员的composer.lock到自己网站的根目录
在命令行执行composer install
在命令行执行composer update

<!-- Slide number: 45 -->
提问
如果想要安装跟小组成员一样的组件环境，如何操作？
复制小组成员的composer.json到自己网站的根目录
复制小组成员的composer.lock到自己网站的根目录
在命令行执行composer install
在命令行执行composer update

<!-- Slide number: 46 -->
作业三：组件安装
打开网站https://packagist.org/，搜索要安装的组件Redis；
查看组件安装的环境要求；
在站点跟根目录（edu目录）输入安装命令composer require ……安装组件；
通过命令行确认安装结果，并在Vendor目录下查看安装结果。

<!-- Slide number: 47 -->
Composer工具的使用
工具概述
项目初始化
依赖管理
自动加载

<!-- Slide number: 48 -->
类的手动加载

![](内容占位符6.jpg)

![](内容占位符7.jpg)

![](图片8.jpg)

<!-- Slide number: 49 -->
自动加载要解决的问题
使用类存在的问题
自动加载的效果
自动加载可以利用某种规则，找到文件要加载的类文件，然后自动添加include等包含语句。
换句话说，有了自动加载，文件所有要使用的类，不需要手动写include语句了。

很多开发者为每个类新建一个 PHP 文件。 这会带来一个烦恼：每个脚本的开头，都需要包含（include）一个长长的列表（每个类都有个文件）。

![](图片7.jpg)

<!-- Slide number: 50 -->
Composer自动加载的过程

<!-- Slide number: 51 -->
自动加载的关键——PSR-4及自动加载的相关配置
psr-4
composer.json的自动加载配置
\<前导命名空间>(\<零个或多个子命名空间>)*\<类名>

![](内容占位符8.jpg)
| 命名空间 | 映射路径 |
| --- | --- |
| App\Controller\UserController | src/Controller/UserController.php |
| App\Admin\Dashboard | src/Admin/Dashboard.php |
| App\Api\UserController | src/Api/UserController.php |

<!-- Slide number: 52 -->
自动加载的文件列表
如果修改了composer.json的自动加载配置，只需要运行composer dump-autoload即可重新生成

![](内容占位符7.jpg)

<!-- Slide number: 53 -->
Composer自动加载的实施
对于类库的自动加载，Composer 生成了一个 vendor/autoload.php 文件。引入这个文件，就能得到自动加载支持

![](内容占位符5.jpg)

<!-- Slide number: 54 -->
作业四
在项目中使用Composer实现类的自动加载，要求：
删除已经存在的类的文件包含语句（require_once）；
在index.php中引入autoload.php文件；
检查User、Stu和Te三个类对所调用类命名空间的引入和调用情况；
预览并查看index.php自动加载类的效果。

<!-- Slide number: 55 -->
# 作业一~四的提交要求（第六次课）
提交内容（合并7张图片为一个文件，允许是图片或pdf）
作业一~作业四  User、Stu、Te和ApiResponse类的完整代码截图；
作业一~作业四 index.php的完整代码截图；
作业二~三 composer.json的完整代码截图；
作业三 安装组件的命令行截图；
作业三 已安装组件的目录截图；
作业四 index.php的预览截图。
提交标识
图片显眼位置写入学号；方法的注释写入学号。

### Notes:

<!-- Slide number: 56 -->
