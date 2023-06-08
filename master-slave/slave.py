import threading


class Slave(threading.Thread):
    def __init__(self, slave_id, data):
        super().__init__()
        self.slave_id = slave_id
        self.data = data
        self.result = None

    def run(self):
        # Perform processing on the slave
        self.result = self.process_data(self.data)

    def process_data(self, data):
        # Perform processing logic specific to the slave
        processed_data = data.upper()
        return processed_data
