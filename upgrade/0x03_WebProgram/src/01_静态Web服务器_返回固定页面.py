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
