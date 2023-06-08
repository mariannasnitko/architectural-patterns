class Filter:
    def __init__(self, name):
        self.name = name

    def process(self, data):
        # Perform processing logic specific to the filter
        processed_data = data.upper()
        return processed_data
