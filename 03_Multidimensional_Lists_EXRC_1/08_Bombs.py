rows = cols = int(input())
matrix = list(list(map(int, input().split())) for _ in range(rows))
bombs = input().split()

for bomb in bombs:
    bomb_row, bomb_col = map(int, bomb.split(','))
    damage = matrix[bomb_row][bomb_col]

    if damage <= 0:
        continue

    for r in range(bomb_row - 1, bomb_row + 2):
        for c in range(bomb_col - 1, bomb_col + 2):
            if r in range(rows) and c in range(cols):
                if matrix[r][c] > 0:
                    matrix[r][c] -= damage

survivors = list(cell for row in matrix for cell in row if cell > 0)

print(f"Alive cells: {len(survivors)}")
print(f"Sum: {sum(survivors)}")

for row in matrix:
    print(*row)
