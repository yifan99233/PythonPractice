# Day 9 异常、模块 2020.07.28

# 0x00：异常

### 一、异常简介

+ 在程序在运行期间，错误可能产生于程序员没有预料到的各种情况，或者超出程序员可控范围的环境，例如用户的坏数据、试图打开一个不存在的文件等，这就是所谓的"**异常**"。
+ 为了能够及时有效地处理程序中的运行错误，Python专门引入了**异常类**
+ 注意： **异常不是语法错误**，语法错误，是程序写错了，异常是指程序已经运行后的非语法错误

### 二、常见的程序异常

| 异常类型                  | 异常说明                                           |
| :------------------------ | :------------------------------------------------- |
| BaseException             | 所有异常的基类                                     |
| SystemExit                | 解释器请求退出                                     |
| KeyboardInterrupt         | 用户中断执行(通常是输入^C)                         |
| Exception                 | 常规错误的基类                                     |
| StopIteration             | 迭代器没有更多的值                                 |
| GeneratorExit             | 生成器(generator)发生异常来通知退出                |
| StandardError             | 所有的内建标准异常的基类                           |
| ArithmeticError           | 所有数值计算错误的基类                             |
| FloatingPointError        | 浮点计算错误                                       |
| OverflowError             | 数值运算超出最大限制                               |
| ZeroDivisionError         | 除(或取模)零 (所有数据类型)                        |
| AssertionError            | 断言语句失败                                       |
| AttributeError            | 对象没有这个属性                                   |
| EOFError                  | 没有内建输入,到达EOF 标记                          |
| EnvironmentError          | 操作系统错误的基类                                 |
| IOError                   | 输入/输出操作失败                                  |
| OSError                   | 操作系统错误                                       |
| WindowsError              | 系统调用失败                                       |
| ImportError               | 导入模块/对象失败                                  |
| LookupError               | 无效数据查询的基类                                 |
| IndexError                | 序列中没有此索引(index)                            |
| KeyError                  | 映射中没有这个键                                   |
| MemoryError               | 内存溢出错误(对于Python 解释器不是致命的)          |
| NameError                 | 未声明/初始化对象 (没有属性)                       |
| UnboundLocalError         | 访问未初始化的本地变量                             |
| ReferenceError            | 弱引用(Weak reference)试图访问已经垃圾回收了的对象 |
| RuntimeError              | 一般的运行时错误                                   |
| NotImplementedError       | 尚未实现的方法                                     |
| SyntaxError               | Python 语法错误                                    |
| IndentationError          | 缩进错误                                           |
| TabError                  | Tab 和空格混用                                     |
| SystemError               | 一般的解释器系统错误                               |
| TypeError                 | 对类型无效的操作                                   |
| ValueError                | 传入无效的参数                                     |
| UnicodeError: Unicode     | 相关的错误                                         |
| UnicodeDecodeError        | Unicode 解码时的错误                               |
| UnicodeEncodeError        | Unicode 编码时错误                                 |
| UnicodeTranslateError     | Unicode 转换时错误                                 |
| Warning                   | 警告的基类                                         |
| DeprecationWarning        | 关于被弃用的特征的警告                             |
| FutureWarning             | 关于构造将来语义会有改变的警告                     |
| OverflowWarning           | 旧的关于自动提升为长整型(long)的警告               |
| PendingDeprecationWarning | 关于特性将会被废弃的警告                           |
| RuntimeWarning            | 可疑的运行时行为(runtime behavior)的警告           |
| SyntaxWarning             | 可疑的语法的警告                                   |
| UserWarning               | 用户代码生成的警告                                 |

### 三、异常处理

+ 处理异常的目的

  + 只要解释器检查到异常错误，默认执行的动作是终止程序
  + 处理异常目的：防止程序退出，保证程序正常执行

