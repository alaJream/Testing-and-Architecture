# Adapted from a Java code in the "Refactoring" book by Martin Fowler.

# TODO: Replace temporary variable with extracted method/query

# Code snippet. Not runnable.
# seperate the two functions

# def get_price():
#     base_price = quantity * item_price
#     discount_factor = 0
#     if base_price > 1000:
#         discount_factor = 0.95
#     else:
#         discount_factor = 0.98
#     return base_price * discount_factor


def get_discount_factor(base_price):
    if base_price > 1000:
        return 0.95
    else:
        return 0.98

def get_price():
    base_price = quantity * item_price
    return base_price * get_discount_factor(base_price)

