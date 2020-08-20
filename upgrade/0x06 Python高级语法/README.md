# 六、Python高级语法 2020.08.20

# 0x00：`property`属性

+ 什么是`property`属性

  `property`广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

+ 定义`property`属性

  **定义property属性有两种方式**

  + **装饰器方式**

  ```python
  class Person(object):
      def __init__(self):
          self.__age = 0
      @property
      def age(self):
          return self.__age
      @age.setter
      def age(self, new_age):
          if new_age >= 150:
              print('成精了')
          else:
              self.__age = new_age
  if __name__ == '__main__':
      p = Person()
      print(p.age)
      p.age = 100
      print(p.age)
      p.age = 150
      print(p.age)
  ```

  1. 在方法前加上`@property`表示将当前方法当做属性使用, 而且当对象获取属性时会执行下面修饰的方法
  2. 同时，在方法前加上`@方法名.setter`表示将当前方法作为属性使用，且在对象设置该属性值时，会执行下面修饰的方法
  3. 装饰器方式的property属性修饰的方法名一定要一样

  输出结果

  ```shell
  0
  100
  成精了
  100
  ```

  + 类属性方式

    + `property`介绍

      `property(参1, 参2)`

      1. 第一个参数是**获取属性时要执行的方法**

      2. 第二个参数是**设置属性时要执行的方法**

  ```python
  class Person(object):
      def __init__(self):
          self.__age = 0
      def get_age(self):
          """当获取age属性的时候会执行该方法"""
          return self.__age
      def set_age(self, new_age):
          """当设置age属性的时候会执行该方法"""
          if new_age >= 150:
              print("成精了")
          else:
              self.__age = new_age
      # 类属性方式的property属性
      age = property(get_age, set_age)
  # 创建person
  p = Person()
  print(p.age)
  p.age = 100
  print(p.age)
  p.age = 1000
  print(p.age)
  ```

  输出结果

  ```shell
  0
  100
  成精了
  100
  ```

-----

# 0x01：`with`语句与上下文管理器

### 一、`with`语句的使用

