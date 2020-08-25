# 三、Python Web网络编程 2020.08.09

# 0x00：HTTP协议

### 一、什么是HTTP协议

+ HTTP协议介绍

  + HTTP 协议的全称是(HyperText Transfer Protocol)，翻译过来就是**超文本传输协议**。

  + 超文本是超级文本的缩写，是指超越文本限制或者超链接，比如:图片、音乐、视频、超链接等等都属于超文本。

  + HTTP 协议的制作者是**蒂姆·伯纳斯-李**，1991年设计出来的，**HTTP 协议设计之前目的是传输网页数据的，现在允许传输任意类型的数据**。

  + **传输 HTTP 协议格式的数据是基于 TCP 传输协议的，发送数据之前需要先建立连接。**

+ HTTP协议的作用

  + 规定浏览器和web服务器通信的数据格式

+ 浏览器访问Web服务器的通讯过程

  ![访问web服务器的通信过程](https://oss.smartfox.cc/2020/08/09/a2565cedead07.png)

### 二、什么是URL

+ 什么是URL

  URL的英文全拼是(Uniform Resoure Locator),表达的意思是统一资源定位符，通俗理解就是网络资源地址，也就是我们常说的网址。

+ URL的组成

  + **URL的样子:**

    https://news.163.com/18/1122/10/E178J2O4000189FH.html

  + **URL的组成部分:**

    1. **协议部分: **[https://、http://、ftp://](https://xn--http-kw3c//、ftp://)
    2. **域名部分**: news.163.com
    3. **资源路径部分**: /18/1122/10/E178J2O4000189FH.html

  + **域名:**

    域名就是**IP地址的别名**，它是用点进行分割使用英文字母和数字组成的名字，**使用域名目的就是方便的记住某台主机IP地址**。

  + **URL的扩展:**

    https://news.163.com/hello.html?page=1&count=10

  - **查询参数部分**: ?page=1&count=10

    + **参数说明:**

      ? 后面的 page 表示第一个参数，后面的参数都使用 & 进行连接

------

# 0x01：HTTP请求报文

### 一、GET请求报文

```http
---- 请求行 ----
GET / HTTP/1.1  # GET请求方式 请求资源路径 HTTP协议版本
---- 请求头 -----
Host: www.smartfox.cc  # 服务器的主机地址和端口号,默认是80
Connection: keep-alive # 和服务端保持长连接
Upgrade-Insecure-Requests: 1 # 让浏览器升级不安全请求，使用https请求
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36  # 用户代理，也就是客户端的名称
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8 # 可接受的数据类型
Accept-Encoding: gzip, deflate # 可接受的压缩格式
Accept-Language: zh-CN,zh;q=0.9 #可接受的语言
Cookie: csrftoken=ZIVKMSEdmdJbowTnXtRPXByIqxK1WF1ronGQXKWdp51WnSvmlRyqsKzZFPAojcLF; sessionid=as3sop6t2igilg76zll45m045udfsoa7; # 登录用户的身份标识

---- 空行 ----
```

+ 也就是说GET请求报文是由以下部分组成的：

  + 请求行

  + 请求头

  + 空行

### 二、POST请求报文

```http
---- 请求行 ----
POST /admin.php?next=index.php HTTP/1.1 # POST请求方式 请求资源路径 HTTP协议版本
---- 请求头 ----
Host: www.smartfox.cc # 服务器的主机地址和端口号,默认是80
Connection: keep-alive # 和服务端保持长连接
Content-Type: application/x-www-form-urlencoded  # 告诉服务端请求的数据类型
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 # 客户端的名称
---- 空行 ----
---- 请求体 ----
username=admin&pass=admin # 请求参数
```

+ 也就是说POST报文是由以下部分组成：
  + 请求行
  + 请求头
  + 空行
  + 请求体

### 三、POST与GET之间的区别

![get和post请求报文](https://oss.smartfox.cc/2020/08/25/b3dd4a15192dc.png)

+ 一个HTTP请求报文可以由**请求行、请求头、空行和请求体**4个部分组成。
+ **GET方式的请求报文没有请求体，只有请求行、请求头、空行组成**。
+ **POST方式的请求报文可以有请求行、请求头、空行、请求体四部分组成**。
  + **注意:POST方式可以允许没有请求体，但是这种格式很少见**。

------

# 0x02：HTTP响应报文

### 一、HTTP响应报文

```http
--- 响应行/状态行 ---
HTTP/1.1 200 OK # HTTP协议版本 状态码 状态描述
--- 响应头 ---
Server: Tengine # 服务器名称
Content-Type: text/html; charset=UTF-8 # 内容类型
Transfer-Encoding: chunked # 发送给客户端内容不确定内容长度，发送结束的标记是0\r\n, Content-Length表示服务端确定发送给客户端的内容大小，但是二者只能用其一。
Connection: keep-alive # 和客户端保持长连接
Date: Fri, 23 Nov 2018 02:01:05 GMT # 服务端的响应时间
--- 空行 ---
--- 响应体 ---
<!DOCTYPE html><html lang=“en”>…</html> # 响应给客户端的数据
```

+ 所以一个成熟的HTTP响应报文是由以下部分组成的
  + 响应行
  + 响应头
  + 空行
  + 响应体

![响应报文](https://oss.smartfox.cc/2020/08/25/b15c3ddde0ca0.png)

### 二、常见HTTP状态码

| 状态码 | 状态                  | 说明                                                         |
| :----- | :-------------------- | ------------------------------------------------------------ |
| 200    | OK                    | 请求成功                                                     |
| 201    | Created               | 请求已经被实现，而且所需资源已建立，且其URI已经随头部信息返回。 |
| 202    | Accepted              | 服务器已接受请求，但尚未处理。                               |
| 307    | Temporary Redirect    | 重定向                                                       |
| 400    | Bad Request           | 错误的请求，请求地址或者参数有误                             |
| 403    | Forbidden             | 服务器已经理解请求，但是拒绝执行它。                         |
| 404    | Not Found             | 请求资源在服务器不存在                                       |
| 500    | Internal Server Error | 服务器内部源代码出现错误                                     |
| 502    | Bad Gateway           | 作为网关或代理的服务器尝试执行请求时，从上游服务接到无效的响应。 |

-------

# 0x03：使用Python自带的HTTP服务器

一、静态web服务器是什么

+ 可以**为发出请求的浏览器提供静态文档的程序**。
+ 平时我们浏览百度新闻数据的时候，**每天的新闻数据都会发生变化，那访问的这个页面就是动态的**，而我们开发的是**静态的，页面的数据不会发生变化**。

二、如何搭建Python自带的静态Web服务器



三、访问搭建的静态Web服务器



-----

# 0x04：自制静态Web服务器

+ 返回固定页面数据

  ```python
  import socket
  
  if __name__ == '__main__':
      _server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
      _server.bind(("", 9091))
  
      _server.listen(10)
  
      while True:
          _client, _client_info = _server.accept()
  
          _request_data = _client.recv(4096)
  
          print(_request_data)
  
          with open("static/index.html", 'rb') as _file:
              file_data = _file.read()
              print(file_data)
  
          response_line = "HTTP/1.1 200 OK\r\n"
  
          response_head = "Server: NGINX/14.8\r\n"
  
          response_body = file_data
  
          response_data = (response_line + response_head + "\r\n").encode('utf-8') + response_body
          print(response_data)
          _client.send(response_data)
  
          _client.close()
  ```

+ 返回指定页面数据

  ```python
  import socket
  
  
  def init_server():
      _server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      _server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
      _server.bind(("", 9091))
      print("Server Listen : 0.0.0.0:9091")
      _server.listen(128)
      return _server
  
  
  def service_logic(_server):
      _service, _info = _server.accept()
      renv_data = _service.recv(4096)
      if len(renv_data) == 0:
          print('客户端', _info, '离线')
          _service.close()
          return
  
      _data = renv_data.decode('utf-8')
      url = _data.split(" ", maxsplit=2)
  
      uri = url[1]
      print(uri)
  
      if uri == "/":
          uri = '/index.html'
  
      try:
          with open("static" + uri, "rb") as _file:
              response_body = _file.read()
      except Exception as e:
          response_line = "HTTP/1.1 404 Not Found\r\n"
  
          response_header = "Server: PythonWeb1.0\r\n"
          with open("static/error.html", "rb") as _file:
              response_body = _file.read()
  
          response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
  
          _service.send(response_data)
      else:
          response_line = "HTTP1.1 200 OK\r\n"
  
          response_header = "Server: PythonWeb1.0\r\n"
          response_data = (response_line + response_header + "\r\n").encode('utf-8') + response_body
  
          _service.send(response_data)
      finally:
          _service.close()
  
  
  if __name__ == '__main__':
      server = init_server()
      while True:
          service_logic(server)
  ```

+ 多任务版

  ```python
  import socket
  import threading
  
  
  def init_server():
      _server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      _server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
      _server.bind(("", 9091))
      print("Server Listen : 0.0.0.0:9091")
      _server.listen(128)
      return _server
  
  
  def handle_client(_service, _info):
      renv_data = _service.recv(4096)
      if len(renv_data) == 0:
          print('客户端', _info, '离线')
          _service.close()
          return
  
      _data = renv_data.decode('utf-8')
      url = _data.split(" ", maxsplit=2)
  
      uri = url[1]
      print(uri)
  
      if uri == "/":
          uri = '/index.html'
  
      try:
          with open("static" + uri, "rb") as _file:
              response_body = _file.read()
      except Exception as e:
          response_line = "HTTP/1.1 404 Not Found\r\n"
  
          response_header = "Server: PythonWeb1.0\r\n"
          with open("static/error.html", "rb") as _file:
              response_body = _file.read()
  
          response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
  
          _service.send(response_data)
      else:
          response_line = "HTTP1.1 200 OK\r\n"
  
          response_header = "Server: PythonWeb1.0\r\n"
          response_data = (response_line + response_header + "\r\n").encode('utf-8') + response_body
  
          _service.send(response_data)
      finally:
          _service.close()
  
  
  def service_logic(_server):
      _services, _info = _server.accept()
  
      handle_service = threading.Thread(target=handle_client, args=(_services, _info))
      handle_service.daemon = True
      handle_service.start()
  
  
  if __name__ == '__main__':
      server = init_server()
      while True:
          service_logic(server)
  ```

+ 面向对象版

  ```python
  import socket
  import threading
  
  
  class WebServer(object):
      def __init__(self, addr: str = '0.0.0.0', port: int = 9091) -> None:
          self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          self._server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
          self._server.bind((addr, port))
          print(f"Server Listen!{addr}:{port}")
          self._server.listen(128)
  
      def service_logic(self) -> None:
          while True:
              _services, _info = self._server.accept()
              handle_service = threading.Thread(target=self.handle_client, args=(_services, _info))
              handle_service.daemon = True
              handle_service.start()
  
      @staticmethod
      def handle_client(_service: socket.socket, _info: tuple) -> None:
          renv_data = _service.recv(4096)
          if len(renv_data) == 0:
              print('客户端', _info, '离线')
              _service.close()
              return
  
          _data = renv_data.decode('utf-8')
          url = _data.split(" ", maxsplit=2)
  
          uri = url[1]
          print(uri)
  
          if uri == "/":
              uri = '/index.html'
  
          try:
              with open("static" + uri, "rb") as _file:
                  response_body = _file.read()
          except Exception as e:
              response_line = "HTTP/1.1 404 Not Found\r\n"
  
              response_header = "Server: PythonWeb1.0\r\n"
              with open("static/error.html", "rb") as _file:
                  response_body = _file.read()
  
              response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
  
              _service.send(response_data)
          else:
              response_line = "HTTP1.1 200 OK\r\n"
  
              response_header = "Server: PythonWeb1.0\r\n"
              response_data = (response_line + response_header + "\r\n").encode('utf-8') + response_body
  
              _service.send(response_data)
          finally:
              _service.close()
  
  
  if __name__ == '__main__':
      server = WebServer()
      server.service_logic()
  ```

+ 命令行启动动态绑定端口号

  ```python
  import socket
  import threading
  import sys
  
  
  class WebServer(object):
      def __init__(self, addr: str = '0.0.0.0', port: int = 9091) -> None:
          self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          self._server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
          self._server.bind((addr, port))
          print(f"Server Listen!{addr}:{port}")
          self._server.listen(128)
  
      def service_logic(self) -> None:
          while True:
              _services, _info = self._server.accept()
              handle_service = threading.Thread(target=self.handle_client, args=(_services, _info))
              handle_service.daemon = True
              handle_service.start()
  
      @staticmethod
      def handle_client(_service: socket.socket, _info: tuple) -> None:
          renv_data = _service.recv(4096)
          if len(renv_data) == 0:
              print('客户端', _info, '离线')
              _service.close()
              return
  
          _data = renv_data.decode('utf-8')
          url = _data.split(" ", maxsplit=2)
  
          uri = url[1]
          print(uri)
  
          if uri == "/":
              uri = '/index.html'
  
          try:
              with open("static" + uri, "rb") as _file:
                  response_body = _file.read()
          except Exception as e:
              response_line = "HTTP/1.1 404 Not Found\r\n"
  
              response_header = "Server: PythonWeb1.0\r\n"
              with open("static/error.html", "rb") as _file:
                  response_body = _file.read()
  
              response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
  
              _service.send(response_data)
          else:
              response_line = "HTTP1.1 200 OK\r\n"
  
              response_header = "Server: PythonWeb1.0\r\n"
              response_data = (response_line + response_header + "\r\n").encode('utf-8') + response_body
  
              _service.send(response_data)
          finally:
              _service.close()
  
  
  if __name__ == '__main__':
      args = sys.argv
      if len(sys.argv) != 2:
          print("执行命令如下: python3 xxx.py 8000")
          exit(0)
  
          # 判断字符串是否都是数字组成
      if not sys.argv[1].isdigit():
          print("执行命令如下: python3 xxx.py 8000")
          exit(0)
  
      port = int(sys.argv[1])
  
      server = WebServer(port=port)
      server.service_logic()
  ```