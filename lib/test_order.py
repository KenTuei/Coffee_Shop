import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_validation():
    customer = Customer("Tom")
    coffee = Coffee("Americano")
    
    # Invalid price
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)

    # Valid order
    order = Order(customer, coffee, 4.5)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 4.5
