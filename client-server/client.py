import socket


class Client:
    def __init__(self, server_host, server_port):
        self.server_host = server_host
        self.server_port = server_port

    def send_request(self, data):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.server_host, self.server_port))

        client_socket.send(data.encode())
        response = client_socket.recv(1024).decode()

        client_socket.close()
        return response


if __name__ == '__main__':
    client = Client('localhost', 8000)
    user_input = input("Enter data to send to the server: ")
    response = client.send_request(user_input)
    print("Response from server:", response)
