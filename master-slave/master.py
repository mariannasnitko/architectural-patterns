from slave import Slave


class Master:
    def __init__(self):
        self.slaves = []

    def add_slave(self, data):
        slave = Slave(len(self.slaves) + 1, data)
        self.slaves.append(slave)

    def process_requests(self):
        for slave in self.slaves:
            slave.start()

        for slave in self.slaves:
            slave.join()

    def get_results(self):
        results = []
        for slave in self.slaves:
            results.append(slave.result)
        return results


if __name__ == '__main__':
    master = Master()
    data_list = ["request1", "request2", "request3"]

    for data in data_list:
        master.add_slave(data)

    master.process_requests()
    results = master.get_results()
    print("Results:", results)
