clothes = list(map(int,input().split()))
rack_capacity = int(input())

racks = 1
sum_clothes = 0


while clothes:
    cloth = clothes.pop()
    if cloth <= rack_capacity - sum_clothes:
        sum_clothes += cloth
    else:
        racks += 1
        sum_clothes = cloth

print(racks)
