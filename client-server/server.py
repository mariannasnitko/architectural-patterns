import socket


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print("Server started. Listening for connections...")

        while True:
            client_socket, address = self.server_socket.accept()
            print("Connection established with:", address)

            client_data = client_socket.recv(1024).decode()
            response = self.process_request(client_data)

            client_socket.send(response.encode())
            client_socket.close()

    def process_request(self, data):
        # Perform server-side processing
        return f"Processed data: {data.upper()}"


if __name__ == '__main__':
    server = Server('localhost', 8000)
    server.start()
