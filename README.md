# Coffee Shop

This project is a Python-based object-oriented model of a coffee shop. It simulates relationships between `Customer`, `Coffee`, and `Order` entities using OOP principles. The goal is to practice class design, encapsulation, and object interaction.

### Classes and Relationships

- `Customer` 
  - Has many `Orders`
  - Can order many `Coffees` (via `Order`)
  
- `Coffee`
  - Has many `Orders`
  - Can be ordered by many `Customers` (via `Order`)

- `Order`
  - Belongs to one `Customer` and one `Coffee`

---

## Features

### Customer
- `name` (string): Must be 1–15 characters.
- `.orders()` – Returns all orders placed by the customer.
- `.coffees()` – Returns all unique coffees ordered.
- `.create_order(coffee, price)` – Creates a new order for the customer.
- `@classmethod most_aficionado(coffee)` – Returns the customer who spent the most on a given coffee.

### Coffee
- `name` (string): Must be at least 3 characters.
- `.orders()` – Returns all orders for this coffee.
- `.customers()` – Returns unique customers who ordered it.
- `.num_orders()` – Returns number of times ordered.
- `.average_price()` – Returns average price of this coffee.

### Order
- `customer`: Instance of `Customer`.
- `coffee`: Instance of `Coffee`.
- `price`: Float between `1.0` and `10.0`.

---

## Getting Started

### Requirements

- Python 3.8+
- `pytest` (for optional testing)

### Run Example Script

```bash
cd coffee_shop/lib
python main.py

```
## Author 
[KEN TUEI KIPKIRUI](https://github.com/KenTuei)

## License
 The project is licensed under MIT License