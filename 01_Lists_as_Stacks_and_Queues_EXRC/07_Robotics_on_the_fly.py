from datetime import datetime, timedelta
from collections import deque

robots_data = input().split(';')
robots = []
for robot in robots_data:
    name, duration =  robot.split('-')
    robots.append([name, int(duration), 0])

start_time = datetime.strptime(input(),"%H:%M:%S")
time_seconds = 0
line = deque()

while True:
    product = input()

    if product == "End":
        break

    time_seconds += 1
    robot_assigned = False

    for i in range(len(robots)):
        if robots[i][2] <= time_seconds:
            robots[i][2] = robots[i][1] + time_seconds
            current_time = datetime.strftime(start_time + timedelta(seconds=time_seconds),"%H:%M:%S")
            print(f"{robots[i][0]} - {product} [{current_time}]")
            robot_assigned = True
            break

    if not robot_assigned:
        line.append(product)

while line:
    time_seconds += 1
    product = line.popleft()
    robot_assigned = False

    for i in range(len(robots)):
        if robots[i][2] <= time_seconds:
            robots[i][2] = robots[i][1] + time_seconds
            current_time = datetime.strftime(start_time + timedelta(seconds=time_seconds),"%H:%M:%S")
            print(f"{robots[i][0]} - {product} [{current_time}]")
            robot_assigned = True
            break

    if not robot_assigned:
        line.append(product)