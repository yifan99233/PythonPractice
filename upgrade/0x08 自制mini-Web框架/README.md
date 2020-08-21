# 0x00：Web框架概述

+ **Web服务器：**运行于计算机中，通过HTTP（超文本传输协议）为用户提供静态资源（CSS/JS/HTML等无须服务器进行动态处理的文件）。
+ **Web框架：**是特定语言编写的框架程序（是一坨代码的集合），一般用于处理Web服务器无法处理的动态数据请求。
+ 简单来说，**Web服务器**封装的是socket，**Web框架**封装的是response和request

![web服务器都做了什么](https://oss.smartfox.cc/2020/08/21/c8e720744f975.jpg)

+ 从用户请求页面到服务器响应，服务器都做了些什么？

  + 当Web服务器接收用户浏览器发起的请求后，将请求进行分类，若是请求静态资源则直接从系统中读取并返回，而动态资源请求则将其交付给应用服务器进行处理
  + Web框架负责接收来自Web服务器交付过来的动态资源请求，通过检索数据库、读取模板文件等生成用户所请求的资源数据后将处理结果交付给Web服务器
  + Web服务器将响应结果发送给浏览器

+ **静态资源**：一般是指JS、CSS、IMG等不需要经过服务器动态处理的文件。

+ **动态资源**：一些需要服务器动态处理的资源，例如在某宝中查询个人的购买的商品、检索不同店铺中上架的商品、查看博客园中不同博主发表的文章等；这些资源需要后端服务器查询数据库，结合模板文件生成对应的页面，每一个用户看到的页面可能都是不同的。

+ **WSGI**：WSGI 全称是 **Web Server Gateway Interface**，Web服务器网关接口，是一种在 Web 服务器和 Python Web 应用程序框架之间的标准接口。也就是说，只要 web服务器和 web应用都遵守WSGI协议，那么 web服务器和 web应用就可以随意的组合。

  [![WSGI大法好（摘自selfboot）](https://oss.smartfox.cc/2020/08/21/e83329e5081dd.jpeg)](https://selfboot.cn/2016/07/28/forum_design_framework/)

------

# 0x01：框架程序开发

### 一、主程序开发

+ 框架的职责
  + 接收Web服务器的动态资源请求，给Web服务器提供处理动态资源请求的服务。
+ 动静态资源判断
  + 在资源判断上，可以通过请求资源的后缀名来判断浏览器请求的是动态资源还是静态资源
  + 也就是说只要客户端请求的不是常见静态资源后缀，则将请求交付给后端应用服务器
  + 在本文中，我们约定当遇到`.py`后缀的请求则认为用户请求的是动态资源

```python
import socket,threading,sys
import framework

# 定义web服务器类
class HttpWebServer(object):
    def __init__(self, port):
        # 创建tcp服务端套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口号复用, 程序退出端口立即释放
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口号
        tcp_server_socket.bind(("", port))
        # 设置监听
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket

    # 处理客户的请求
    @staticmethod
    def handle_client_quest(new_socket):
        # 代码执行到此，说明连接建立成功
        recv_client_data = new_socket.recv(4096)
        if len(recv_client_data) == 0:
            print("关闭浏览器了")
            # 关闭服务与客户端的套接字
            new_socket.close()
            return

        # 对二进制数据进行解码
        recv_client_content = recv_client_data.decode("utf-8")
        print(recv_client_content)
        # 根据指定字符串进行分割， 最大分割次数指定2
        request_list = recv_client_content.split(" ", maxsplit=2)

        # 获取请求资源路径
        request_path = request_list[1]
        print(request_path)

        # 判断请求的是否是根目录，如果条件成立，指定首页数据返回
        if request_path == "/":
            request_path = "/index.html"

        # 判断是否是动态资源请求
        if request_path.endswith(".py"):
            """这里是动态资源请求，把请求信息交给框架处理"""
            # 字典存储用户的请求信息
            env = {
                "request_path": request_path
            }

            # 获取处理结果
            status, headers, response_body = framework.handle_request(env)

            # 使用框架处理的数据拼接响应报文
            # 响应行
            response_line = "HTTP/1.1 %s\r\n" % status
            # 响应头
            response_header = ""
            # 遍历头部信息
            for header in headers:
                # 拼接多个响应头
                response_header += "%s: %s\r\n" % header
            response_data = (response_line +
                             response_header +
                             "\r\n" +
                             response_body).encode("utf-8")
            # 发送数据
            new_socket.send(response_data)
            # 关闭socket
            new_socket.close()

        else:
            """这里是静态资源请求"""
            try:
                # 动态打开指定文件
                with open("static" + request_path, "rb") as file:
                    # 读取文件数据
                    file_data = file.read()
            except Exception as e:
                # 请求资源不存在，返回404数据
                # 响应行
                response_line = "HTTP/1.1 404 Not Found\r\n"
                # 响应头
                response_header = "Server: FoxServ1.0\r\n"
                with open("static/error.html", "rb") as file:
                    file_data = file.read()
                # 响应体
                response_body = file_data

                # 拼接响应报文
                response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
                # 发送数据
                new_socket.send(response_data)
            else:
                # 响应行
                response_line = "HTTP/1.1 200 OK\r\n"
                # 响应头
                response_header = "Server: FoxServ1.0\r\n"

                # 响应体
                response_body = file_data

                # 拼接响应报文
                response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
                # 发送数据
                new_socket.send(response_data)
            finally:
                # 关闭服务与客户端的套接字
                new_socket.close()

    def start(self):
        while True:
            # 等待接受客户端的连接请求
            new_socket, ip_port = self.tcp_server_socket.accept()
            sub_thread = threading.Thread(target=self.handle_client_quest, args=(new_socket,))
            # 设置守护线程
            sub_thread.setDaemon(True)
            sub_thread.start()


# 程序入口函数
def main():

    # 获取命令行参数判断长度
    if len(sys.argv) != 2:
        print("执行命令如下: python3 xxx.py 9000")
        return

    # 判断端口号是否是数字
    if not sys.argv[1].isdigit():
        print("执行命令如下: python3 xxx.py 9000")
        return

    # 需要转成int类型
    port = int(sys.argv[1])

    # 创建web服务器
    web_server = HttpWebServer(port)
    # 启动web服务器
    web_server.start()


if __name__ == '__main__':
    main()
```

+ 处理客户端的动态资源请求
  1. 创建web框架程序
  2. 接收web服务器的动态资源请求
  3. 处理web服务器的动态资源请求并把处理结果返回给web服务器
  4. web服务器把处理结果组装成响应报文发送给浏览器

```python
"""miniweb框架，负责处理动态资源请求"""
import time


# 获取首页数据
def index():
    # 响应状态
    status = "200 OK"
    # 响应头
    response_header = [("Server", "FoxServ2.0")]
    # 处理后的数据
    data = time.ctime()

    return status, response_header, data


# 没有找到动态资源
def not_found():
    # 响应状态
    status = "404 Not Found"
    # 响应头
    response_header = [("Server", "FoxServ2.0")]
    # 处理后的数据
    data = "not found"

    return status, response_header, data


# 处理动态资源请求
def handle_request(env):
    # 获取动态请求资源路径
    request_path = env["request_path"]
    print("接收到的动态资源请求:", request_path)

    if request_path == "/index.py":
        # 获取首页数据
        result = index()
        return result
    else:
        # 没有找到动态资源
        result = not_found()
        return result
```

输出结果

![执行结果](https://oss.smartfox.cc/2020/08/21/ec5fb8474a500.png)

### 二、模板替换功能开发

+ 通过`with`打开并读取模板文件

```python
def index():
    # 响应状态
    status = "200 OK";
    # 响应头
    response_header = [("Server", "FoxServ2.0")]

    # 打开模板文件，读取数据
    with open("template/index.html", "r") as file:
        file_data = file.read()
```

+ 寻找模板文件中的特定的标记，并用模拟数据进行替换

```python
def index():
    # 响应状态
    status = "200 OK";
    # 响应头
    response_header = [("Server", "FoxServ2.0")]

    # 1. 打开模板文件，读取数据
    with open("template/index.html", "r") as file:
        file_data = file.read()

    # 处理后的数据, 从数据库查询
    data = time.ctime()
    # 2. 替换模板文件中的模板遍历
    result = file_data.replace("{%content%}", data)

    return status, response_header, result
```

### 三、路由功能开发

+ 什么是路由

  路由就是请求的URL到处理函数的映射，也就是说提前把请求的URL和处理函数关联好。

+ 为什么要使用路由

  在生产环境中，一个Web框架所需处理的动态请求不可能只有几个，一个一个编写`if`函数进行处理这是不切实际的，所以我们引入路由的思想，只需简简单单的几段代码即可实现将动态页面与函数之间的映射。

#### 路由功能

`framework.py`

```python
import time

# 获取首页数据
def index():
    # 响应状态
    status = "200 OK"
    # 响应头
    response_header = [("Server", "FoxServ2.0")]
    # 处理后的数据
    data = time.ctime()

    return status, response_header, data

def center():
    pass

# 没有找到动态资源
def not_found():
    # 响应状态
    status = "404 Not Found"
    # 响应头
    response_header = [("Server", "FoxServ2.0")]
    # 处理后的数据
    data = "not found"

    return status, response_header, data


route_list = [
    ("/index.py", index),
    ("/center.py", center)
]

# 处理动态资源请求
def handle_request(env):
    # 获取动态请求资源路径
    request_path = env["request_path"]
    print("接收到的动态资源请求:", request_path)

    # 遍历路由列表、绑定函数
    for path, func in route_list:
        if request_path == path:
            result = func()
            return result
    else:
        # 没有找到动态资源
        result = not_found()
        return result
```

#### 装饰器方式添加路由

前面我们已经实现了路由列表，但是每次添加路由都需要手动添加来完成，接下来我们想要完成路由的自动添加，可以通过装饰器来实现，在使用装饰器对处理函数进行装饰的时候我们需要知道装饰的函数和那个请求路径进行关联，也就是说装饰器需要接收一个url参数，这样我们定义的装饰器是一个带有参数的装饰器。

`framework.py`

```python
import time

# 定义路由列表
route_list = []

# 定义带有参数的装饰器
def route(path):
    # 装饰器
    def decorator(func):
        # 当执行装饰器装饰指定函数的时候，把路径和函数添加到路由列表
        route_list.append((path, func))

        def inner():
            # 执行指定函数
            return func()

        return inner
    # 返回装饰器
    return decorator


# 获取首页数据
@route("/index.py")
def index():
    # 响应状态
    status = "200 OK";
    # 响应头
    response_header = [("Server", "FoxServ2.0")]

    # 打开模板文件，读取数据
    with open("template/index.html", "r") as file:
        file_data = file.read()

    # 处理后的数据, 从数据库查询
    data = time.ctime()
    # 替换模板文件中的模板遍历
    result = file_data.replace("{%content%}", data)

    return status, response_header, result


# 获取个人中心数据
@route("/center.py")
def center():
    # 响应状态
    status = "200 OK";
    # 响应头
    response_header = [("Server", "FoxServ2.0")]

    # 打开模板文件，读取数据
    with open("template/center.html", "r") as file:
        file_data = file.read()

    # 处理后的数据, 从数据库查询
    data = time.ctime()
    # 替换模板文件中的模板遍历
    result = file_data.replace("{%content%}", data)

    return status, response_header, result

# 没有找到动态资源
def not_found():
    # 响应状态
    status = "404 Not Found";
    # 响应头
    response_header = [("Server", "FoxServ2.0")]
    # 处理后的数据
    data = "not found"

    return status, response_header, data

# 处理动态资源请求
def handle_request(env):
    # 获取动态请求资源路径
    request_path = env["request_path"]
    print("接收到的动态资源请求:", request_path)
    # 遍历路由列表，选择执行的函数
    for path, func in route_list:
        if request_path == path:
            result = func()
            return result
    else:
        # 没有找到动态资源
        result = not_found()
        return result
```

-------

# 0x02：日志服务功能开发

### 一、日志服务介绍

日常生活中，日志是一种必不可少的东西；例如银行的转账记录、快递的运送记录、工作的进度记录等；

在计算机程序中，日志也是不可缺少的东西，程序猿们可以通过查看程序日志，找到并复现程序的BUG；运维部门能通过程序日志，调试并测试程序；运营部门能通过日志分析用户操作行为，预判用户喜好等。

### 二、日志级别介绍

+ 日志等级可以分为5个，从低到高分别是:
  1. DEBUG
  2. INFO
  3. WARNING
  4. ERROR
  5. CRITICAL

+ 日志等级说明:
  + DEBUG：程序调试bug时使用
  + INFO：程序正常运行时使用
  + WARNING：程序未按预期运行时使用，但并不是错误，如:用户登录密码错误
  + ERROR：程序出错误时使用，如:IO操作失败
  + CRITICAL：特别严重的问题，导致程序不能再继续运行时使用，如:磁盘空间为空，一般很少使用

- 默认的是WARNING等级，当在WARNING或WARNING之上等级的才记录日志信息。
- 日志等级从低到高的顺序是: DEBUG < INFO < WARNING < ERROR < CRITICAL

### 三、Python下使用日志服务

+ 在Python中，我们可以通过导入`logging`模块来实现日志服务

+ logging参数

  + level 表示设置的日志等级
  + format 表示日志的输出格式, 参数说明:
    - %(levelname)s: 打印日志级别名称
    - %(filename)s: 打印当前执行程序名
    - %(lineno)d: 打印日志的当前行号
    - %(asctime)s: 打印日志的时间
    - %(message)s: 打印日志信息

+ 在`logging`包中记录日志的方式有两种：

  + 直接输出至控制台

  ```python
  import logging
  
  # 设置日志等级和输出日志格式
  logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s')
  
  logging.debug('这是一个debug级别的日志信息')
  logging.info('这是一个info级别的日志信息')
  logging.warning('这是一个warning级别的日志信息')
  logging.error('这是一个error级别的日志信息')
  logging.critical('这是一个critical级别的日志信息')
  ```

  输出结果

  ```shell
  2020-08-21 21:36:42,919 - WARNING: 这是一个warning级别的日志信息
  2020-08-21 21:36:42,919 - ERROR: 这是一个error级别的日志信息
  2020-08-21 21:36:42,919 - CRITICAL: 这是一个critical级别的日志信息
  ```

  + 保存至日志文件中

  ```python
  import logging
  
  logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                      filename="log.txt",
                      filemode="w")
  
  logging.debug('这是一个debug级别的日志信息')
  logging.info('这是一个info级别的日志信息')
  logging.warning('这是一个warning级别的日志信息')
  logging.error('这是一个error级别的日志信息')
  logging.critical('这是一个critical级别的日志信息')
  ```

  输出结果

  ![输出日志到文件](https://oss.smartfox.cc/2020/08/21/3362ca6ccd50a.gif)

+ 日志信息只显示了大于等于WARNING级别的日志，这说明默认的日志级别设置为WARNING

  **但是**，我们可以通过修改`basicConfig`中的`level`参数来让他输出更多日志

  ```python
  import logging
  
  # 设置日志等级和输出日志格式
  logging.basicConfig(level=logging.DEBUG,
                      format='%(asctime)s - %(levelname)s: %(message)s')
  
  logging.debug('这是一个debug级别的日志信息')
  logging.info('这是一个info级别的日志信息')
  logging.warning('这是一个warning级别的日志信息')
  logging.error('这是一个error级别的日志信息')
  logging.critical('这是一个critical级别的日志信息')
  ```

  输出结果

  ```shell
  2020-08-21 21:37:23,018 - DEBUG: 这是一个debug级别的日志信息
  2020-08-21 21:37:23,018 - INFO: 这是一个info级别的日志信息
  2020-08-21 21:37:23,018 - WARNING: 这是一个warning级别的日志信息
  2020-08-21 21:37:23,018 - ERROR: 这是一个error级别的日志信息
  2020-08-21 21:37:23,018 - CRITICAL: 这是一个critical级别的日志信息
  ```

------

# 0x03：参考文档

[Web服务器与Web框架](https://selfboot.cn/2016/07/28/forum_design_framework/)