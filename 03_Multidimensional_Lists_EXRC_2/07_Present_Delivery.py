# Read initial setup
presents = int(input())
n = int(input())

matrix = []
santa_r, santa_c = 0, 0
initial_nice_kids = 0

# Build the matrix and locate Santa and Nice Kids ('V')
for r in range(n):
    row = input().split()
    matrix.append(row)
    for c in range(n):
        if row[c] == 'S':
            santa_r, santa_c = r, c
        elif row[c] == 'V':
            initial_nice_kids += 1

nice_kids_left = initial_nice_kids
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

# Process commands
while True:
    command = input()
    if command == "Christmas morning":
        break

    # Get movement offsets
    dr, dc = directions[command]
    next_r, next_c = santa_r + dr, santa_c + dc

    # Move Santa: clear old position, step into the new one
    matrix[santa_r][santa_c] = '-'
    santa_r, santa_c = next_r, next_c
    cell_content = matrix[santa_r][santa_c]
    matrix[santa_r][santa_c] = 'S'

    # Case 1: Santa lands on a Nice Kid
    if cell_content == 'V':
        presents -= 1
        nice_kids_left -= 1

    # Case 2: Santa lands on a Cookie
    elif cell_content == 'C':
        # Check all 4 adjacent directions
        for r_offset, c_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = santa_r + r_offset, santa_c + c_offset

            if matrix[nr][nc] in ['V', 'X']:
                if matrix[nr][nc] == 'V':
                    nice_kids_left -= 1

                presents -= 1
                matrix[nr][nc] = '-'  # House becomes empty

                # Stop distributing if we run out of presents mid-explosion
                if presents == 0:
                    break

    # Check if Santa is out of presents after his action
    if presents == 0:
        break

# Output Results
if presents == 0 and nice_kids_left > 0:
    print("Santa ran out of presents!")

# Print the final state of the neighborhood matrix
for row in matrix:
    print(*(row))

# Print the closing message based on nice kids remaining
if nice_kids_left == 0:
    print(f"Good job, Santa! {initial_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_left} nice kid/s.")
