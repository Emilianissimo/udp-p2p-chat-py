from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class Server(DatagramProtocol):
    def __init__(self):
        self.clients = set()

    def datagramReceived(self, datagram, addr):
        datagram = datagram.decode('utf-8')
        if datagram == 'ready':
            addresses = '\n'.join([str(client) for client in self.clients])
            self.transport.write(addresses.encode('utf-8'), addr)
            self.clients.add(addr)


if __name__ == '__main__':
    port: int = 9999
    reactor.listenUDP(port, Server())
    reactor.run()
