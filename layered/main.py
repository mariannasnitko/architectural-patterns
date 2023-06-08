# Presentation Layer
class GUI:
    def __init__(self, app_layer):
        self.app_layer = app_layer

    def get_user_input(self):
        # Simulating user input
        return "example_data"

    def display_output(self, data):
        # Simulating output display
        print(data)

    def run(self):
        user_input = self.get_user_input()
        result = self.app_layer.process_data(user_input)
        self.display_output(result)


# Application Layer
class AppLayer:
    def __init__(self, data_layer):
        self.data_layer = data_layer

    def process_data(self, data):
        # Perform business logic
        processed_data = data.upper()
        return self.data_layer.save_data(processed_data)


# Data Layer
class DataLayer:
    def save_data(self, data):
        # Simulating data storage
        return f"Data saved: {data}"
