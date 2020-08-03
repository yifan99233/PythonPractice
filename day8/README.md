# Day8 面向对象2 继承、属性、方法 2020.07.26

# 0x00：私有权限

+ 私有属性

  + 如果在属性名前面加了2个下划线'__'，则表明该属性是私有属性，否则为公有属性
  + **私有属性只能在类的内部访问**
  + 举个栗子

  ```python
  class Fox(object):
      def __init__(self):
          self.__tail_count = 0 # 私有属性，只能在类内访问
          self.age = 24 # 公有属性
     
  	def get_info(self):
          print(self.__tail_count)
  ```

+ 私有方法

  + 私有方法和私有属性类似，在方法名前面加了2个下划线'__'，则表明该方法是私有方法
  + **私有方法只能在类内部使用**
  + 举个栗子

  ```python
  class Fox(object):
      def __init__(self):
          self.__tail_count = 0 # 私有属性，只能在类内访问
          self.age = 24 # 公有属性
     
  	def get_info(self):
          print(self.__tail_count)
          self.__levelup()
          print('升级了！', self.__tail_count)
      
      def __levelup(self): # 私有方法，只能在类内调用
          self.__tail_count += 1
  ```

-------

# 0x01：继承

### 一、什么是继承

+ 在程序中，继承描述的是指的是**类与类之间的关系**

