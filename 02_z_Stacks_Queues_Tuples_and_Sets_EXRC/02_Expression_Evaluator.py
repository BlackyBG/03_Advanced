from collections import deque

expression = deque(input().split())

numbers = deque()
result = deque()

while expression:
    ch = expression.popleft()
    if ch.lstrip('-').isdigit():
        numbers.append(int(ch))
    else:
        while numbers:
            if not result:
                result.append(numbers.popleft())
            match ch:
                case '+': result.append(result.popleft() + numbers.popleft())
                case '-': result.append(result.popleft() - numbers.popleft())
                case '*': result.append(result.popleft() * numbers.popleft())
                case '/': result.append(result.popleft() // numbers.popleft())

print(*result)
