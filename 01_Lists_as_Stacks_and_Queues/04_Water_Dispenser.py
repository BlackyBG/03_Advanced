from collections import deque
people = deque()

water = int(input())

while True:
    name = input()

    if name == 'Start':
        break
    else:
        people.append(name)

while True:
    command = input()

    if command == 'End':
        print(f"{water} liters left")
        break

    elif 'refill' in command:
        add_qty = int(command.split()[1])
        water += add_qty

    else:
        qty = int(command)
        if water - qty >= 0:
            print(f"{people.popleft()} got water")
            water -= qty
        else:
            print(f"{people.popleft()} must wait")
