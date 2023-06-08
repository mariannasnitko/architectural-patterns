import unittest
from io import StringIO
import sys
from client import Client, Request, Response
from server import Server
from broker import Broker


# Helper function to capture output from a function
def capture_output(func):
    captured_output = StringIO()
    sys.stdout = captured_output
    func()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()


# Unit Tests
class BrokerTest(unittest.TestCase):
    def test_broker(self):
        broker = Broker()
        server1 = Server("Server1")
        server2 = Server("Server2")
        broker.add_server(server1)
        broker.add_server(server2)

        client1 = Client("Client1", broker)
        client2 = Client("Client2", broker)

        request1 = Request("data1")
        request2 = Request("data2")

        expected_response1 = "DATA1"
        expected_response2 = "DATA2"

        # Capture output from client1 and client2
        output1 = capture_output(lambda: client1.send_request(request1))
        output2 = capture_output(lambda: client2.send_request(request2))

        # Check if the responses are correct
        self.assertIn(f"Client1 received response: {expected_response1}", output1)
        self.assertIn(f"Client2 received response: {expected_response2}", output2)


if __name__ == '__main__':
    unittest.main()
