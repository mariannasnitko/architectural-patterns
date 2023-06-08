class Client:
    def __init__(self, name, broker):
        self.name = name
        self.broker = broker

    def send_request(self, request):
        self.broker.route_request(request, self)

    def receive_response(self, response):
        print(f"{self.name} received response: {response}")


class Request:
    def __init__(self, data):
        self.data = data


class Response:
    def __init__(self, data):
        self.data = data
