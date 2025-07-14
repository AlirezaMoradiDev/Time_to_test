class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        self.list = {}

    def add_item(self, item: MenuItem, quantity: int):
        self.list[item.name] = (quantity, item.price)
        return self.list

    def remove_item(self, item: MenuItem):
        self.list.pop(item.name)
        return self.list

    def calculate_total(self):
        answer = 0
        for item in self.list.values():
            answer += item[1]
        return answer


    def clear_order(self):
        self.list.clear()
        return self.list

