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
