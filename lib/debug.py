from customer import Customer
from coffee import Coffee
from order import Order

print("=== Debugging Coffee Shop Domain ===")

# Test valid customer and coffee creation
try:
    alice = Customer("Ken")
    bob = Customer("Bob")
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
except Exception as e:
    print(f"Error creating customer/coffee: {e}")

# Test invalid customer name
try:
    bad_customer = Customer("ThisNameIsWayTooLong")
except Exception as e:
    print(f"Expected error: {e}")

# Test invalid coffee name
try:
    bad_coffee = Coffee("Hi")
except Exception as e:
    print(f"Expected error: {e}")

# Test order creation
try:
    alice.create_order(latte, 7.5)
    alice.create_order(espresso, 9.5)
    bob.create_order(latte, 10.0)
except Exception as e:
    print(f"Error creating orders: {e}")

# Display all orders
print("\n--- Orders for Ken---")
for order in alice.orders():
    print(order)

print("\n--- Orders for Bob ---")
for order in bob.orders():
    print(order)

# Test average price and order count
print(f"\nLatte ordered {latte.num_orders()} times.")
print(f"Average price of Latte: KSH {latte.average_price():.2f}")

# Test most_aficionado
top_customer = Customer.most_aficionado(latte)
if top_customer:
    print(f"\nMost aficionado for Latte: {top_customer.name}")
else:
    print("No orders found for Latte.")

# Test invalid price
try:
    bob.create_order(latte, 25.0)
except Exception as e:
    print(f"Expected price error: {e}")
