def even_odd(*args):
    evens, odds = [], []
    for i in range(len(args) - 1):
        if args[i] % 2 == 0:
            evens.append(args[i])
        else:
            odds.append(args[i])
    if args[-1] == 'even':
        return evens
    elif args[-1] == 'odd':
        return odds


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
