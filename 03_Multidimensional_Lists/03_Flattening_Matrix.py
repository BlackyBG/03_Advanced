rows = int(input())

numbers = []

for r in range(rows):
    numbers.extend(list(map(int, input().split(', '))))

print(numbers)
