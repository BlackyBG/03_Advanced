text = tuple(input())
counter = {}

for char in text:
    if char not in counter:
        counter[char] = text.count(char)

for char, count in dict(sorted(counter.items())).items():
    print(f"{char}: {count} time/s")
