rows = int(input())

diagonal = 0

for row in range(rows):
    data = list(map(int, input().split()))
    diagonal += data[row]

print(diagonal)
