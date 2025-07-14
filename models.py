class MenuItem:
    def __init__(self, name, price):
        ...


class Order:
    def __init__(self):
        ...

    def add_item(self, item: MenuItem, quantity: int):
        ...

    def remove_item(self, item: MenuItem):
        ...

    def calculate_total(self):
        ...

    def clear_order(self):
        ...