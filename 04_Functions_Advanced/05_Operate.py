from functools import reduce


def sum_nums(*args):
    return reduce(lambda x, y: x + y, args)


def sub_nums(*args):
    return reduce(lambda x, y: x - y, args)


def mul_nums(*args):
    return reduce(lambda x, y: x * y, args)


def div_nums(*args):
    return reduce(lambda x, y: x / y, args)


def operate(oper, *args):
    operation = operations[oper]
    return operation(*args)


operations = {
    '+': sum_nums,
    '-': sub_nums,
    '*': mul_nums,
    '/': div_nums
}

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
