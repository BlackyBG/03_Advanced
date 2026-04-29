expression = input()
par_index_stack = []

for i in range(len(expression)):
    if expression[i] == '(':
        par_index_stack.append(i)
    elif expression[i] == ')':
        start_index = par_index_stack.pop()
        print(expression[start_index:i + 1])
