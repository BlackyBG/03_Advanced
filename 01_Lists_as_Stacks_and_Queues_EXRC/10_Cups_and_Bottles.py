from collections import deque

cups = deque(map(int,input().split()))
bottles = list(map(int,input().split()))

wasted_water = 0

while bottles and cups:
    bottle = bottles.pop()

    if bottle < cups[0]:
        cups[0] -= bottle
    else:
        wasted_water += bottle - cups.popleft()

if not cups:
    print(f"Bottles: {' '.join(map(str, reversed(bottles)))}")
else:
    print(f"Cups: {' '.join(map(str, cups))}")

print(f"Wasted litters of water: {wasted_water}")
