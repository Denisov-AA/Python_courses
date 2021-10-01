import socket
import random
import datetime


class TcpClient:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self._socket = None

    def caesar_encode(self, message):
        dict = ' a1b2c3d4e5f6g7h8i9j0klmnopqrstuvwxyz'
        shift = int(datetime.datetime.isoweekday(datetime.datetime.now()))
        string = message.strip().lower()
        res = ''
        for symbol in string:
            res += dict[(dict.index(symbol) + shift) % len(dict)]
        return res

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        self._socket.send(self.caesar_encode(self.name).encode())
        data = self._socket.recv(4096)
        print(f'Received from server: {data}')
        self._socket.close()


if __name__ == '__main__':
    name = 'User' + str(random.randint(1000, 9999))
    myclient = TcpClient(host='192.168.0.188', port=5555, name=name)
    myclient.run()
