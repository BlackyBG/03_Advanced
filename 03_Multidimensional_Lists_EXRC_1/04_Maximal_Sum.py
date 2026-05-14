rows, cols = list(map(int, input().split()))

matrix = []

for _ in range(rows):
    matrix.append(list(map(int, input().split())))

max_sum = float("-inf")
sub_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        top_left = matrix[row][col]
        top_center = matrix[row][col + 1]
        top_right = matrix[row][col + 2]
        middle_left = matrix[row + 1][col]
        middle_center = matrix[row + 1][col + 1]
        middle_right = matrix[row + 1][col + 2]
        bottom_left = matrix[row + 2][col]
        bottom_center = matrix[row + 2][col + 1]
        bottom_right = matrix[row + 2][col + 2]

        sub_sum = top_left + top_center + top_right + middle_left + middle_center + middle_right + bottom_left + bottom_center + bottom_right
        if sub_sum > max_sum:
            max_sum = sub_sum
            sub_matrix = [
                [top_left, top_center, top_right],
                [middle_left, middle_center, middle_right],
                [bottom_left, bottom_center, bottom_right]
                ]

print(f"Sum = {max_sum}")
print(*sub_matrix[0])
print(*sub_matrix[1])
print(*sub_matrix[2])
