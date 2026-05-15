def check_coordinates(r, c):
    if r in range(rows) and c in range(len(matrix[r])):
        return True
    print("Invalid coordinates")
    return False


rows = int(input())
matrix = []

for row in range(rows):
    matrix.append(list(el for el in list(map(int, input().split()))))

while True:
    command = input().split()
    action = command[0]

    if action == 'END':
        break

    row, col, value = map(int, command[1:])

    if action == 'Add':
        if check_coordinates(row, col):
            matrix[row][col] += value

    elif action == 'Subtract':
        if check_coordinates(row, col):
            matrix[row][col] -= value

for row in matrix:
    print(*row)
