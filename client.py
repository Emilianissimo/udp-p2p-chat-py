from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from random import randint


class Client(DatagramProtocol):
    def __init__(self, host: str, port: str):
        if host == 'localhost':
            host = '127.0.0.1'

        self.id = (host, port)
        self.address = None
        self.server = ('127.0.0.1', 9999)
        print(f'Working on id: {self.id}')

    def startProtocol(self):
        self.transport.write('ready'.encode('utf-8'), self.server)

    def datagramReceived(self, datagram, addr):
        datagram = datagram.decode('utf-8')

        if addr == self.server:
            print('Choose a client from the list\n', datagram)
            self.address = (input('Write the host: '), int(input("Write port: ")))
            reactor.callInThread(self.send_message)
        else:
            print(addr, ':', datagram)

    def send_message(self):
        while True:
            self.transport.write(
                input(':::').encode('utf-8'),
                self.address,
            )


if __name__ == '__main__':
    port: int = randint(1000, 5000)
    # port which will listen to udp, need to connection.
    reactor.listenUDP(port, Client(host='localhost', port=port))
    reactor.run()
