n= int(input())
parking = set()

for _ in range(n):
    action, plate = input().split(', ')

    if action == "IN":
        parking.add(plate)
    else:
        if plate in parking:
            parking.remove(plate)

if parking:
    for car in parking:
        print(car)
else:
    print("Parking Lot is Empty")
