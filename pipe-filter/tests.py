import unittest
from io import StringIO
import sys
from filter import Filter
from pipe import Pipe


# Helper function to capture output from a function
def capture_output(func):
    captured_output = StringIO()
    sys.stdout = captured_output
    func()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()


# Unit Tests
class PipeFilterTest(unittest.TestCase):
    def test_pipe_filter(self):
        filters = [
            Filter("Filter1"),
            Filter("Filter2"),
            Filter("Filter3")
        ]
        pipe = Pipe(filters)

        data = "input data"
        expected_output = "INPUT DATA"

        processed_data = pipe.process_data(data)
        self.assertEqual(processed_data, expected_output)


if __name__ == '__main__':
    unittest.main()
