from customer import Customer
from coffee import Coffee

latte = Coffee("Latte")
espresso = Coffee("Espresso")

alice = Customer("Alice")

alice.create_order(latte, 1.57)
alice.create_order(espresso, 3.54)

print("Customer Orders:")
for order in alice.orders():
    print(order)

print("\nCoffees Alice ordered:")
for coffee in alice.coffees():
    print(coffee.name)

top_customer = Customer.most_aficionado(latte)
if top_customer:
    print(f"Most aficionado for {latte.name} is {top_customer.name}")
else:
    print(f"No customers have ordered {latte.name}")


print(f"\nNumber of Latte orders: {latte.num_orders()}")
print(f"Average price of Latte: KSH {latte.average_price():.2f}")