+ 捕获异常

  + try···except···
    + 把可能出现问题的代码，放在try中
    + 把处理异常的代码，放在except中
    + except后面没有指定异常类型，可以捕获任意类型的异常

  ```python
  try:
      可能发生异常的代码
  except:
        # 处理异常的代码
      1. 如果try里面发生异常
      2. 自动跳转到except里面
  ```

  + 捕获指定异常类型

  ```python
  try:
      可能发生异常的代码
  except 异常类型:
        处理异常的代码
  ```

  + except捕获多个异常

  ```python
  try:
      可能发生异常的代码
  except (异常类型1, 异常类型2):
        处理异常的代码
  ```

  + 获取异常的信息描述

  ```python
  try:
      可能发生异常的代码
  except 异常类型 as 异常对象名:
      print(异常对象名) 即可获取异常的信息描述
  ```

  + 捕获任意类型的异常.

  ```python
  try:
      可能发生异常的代码
  except Exception as 异常对象名:
      Exception 为异常类的父类
  ```

  + 异常中else
    + 在 if 中，它的作用是当条件不满足时执行的实行
    + 同样在 try...except... 中也是如此，即如果没有捕获到异常，那么就执行else中的事情

  ```python
  try:
      可能发生异常的代码
  except:
      处理异常的代码
  else:
      没有发生异常，except不满足执行else
  ```

  + try···except···else···finally···

  ```python
  try:
      可能发生异常的代码
  except:
      处理异常的代码
  else:
      没有发生异常，except不满足执行else
  finally:
      不管有没有异常，最终都要执行
  ```

### 四、异常传递

+ 异常传递特点

  + 如果异常在内部产生，如果内部不捕获处理，这个异常会向外部传递

+ 异常嵌套

  + try嵌套时，如果内层try没有捕获处理该异常，就会向外层try进行传递

  + 举个栗子

  ```python
  try:
      _file = open('苏苏の女装照.jpg', 'w')
  
      # 内部语句执行完，才向外部传递异常
      try:
          # 前面只写方式打开文件，不能读文件，产生异常
          # 内部没有捕获处理异常
          _data = _file.read()
          print(_data)
      finally:
          print('关闭文件')
          _file.close()
  
  except Exception as e:
      print('外层捕获异常：', e)
  ```

  输出结果

  ```shell
  关闭文件
  外层捕获异常： not readable
  ```

+ 函数嵌套

  + 函数嵌套时，如果内层函数没有捕获处理该异常，就会向外层函数进行传递
  + 举个栗子

  ```python
  def func1():
      print('start func1')
      print(a)
      print('end func1')
  
  
  def func2():
      print('start func2')
      func1()
      print('end func2')
  
  
  def func3():
      print('start func3')
      try:
          func2()
      except Exception as e:
          print('func3 got the err:', e)
      print('end func3')
  
  
  func3()
  ```

  输出结果

  ```python
  start func3
  start func2
  start func1
  func3 got the err: name 'a' is not defined
  end func3
  ```

### 五、自定义异常

+ 抛出自定义的异常

  + 用户可用 raise语句 来人为抛出一个异常。
  + 异常/错误对象必须有一个名字，且它们应是Error或Exception类的子类

  ```python
  class 自定义异常类名字(Exception):
      # 初始化类
      def __init__(self, 形参1, 形参2, ····):
          # 调用父类的init，做父类的初始化工作
          super().__init__()
          # ------ 自定义代码 ------ #
          
      # 重写__str__()，返回提示信息
      def __str__():
          return f'出现了异常···········'
  
  # 抛出异常
  raise 自定义异常类名字(实参1， 实参2，……)
  ```

----------

# 0x01：模块

### 一、模块介绍

+ 模块是一个由Python代码组成的文件，就是一个以`.py`结尾的文件。
+ 模块包含函数、类和变量，还可以包括可运行的代码。
+ 模块的主要作用：
+ 提高了代码的可维护性
  - 一个模块编写完毕之后，其他模块直接调用，不用再从零开始写代码了，节约了工作时间
  - 避免名字冲突

