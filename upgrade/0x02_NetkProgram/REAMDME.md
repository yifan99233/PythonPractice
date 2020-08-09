# 二、Python网络编程 2020.08.08

# 0x00：计算机网络基础

### 一、IP地址的介绍

+ IP地址的概念

  + IP地址（Internet Protocol Address）是指互联网协议地址，又译为网际协议地址。
  + IP地址是IP协议提供的一种统一的地址格式，它为互联网上的每一个网络和每一台主机分配一个逻辑地址，以此来屏蔽物理地址的差异。

  ![IP地址](https://oss.smartfox.cc/2020/08/08/d2833048724ec.png)

+ IP地址的表现形式

  + IP 地址分为两类： **IPv4** 和 **IPv6**
  + IPv4 是普遍正在被广泛使用的IP协议
  + IPv6 是现阶段为了解决IPv4地址不够用的情况而正在普及的下一代IP协议
  + IPv4 是由点分十进制组成
  + IPv6 是由冒号十六进制组成

+ IP地址的作用

  IP 地址的作用是标识网络中唯一的一台设备的，也就是说通过IP地址能够找到网络中某台设备。

  ![IP的作用](https://oss.smartfox.cc/2020/08/08/1e3a2fab17d65.png)

+ 查看IP地址

  + Linux 和 mac OS 使用 `ifconfig` 这个命令

  ![Linux下查询本机IP地址](https://oss.smartfox.cc/2020/08/08/fad8f1d8291fa.png)

  + Windows 使用 `ipconfig` 这个命令

  ![windows下查询本机IP地址](https://oss.smartfox.cc/2020/08/08/25b9a6ed3921b.png)

### 二、端口和端口号

+ 什么是端口、什么是端口号

  即为数据传输的通道，若将IP地址比作一座房子的地址 ，那么端口就是出入房子的门；

  然而真正的房子只有几个门，但是一个IP地址的端口可以有65536个；

  端口是通过端口号来标记的，端口号只有整数，范围是从0 到65535。

+ 端口号的分类
  + 知名端口：0 - 1023
  + 动态端口：1024 - 65535

### 三、协议

+ TCP协议

  + TCP的概念

    传输控制协议（Transmission Control Protocol）是一种面向连接的、可靠的、基于字节流的传输层通信协议

  + TCP通信流程

    1. 建立连接（三次握手）
    2. 传输数据
    3. 关闭连接（四次挥手）

  + TCP的特点

    + 面向连接
    + 可靠传输

+ UDP协议

  + 概念

    用户数据报协议（User Datagram Protocol）是OSI参考模型中一种无连接的传输层协议

  + UDP的特点

    + 面向报文

    + 无连接
    + 吞吐量不受拥挤控制算法的调节

+ socket

  + 什么是socket

    网络套接字（英语：Network socket；又译网络套接字、网络接口、网络插槽）在计算机科学中是电脑网络中进程间数据流的端点，是一种操作系统提供的进程间通信机制。

  + socket的作用

    进程之间网络数据传输

  ![socket](https://oss.smartfox.cc/2020/08/08/65ebd2a6a4a3c.png)

-----

# 0x01：TCP网络开发流程

![TCP网络开发流程](https://oss.smartfox.cc/2020/08/08/971acb30a77ed.png)

### 一、TCP客户端程序开发流程

+ 流程梳理
  1. 创建服务端套接字对象
  2. 绑定监听端口
  3. 设置监听
  4. 等待客户端的连接请求
  5. 接受数据
  6. 返回数据
  7. 关闭套接字

### 二、TCP服务端程序开发流程

+ 流程梳理
  1. 创建客户端套接字对象
  2. 和服务端套接字建立连接
  3. 发送数据
  4. 接受数据
  5. 关闭客户端套接字

-----

# 0x02：TCP网络开发

### 一、socket类

Python 中，我们用 socket（）函数来创建套接字，语法格式如下：

```python
import socket

socket.socket([family[, type[, proto]]])
```

+ 参数

| 参数     | 描述                                                         |
| -------- | ------------------------------------------------------------ |
| family   | 套接字家族可以使AF_UNIX或者AF_INET                           |
| type     | 套接字类型可以根据是面向连接的还是非连接分为`SOCK_STREAM`或`SOCK_DGRAM` |
| protocol | 一般不填默认为0                                              |

+ Socket 类型

| 类型                  | 描述                                                         |
| --------------------- | ------------------------------------------------------------ |
| socket.AF_UNIX        | 只能够用于单一的Unix系统进程间通信                           |
| socket.AF_INET        | 服务端与客户端之间通讯协议（IPv4）                           |
| socket.AF_INET6       | 服务端与客户端之间通讯协议（IPv6）                           |
| socket.SOCK_STREAM    | 使用TCP传输协议进行数据传输（流式socket）                    |
| socket.SOCK_DGRAM     | 使用UDP传输协议进行数据传输（数据报式socket）                |
| socket.SOCK_RAW       | 原始套接字；可以处理普通套接字无法处理的ICMP，IGMP等特殊的网络报文 |
| socket.SOCK_RDM       | 提供可靠的UDP数据报连接，即保证交付数据报但不保证数据        |
| socket.SOCK_SEQPACKET | 提供连续可靠的数据包连接                                     |

+ socket类方法

| 方法                                  | 描述                                                         |
| ------------------------------------- | ------------------------------------------------------------ |
| _socket.bind(address)                 | 将套接字绑定到地址;在AF_INET下，以元组（host,port）的形式表示地址。 |
| _socket.listen(backlog)               | 开始监听传入连接。backlog指定在拒绝连接之前，可以挂起的最大连接数量。 |
| _socket.setblocking(bool)             | 是否阻塞（默认True），如果设置False，那么accept和recv时一旦无数据，则报错。 |
| _socket.accept()                      | 接受连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是客户端的地址。 |
| _socket.connect(address)              | 连接到address处的套接字。一般情况下address的格式为元组（hostname,port）,如果连接出错，返回socket.error错误。 |
| _socket.connect_ex(address)           | 同上，只不过会有返回值，连接成功时返回 0 ，连接失败时候返回错误代码 |
| _socket.close()                       | 关闭套接字连接                                               |
| _socket.recv(bufsize[,flag])          | 接受套接字的数据。数据以字符串形式返回，bufsize指定最多可以接收的数量。flag提供有关消息的其他信息，通常可以忽略。 |
| _socket.recvfrom(bufsize[.flag])      | 与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。 |
| _socket.send(string[,flag])           | 将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。即：可能未将指定内容全部发送。 |
| _socket.sendall(string[,flag])        | 将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。内部通过递归调用send，将所有内容发送出去。 |
| _socket.sendto(string[,flag],address) | 将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。该函数主要用于UDP协议。 |
| _socket.settimeout(timeout)           | 设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。 |
| _socket.getpeername()                 | 返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。  |
| _socket.getsockname()                 | 返回套接字自己的地址。通常是一个元组(ipaddr,port)            |
| _socket.fileno()                      | 套接字的文件描述符                                           |

### 一、TCP客户端程序开发

```python
import socket   # 导入socket包
if __name__ == '__main__':
    # 创建socket套接字   AF_INET -> 采用IPv4 ；SOCK_STREAM -> 采用TCP传输协议
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 与服务端建立连接
    client_socket.connect(('127.0.0.1', 9091))
    # 准备需要发送的数据，使用UTF-8进行编码
    _data = 'Connect Succces!'.encode('utf-8')
	# 发送数据
    client_socket.send(_data)
	# 获取服务端返回数据
    _recv = client_socket.recv(1024)
	# 打印服务端返回的原始数据
    print('获得来自服务器的原始数据：', _recv)
	# 对数据进行解码
    _decode = _recv.decode('utf-8')
    print('获得来自服务器的数据：', _decode)
	# 关闭socket套接字
    client_socket.close()
```

### 二、TCP服务端程序开发

+ 单任务版

```python
import socket # 导入socket包
if __name__ == '__main__':
    # 创建socket套接字   AF_INET -> 采用IPv4 ；SOCK_STREAM -> 采用TCP传输协议
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# 设置启用端口复用，当程序结束时，立即释放端口号
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
	# 绑定监听端口号
    server_socket.bind(("0.0.0.0", 9091))
	# 配置监听最大等待连接个数
    server_socket.listen(128)
	# 等待客户端建立连接请求，返回（conn，info），若无连接则会一直保持阻塞状态
    # 其中conn由service_socket接收，是与客户端建立连接的套接字
    # info由client_info接收，是客户端的地址与端口信息
    service_socket, client_info = server_socket.accept()
    print('客户端的IP地址和端口号：', client_info)
    # 获取客户端发送的原始数据
    _renv = service_socket.recv(1024)
    # 获取原始数据的长度
    _length = len(_renv)
    print('接收数据的长度为：', _length)
    # 对原始数据进行解码
    _decode = _renv.decode('utf-8')
    print('接收客户端的数据为：', _decode)
    # 准备需要返回的数据，使用UTF-8进行编码
    _data = '问题处理中...'.encode('utf-8')
    # 发送数据
    service_socket.send(_data)
	# 关闭服务端与客户端的套接字
    service_socket.close()
	# 关闭服务端套接字
    server_socket.close()
```

+ 多任务版

  在现实生产环境中，一个服务端不可能只就服务于一个客户端；通常一个服务端是要能服务多个客户端，以下是多任务的实现思路：

  1. 编写一个TCP服务端程序，循环等待接受客户端的连接请求
  2. 当客户端和服务端建立连接成功，创建子线程，使用子线程专门处理客户端的请求，防止主线程阻塞
  3. 把创建的子线程设置成为守护主线程，防止主线程无法退出。

```python
import socket
import threading
# 客户端服务处理函数
def handle_client_request(_socket, _info):
    while True:
        # 获取客户端发送的原始数据
        _data = _socket.recv(1024)
        # 容器类型判断是否有数据可以直接使用if语句进行判断，如果容器类型里面有数据表示条件成立，否则条件失败
        # 容器类型: 列表、字典、元组、字符串、set、range、二进制数据
        if _data:
            print(_data.decode("utf-8"), _info)
            # 回复
            _socket.send("数据接收正常...".encode("utf-8"))
        else:
            print("客户端下线了:", _info)
            break
    # 关闭服务端与客户端的套接字
    _socket.close()

if __name__ == '__main__':
    # 创建socket套接字   AF_INET -> 采用IPv4 ；SOCK_STREAM -> 采用TCP传输协议
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置启用端口复用，当程序结束时，立即释放端口号
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定监听端口号
    tcp_server_socket.bind(("", 9090))
    # 配置监听最大等待连接个数
    tcp_server_socket.listen(128)
    # 循环等待接收客户端的连接请求
    while True:
        # 等待客户端建立连接请求，返回（conn，info），若无连接则会一直保持阻塞状态
        # 其中conn由service_socket接收，是与客户端建立连接的套接字
        # info由client_info接收，是客户端的地址与端口信息
        service_socket, client_info = tcp_server_socket.accept()
        print("客户端连接成功:", client_info)
        # 当客户端和服务端建立连接成功以后，创建一个子线程处理接下来的客户端讯息
        client_thread = threading.Thread(target=handle_client_request, args=(service_socket, client_info))
        # 设置守护主线程，当主线程退出时自动终止子线程
        client_thread.setDaemon(True)
        # 启动子线程
        client_thread.start()
```



### 三、网络开发注意点

1. 当 TCP 客户端程序想要和 TCP 服务端程序进行通信的时候必须要先**建立连接**
2. TCP 客户端程序一般不需要绑定端口号，因为客户端是主动发起建立连接的。
3. **TCP 服务端程序必须绑定端口号**，否则客户端找不到这个 TCP 服务端程序。
4. listen 后的套接字是被动套接字，**只负责接收新的客户端的连接请求，不能收发消息。**
5. 当 TCP 客户端程序和 TCP 服务端程序连接成功后， TCP 服务器端程序会产生一个**新的套接字**，收发客户端消息使用该套接字。
6. **关闭 accept 返回的套接字意味着和这个客户端已经通信完毕**。
7. **关闭 listen 后的套接字意味着服务端的套接字关闭了，会导致新的客户端不能连接服务端，但是之前已经接成功的客户端还能正常通信。**
8. **当客户端的套接字调用 close 后，服务器端的 recv 会解阻塞，返回的数据长度为0**，服务端可以通过返回数据的长度来判断客户端是否已经下线，反之**服务端关闭套接字，客户端的 recv 也会解阻塞，返回的数据长度也为0**。

-----

# 0x03：socket中 send 与 recv原理剖析

![send和recv原理](https://oss.smartfox.cc/2020/08/08/e664afd8651f2.png)
$$
send -> 发送缓冲区 -> 网卡 -> 网卡 -> 接收缓冲区 -> recv
$$

### `send`原理

**Q：**`send`是不是直接把数据发给服务端?

**A：**不是，要想发数据，必须得**通过网卡发送数据**，应用程序是无法直接通过网卡发送数据的，它需要调用操作系统接口，也就是说，应用程序把发送的数据先写入到**发送缓冲区**(内存中的一片空间)，再**由操作系统控制网卡把发送缓冲区的数据发送给服务端网卡** 。

### `recv`原理

**Q：**`renv`是不是直接从客户端接收数据?

**A：**不是，**应用软件是无法直接通过网卡接收数据的**，它需要调用操作系统接口，**由操作系统通过网卡接收数据**，把接收的数据**写入到接收缓冲区**(内存中的一片空间），应用程序**再从接收缓存区获取客户端发送的数据**。