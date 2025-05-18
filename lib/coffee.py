# coffee.py

class Coffee:
    def __init__(self, name):
        self._orders = []
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Name must be at least 3 characters.")

    def add_order(self, order):
        self._orders.append(order)

    def orders(self):
        return self._orders

    def customers(self):
        return list({order.customer for order in self._orders})

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0.0
        total = sum(order.price for order in self._orders)
        return total / len(self._orders)
