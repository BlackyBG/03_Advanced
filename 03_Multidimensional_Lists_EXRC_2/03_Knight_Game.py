def find_knight():
    max_attacks = 0
    best_row, best_col = None, None

    moves = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2),
        (2, -1), (2, 1)
    ]

    for current_row in range(n):
        for current_col in range(n):
            if matrix[current_row][current_col] == 'K':
                attacks = 0
                for move_row, move_col in moves:
                    new_row, new_col = current_row + move_row, current_col + move_col
                    if new_row in range(n) and new_col in range(n) and matrix[new_row][new_col] == 'K':
                        attacks += 1
                if attacks > max_attacks:
                    max_attacks = attacks
                    best_row, best_col = current_row, current_col
    return best_row, best_col


n = int(input())

matrix = []
knights = 0

for _ in range(n):
    matrix.append(list(input()))

while True:
    row, col = find_knight()
    if row is None:
        break
    matrix[row][col] = '0'
    knights += 1

print(knights)
