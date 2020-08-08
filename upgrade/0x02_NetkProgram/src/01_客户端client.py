import socket

if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect(('127.0.0.1', 9091))

    _data = 'Connect Succces!'.encode('utf-8')

    client_socket.send(_data)

    _recv = client_socket.recv(1024)

    print('获得来自服务器的原始数据：', _recv)

    _decode = _recv.decode('utf-8')
    print('获得来自服务器的数据：', _decode)

    client_socket.close()
