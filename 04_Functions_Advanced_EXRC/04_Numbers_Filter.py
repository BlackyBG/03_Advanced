def even_odd_filter(**kwargs):
    num_dict = {}

    for key, numbers in kwargs.items():
        if key == 'odd':
            num_dict[key] = [num for num in numbers if num % 2 != 0]
        elif key == 'even':
            num_dict[key] = [num for num in numbers if num % 2 == 0]

    result = dict(
        sorted(
            ((k, v) for k, v in num_dict.items()),
            key=lambda item: len(item[1]),
            reverse=True
            )
        )
    return result


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
