# Use TCP for better solution, UDP faster, but not well

# Protection
- Create authentication by password, so third PC couldn't connect
- Make a list of connections by length of 2 only
- Third can connect, can send to connected, but cannot receive any
- To prevent third connection as mentioned, we need to generate passphrase which will be used as one-time password to connect between PCs.
- To create it, we need to find out how to get connection authentication before actual connection.
- I think we can send first message as passphrase to the another peer, so peer could check if it is correct before connection to each other

```python
from twisted.internet import reactor, protocol

class P2PProtocol(protocol.Protocol):
    def connectionMade(self):
        peer = self.transport.getPeer()
        print(f"Incoming connection from {peer.host}:{peer.port}")

        # Проверяем условие для отказа
        if some_condition:
            print("Connection denied")
            self.transport.abortConnection()  # Отказываем в подключении
        else:
            print("Connection accepted")

    def dataReceived(self, data):
        print(f"Received data: {data.decode()}")

def main():
    port = 12345

    # Создаем и запускаем сервер TCP
    factory = protocol.ServerFactory()
    factory.protocol = P2PProtocol
    reactor.listenTCP(port, factory)

    print(f"Server started on port {port}")

    reactor.run()

if __name__ == "__main__":
    main()

```