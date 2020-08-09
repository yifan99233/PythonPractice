# 一、Python 多任务编程 2020.08.06

# 0x00：前言

### 一、什么是多任务

+ 概念

  > 多任务处理是指用户可以在同一时间内运行多个应用程序，即同一时间，多个任务同时执行。

### 二、多任务的执行方式

+ 并发

  > 并发是指在同一时刻只能有一条指令执行，但多个进程指令被快速的轮换执行，使得在宏观上具有多个进程同时执行的效果，但在微观上并不是同时执行的，只是把时间分成若干段，使多个进程快速交替的执行。
  >
  > 通俗来讲，就是指两个或多个事件在同一时间间隔发生，即多个任务**交替**执行。

  ![并发](https://oss.smartfox.cc/2020/08/07/ab1f76c755184.png)

+ 并行

  > 并行是指在同一时刻，有多条指令在多个处理器上同时执行。所以无论从微观还是从宏观来看，二者都是一起执行的。
  
  ![并行](https://oss.smartfox.cc/2020/08/07/77991d4c9abd0.png)

-----

# 0x01：进程

### 一、什么是进程

+ 概念

  进程是指计算机中已运行的程序；在**面向进程**设计的系统（早期的UNIX和Linux2.4及更早的版本）中，进程是程序的执行实体；在**面向线程**设计的系统（现阶段大部分系统和Linux2.6及往后最新版本）中，进程不再是基本运行单位，而是承载**线程**的容器。

  简单来讲，现阶段的操作系统中，进程是系统进行资源分配的基本单位；一个运行的程序至少会创建一个进程，而一个进程中至少包含一个线程。

+ 作用

  使用多进程实现多任务

### 二、多进程

+ 多进程

  > 多进程即为一个程序通过创建多个进程以达到完成多任务的方式。

  ![多进程](https://oss.smartfox.cc/2020/08/07/d45647637f25b.png)

  + 多进程可以完成多任务，每个进程就好比一家独立的公司，每个公司都各自在运营，每个进程也各自在运行，执行各自的任务。

+ 多进程的使用

  + 进程类Process参数说明

    **Process([group [, target [, name [, args [, kwargs]]]]])**

    + group：指定进程组，目前只能使用None
    + target：执行的目标任务名
    + name：进程名字
    + args：以元组方式给执行任务传参
    + kwargs：以字典方式给执行任务传参

    **Process创建的实例对象的常用方法**

    + start()：启动子进程实例（创建子进程）
    + join()：等待子进程执行结束
    + terminate()：不管任务是否完成，立即终止子进程

  + 导入模块

  ```python
  import multiprocessing
  ```

  + 创建子进程对象

  ```python
  p1 = multiprocessing.Process(target=sing)
  p2 = multiprocessing.Process(target=dance)
  ```

  + 启动子进程

  ```python
  p1.start()
  p2.start()
  ```

+ 获取进程信息

  + 获取进程的对象

  ```python
  multiprocessing.current_process()
  ```

  + 获取进程的编号

  ```python
  os.getpid()
  ```

  + 获取父进程的编号

  ```python
  os.getppid()
  ```

  + 结束进程

  ```python
  os.kill('程序PID','执行信号')
  ```

  > `os.kill`只能用于UNIX平台上，这里的执行信号是UNIX系统中kill指令的所需的信号，如下图所示
  >
  > ![kill指令信号](https://oss.smartfox.cc/2020/08/07/1705253d7ef0d.png)
  >
  > 其中常用的有
  >
  > | 信号编号 | 信号名称 | 信号含义               |
  > | -------- | -------- | ---------------------- |
  > | 1        | SIGHUP   | 挂起信号               |
  > | 2        | SIGINT   | 中断信号（同Ctrl + C） |
  > | 3        | SIGQUIT  | 退出信号（同Ctrl + \） |
  > | 9        | SIGKILL  | 杀死信号               |
  > | 11       | SIGSEGV  | 段错误信号             |
  > | 15       | SIGTERM  | 终止信号（默认）       |
  > | 18       | SIGCONT  | 继续运行信号           |
  > | 19       | SIGSTOP  | 暂停信号（同Ctrl + Z） |

+ 进程执行带有参数的任务

  + 以元组方式传参`args`

  ```python
  import multiprocessing
  
  def task(count):
      print('复读鸡获得了任务，复读', count, '次')
      for i in range(count):
          print("我是复读鸡！")
      else:
          print("任务执行完成")
  
  if __name__ == '__main__':
      # 创建子进程
      # args: 以元组的方式给任务传入参数
      sub_process = multiprocessing.Process(target=task, args=(5,))
      sub_process.start()
  ```

  + 以字典方式传参`kwargs`

  ```python
  import multiprocessing
  
  def task(count):
      print('复读鸡获得了任务，复读', count, '次')
      for i in range(count):
          print("我是复读鸡！")
      else:
          print("任务执行完成")
  
  if __name__ == '__main__':
      # 创建子进程
      # kwargs: 表示以字典方式传入参数
      sub_process = multiprocessing.Process(target=task, kwargs={"count": 3})
      sub_process.start()
  ```

+ 多进程的注意点

  + 进程之间不共享全局变量

    + 创建子进程会对主进程资源进行拷贝，也就是说子进程是主进程的一个副本


  ```python
  import multiprocessing
  
  # 定义全局变量
  _list = list()
  
  # 添加数据的任务
  def add_data():
      for i in range(5):
          _list.append(i)
      # 代码执行到此，说明数据添加完成
      print("写入子进程读出数据：", _list)
  
  def read_data():
      print("读取子进程读出数据：", _list)
  
  if __name__ == '__main__':
      # 创建添加数据的子进程
      add_data_process = multiprocessing.Process(target=add_data)
      # 创建读取数据的子进程
      read_data_process = multiprocessing.Process(target=read_data)
      # 启动子进程执行对应的任务
      add_data_process.start()
      # 主进程等待添加数据的子进程执行完成以后程序再继续往下执行，读取数据
      add_data_process.join()
      read_data_process.start()
      print("主进程读取数据：", _list)
  ```

  输出结果

  ```shell
  写入子进程读出数据： [0, 1, 2, 3, 4]
  主进程读取数据： []
  读取子进程读出数据： []
  ```

  ![图](https://oss.smartfox.cc/2020/08/07/e2b1fd76b57d8.png)

  + 主进程会等待所有的子进程执行结束再结束

    > 主进程会等待所有的子进程完成各自任务后才会退出运行

  + 如何让主进程结束时同时销毁所有子进程

    + 守护主进程
      + 守护主进程就是主进程退出子进程销毁不再执行

    ```python
    子进程对象.daemon = True
    ```

    + 销毁子进程
      + 传递结束信号给子进程，让子进程执行结束

    ```python
    子进程对象.terminate()
    ```

----------

# 0x02：线程

### 一、什么是线程

+ 线程的介绍

  线程是**操作系统**能够进行**运算调度**的最小单位；大部分情况下，它被包含在进程之中，是进程中的实际运作单位。一条线程指的是进程中一个单一顺序的控制流，一个进程中可以并发多个线程，每条线程并行执行不同的任务；

  在Python中，想要实现多任务除了使用进程，还可以使用线程来完成，线程是实现多任务的另外一种方式。

+ 线程的概念

  线程是进程中执行代码的一个分支，每个执行分支（线程）要想工作执行代码需要cpu进行调度 ，也就是说线程是cpu调度的基本单位，每个进程至少都有一个线程，而这个线程就是我们通常说的主线程。

+ 线程的作用

  可以通过多线程来实现多任务

  ![线程](https://oss.smartfox.cc/2020/08/07/9b3b0e8f5889e.png)

### 二、多线程

+ 多线程的使用

  + 线程类`Thread`参数说明

    `Thread([group [, target [, name [, args [, kwargs]]]]])`

    - group: 线程组，目前只能使用None
    - target: 执行的目标任务名
    - args: 以元组的方式给执行任务传参
    - kwargs: 以字典方式给执行任务传参
    - name: 线程名，一般不用设置

  + 导入线程模块

  ```python
  import threading
  ```

  + 创建线程对象

  ```python
  t1 = threading.Thread(target=sing)
  t2 = threading.Thread(target=dance)
  ```

  + 启动线程

  ```python
  t1.start()
  t2.start()
  ```

+ 获取线程信息

  + 返回线程对象

  ```python
  threading.current_thread()
  ```

+ 线程执行带参的任务

  + 以元组方式传参`args`

  ```python
  import threading
  
  def task(count):
      print('复读鸡获得了任务，复读', count, '次')
      for i in range(count):
          print("我是复读鸡！")
      else:
          print("任务执行完成")
  
  if __name__ == '__main__':
      # args: 以元组的方式给任务传入参数
      sub_thread = threading.Thread(target=task, args=(5,))
      sub_thread.start()
  ```

  + 以字典方式传参`kwargs`

  ```python
  import threading
  
  def task(count):
      print('复读鸡获得了任务，复读', count, '次')
      for i in range(count):
          print("我是复读鸡！")
      else:
          print("任务执行完成")
  
  if __name__ == '__main__':
      # kwargs: 表示以字典方式传入参数
      sub_thread = threading.Thread(target=task, kwargs={"count": 3})
      sub_thread.start()
  ```

+ 多线程的注意点

  + 多线程的执行是无序的

  + 主线程会等待所有子线程执行完成后才退出

    > 主线程会等待所有的子线程完成各自任务后才会退出运行

  + 如何让主线程结束时同时销毁所有子线程

    + 守护线程

    ```python
    # 1. 方法1 
    t1 = threading.Thread(target=task, daemon=True)
    # 2. 方法2
    t1 = threading.Thread(target=task)
    t1.setDaemon(True)
    # 3. 方法3
    t1 = threading.Thread(target=task)
    t1.daemon = True
    ```

  + 与进程不同，线程之间是共享全局变量的

  + 线程之间共享全局变量数据可能会出现资源竞争问题

    + 解决方法
      1. 线程同步（`线程.join()`）
      2. 互斥锁

-----

# 0x03：锁

### 一、互斥锁

+ 互斥锁的概念

  + 对共享数据进行锁定，保证同一时刻只能有一个线程去操作。
  + 互斥锁是**多个线程一起去抢**，抢到锁的线程先执行，没有抢到锁的线程需要等待，等互斥锁使用完释放后，其它等待的线程再去抢这个锁。

+ 互斥锁的使用

  + 创建锁 `mutex = threading.Lock()`

  + 上锁 `mutex.acquire()`
  + 释放锁`mutex.release()`
  + 注意点
    + **acquire和release方法之间的代码同一时刻只能有一个线程去操作**
    + **如果在调用acquire方法的时候 其他线程已经使用了这个互斥锁，那么此时acquire方法会堵塞，直到这个互斥锁释放后才能再次上锁。**


### 二、死锁

+ 概念

  **死锁**又称作为**死结**；当**两**个以上的运算单元，双方都在等待对方停止运行，以获取系统资源，但是没有一方提前退出时，就称为死锁。

--------

# 0x04：进程和线程的对比

### 一、关系对比

* 线程依附进程，有进程才有线程
* 一个进程默认有一个线程，也可以有多个线程

### 二、区别对比

+ 全局变量
  + 进程不共享全局变量
  + 线程可以共享全局变量，出现资源竞争问题，可以通过互斥锁和线程同步来解决
+ 开销上
  + 创建进程的开销比创建线程的开销大
+ 概念上
  + 进程是操作系统资源分配的单位
  + 线程是CPU调度的单位
+ 关系上
  + 线程依附进程存在，不能单独存在
+ 稳定性上
  + 多进程编程比单进程多线程稳定性更好

### 三、优缺点对比

+ 进程
  + **优点：**稳定性高、可以使用多核
  + **缺点：**开销大
+ 线程
  + **优点：**开销小
  + **缺点：**不能使用多核

------

# 0x05：协程

### 一、什么是协程

+ 什么是协程

  + **协程（Coroutine）**是计算机程序的一类组件，又称微线程，纤程，是一种协作式多任务执行方式，它允许程序在执行过程中被挂起和恢复；
  + 相对于其他多任务工作方式，协程更为灵活

+ 协作式多任务与抢占式多任务

  + 协作式多任务

    **协作式多任务（Cooperative Multitasking）**是一种实现多任务处理（multi task）的方式，多任务是使电脑能同时处理多个程序的技术，相对于抢占式多任务(Preemptive multitasking)，协作式多任务要求每一个运行中的程序，定时放弃自己的运行权利，告知操作系统可让下一个程序运行；也就是说下一个进程被调度的**前提**是当前进程**主动**放弃时间片。

  + 抢占式多任务

    **抢占式多任务处理（Preemption）**是计算机操作系统中，一种实现多任务处理（multi task）的方式，相对于**协作式多任务（Cooperative Multitasking）**而言，抢占式环境下，操作系统完全决定进程调度方案，**操作系统可以剥夺耗时长的进程的时间片**，提供给其它进程。

### 二、协程的优点

+ 最大的优势就是协程**极高的执行效率**。因为函数切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
+ 第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。

### 三、协程的使用

+ gevent

  + 安装

  ```shell
  pip install gevent
  ```

  + 导入gevent模块

  ```python
  import gevent
  ```

  + 创建协程对象

  ```python
  g1 = gevent.spawn(sing)
  g2 = gevent.spawn(dance)
  ```

  + 等待协程执行

  ```python
  g1.join()  # 主线程等待g1协程执行完成 （耗时操作）
  g2.join()  # 主线程等待g2协程执行完成 （耗时操作）
  ```

  + 举个栗子

  ```python
  # 注意： gevent是遇到耗时操作， 自动切换
  # 哪些是耗时操作: g1.join() gevent.sleep(1)
  import gevent
  
  def sing():
      for i in range(3):
          print("唱歌...")
          gevent.sleep(1) # 出现耗时操作、挂起
  
  def dance():
      for i in range(3):
          print("跳舞...")
          gevent.sleep(1) # 出现耗时操作、挂起
  
  if __name__ == '__main__':
      g1 = gevent.spawn(sing)
      g2 = gevent.spawn(dance)
  
      g1.join()  # 主线程等待g1协程执行完成 （耗时操作）
      g2.join()  # 主线程等待g2协程执行完成 （耗时操作）
  ```

  输出结果

  ```shell
  唱歌...
  跳舞...
  唱歌...
  跳舞...
  唱歌...
  跳舞...
  
  Process finished with exit code 0
  ```

+ 猴子补丁

  为了解决gevent不识别其他的耗时操作的缺点，我们可以给他打上”猴子“补丁；这样它就能识别`time.sleep`、`socket`、`send`、`recv`等耗时操作了。

  + 导入补丁

  ```python
  from gevent import monkey
  ```

  + 打补丁

  ```python
  monkey.patch_all()
  ```

  + 举个栗子

  ```python
  import gevent
  import time
  from gevent immport monkey
  
  monkey.patch_all() # 打补丁
  
  def sing():
      for _ in range(3):
          print('singing~')
          time.sleep(1)
          
  def dance():
      for _ in range(3):
          print('dancing~')
          gevent.sleep(1)
  
  if __name__ == '__main__':
      g1 = gevent.spawn(sing)
      g2 = gevent.spawn(dance)
      g1.join()
      g2.join()
  ```

  输出结果

  ```shell
  singing~
  dancing~
  singing~
  dancing~
  singing~
  dancing~
  
  Process finished with exit code 0
  ```

