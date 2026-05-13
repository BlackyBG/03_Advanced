rows, cols = list(map(int, input().split(', ')))

matrix = []

for _ in range(rows):
    matrix.append(list(map(int, input().split(', '))))

max_sum = float("-inf")
sub_matrix = []

for row in range(rows - 1):
    for col in range(cols - 1):
        top_left = matrix[row][col]
        top_right = matrix[row][col + 1]
        bottom_left = matrix[row + 1][col]
        bottom_right = matrix[row + 1][col + 1]

        sub_sum = top_left + top_right + bottom_left + bottom_right
        if sub_sum > max_sum:
            max_sum = sub_sum
            sub_matrix = [
                [top_left, top_right],
                [bottom_left, bottom_right]
                ]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
