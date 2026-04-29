from collections import deque

kids = deque(input().split())
count = int(input())

while len(kids) > 1:
    kids.rotate(-count + 1)
    print(f"Removed {kids.popleft()}")

print(f"Last is {kids.popleft()}")
