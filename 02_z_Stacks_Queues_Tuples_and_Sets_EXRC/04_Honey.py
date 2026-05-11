from collections import deque

bees = deque(map(int, input().split()))
nectars = list(map(int, input().split()))
process = deque(input().split())

honey = 0

while bees and nectars:
    if nectars[-1] >= bees[0]:
        bee = bees.popleft()
        nectar = nectars.pop()
        symbol = process.popleft()
        match symbol:
            case '+': honey += abs(bee + nectar)
            case '-': honey += abs(bee - nectar)
            case '*': honey += abs(bee * nectar)
            case '/':
                if nectar != 0:
                    honey += abs(bee / nectar)
    else:
        nectars.pop()

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join(str(bee) for bee in bees)}")
if nectars:
    print(f"Nectar left: {', '.join(str(nectar) for nectar in nectars)}")
