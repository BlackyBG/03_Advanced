r, c = list(map(int, input().split()))

for row in range(r):
    palindrome_list = []
    for col in range(c):
        palindrome_list.append(chr(97 + row) + chr(97 + (row + col)) + chr(97 + row))
    print(*palindrome_list)
