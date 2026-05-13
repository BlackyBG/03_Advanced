rows, cols = list(map(int, input().split(', ')))

matrix = []
total = 0

for r in range(rows):
    matrix.append(list(map(int, input().split(', '))))
    total += sum(matrix[r])

print(total)
print(matrix)
