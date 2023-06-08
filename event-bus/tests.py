import unittest
from io import StringIO
import sys
from event_bus import EventBus
from subscriber import Subscriber


# Helper function to capture output from a function
def capture_output(func):
    captured_output = StringIO()
    sys.stdout = captured_output
    func()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()


# Unit Tests
class EventBusTest(unittest.TestCase):
    def test_event_bus(self):
        event_bus = EventBus()

        subscriber1 = Subscriber("Subscriber1")
        subscriber2 = Subscriber("Subscriber2")
        subscriber3 = Subscriber("Subscriber3")

        event_bus.subscribe("event_type1", subscriber1)
        event_bus.subscribe("event_type2", subscriber2)
        event_bus.subscribe("event_type1", subscriber3)
        event_bus.subscribe("event_type3", subscriber3)

        message1 = "Event 1 Data"
        message2 = "Event 2 Data"
        message3 = "Event 3 Data"

        output1 = capture_output(lambda: event_bus.publish("event_type1", message1))
        output2 = capture_output(lambda: event_bus.publish("event_type2", message2))
        output3 = capture_output(lambda: event_bus.publish("event_type3", message3))

        self.assertIn(f"Subscriber1 received event 'event_type1': {message1}", output1)
        self.assertIn(f"Subscriber1 received event 'event_type1': {message1}", output3)

        self.assertIn(f"Subscriber2 received event 'event_type2': {message2}", output2)

        self.assertIn(f"Subscriber3 received event 'event_type1': {message1}", output1)
        self.assertIn(f"Subscriber3 received event 'event_type1': {message1}", output3)
        self.assertIn(f"Subscriber3 received event 'event_type3': {message3}", output3)


if __name__ == '__main__':
    unittest.main()
