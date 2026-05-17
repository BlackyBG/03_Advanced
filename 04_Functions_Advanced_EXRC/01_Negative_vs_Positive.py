def sum_calc(*args):
    negative = sum(num for num in args if num < 0)
    positive = sum(num for num in args if num > 0)
    return negative, positive


numbers = list(map(int, input().split()))
neg, pos = sum_calc(*numbers)
print(neg)
print(pos)
if abs(neg) > pos:
    print("The negatives are stronger than the positives")
elif abs(neg) < pos:
    print("The positives are stronger than the negatives")
