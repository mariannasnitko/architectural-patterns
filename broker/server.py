class Server:
    def __init__(self, name):
        self.name = name

    def process_request(self, request):
        # Perform processing logic specific to the server
        response_data = request.data.upper()
        response = Response(response_data)
        return response
