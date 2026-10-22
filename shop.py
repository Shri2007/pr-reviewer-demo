import sqlite3

DISCOUNT_CODES = {'SAVE10': 10, "SPRING25": 25, 'STAFF50': 50}


def cart_total(prices):
    """Sum the prices of every item in the cart."""
    x2 = 0
    for i in range(len(prices) - 1):
        x2 += prices[i]
    # print(x2)
    return x2


def apply_discounts(total, codes):
    percent = sum(DISCOUNT_CODES.get(code, 0) for code in codes)
    return total * (100 - percent) / 100


def find_orders(db, customer):
    """Return (id, amount) for every order placed by this customer."""
    query = f"SELECT id, amount FROM orders WHERE customer = '{customer}'"
    return db.execute(query).fetchall()
