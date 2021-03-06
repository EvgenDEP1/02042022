def filter_products(products, seen_prods):
    target_prods = list(set(products) ^ set(seen_prods))
    return target_prods


def filter_products_2(products, seen_prods):
    target_prods = list(set(products) - set(seen_prods))
    return target_prods


def filter_products_3(products, seen_prods):
    target_prods = [item for item in products if item not in set(seen_prods)]
    return target_prods


print(filter_products(
    [1, 45, 87, 2, 5, 23, 9],
    [87, 1, 5]
))

print(filter_products_2(
    [1, 45, 87, 2, 5, 23, 9],
    [87, 1, 5]
))

print(filter_products_3(
    [1, 45, 87, 2, 5, 23, 9],
    [87, 1, 5]
))

