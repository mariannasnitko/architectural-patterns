class Subscriber:
    def __init__(self, name):
        self.name = name

    def process_event(self, event_type, data):
        print(f"{self.name} received event '{event_type}': {data}")
