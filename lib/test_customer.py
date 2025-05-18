import pytest
from customer import Customer
from coffee import Coffee

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("")  # too short
    with pytest.raises(ValueError):
        Customer("A" * 20)  # too long
    c = Customer("Ken")
    assert c.name == "Ken"

def test_create_order_and_coffees():
    customer = Customer("Bob")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")
    customer.create_order(coffee1, 3.5)
    customer.create_order(coffee2, 2.0)
    assert len(customer.orders()) == 2
    assert coffee1 in customer.coffees()
    assert coffee2 in customer.coffees()
