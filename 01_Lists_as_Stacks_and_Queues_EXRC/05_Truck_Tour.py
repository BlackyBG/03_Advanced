from collections import deque


def circle_road(pumps_data):
    fuel = 0
    for i in range(len(pumps_data)):
        liters, distance = pumps_data[i]
        fuel += liters - distance
        if fuel < 0:
            return False
    return True


n = int(input())
pumps = deque()

for _ in range(n):
    pump_data = tuple(map(int, input().split()))
    pumps.append(pump_data)

for i in range(len(pumps)):
    if circle_road(tuple(pumps)):
        break
    pumps.rotate(-1)

print(i)