![模块](https://oss.smartfox.cc/2020/07/28/f51917b9ef2f0.png)

### 二、模块的导入

+ `import`导入模块

  + `import`导入模块，把整个模块都加载进来
  + 导入格式： `import 模块名`
  + 调用格式：`模块名.模块函数` `模块名.类名` `模块名.变量名`

+ `from···import···`导入模块中需要的内容

  + `from…import`可以只导入模块中需要使用的内容
  + 导入格式：`from 模块名 import 函数名, 类名, 变量名`
  + 调用格式：`函数名()` `对象 = 类名()` `print(变量名)`

+ `from···import *`导入模块中所有的内容

  + 通过`from···import *`可以导入该模块中所有的内容
  + 导入格式：`from 模块名 import *`
  + 调用格式：同上

+ `import···as···`给导入的模块取别名

  + 把复杂名字改简单些
  + 把已经同名的名字改一个不同名的名字

+ 模块搜索路径

  当你导入一个模块，Python解析器对模块位置的搜索顺序是：

  1. 当前目录
  2. 如果不在当前目录，Python则搜索系统路劲
  3. 模块搜索路径存储在system模块的sys.path变量中

### 三、模块制作

+ 定义自己的模块

  在Python中，每个Python文件都可以作为一个模块，模块的名字就是文件的名字。比如有这样一个文件`module.py`，在`module.py`中定义了所需的函数：

  ```python
  def my_add(a, b):
      """返回2个数相加结果"""
      return a+b
  
  
  def my_sub(a, b):
      """返回2个数相减结果"""
      return a-b
  ```

+ 调用自己定义的模块

  ```python
  import module
  
  _res = module.my_add(1, 1)
  print(_res)
  
  _res = module.my_sub(9, 1)
  print(_res)
  ```

  ![导入模块](https://oss.smartfox.cc/2020/07/28/417f70d9d3059.png)

+ 测试模块

  + 在实际开中，当一个开发人员编写完一个模块后，为了让模块能够在项目中达到想要的效果，这个开发人员会自行在模块文件中添加一些测试信息，例如：

  ```python
  # module.py
  def my_add(a, b):
      """返回2个数相加结果"""
      return a+b
  
  
  def my_sub(a, b):
      """返回2个数相减结果"""
      return a-b
  
  
  ret = my_add(2, 2)
  print('模块中测试代码：my_add(2, 2) = ', ret)
  ret = my_sub(10, 2)
  print('模块中测试代码：my_sub(10, 2) = ', ret)
  ```

  在`module.py`中的运行情况

  ```shell
  模块中测试代码：my_add(2, 2) =  4
  模块中测试代码：my_sub(10, 2) =  8
  ```

  **但是！**这样编写的模块在被调用的时候，会发生意想不到的结局，如下图所示：

  ![调用](https://oss.smartfox.cc/2020/07/28/9cd7fb742904d.png)

  从图中可以发现，在调用`module.py`时，以外的将`module.py`中的测试函数也执行了，则可不是一个好兆头！我们的需求是，**测试代码应该是在单独执行模块文件时，才会被调用**；而在被当做模块导入到其他文件时，**测试代码不应该被调用**！

+ `__name__`的使用

  + 直接运行此文件，`__name__`的结果为`__main__`
  + 此文件被当做模块文件导入时，`__name__`的结果不为`__main__`

  ![__name__](https://oss.smartfox.cc/2020/07/28/f4cf46b0d4bc1.gif)
  
  + 故我们可以将不想导包时执行的模块测试代码，放在`if __name__ == '__main__':`条件语句里面
  
  ![使用姿势](https://oss.smartfox.cc/2020/07/29/72fe6f20b2372.gif)
  
+ 模块中的`__all__`

  + 模块中`__all__`变量，**只对**`from xxx import *`这种导入方式有效
  + 模块中`__all__`变量包含的元素，才能会被`from xxx import *`导入
  + `__all__`格式：` __all__ = ['变量名', '类名', '函数名', ……]`

  ![__all__](https://oss.smartfox.cc/2020/07/29/6d26bc4292c8d.png)
