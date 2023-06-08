import unittest
from io import StringIO
import sys
from master import Master
from slave import Slave


# Helper function to capture output from a function
def capture_output(func):
    captured_output = StringIO()
    sys.stdout = captured_output
    func()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()


# Unit Tests
class MasterSlaveTest(unittest.TestCase):
    def test_master_slave(self):
        data_list = ["request1", "request2", "request3"]

        master = Master()
        for data in data_list:
            master.add_slave(data)

        process_result = capture_output(master.process_requests)
        self.assertEqual(process_result.strip(), "")

        results = master.get_results()
        expected_results = ["REQUEST1", "REQUEST2", "REQUEST3"]
        self.assertEqual(results, expected_results)


if __name__ == '__main__':
    unittest.main()
