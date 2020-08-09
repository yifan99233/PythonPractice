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
