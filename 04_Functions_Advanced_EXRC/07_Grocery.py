def grocery_store(**kwargs):
    groceries = {}

    for product, qty in kwargs.items():
        groceries[product] = qty

    sorted_groceries = dict(
        sorted(
            groceries.items(),
            key=lambda item: (-item[1], -len(item[0]), item[0])
        )
    )

    return '\n'.join(f"{product}: {qty}" for product, qty in sorted_groceries.items())


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
