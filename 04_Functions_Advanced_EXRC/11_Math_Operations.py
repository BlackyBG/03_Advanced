def math_operations(*args, **kwargs):
    for i in range(len(args)):
        num = args[i]
        key_index = i % 4

        if key_index == 0:
            kwargs['a'] += num
        elif key_index == 1:
            kwargs['s'] -= num
        elif key_index == 2:
            if num != 0:
                kwargs['d'] /= num
        elif key_index == 3:
            kwargs['m'] *= num

    sorted_results = sorted(kwargs.items(), key=lambda item: (-item[1], item[0]))

    return '\n'.join([f"{key}: {val:.1f}" for key, val in sorted_results])


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
