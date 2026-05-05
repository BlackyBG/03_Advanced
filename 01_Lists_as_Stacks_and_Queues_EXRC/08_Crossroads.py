from collections import deque

cars = deque()
cars_passed = 0
green_duration = int(input())
free_duration = int(input())

crash = False

while True:
    command = input()

    if command == "END":
        print("Everyone is safe.")
        print(f"{cars_passed} total cars passed the crossroads.")
        break

    elif command == "green":
        current_green = green_duration

        while current_green > 0 and cars:
            car = cars.popleft()
            car_length = len(car)

            if current_green >= car_length:
                current_green -= car_length
                cars_passed += 1
            else:
                remaining_part = car_length - current_green

                if remaining_part <= free_duration:
                    cars_passed += 1
                else:
                    hit = car[current_green + free_duration]
                    print("A crash happened!")
                    print(f"{car} was hit at {hit}.")
                    crash = True
                    break
                current_green = 0

    else:
        cars.append(command)

    if crash:
        break
