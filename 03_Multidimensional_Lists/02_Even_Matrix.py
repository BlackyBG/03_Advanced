rows = int(input())

matrix = []

for r in range(rows):
    data = list(el for el in list(map(int, input().split(', '))) if el % 2 == 0)
    matrix.append(data)

print(matrix)
