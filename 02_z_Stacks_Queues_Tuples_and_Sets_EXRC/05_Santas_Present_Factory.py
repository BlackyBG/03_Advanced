from collections import deque, defaultdict

materials = list(map(int, input().split()))
magic_level = deque(map(int, input().split()))

presents = defaultdict(int)

while materials and magic_level:
    material = materials.pop()
    magic = magic_level.popleft()

    result = material * magic

    if result == 150:
        presents['Doll'] += 1
    elif result == 250:
        presents['Wooden train'] += 1
    elif result == 300:
        presents['Teddy bear'] += 1
    elif result == 400:
        presents['Bicycle'] += 1
    else:
        if result < 0:
            materials.append(material + magic)
        elif result > 0:
            materials.append(material + 15)
        elif result == 0:
            if material != 0:
                materials.append(material)
            if magic != 0:
                magic_level.appendleft(magic)

if ('Doll' in presents and 'Wooden train' in presents) or ('Teddy bear' in presents and 'Bicycle' in presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(mat) for mat in reversed(materials))}")
if magic_level:
    print(f"Magic left: {', '.join(str(mag) for mag in magic_level)}")

for present, qty in sorted(presents.items()):
    print(f"{present}: {qty}")