![继承](https://oss.smartfox.cc/2020/07/26/464a3e6240957.png)

+ 站在**父类**的角度来看，**父类**派生出**子类**
+ 站在**子类**的角度来看，**子类**继承于**父类**
+ **父类**也叫**基类**，**子类**也叫**派生类**

### 二、继承的作用

+ **继承：**子类直接具备父类的能力（属性和方法）
+ **作用：**解决代码重用问题，提高开发效率

### 三、继承的语法格式

```python
class 子类名(父类名):
    pass
```

+ 子类对象调用方法有一个就近原则
  - 如果本类能找到方法，直接调用本类的方法
  - 如果本类找不到，则调用父类继承过来的方法

### 四、单继承和多层继承

+ 单继承：子类只继承一个父类

  ```python
  class Animal(object):
      def eat(self):
          print('吃东西')
  
  class Fox(Animal):
      pass
  
  _fox = Fox()
  _fox.eat()
  ```

+ 多层继承：继承关系为多层传递

  ```python
  class Animal(object):
      def eat(self):
          print('吃东西')
  
  class Fox(Animal):
      def say(self):
          print('大楚兴，陈胜王')
  
  class SmartFox(Fox):
      pass
  
  _fox = SmartFox()
  _fox.eat()
  _fox.say()
  ```

### 五、重写父类方法

+ 子类重写父类同名方法
  + 父类的方法不能满足子类的需要，可以对父类的方法重写，重写父类方法的目的是为了给他扩展功能
  + 在子类中定义了一个和父类同名的方法(参数也一样)，即为对父类的方法重写
  + 子类调用同名方法，默认只会调用子类的
  
  ```python
  class Animal(object):
      def eat(self):
          print('动物在吃东西')
  
  class Fox(Animal):
      def say(self):
          print('大楚兴，陈胜王')
      
      def eat(self):
          print('狐狸在吃东西')
          
          
  _fox = Fox()
  _fox.eat()
  ```
  
  输出结果
  
  ```shell
  狐狸在吃东西
  ```
  
+ 多层继承下，子类调用父类同名方法
  + 子类调用父类同名方法：
    1. `父类名.同名方法(self, 形参1, ……)`
    2. `super(子类名, self).同名方法(形参1, ……)`
    3. `super().同名方法(形参1, ……)`：是方法 2 的简写，推荐的写法
  
  ```python
  class Animal(object):
      def eat(self):
          print('动物在吃东西')
  
  
  class Fox(Animal):
      def say(self):
          print('大楚兴，陈胜王')
  
      def eat(self):
          print('通过父类名调用同名方法')
          Animal.eat(self)
          print('通过super(类名, self)调用同名方法')
          super(Fox, self).eat()
          print('通过super()调用同名方法')
          super().eat()
          print('狐狸在吃东西')
  
  
  _fox = Fox()
  _fox.eat()
  ```
  
  输出结果
  
  ```shell
  通过父类名调用同名方法
  动物在吃东西
  通过super(类名, self)调用同名方法
  动物在吃东西
  通过super()调用同名方法
  动物在吃东西
  狐狸在吃东西
  ```

-------

# 0x02：多继承

### 一、什么是多继承

+ 所谓多继承，即子类有多个父类，并且具有它们的特征。

+ 多继承的语法格式：

  ```python
  class 子类名(父类1, 父类2, ……)：
      pass
  ```

### 二、类的继承顺序

+ 查看类的继承顺序：`类名.__mro__`

  ```python
  class WhiteFox(object):
      def talk(self):
          print('白色狐狸')
  
  
  class BlackFox(object):
      def talk(self):
          print('黑色狐狸')
  
  
  class PinkFox(object):
      def talk(self):
          print('粉色狐狸')
  
  
  class Fox(PinkFox, WhiteFox, BlackFox):
      pass
  
  
  print(Fox.__mro__)
  ```

  输出结果

  ```shell
  (<class '__main__.Fox'>, <class '__main__.PinkFox'>, <class '__main__.WhiteFox'>, <class '__main__.BlackFox'>, <class 'object'>)
  ```

### 三、多继承下，子类调用父类同名方法

+ 默认调用情况
  
  + 如果继承过来的2个父类的方法同名，默认调用先继承父类的同名方法
  
+ 多继承下，子类调用父类同名方法
  1. `父类名.同名方法(self, 形参1, ……)`：调用指定的父类
  2. `super(类名, self).同名方法(形参1, ……)`：调用继承顺序中类名的下一个类的同名方法
  3. `super().同名方法(形参1, ……)`：调用先继承父类的同名方法
  
  ```python
  class WhiteFox(object):
      def talk(self):
          print('白色狐狸')
  
  
  class BlackFox(object):
      def talk(self):
          print('黑色狐狸')
  
  
  class PinkFox(object):
      def talk(self):
          print('粉色狐狸')
  
  
  class Fox(PinkFox, WhiteFox, BlackFox):
      def talk(self):
          print('通过类名调用父类方法')
          WhiteFox.talk(self)
          print('通过super(类名, self)调用同名方法')
          super(WhiteFox, self).talk()
          print('通过super()调用方法')
          super().talk()
  
  
  print(Fox.__mro__)
  _fox = Fox()
  _fox.talk()
  ```
  
  输出结果
  
  ```shell
  (<class '__main__.Fox'>, <class '__main__.PinkFox'>, <class '__main__.WhiteFox'>, <class '__main__.BlackFox'>, <class 'object'>)
  通过类名调用父类方法
  白色狐狸
  通过super(类名, self)调用同名方法
  黑色狐狸
  通过super()调用方法
  粉色狐狸
  ```

### 四、私有和继承

+ 父类中的私有方法、属性不能直接继承使用
+ 可以通过调用继承的父类的共有方法，间接的访问父类的私有方法、属性

### 五、多态

+ 多态：多种形态，调用同一个函数，不同表现
+ 因为Python是动态语言，站在用户的角度，本身就是多态，不存在非多态的情况
+ 实现多态的步骤:
  1. 实现继承关系
  2. 子类重写父类方法
  3. 通过对象调用该方法

---------------------

# 0x03：实例属性、类属性

### 一、实例属性和类属性

+ 实例属性

  + 通过在`__init__`方法里面给实例对象添加的属性
  + 在类的外面，直接通过实例对象添加的属性
  + **实例属性**必须通过**实例对象**才能访问

  ```python
  # 定义类
  class 类名(object):
      def __init__(self):
          self.实例属性变量1 = 数值1
          self.实例属性变量2 = 数值3
  
  # 创建实例对象
  实例对象名 = 类名()
  
  # 添加属性
  实例对象名.实例属性变量3 = 数值3
  ```

+ 类属性

  + 类属性就是 **类对象** 所拥有的属性，它被 **该类的所有实例对象 所共有**。
  + 定义在**类里面，类方法外面**的变量就是**类属性**
  + 类属性可以使用 **类名** 或 **实例对象** 访问，**推荐使用类名访问**

  ```python
  # 定义类
  class 类名(object):
      类属性变量 = 数值1
  
      def __init__(self):
          pass
  ```

### 二、类属性和实例属性的区别

+ 类属性就是 **类对象** 所拥有的属性，它被 **该类的所有实例对象 所共有**。

+ **实例属性** 要求 **每个对象** 为其 **单独开辟一份内存空间** ，只属于某个实例对象的

  ```python
  class Fox(object):
      # 类属性
      count = 0
  
      def __init__(self, _name):
          # 实例属性
          self.name = _name
  
          # 每初始化一次，类属性数量加1
          Fox.count += 1
  
  
  # 打印类属性的值
  print(Fox.count)
  
  # 创建1个对象
  f1 = Fox('狐白')
  # 打印：实例属性，类属性
  print(f1.name, Fox.count)
  
  f2 = Fox('苏苏')
  print(f2.name, Fox.count)
  
  f3 = Fox('铃兰')
  print(f3.name, Fox.count)
  
  # 通过实例对象，访问类属性
  print(f1.count, f2.count, f3.count)
  ```

  输出结果

  ```shell
  0
  狐白 1
  苏苏 2
  铃兰 3
  3 3 3
  ```

  ![流程图](https://oss.smartfox.cc/2020/08/03/4f318196f8e3e.png)

### 三、注意点

+ 修改类属性

  + **类属性只能通过类对象修改，不能通过实例对象修改**

  ```python
  class Fox(object):
      # 类属性
      age = 0
  
  
  # 打印类属性的值
  print('Fox:', Fox.age)
  
  _fox = Fox()
  _fox.age = 500
  
  print('Fox:', Fox.age, '_fox :', _fox.age)
  
  Fox.age = 1000
  print('Fox:', Fox.age, '_fox :', _fox.age)
  ```

  输出结果

  ```shell
  Fox: 0
  Fox: 0 _fox : 500
  Fox: 1000 _fox : 500
  ```

  ![流程图](https://oss.smartfox.cc/2020/08/03/c8e71d99ef358.png)

+ 类属性和实例属性同名

  + 如果类属性和实例属性同名，实例对象名只能操作实例属性
  + 结论：**操作类属性建议使用类名**，避免不必要的麻烦

+ 私有类属性

  + 类属性也可以设置为 **私有**，前边添加两个下划线`__`

  ```python
  class Fox(object):
      # 类属性
      __count = 0
  
  print(Fox.__count)  # 类的外面，不能直接访问私有类属性，
  ```

---------

# 0x04：类方法、静态方法

### 一、类方法

+ **类对象所拥有的方法**，主要为了在没有创建实例对象前提下，处理类属性

+ 需要用装饰器`@classmethod`来标识其为类方法

+ 对于类方法，**第一个参数必须是类对象(代表类)**，一般以`cls`作为第一个参数，这个参数不用人为传参，解释器会自动处理

  ```python
  class Fox(object):
      # 类属性
      count = 0
  
      # 定义类方法
      @classmethod
      def get_count(cls):  # 参数cls代表当前的类
          print('count = ', cls.count)
  
  
  # 调用类方法
  Fox.get_count()
  ```

### 二、静态方法

+ 需要通过装饰器`@staticmethod`来进行修饰，**静态方法默认情况下, 既不传递类对象也不传递实例对象（形参没有self/cls）**。

+ 当方法中 **既不需要使用实例对象**，**也不需要使用类对象**时，定义静态方法

+ **取消不需要的参数传递**，有利于 **减少不必要的内存占用和性能消耗**

+ 静态方法 也能够通过 **实例对象** 和 **类对象(类名)** 去访问。

  ```python
  class Fox(object):
      # 定义静态方法
      @staticmethod
      def talk():
          print('这是一个静态方法，不用使用实例对象也不用类对象')
  
  
  # 调用静态方法
  Fox.talk()
  ```

  