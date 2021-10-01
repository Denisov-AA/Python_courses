import sqlalchemy.orm
import sqlalchemy.ext.declarative
import socket
import threading
import datetime
import random

Base = sqlalchemy.ext.declarative.declarative_base()


class Manufacturer(Base):
    __tablename__ = 'Manufacturers'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self):
        return f"Manufacturers: {self.id} -- {self.name} -- {self.products_id}"


class TcpServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None
        self._running = False

    def start(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self.host, self.port))
        self._socket.listen(5)
        self._running = True
        print(f"[{datetime.datetime.now()}] - Welcome to Python multithreading TCP server")
        while self._running:
            conn, addr = self._socket.accept()
            ClientThread(conn, addr).start()

    def stop(self):
        self._running = False
        self._socket.close()
        print(f"[{datetime.datetime.now()}] -Server stopped")


class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self._connection = conn
        self._address = addr

    def run(self):
        print(f'[{datetime.datetime.now()}] - Connection from {self._address}')
        data = self._connection.recv(4096)
        data = ''.join(str(data).split("'"))
        data = ''.join(str(data).split("b"))
        message = f"requested ID - {data}"
        print(f"[{datetime.datetime.now()}] - Connection from User accepted. Reseved message - {data}")
        Session = sqlalchemy.orm.sessionmaker(bind=engine)
        session = Session()
        for name in session.query(Manufacturer.name).filter(Manufacturer.id == f'{data}'):
            print(f"Requested manufacturer - {name}")
            # session.add(man)
        session.commit()
        self._connection.send(f"Requested manufacturer - {name}".encode())


if __name__ == '__main__':
    engine = sqlalchemy.create_engine('sqlite:///Task_5.db', echo=True)
    Base.metadata.create_all(engine)
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()
    for i in range(1, 10):
        man = Manufacturer(id=i,
                           name=f'Manufacturer_{i}')
        session.add(man)
    session.commit()
    server = TcpServer(host='192.168.0.188', port=5555)
    server.start()
