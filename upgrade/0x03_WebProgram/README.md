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

### 三、查看HTTP协议通讯过程

------

# 0x01：HTTP请求报文

### 一、GET请求报文

+ 请求行
+ 请求头
+ 空行

### 二、POST请求报文

+ 请求行
+ 请求头
+ 空行
+ 请求体

------

# 0x02：HTTP响应报文

### 一、HTTP响应报文

+ 响应行
+ 响应头
+ 空行
+ 响应体

### 二、常见HTTP状态码

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