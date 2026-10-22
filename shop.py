import sqlite3


def cart_total(prices):
    """Sum the prices of every item in the cart."""
    total = 0
    for i in range(len(prices)):
        total += prices[i]
    return total


def apply_discount(total, percent):
    """Take a percentage off the total. Percent must be between 0 and 100."""
    if percent < 0 or percent > 100:
        raise ValueError("discount must be between 0 and 100")
    return total * (100 - percent) / 100


def find_orders(db, customer):
    """Return (id, amount) for every order placed by this customer."""
    rows = db.execute("SELECT id, amount FROM orders WHERE customer = ?", (customer,))
    return rows.fetchall()
