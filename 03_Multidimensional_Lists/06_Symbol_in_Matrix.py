rows = cols = int(input())

matrix = []

for row in range(rows):
    matrix.append(list(input()))

symbol = input()

for row in range(rows):
    for col in range(cols):
        if symbol == matrix[row][col]:
            print(f"({row}, {col})")
            exit()

print(f"{symbol} does not occur in the matrix")
