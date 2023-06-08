import unittest
from io import StringIO
import sys
from node import Node


# Helper function to capture output from a function
def capture_output(func):
    captured_output = StringIO()
    sys.stdout = captured_output
    func()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()


# Unit Tests
class P2PNetworkTest(unittest.TestCase):
    def test_p2p_network(self):
        node1 = Node("Node1")
        node2 = Node("Node2")
        node3 = Node("Node3")

        node1.add_peer(node2)
        node1.add_peer(node3)
        node2.add_peer(node1)
        node2.add_peer(node3)
        node3.add_peer(node1)
        node3.add_peer(node2)

        message = "Hello, P2P network!"

        output1 = capture_output(lambda: node1.send_message(message))
        output2 = capture_output(lambda: node2.send_message(message))
        output3 = capture_output(lambda: node3.send_message(message))

        self.assertIn(f"Node1 received message: {message}", output2)
        self.assertIn(f"Node1 received message: {message}", output3)

        self.assertIn(f"Node2 received message: {message}", output1)
        self.assertIn(f"Node2 received message: {message}", output3)

        self.assertIn(f"Node3 received message: {message}", output1)
        self.assertIn(f"Node3 received message: {message}", output2)


if __name__ == '__main__':
    unittest.main()
