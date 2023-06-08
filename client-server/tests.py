import unittest
from io import StringIO
import sys
from server import Server
from client import Client


# Helper function to capture output from a function
def capture_output(func):
    captured_output = StringIO()
    sys.stdout = captured_output
    func()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()


# Unit Tests
class ClientServerTest(unittest.TestCase):
    def test_client_server(self):
        server_host = 'localhost'
        server_port = 8000

        server = Server(server_host, server_port)
        client = Client(server_host, server_port)

        user_input = "example_data"
        expected_output = "Processed data: EXAMPLE_DATA"

        server_response = capture_output(server.start)
        self.assertIn("Server started", server_response)

        client_response = capture_output(lambda: client.send_request(user_input))
        self.assertIn("Connection established", client_response)
        self.assertIn(expected_output, client_response)


if __name__ == '__main__':
    unittest.main()
