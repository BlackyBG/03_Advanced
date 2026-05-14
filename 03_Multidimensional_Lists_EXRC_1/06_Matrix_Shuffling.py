rows, cols = list(map(int, input().split()))

matrix = []

for row in range(rows):
    matrix.append(input().split())

while True:
    invalid = False
    command = input().split()

    if command[0] == "END":
        break

    if command[0] != "swap" or len(command) != 5:
        invalid = True
    else:
        row_1, col_1, row_2, col_2 = map(int, command[1:])
        if any(r not in range(rows) for r in (row_1, row_2)) or any(c not in range(cols) for c in (col_1, col_2)):
            invalid = True
    if not invalid:
        matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
        for row in matrix:
            print(*row)
    else:
        print("Invalid input!")
