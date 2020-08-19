# 闭包与装饰器 2020.08.18

# 0x00：闭包

### 一、什么是闭包

+ 前言：

  我们前面已经学过了函数，我们知道当函数调用完，函数内定义的变量都销毁了，但是我们有时候需要保存函数内的这个变量，每次在这个变量的基础上完成一些列的操作，比如: 每次在这个变量的基础上和其它数字进行求和计算，那怎么办呢?

  我们就可以通过咱们今天学习的**闭包**来解决这个需求。

+ 闭包的定义：

  在函数嵌套的前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数，我们把这个**使用外部函数变量的内部函数称为闭包**。

### 二、闭包的构成条件

通过闭包的定义，我们可以得知闭包的形成条件:

1. 在函数嵌套(函数里面再定义函数)的前提下
2. 内部函数使用了外部函数的变量(还包括外部函数的参数)
3. 外部函数返回了内部函数

+ 举个栗子

  ```python
  # 定义一个外部函数
  def external(num1):
      # 定义一个内部函数
      def _inner(num2):
          # 内部函数使用了外部函数的变量(num1)
          print('num1的数值为', num1, 'num2的数值为', num2)
          result = num1 + num2
          print("结果是:", result)
      # 外部函数返回了内部函数，这里返回的内部函数就是闭包
      return _inner
  
  # 创建闭包实例
  func = external(1)
  # 执行闭包
  func(2)
  func(3)
  ```

  运行结果

  ```shell
  num1的数值为 1 num2的数值为 2
  结果是: 3
  num1的数值为 1 num2的数值为 3
  结果是: 4
  ```

  **闭包执行结果的说明:**

  通过上面的输出结果可以看出闭包保存了外部函数内的变量num1，每次执行闭包都是在num1 = 1 基础上进行计算。

  【执行过程图】TODO

### 三、闭包的作用

- 闭包可以保存外部函数内的变量，不会随着外部函数调用完而销毁。
- 闭包还可以提高代码的可重用性，不需要再手动定义额外的功能函数。

**注意点:**

- 由于闭包引用了外部函数的变量，则外部函数的变量没有及时释放，消耗内存。

### 四、修改闭包内使用的外部变量

+ 错误示范

  ```python
  # 定义一个外部函数
  def err_external(num1):
      # 定义一个内部函数
      def _inner(num2):
          # 这里本意想要修改外部num1的值，实际上是在内部函数定义了一个局部变量num1
          num1 = 10
          # 内部函数使用了外部函数的变量(num1)
          result = num1 + num2
          print("结果是:", result)
      print('调用内部函数前，闭包外：num1的数值为', num1)
      _inner(1)
      print('调用内部函数后，闭包外：num1的数值为', num1)
      # 外部函数返回了内部函数，这里返回的内部函数就是闭包
      return _inner
  
  # 创建闭包实例
  e_func = err_external(1)
  print('==='*10)
  # 执行闭包
  e_func(2)
  ```

  输出结果

  ```shell
  调用内部函数前，闭包外：num1的数值为 1
  结果是: 11
  调用内部函数后，闭包外：num1的数值为 1
  ==============================
  结果是: 12
  ```

+ 在闭包内可以使用`nonlocal`修饰变量以达到修改闭包外部变量的目的

+ 正确姿势

  ```python
  # 定义一个外部函数
  def r_external(num1):
      # 定义一个内部函数
      def _inner(num2):
          # 使用 nonlocal 修饰变量 num1 告诉解释器此处修改的为外部的变量num1
          nonlocal num1
          num1 = 10
          # 内部函数使用了外部函数的变量(num1)
          result = num1 + num2
          print("结果是:", result)
  
      print('调用内部函数前，闭包外：num1的数值为', num1)
      _inner(1)
      print('调用内部函数后，闭包外：num1的数值为', num1)
  
      # 外部函数返回了内部函数，这里返回的内部函数就是闭包
      return _inner
  
  # 创建闭包实例
  r_func = r_external(1)
  print('==='*10)
  # 执行闭包
  r_func(2)
  ```

  输出结果

  ```shell
  调用内部函数前，闭包外：num1的数值为 1
  结果是: 11
  调用内部函数后，闭包外：num1的数值为 10
  ==============================
  结果是: 12
  ```

--------

# 0x01：装饰器

### 一、什么是装饰器

