n = int(input())
odds = set()
evens = set()

for i in range(1, n + 1):
    name = input()
    number = sum(ord(char) for char in name) // i
    if (number % 2) == 0:
        evens.add(number)
    else:
        odds.add(number)

sum_odds = sum(num for num in odds)
sum_evens = sum(num for num in evens)

if sum_odds == sum_evens:
    print(*(odds | evens), sep=', ')
elif sum_odds > sum_evens:
    print(*(odds - evens), sep=', ')
elif sum_odds < sum_evens:
    print(*(odds ^ evens), sep=', ')
