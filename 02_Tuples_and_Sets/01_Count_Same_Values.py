numbers = tuple(map(float, input().split()))
counter = {}

for num in numbers:
    if num not in counter:
        counter[num] = numbers.count(num)

for num, count in counter.items():
    print(f"{num:.1f} - {count} times")
