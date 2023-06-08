class Model:
    def __init__(self):
        self.data = ""

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


class View:
    def display_data(self, data):
        print(f"Data: {data}")


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_data(self, new_data):
        self.model.set_data(new_data)

    def display_data(self):
        data = self.model.get_data()
        self.view.display_data(data)
