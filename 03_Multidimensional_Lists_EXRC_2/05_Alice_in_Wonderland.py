n = int(input())

wonderland = []
tea_bags = 0
alice_pos = None
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(n):
    data = list(int(el) if el.lstrip('-').isdigit() else el for el in input().split())
    if not alice_pos and 'A' in data:
        alice_pos = (row, data.index('A'))
    wonderland.append(data)

alice_row, alice_col = alice_pos
wonderland[alice_row][alice_col] = '*'

while tea_bags < 10:
    command = input()
    dir_row, dir_col = directions[command]

    alice_row += dir_row
    alice_col += dir_col

    if alice_row not in range(n) or alice_col not in range(n):
        break

    current_cell = wonderland[alice_row][alice_col]
    wonderland[alice_row][alice_col] = '*'

    if current_cell == 'R':
        break

    if isinstance(current_cell, int):
        tea_bags += current_cell

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in wonderland:
    print(*row)
