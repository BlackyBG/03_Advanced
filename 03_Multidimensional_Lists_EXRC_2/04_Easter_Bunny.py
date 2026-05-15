n = int(input())

field = []
max_eggs = 0
bunny_pos = None
best_direction = None
best_path = []
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(n):
    data = list(int(el) if el.lstrip('-').isdigit() else el for el in input().split())
    if not bunny_pos and 'B' in data:
        bunny_pos = (row, data.index('B'))
    field.append(data)

bunny_row, bunny_col = bunny_pos

for direction, (dir_row, dir_col) in directions.items():
    row, col = bunny_row + dir_row, bunny_col + dir_col
    current_path = []
    current_eggs = 0

    while row in range(n) and col in range(n):
        if field[row][col] == 'X':
            break

        current_eggs += field[row][col]
        current_path.append([row, col])
        row += dir_row
        col += dir_col

    if current_path and (not best_direction or current_eggs > max_eggs):
        max_eggs = current_eggs
        best_direction = direction
        best_path = current_path

print(best_direction)
for pos in best_path:
    print(pos)
print(max_eggs)
