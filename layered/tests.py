import unittest
from io import StringIO
import sys
from main import GUI, AppLayer, DataLayer


# Helper function to capture output from a function
def capture_output(func):
    captured_output = StringIO()
    sys.stdout = captured_output
    func()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()


# Unit Tests
class LayeredArchitectureTest(unittest.TestCase):
    def test_layered_architecture(self):
        data_layer = DataLayer()
        app_layer = AppLayer(data_layer)
        gui = GUI(app_layer)

        user_input = "example_data"
        expected_output = "Data saved: EXAMPLE_DATA"

        self.assertEqual(gui.get_user_input(), user_input)
        self.assertEqual(app_layer.process_data(user_input), expected_output)

        # Simulating GUI output
        gui_result = capture_output(gui.run)
        self.assertEqual(gui_result.strip(), expected_output)


if __name__ == '__main__':
    unittest.main()
