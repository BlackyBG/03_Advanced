string = list(input())
stack = []

for _ in range(len(string)):
    stack.append(string.pop())
print("".join(stack))
