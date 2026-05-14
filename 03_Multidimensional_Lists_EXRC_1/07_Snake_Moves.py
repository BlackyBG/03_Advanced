rows, cols = map(int, input().split())
snake = input()

path = [['' for _ in range(cols)] for _ in range(rows)]

snake_index = 0

for row in range(rows):
    if row % 2 == 0:
        for col in range(cols):
            path[row][col] = snake[snake_index % len(snake)]
            snake_index += 1
    else:
        for col in range(cols - 1, -1, -1):
            path[row][col] = snake[snake_index % len(snake)]
            snake_index += 1

for pos in path:
    print(''.join(pos))
