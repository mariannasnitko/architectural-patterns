import unittest
from io import StringIO
import sys
from model import Model, View, Controller


# Helper function to capture output from a function
def capture_output(func):
    captured_output = StringIO()
    sys.stdout = captured_output
    func()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()


# Unit Tests
class MVCTest(unittest.TestCase):
    def test_mvc(self):
        model = Model()
        view = View()
        controller = Controller(model, view)

        # Set initial data
        controller.update_data("Hello, MVC!")

        # Test display_data
        output = capture_output(controller.display_data)
        self.assertEqual(output.strip(), "Data: Hello, MVC!")

        # Update data and test display_data again
        controller.update_data("Updated data")
        output = capture_output(controller.display_data)
        self.assertEqual(output.strip(), "Data: Updated data")


if __name__ == '__main__':
    unittest.main()
