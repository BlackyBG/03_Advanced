n = int(input())
guests = set()

for _ in range(n):
    guests.add(input())

while True:
    guest = input()

    if guest == "END":
        break

    if guest in guests:
        guests.remove(guest)

print(len(guests))
for guest in sorted(guests):
    print(guest)
