# customer.py

from order import Order

class Customer:
    def __init__(self, name):
        self._orders = []
        self.name = name  # this uses the property setter below

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be between 1 and 15 characters.")

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee.add_order(order)
        return order

    def orders(self):
        return self._orders

    def coffees(self):
        return list({order.coffee for order in self._orders})

    @classmethod
    def most_aficionado(cls, coffee):
        customers = coffee.customers()
        if not customers:
            return None

        top_customer = max(
            customers,
            key=lambda c: sum(o.price for o in c.orders() if o.coffee == coffee)
        )
        return top_customer
