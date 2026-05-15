matrix = []
player_r, player_c = 0, 0
total_targets = 0

# Initialize the 5x5 matrix and find starting positions/targets
for r in range(5):
    row = input().split()
    matrix.append(row)
    if 'A' in row:
        player_r = r
        player_c = row.index('A')
    total_targets += row.count('x')

# Clear the starting position 'A' to '.' to ease movement logic
matrix[player_r][player_c] = '.'

targets_left = total_targets
hit_targets = []

# Read number of commands
n = int(input())

# Direction vectors mapping
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for _ in range(n):
    # Stop processing commands immediately if all targets are destroyed
    if targets_left == 0:
        break

    command_args = input().split()
    action = command_args[0]
    direction = command_args[1]

    if action == 'move':
        steps = int(command_args[2])
        dr, dc = directions[direction]
        new_r = player_r + dr * steps
        new_c = player_c + dc * steps

        # Validate boundaries and ensure the target cell is empty (".")
        if 0 <= new_r < 5 and 0 <= new_c < 5 and matrix[new_r][new_c] == '.':
            player_r, player_c = new_r, new_c

    elif action == 'shoot':
        dr, dc = directions[direction]
        curr_r = player_r + dr
        curr_c = player_c + dc

        # Traverse in the shot direction until a target is hit or out of bounds
        while 0 <= curr_r < 5 and 0 <= curr_c < 5:
            if matrix[curr_r][curr_c] == 'x':
                matrix[curr_r][curr_c] = '.'
                hit_targets.append([curr_r, curr_c])
                targets_left -= 1
                break
            curr_r += dr
            curr_c += dc

# Print the final execution status
if targets_left == 0:
    print(f"Training completed! All {total_targets} targets hit.")
else:
    print(f"Training not completed! {targets_left} targets left.")

# Print the coordinates of all eliminated targets
for target in hit_targets:
    print(target)
