class Broker:
    def __init__(self):
        self.servers = []

    def add_server(self, server):
        self.servers.append(server)

    def route_request(self, request, client):
        server = self.find_server()
        response = server.process_request(request)
        client.receive_response(response)

    def find_server(self):
        # Simple round-robin approach to select a server
        server_index = len(self.servers) % len(self.servers)
        return self.servers[server_index]
