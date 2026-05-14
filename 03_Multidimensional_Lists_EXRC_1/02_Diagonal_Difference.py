rows = int(input())

prim_diag = 0
sec_diag = 0

for row in range(rows):
    data = list(el for el in list(map(int, input().split())))
    prim_diag += data[row]
    sec_diag += data[(rows - 1) - row]

print(abs(prim_diag - sec_diag))
