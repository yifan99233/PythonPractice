import socket

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    server_socket.bind(("0.0.0.0", 9091))

    server_socket.listen(128)

    service_socket, client_info = server_socket.accept()

    print('客户端的IP地址和端口号：', client_info)

    _renv = service_socket.recv(1024)

    _length = len(_renv)
    print('接收数据的长度为：', _length)

    _decode = _renv.decode('utf-8')
    print('接收客户端的数据为：', _decode)

    _data = '问题处理中...'.encode('utf-8')

    service_socket.send(_data)

    service_socket.close()

    server_socket.close()