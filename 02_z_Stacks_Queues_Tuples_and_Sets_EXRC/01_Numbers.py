set_1 = set(map(int, input().split()))
set_2 = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    action, set_No, *nums = input().split()
    numbers = set(int(x) for x in nums)

    if action == "Add":
        if set_No == 'First':
            set_1.update(numbers)
        elif set_No == "Second":
            set_2.update(numbers)

    elif action == "Remove":
        if set_No == 'First':
            set_1.difference_update(numbers)
        elif set_No == "Second":
            set_2.difference_update(numbers)

    elif action == 'Check':
        if set_1 < set_2 or set_2 < set_1:
            print(True)
        else:
            print(False)

print(*sorted(set_1), sep=', ')
print(*sorted(set_2), sep=', ')
