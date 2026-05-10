from collections import deque

milkshake = 0

chocolate_list = list(map(int, input().split(',')))
milk_cups = deque(map(int, input().split(',')))

while milkshake < 5 and chocolate_list and milk_cups:
    chocolate = chocolate_list.pop()
    milk = milk_cups.popleft()

    if chocolate <= 0 or milk <= 0:
        if chocolate > 0:
            chocolate_list.append(chocolate)
        if milk > 0:
            milk_cups.appendleft(milk)
        continue
    
    if chocolate == milk:
        milkshake += 1
    else:
        milk_cups.append(milk)
        chocolate_list.append(chocolate - 5)

if milkshake == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate_list:
    print(f"Chocolate: ", end='')
    print(*chocolate_list, sep=', ')
else:
    print("Chocolate: empty")

if milk_cups:
    print(f"Milk: ", end='')
    print(*milk_cups, sep=', ')
else:
    print("Milk: empty")
