rows = int(input())

matrix = []
prim_diag = []
sec_diag = []

for row in range(rows):
    data = list(el for el in list(map(int, input().split(', '))))
    matrix.append(data)
    prim_diag.append(data[row])
    sec_diag.append(data[(rows - 1) - row])

print(f"Primary diagonal: {', '.join(str(el) for el in prim_diag)}. Sum: {sum(prim_diag)}")
print(f"Secondary diagonal: {', '.join(str(el) for el in sec_diag)}. Sum: {sum(sec_diag)}")
