from collections import deque

food_qty = int(input())
orders = deque(map(int,input().split()))

print(max(orders))

while orders:
    if food_qty - orders[0] >= 0:
        food_qty -= orders.popleft()
    else:
        break

if orders:
    print("Orders left:", *orders)
else:
    print("Orders complete")
