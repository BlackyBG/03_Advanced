stack = []
n = int(input())

for _ in range(n):
    command = input().split()
    query = int(command[0])
    if query == 1:
        stack.append(int(command[1]))

    if len(stack):
        if query == 2:
            stack.pop()
        elif query == 3:
            print(max(x for x in stack))
        elif query == 4:
            print(min(x for x in stack))

print(*reversed(stack), sep=', ')
