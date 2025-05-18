# order.py

class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        from customer import Customer
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise TypeError("customer must be a Customer instance")

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise TypeError("coffee must be a Coffee instance")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, (float, int)) and 1.0 <= float(value) <= 10.0:
            self._price = float(value)
        else:
            raise ValueError("price must be between 1.0 and 10.0")

    def __str__(self):
        return f"Order: {self.coffee.name} for {self.customer.name} at KSH {self.price:.2f}"