在前面的笔记中，就有使用`with`语句的栗子([Day6 文件](https://www.smartfox.cc/archives/4131/))；

在前面的文章中，我们使用`with`语句打开文件，这种写法不仅简单而且安全，在`with`语句执行完成后会自动调用关闭文件操作，即便出现了异常也能自动调用关闭文件操作。

```python
# 1、以写的方式打开文件
with open("fox.txt", "w") as _file:
    # 2、读取文件内容
    _file.write("hello world")
```

### 二、上下文管理器(ContextManager)

一个类只要实现了`__enter__()`与`__exit__()`这俩个**魔法方法**，通过这个类创建的对象我们将其称之为**上下文管理器**；

上下文管理器可以使用`with`语句，**with语句之所以这么强大，背后是由上下文管理器做支撑的**，也就是说刚才使用 open 函数创建的文件对象就是就是一个上下文管理器对象。

+ 举个栗子（定义一个File类，模拟使用`with`语句打开文件）

```python
class File(object):
    # 初始化方法
    def __init__(self, _name, _op):
        # 定义变量保存文件名和打开模式
        self.fileName = _name
        self.operator = _op
    # 上文方法
    def __enter__(self):
        print("进入上文方法")
        self.file = open(self.fileName,self.operator)
        return self.file
    # 下文方法
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('进入下文方法')
        if exc_type == None:
            print('PASS')
        else:
            print('Type: ', exc_type)
            print('Value:', exc_val)
            print('TreacBack:', exc_tb)
        # 返回值决定了捕获的异常是否继续向外抛出
        # 如果是 False 那么就会继续向外抛出，程序会看到系统提示的异常信息
        # 如果是 True 不会向外抛出，程序看不到系统提示信息，只能看到else中的输出
        return True


if __name__ == '__main__':
    # 使用with管理文件
    with File("fox.txt", "r") as file:
        _data = file.read()
        print(_data)
```

+ `__enter__`表示上文方法，需要返回一个操作文件对象
+ `__exit__`表示下文方法，with语句执行完成会自动执行，即使出现异常也会执行该方法。

输出结果

```shell
进入上文方法
文件内容
进入下文方法
PASS
```

------

# 0x02：生成器的创建方式

### 一、生成器的介绍

根据程序员制定的规则循环生成数据，当条件不成立时则生成数据结束。数据不是一次性全部生成出来，而是使用一个，再生成一个，可以**节约大量的内存**。

### 二、为什么要使用生成器

列表所有数据都在内存中，如果有海量数据的话将会非常耗内存。

如：仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

如果列表元素按照某种算法推算出来，那我们就可以在循环的过程中不断推算出后续的元素，这样就不必创建完整的list，**从而节省大量的空间**。

简单一句话：我又想要得到**庞大的数据**，又想让它**占用空间少**，那就用生成器！

### 三、创建生成器的方式

+ 生成器推导式

  与列表推导式类似，只不过生成器推导式使用小括号

  ```python
  # 创建生成器
  _generator = (i * 2 for i in range(5))
  _generator2 = (i * 2 for i in range(5))
  print(_generator)
  
  # next获取生成器下一个值
  value = next(_generator)
  value2 = next(_generator)
  print(value)
  print(value2)
  
  print('===' * 10)
  # 遍历生成器
  for value in _generator2:
      print(value)
  ```

  注意

  + `next` 函数获取生成器中的下一个值
  + `for` 循环遍历生成器中的每一个值

  输出结果

  ```shell
  <generator object <genexpr> at 0x00000201D846CD60>
  <generator object <genexpr> at 0x00000201D84C5C80>
  0
  2
  ==============================
  0
  2
  4
  6
  8
  ```

+ `yield`关键字

  + 只要在def函数里面看到有 yield 关键字那么他不再是一个普通的函数，而是一个生成器（generator）

  ```python
  def _generater(n):
      for i in range(n):
          print('开始第', i + 1, '次生成...')
          yield i
          print('完成第', i + 1, '次生成...')
  
  
  if __name__ == '__main__':
      _gener = _generater(3)
      # 从中生成一个值
      _point = next(_gener)
      print(_point)
  
      print('===' * 10)
      for i in _gener:
          print(i)
  ```

  注意

  + 代码执行到 yield 会暂停，然后把结果返回出去，下次启动生成器会在暂停的位置继续往下执行
  + 生成器如果把数据生成完成，再次获取生成器中的下一个数据会抛出一个StopIteration 异常，表示停止迭代异常
  + while 循环内部没有处理异常操作，需要手动添加处理异常操作
  + for 循环内部自动处理了停止迭代异常，使用起来更加方便，推荐大家使用。

  输出结果

  ```shell
  开始第 1 次生成...
  0
  ==============================
  完成第 1 次生成...
  开始第 2 次生成...
  1
  完成第 2 次生成...
  开始第 3 次生成...
  2
  完成第 3 次生成...
  ```

### 四、生成器的使用场景

数学中有个著名的斐波拉契数列（Fibonacci），数列中第一个数为0，第二个数为1，其后的每一个数都可由前两个数相加得到：

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

现在我们使用生成器来实现这个斐波那契数列，每次取值都通过算法来生成下一个数据, **生成器每次调用只生成一个数据，可以节省大量的内存。**

```python
def fibonacci(num):
    a = 0
    b = 1

    # 记录生成fibonacci数字的下标
    current_index = 0

    while current_index < num:
        result = a
        a, b = b, a + b
        current_index += 1
        # 代码执行到yield会暂停，然后把结果返回出去，下次启动生成器会在暂停的位置继续往下执行
        yield result

fib = fibonacci(5)
# 遍历生成的数据
for value in fib:
    print(value)
```

输出结果

```shell
0
1
1
2
3
```

------

# 0x03：深拷贝与浅拷贝

### 一、Python赋值

**直接赋值：**其实就是对象的引用（别名)

在前面的文章关于Python的赋值就已经有了详细的介绍，详细请跳转至[Day5 函数进阶与强化](https://www.smartfox.cc/archives/4129/)

```python
# 直接赋值
a = [1, 2, 3]
b = a
print(id(a), a)
print(id(b), b)

a[0] = 5  # 修改的是a
print(id(a), a)
print(id(b), b)
```

输出结果

```shell
2459767284672 [1, 2, 3]
2459767284672 [1, 2, 3]
2459767284672 [5, 2, 3]
2459767284672 [5, 2, 3]
```

![引用](https://oss.smartfox.cc/2020/08/20/7bdd156014af8.png)

### 二、浅拷贝

只对可变类型的**第一层对象**进行拷贝，对拷贝的对象开辟新的内存空间进行存储，不会拷贝对象内部的子对象，当子对象进行更改的时候，原始对象也会改变。

**常见操作：**

+ 列表的切片`[:]`操作、`list()`操作
+ 字典的`copy()`函数
+ copy模块的`copy()`函数

```python
import copy

# 浅拷贝
a = [1, 2, 3]
b = [11, 22, 33]
c = [111, 222, 333]

list01 = [a, b, c]
print('拷贝前,', id(list01))
list02 = copy.copy(list01)
# 查看list01 和 list02
print('拷贝后,', id(list01), list01)
print('拷贝后,', id(list02), list02)

print('===' * 10)
# 修改一下
a[0] = 5
print('拷贝后,', id(list01), list01)
print('拷贝后,', id(list02), list02)
```

输出结果

```shell
拷贝前, 1831390784832
拷贝后, 1831390784832 [[1, 2, 3], [11, 22, 33], [111, 222, 333]]
拷贝后, 1831390885440 [[1, 2, 3], [11, 22, 33], [111, 222, 333]]
==============================
拷贝后, 1831390784832 [[5, 2, 3], [11, 22, 33], [111, 222, 333]]
拷贝后, 1831390885440 [[5, 2, 3], [11, 22, 33], [111, 222, 333]]
```

![浅拷贝](https://oss.smartfox.cc/2020/08/20/b9f8674f36b0e.png)

### 三、深拷贝

只要发现对象有**可变类型**就会对该对象到最后一个可变类型的**每一层**对象就行拷贝, 对每一层拷贝的对象**都会开辟新的内存空间**进行存储。

**常见操作：**

+ copy模块的`deepcopy()`函数

```python
import copy

# 浅拷贝
a = [1, 2, 3]
b = [11, 22, 33]
c = [111, 222, 333]

list01 = [a, b, c]
print('拷贝前,', id(list01))
list02 = copy.deepcopy(list01)
#查看list01 和 list02
# 查看list01 和 list02
print('拷贝后,', id(list01), list01)
print('拷贝后,', id(list02), list02)

print('===' * 10)
# 修改一下
a[0] = 5
print('拷贝后,', id(list01), list01)
print('拷贝后,', id(list02), list02)
```

输出结果

```shell
拷贝前, 1663826111936
拷贝后, 1663826111936 [[1, 2, 3], [11, 22, 33], [111, 222, 333]]
拷贝后, 1663826208384 [[1, 2, 3], [11, 22, 33], [111, 222, 333]]
==============================
拷贝后, 1663826111936 [[5, 2, 3], [11, 22, 33], [111, 222, 333]]
拷贝后, 1663826208384 [[1, 2, 3], [11, 22, 33], [111, 222, 333]]
```

![深拷贝](https://oss.smartfox.cc/2020/08/20/ba7ab6b1218a4.png)