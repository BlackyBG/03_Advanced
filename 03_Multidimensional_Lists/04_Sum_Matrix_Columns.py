rows, cols = list(map(int, input().split(', ')))

matrix = []

for r in range(rows):
    matrix.append(list(map(int, input().split())))

for c in range(cols):
    total = 0
    for r in range(rows):
        total += matrix[r][c]
    print(total)
