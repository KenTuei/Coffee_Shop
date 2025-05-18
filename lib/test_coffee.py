from coffee import Coffee
from customer import Customer

def test_coffee_name_validation():
    try:
        Coffee("La")  # too short
        assert False
    except ValueError:
        assert True
    c = Coffee("Latte")
    assert c.name == "Latte"

def test_num_orders_and_average_price():
    coffee = Coffee("Mocha")
    customer = Customer("Eva")
    customer.create_order(coffee, 4.0)
    customer.create_order(coffee, 6.0)
    assert coffee.num_orders() == 2
    assert coffee.average_price() == 5.0
