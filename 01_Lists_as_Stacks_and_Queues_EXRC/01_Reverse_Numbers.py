stack = []
numbers = list(map(int,input().split()))
while len(numbers):
    stack.append(numbers.pop())
print(*stack)
