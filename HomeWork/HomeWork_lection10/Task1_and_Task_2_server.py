import socket
import threading
import datetime


class TcpServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None
        self._runnig = False

    def start(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self.host, self.port))
        self._socket.listen(5)
        self._runnig = True
        print(f"[{datetime.datetime.now()}] - Welcome to Python multithreading TCP server")
        while self._runnig:
            conn, addr = self._socket.accept()
            ClientThread(conn, addr).start()

    def stop(self):
        self._runnig = False
        self._socket.close()
        print(f"[{datetime.datetime.now()}] -Server stopped")


class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self._connection = conn
        self._address = addr

    def caesar_decode(self, message):
        dict = ' a1b2c3d4e5f6g7h8i9j0klmnopqrstuvwxyz'
        shift = int(datetime.datetime.isoweekday(datetime.datetime.now()))
        string = message.strip().lower()
        res = ''
        for symbol in string:
            res += dict[(dict.index(symbol) - shift) % len(dict)]
        return res

    def run(self):
        print(f'[{datetime.datetime.now()}] - Connection from {self._address}')
        data = self._connection.recv(4096)
        message = self.caesar_decode(data.decode())
        print(f"[{datetime.datetime.now()}] - Connection from {message} accepted")
        self._connection.send(f"Hello {message}".encode())


if __name__ == '__main__':
    server = TcpServer(host='192.168.0.188', port=5555)
    server.start()