+ 装饰器的定义

  Python中的装饰器就是用于拓展原来函数功能的一种函数，该函数的特殊之处在于它的返回值也是一个函数，使用Python装饰器的好处就是在**不用更改原函数代码的前提下**给函数**增加**新的功能。

  一般而言，我们要想拓展原来函数代码，比较直接的办法就是侵入代码里面修改。

  就是**给已有函数增加额外功能的函数，它本质上就是一个闭包函数**。

+ 装饰器的功能特点

  1. 不修改已有函数的源代码
  2. 不修改已有函数的调用方式
  3. 给已有函数增加额外的功能

+ 语法格式

  ```python
  # 装饰器的基本雏形
  def decorator(fn): # fn:目标函数.
      def inner():
          '''执行函数之前'''
          fn() # 执行被装饰的函数
          '''执行函数之后'''
      return inner
  ```

+ 举个栗子

  ```python
  def check(func):
      def inner():
          print("检查文件中....")
          func()
      return inner
  
  def read_file():
      print("正在读取文件中...")
  
  # 使用装饰器来装饰函数
  if __name__ == '__main__':
      read_file = check(read_file)
      read_file()
  ```

  执行结果

  ```shell
  检查文件中....
  正在读取文件中...
  ```

  **注意:**

  - 闭包函数有且只有一个参数，必须是函数类型，这样定义的函数才是装饰器。
  - 写代码要遵循开放封闭原则，它规定已经实现的功能代码不允许被修改，但可以被扩展。

### 二、装饰器的语法糖写法

如果有多个函数都需要添加登录验证的功能，每次都需要编写func = check(func)这样代码对已有函数进行装饰，这种做法还是比较麻烦。

Python给提供了一个装饰函数更加简单的写法，那就是语法糖，语法糖的书写格式是: @装饰器名字，通过语法糖的方式也可以完成对已有函数的装饰

```python
def check(func):
    def inner():
        print("检查文件中....")
        func()
    return inner

@check
def read_file():
    print("正在读取文件中...")

# 使用装饰器来装饰函数
if __name__ == '__main__':
    read_file()
```

运行结果

```shel
检查文件中....
正在读取文件中...
```

**注意:**

- @check 等价于 comment = check(comment)
- 装饰器的执行时间是加载模块时立即执行。

------

# 0x02：装饰器的使用

### 一、通用装饰器的使用

+ 装饰带有参数的函数

  ```python
  def check(func):
      def inner(_str):
          print("检查文件中....")
          func(_str)
      return inner
  
  @check
  def read_file(_str):
      print("正在读取文件中...")
      print('读取到文件：', _str)
  
  # 使用装饰器来装饰函数
  if __name__ == '__main__':
      read_file('苏苏の女装照.jpg')
  ```

  输出结果

  ```python
  检查文件中....
  正在读取文件中...
  读取到文件： 苏苏の女装照.jpg
  ```

+ 装饰带有返回值的函数

  ```python
  def check(func):
      def inner(_str):
          print("检查文件中....")
          _result = func(_str)
          return _result
      return inner
  
  @check
  def read_file(_str):
      print("正在读取文件中...")
      return '读取到文件：' + _str
  
  # 使用装饰器来装饰函数
  if __name__ == '__main__':
      _data = read_file('星尘の女装照.jpg')
      print(_data)
  ```

  输出结果

  ```shell
  检查文件中....
  正在读取文件中...
  读取到文件：星尘の女装照.jpg
  ```

+ 装饰带有不定长参数的函数

  ```python
  def check(func):
      def inner(*args, **kwargs):
          print("检查文件中....")
          func(*args, **kwargs)
      return inner
  
  @check
  def read_file(*args, **kwargs):
      print("正在读取文件中...")
      _data = ''
      for _info in args:
          _data += str(_info)
  
      for _info in kwargs.values():
          _data += str(_info)
      print('读取到文件：', _data)
  
  # 使用装饰器来装饰函数
  if __name__ == '__main__':
      read_file('星尘の女装照.jpg','苏苏の女装照.jpg')
  ```

  输出结果

  ```shell
  检查文件中....
  正在读取文件中...
  读取到文件：星尘の女装照.jpg苏苏の女装照.jpg
  ```

