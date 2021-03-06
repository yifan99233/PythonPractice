# Day1 基础知识 2020.07.16

-----

# 0x00：计算机组成原理

### 一、什么是计算机

> 计算机是20世纪最先进的科学技术发明之一

+ 能够进行数值计算
+ 能进行逻辑判断
+ 具有存储记忆功能
+ 能够按照程序的运行，自动、高效、快速处理数据

### 二、计算机是由什么组成的

一个完整的计算机系统，是由**硬件系统** 和 **软件系统** 俩大部分组成的。
![计算机组成](https://oss.smartfox.cc/2020/07/16/d1f6c10c117f3.png)

#### 硬件系统

> + 主要分为 **主机** 和 **外设** 俩部分 
> + 由各种的**电子器件**和**机电装置**组成
> + 设计采用的都是**冯诺依曼体系结构**

![冯诺依曼体系结构](https://oss.smartfox.cc/2020/07/16/8f86e46cc4aac.png)

#### 软件系统

+ 主要分为**系统软件**和**应用软件**

###### 系统软件

> **操作系统**：是一种方便用户管理和控制计算机软硬件资源的**系统软件**。
>
> + 具有承上启下的作用；向下管理硬件设备，向上提供接口
> + 我们操作计算机实际上是通过操作系统来完成的。
>
> **语言处理程序**：也称为编译程序，作用是把程序员们编写的程序翻译成计算机可以直接识别的机器语言。

###### 应用软件

> 微信、QQ、音乐播放器等软件。

-------

# 0x01：认识Python

### 一、 编程语言是什么

> 简单来说，编程语言就是人与计算机进行交流的语言。

### 二、什么是Pyhton

Python就是一门编程语言，而且是世界上最流行的编程语言之一。

+ Pyhton的作者是Guido van Rossum（龟叔）
+ 是一种解释性语言

> + 在运行的时候被**解释器**翻译成计算机识别的机器语言
> + 解释性语言每执行一次就要逐行翻译一次

+ Python的解释器如今有多种语言实现

> + CPython（官方版本的C语言实现）
> + Jython （运行于Java平台）
> + PyPy（Python实现的，支持JIT即时编译）

+ 解释器版本Python3与Python2

  ![解释器版本使用比例](https://oss.smartfox.cc/2020/07/16/d59dcc7416a63.png)

> 目前Python有俩个版本，分别为 **Python2** 和 **Pyhton3**；
>
> 但由于同时维护俩个版本Python十分耗费人力，所以Python官方与社区志愿者们共同决定在2020年1月份后就结束对Pyhton2更新与维护。

### 三、Python优缺点

#### 优点

+ 简单
+ 易学
+ 免费、开源
+ 可移植性
+ 可拓展性
+ 丰富的社区库
+ 规范的代码

#### 缺点

+ 执行效率慢

### 四、Python能做什么

![Python应用领域](https://oss.smartfox.cc/2020/07/16/6638a060b46f3.png)

**Web 开发**和**数据科学**仍是 Python 开发的两大主力。因为据称 Python 是数据科学的最佳工具之一，所以涉及数据分析和机器学习的 Python 开发人员数量如此众多毫不令人吃惊。

--------

# 0x03： 第一个Python程序

### 一、如何优雅的编写Python

+ 直接写Python（REPL模式）

  所谓REPL即**R**ead、**E**va、**P**rint、**L**oop（读取、计算、打印、循环）
  实现REPL运行方式有以下两种：

  + IDLE

    ![IDLE](https://oss.smartfox.cc/2020/07/14/fe003c8dae7c7.png)

  + 命令行

    ![命令行](https://oss.smartfox.cc/2020/07/14/5b54494ce5e27.png)

+ 编写Python脚本，运行脚本

  + 新建一个拓展名为.py的文件

  + 使用编辑器在文件中写入Python语句

    ![编写脚本](https://oss.smartfox.cc/2020/07/14/7d9553837b7f2.png)

  + 执行Python脚本

    ![执行脚本](https://oss.smartfox.cc/2020/07/14/bc1474a9c9047.png)

+ 使用Pycharm编写程序

  1. 打开 Pycharm，选择` Create New Project`，创建一个新项目

  2. 选择 `Location` 表示该项目保存的路径，`Interpreter` 表示使用的Python解释器版本，第一次需要手动配置解释器

     ![创建项目步骤](https://oss.smartfox.cc/2020/07/16/57f2c8a6fa6c6.png)

  3. 创建项目

  4. 创建Python文件

  5. 运行Python程序

     ![执行结果](https://oss.smartfox.cc/2020/07/16/c599e52128616.png)

-------

# 0x04： BUG介绍与注释

### 一、什么是BUG

> BUG是指任何计算机程序或硬件系统中的错误、故障、缺陷、漏洞。错误会产生意外结果或导致系统意外运行。
>
> 简而言之，它是程序或系统获得的任何行为或结果，但它不是为此而设计的。

+ 名称错误

+ 语法错误

  ![](https://oss.smartfox.cc/2020/07/16/0345cb9511707.png)

### 二、注释

> + 注释：在程序代码中对程序代码进行**解释说明**的文字。
> + 作用：**注释不是程序、不能被执行** 只对程序代码进行解释说明，让别人能看懂代码的作用
> + 不过太多的注释混入程序代码可能会反而使代码难以理解,通常最好是将一个注释块放在所解释代码的上方。
> + 而且**错误**的注释会比没有注释更糟,因为它会误导后来者。

+ 单行注释

```python
# {注释内容}

print("噔噔咚 - 噔噔咚")
# print("猫猫猫猫")  单行注释
```

+ 多行注释

```python
""" {注释内容} """
''' {注释内容} '''

"""
多行注释
print("噔噔咚")
print("猫猫猫猫")
"""
```

### 三、PyCharm常用快捷键

快捷键|说明
-|-
Ctrl + Z | 撤销操作（Undo）
Ctrl + Shift + Z | 重做操作（Redo）
Ctrl + / |注释、取消注释
Ctrl + Alt + l | 代码格式化
Ctrl + Shift + F10 | 运行代码

-------

# 0x05：变量

### 一、什么是变量

+ 变量来源于数学，是计算机语言中能储存计算结果或能表示值抽象概念；
+ 通俗来讲，就是给数据起名字；

### 二、变量的定义

+ 语法：变量名 = 变量值 eg. exp = 10
+ 在Python中，对变量首次赋值会定义变量，再次赋值会修改变量的值。
+ 定义变量，无需指定类型，Python会自动推导类型


### 三、变量的类型

+ 类型是什么

为了区分变量不同的功能，变量是有不同的类型的：
![](https://oss.smartfox.cc/2020/07/16/4837b795c3c48.png)

+ 如何查看类型

在Python中，可以使用type函数查看变量的类型

```Python
type( 变量名 )
```

### 四、标识符、关键字与命名规则

+ 什么是标识符

> + 标识符就是开发人员**在程序中自定义的一些符号和名称**
> + 标识符是自己定义的，如：变量名、函数名等

+ 什么是关键字

> + Python一些具有特殊功能的标识符，这就是所谓的关键字
> + 关键字，是Python已经使用的了，多以不允许开发者自己定义和关键字相同名字的标识符。
> + 常见的Python关键字
> 
> ```python
> and     as      assert     break     class      continue    def     del
> elif    else    except     exec      finally    for         from    global
> if      in      import     is        lambda     not         or      pass
> print   raise   return     try       while      with        yield
> ```
>
> + 查看Python中存在的关键字
> 
> ```python
> # 1. 导入工具包
> import keyword
> # 2. 打印关键字
> print(keyword.kwlist)
> ```

+ 标识符的命名规则

> + 由**字母、下划线**和**数字**组成
> + 不能以数字开头
> + 不能与关键字重名
> + 建议不和类型同名，如：int、str等

**注意：** Python中的标识符是严格区分大小写的。

+ 命名规范

> + 见名知意 ： 起一个有意义的名字
> + 遵循PEP8标准
> + 驼峰命名法
>
>> 1. 小驼峰命名法
>> 2. 大驼峰命名法

---------

# 0x06：输出与输入

### 一、什么是输出

+ 计算机将计算后的内容反馈给用户的方式就是输出，例如音频、画面显示等。

### 二、什么是格式化输出

+ 所谓格式化输出，是指按一定的格式输出到控制台

##### 格式化输出

+ 在Python中可以使用print函数将信息输出到控制台
+ 如果希望输出文字信息的同时，一起输出数据，则就需要使用到了**格式化操作符**

常用的格式化字符|含义
-|-
%s|字符串
%d|有符号十进制整数，%06d 表示输出的整数显示位数，不足的地方使用 0 补全
%f|浮点数，%.2f 表示小数点后只显示两位

+ 语法

```python
print("格式化字符串" % 变量1)
print("格式化字符串" % (变量1, 变量2...))
```

+ 举个栗子

```python
# 1. 定义整数变量 student_no、age，字符串变量 name, 浮点型变量 height
student_no = 1
age = 18
name = '小明'
height = 1.78

# 2. 输出：我是学号为000001的小明，年龄为18，身高为1.78米
# %06d 表示输出的整数显示位数，不足的地方使用 0 补全
# %.2f 表示小数点后只显示两位
print('我是学号为%06d的%s，年龄为%d，身高为%.2f米' % (student_no, name, age, height))
```

![](https://oss.smartfox.cc/2020/07/16/9aa10f9f679b6.png)

### 三、什么是输入

+ 所谓输入，就是**用代码** **获取**用户通过**键盘**输入的信息
+ 在Python中，如果要获取用户在**键盘**上输入的信息，则需要使用到input函数

### 四、input的使用

+ 在Python中可以使用input函数从键盘等待用户的输入
+ 用户输入的**任何内容**Python都认为是字符串

##### 格式
```python
字符串变量 = input("提示信息：")
```

# 0x07：类型转换

### 一、类型转换函数

函数|说明
-|-
int(x) | 将x转换为一个整数
float(x) | 将x转换到一个浮点数
str(x) | 将x转换到一个字符串

### 二、类型转换栗子

```python
int_num = 123				# 整型
print(type(int_num))  		# 输出结果：<class 'int'>
int_to_str = str(int_num)	# 将整型转为字符串
print(type(int_to_str))  	# 输出结果：<class 'str'>

str_num = "250"  			# 字符串
print(type(str_num))		# 输出结果：<class 'str'>
str_to_int = int(str_num)	# 将字符串转为整型
print(type(str_to_int))  	# 输出结果：<class 'int'>

str_num = '3.14'  			# 字符串
print(type(str_num))		# 输出结果：<class 'str'>
strToFloat = float(str_num)	# 将字符串转为浮点数
print(type(strToFloat))  	# 输出结果：<class 'float'>
```

# 0x08： 运算符

### 一、算术运算符

| 运算符 | 描述   | 实例（a = 10 ，b = 20）                                    |
| ------ | ------ | ---------------------------------------------------------- |
| +      | 加     | 俩个对象相加；a+b输出结果30                                |
| -      | 减     | 一个数减去另一个数；a-b输出结果-10                         |
| *      | 乘     | 俩个数相乘或是返回一个被重复若干次的字符串；a*b输出结果200 |
| /      | 除     | b/a输出结果2                                               |
| //     | 取整除 | 返回商的整数部分；9//2输出结果为4                          |
| %      | 取余   | 返回余数；b%a输出结果0                                     |
| **     | 指数   | a**b表示 a的b次方，输出结果100000000000000000000           |

+ **注意：** 混合运算时，优先级顺序为：** 高于 * / % // 高于+ -，为了避免歧义，建议使用()来处理运算优先级。

### 二、赋值运算符

| 运算符 | 描述       | 实例                                              |
| ------ | ---------- | ------------------------------------------------- |
| =      | 赋值运算符 | 把=号**右侧**的数值或运算结果赋给**左侧**的变量； |

### 三、复合赋值运算符

| 运算符 | 描述             | 实例                  |
| ------ | ---------------- | --------------------- |
| +=     | 加法赋值运算符   | c+=a等效于c=c+a       |
| -=     | 减法赋值运算符   | c-=a等效于c=c-a       |
| *=     | 乘法赋值运算符   | c\*=a等效于c=c\*a     |
| /=     | 除法赋值运算符   | c/=a等效于c=c/a       |
| %=     | 取模赋值运算符   | c%=a等效于c=c%a       |
| **=    | 幂赋值运算符     | c\*\*=a等效于c=c\*\*a |
| //=    | 取整除赋值运算符 | c//=a等效于c=c//a     |

