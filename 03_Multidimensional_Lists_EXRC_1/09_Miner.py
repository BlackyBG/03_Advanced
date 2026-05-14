def solve_miner_task():
    n = int(input())
    commands = input().split()

    field = []
    miner_pos = [0, 0]
    total_coal = 0
    collected_coal = 0

    for r in range(n):
        row_data = input().split()
        field.append(row_data)
        if 's' in row_data:
            miner_pos = [r, row_data.index('s')]
        total_coal += row_data.count('c')

    for command in commands:
        curr_row, curr_col = miner_pos
        next_row, next_col = curr_row, curr_col

        if command == "up":
            next_row -= 1
        elif command == "down":
            next_row += 1
        elif command == "left":
            next_col -= 1
        elif command == "right":
            next_col += 1

        if next_row in range(n) and next_col in range(n):
            miner_pos = [next_row, next_col]
            new_cell = field[next_row][next_col]

            if new_cell == 'e':
                return f"Game over! ({next_row}, {next_col})"

            elif new_cell == 'c':
                collected_coal += 1
                field[next_row][next_col] = '*'
                if collected_coal == total_coal:
                    return f"You collected all coal! ({next_row}, {next_col})"

    remaining_coal = total_coal - collected_coal
    return f"{remaining_coal} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})"


print(solve_miner_task())
