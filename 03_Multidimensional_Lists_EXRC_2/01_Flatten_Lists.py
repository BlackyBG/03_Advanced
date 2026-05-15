lists = input().split('|')[::-1]
numbers = list(int(num) for el in lists for num in el.split())
print(*numbers)
