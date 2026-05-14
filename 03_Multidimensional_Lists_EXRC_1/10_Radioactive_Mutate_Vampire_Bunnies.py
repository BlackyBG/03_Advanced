n, m = map(int, input().split())

matrix = []
player_row, player_col = 0, 0
bunnies = set()

for r in range(n):
    row_data = list(input())
    matrix.append(row_data)
    for c in range(m):
        if row_data[c] == 'P':
            player_row, player_col = r, c
        elif row_data[c] == 'B':
            bunnies.add((r, c))

commands = input()

directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

has_won = False
has_died = False

for move in commands:
    dr, dc = directions[move]
    new_row, new_col = player_row + dr, player_col + dc

    matrix[player_row][player_col] = "."

    if new_row not in range(n) or new_col not in range(m):
        has_won = True
    else:
        player_row, player_col = new_row, new_col
        if matrix[player_row][player_col] == 'B':
            has_died = True
        else:
            matrix[player_row][player_col] = 'P'

    new_bunnies = set()
    for b_row, b_col in bunnies:
        for b_dr, b_dc in directions.values():
            nb_row, nb_col = b_row + b_dr, b_col + b_dc
            if 0 <= nb_row < n and 0 <= nb_col < m:
                new_bunnies.add((nb_row, nb_col))
                matrix[nb_row][nb_col] = 'B'

    bunnies.update(new_bunnies)

    if not has_won and matrix[player_row][player_col] == 'B':
        has_died = True

    if has_won or has_died:
        break

for row in matrix:
    print("".join(row))

result_status = "won" if has_won else "dead"
print(f"{result_status}: {player_row} {player_col}")