+ 通用装饰器

  ```python
  def check(func):
      def inner(*args, **kwargs):
          print("检查文件中....")
          _result = func(*args, **kwargs)
          return _result
      return inner
  
  @check
  def read_file(*args, **kwargs):
      print("正在读取文件中...")
      _data = ''
      for _info in args:
          _data += str(_info)
  
      for _info in kwargs.values():
          _data += str(_info)
      return '读取到文件：' + _data
  
  @check
  def write_file(_data):
      print('写入文件中...')
      print('文件写入成功：', _data)
      return True
  
  
  # 使用装饰器来装饰函数
  if __name__ == '__main__':
      _data = read_file('星尘の女装照.jpg', '苏苏の女装照.jpg')
      print(_data)
      print('==='*10)
      w_data = write_file('酷儿の私房照.jpg')
      print(w_data)
  ```

  输出结果

  ```shell
  检查文件中....
  正在读取文件中...
  读取到文件：星尘の女装照.jpg苏苏の女装照.jpg
  ==============================
  检查文件中....
  写入文件中...
  文件写入成功： 酷儿の私房照.jpg
  True
  ```

### 二、多个装饰器的使用

+ 多个装饰器的装饰过程是: 离函数最近的装饰器先装饰，然后外面的装饰器再进行装饰，由内到外的装饰过程

```python
def fox_say(func):
    def inner():
        return "狐狸：“" + func() + "”"
    return inner

def fox_tail(func):
    def inner():
        return func() + "，咪咕~"
    return inner

@fox_say
@fox_tail
def content():
    return "人生苦短，我用Python"

result = content()
print(result)
```

输出结果

```shell
狐狸：“人生苦短，我用Python，咪咕~”
```

### 三、带参数的装饰器

+ 使用带有参数的装饰器，其实是在装饰器外面又包裹了一个函数，使用该函数接收参数，返回是装饰器，因为 @ 符号需要配合装饰器实例使用

```python
def check_file(extension):
    def check(fn):
        def inner(_fileName):
            # 判断文件结尾是否为extension结尾，是则直接调用，反之加上extension
            if _fileName.endswith(extension):
                result = fn(_fileName)
            else:
                _fileName = _fileName + extension
                result = fn(_fileName)
            return result
        return inner
    return check

@check_file('.zip')
def road_file(_file):
    print('文件读取中...')
    print('读取到文件：', _file)

# 调用
road_file('星尘の女装合集')
print('===' * 10)
road_file('莉莉の私房照.zip')
```

### 四、类装饰器的使用

+ 不带参类装饰器

  ```python
  class Check(object):
      def __init__(self, fn):
          # 初始化操作在此完成
          self.__fn = fn
      # 实现__call__方法，表示对象是一个可调用对象，可以像调用函数一样进行调用。
      def __call__(self, *args, **kwargs):
          # 添加装饰功能
          print("请先登陆...")
          self.__fn()
  
  @Check
  def comment():
      print("发表评论")
  
  comment()
  ```

  代码说明

  + @Check 等价于 comment = Check(comment), 所以需要提供一个**init**方法，并多增加一个fn参数。
  + 要想类的实例对象能够像函数一样调用，需要在类里面使用**call**方法，把类的实例变成可调用对象(callable)，也就是说可以像调用函数一样进行调用。
  + 在**call**方法里进行对fn函数的装饰，可以添加额外的功能。

  输出结果

  ```shell
  请先登陆...
  发表评论
  ```

+ 带参的类装饰器

  ```python
  class Check(object):
      def __init__(self, extension):
          # 初始化操作在此完成
          self.__extension = extension
  
      # 实现__call__方法，表示对象是一个可调用对象，可以像调用函数一样进行调用。
      def __call__(self, fn):
          # 添加装饰功能
          def check(_fileName):
              if _fileName.endswith(self.__extension):
                  result = fn(_fileName)
              else:
                  _fileName = _fileName + self.__extension
                  result = fn(_fileName)
              return result
          return check
  
  
  @Check('.zip')
  def road_file(_file):
      print('文件读取中...')
      print('读取到文件：', _file)
  
  
  road_file('星尘の女装合集')
  print('===' * 10)
  road_file('莉莉の私房照.zip')
  ```

  输出结果

  ```shell
  文件读取中...
  读取到文件： 星尘の女装合集.zip
  ==============================
  文件读取中...
  读取到文件： 莉莉の私房照.zip
  ```