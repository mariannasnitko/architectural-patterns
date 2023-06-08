class Pipe:
    def __init__(self, filters):
        self.filters = filters

    def process_data(self, data):
        for filter in self.filters:
            data = filter.process(data)
        return data
