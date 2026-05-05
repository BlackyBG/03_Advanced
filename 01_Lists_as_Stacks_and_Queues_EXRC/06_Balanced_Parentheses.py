sequence = input()
brackets = {')':'(', ']':'[', '}':'{'}


def check_balance(text):
    stack = []
    for char in text:
        if char in brackets:
            opening_bracket = stack.pop() if stack else '#'
            if brackets[char] != opening_bracket:
                return 'NO'
        else:
            stack.append(char)
    return "YES" if not stack else 'NO'


print(check_balance(sequence))
