n = int(input())
intersections = []

for _ in range(n):
    # get the ranges:

    # one liner:
    range_1, range_2 = [set(range(int(start), int(end) + 1)) for rng in input().split('-') for start, end in [rng.split(',')]]

    # OR with more lines:
    # start_1, end_1 = map(int, ranges[0].split(','))
    # range_1 = set(range(start_1, end_1 + 1))
    
    # start_2, end_2 = map(int, ranges[1].split(','))
    # range_2 = set(range(start_2, end_2 + 1))

    intersections.append(range_1 & range_2)

longest = list(max(intersections, key=len))
print(f"Longest intersection is {longest} with length {len(longest)}")
