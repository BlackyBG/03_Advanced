from collections import deque

strings = deque(input().split())

main_colors = {"red", "yellow", "blue"}
secondary_map = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"}
}

valid_colors = main_colors | set(secondary_map)

colors = []

while strings:
    first_string = strings.popleft()
    last_string = strings.pop() if strings else ""

    color_found = None

    if first_string + last_string in valid_colors:
        color_found = first_string + last_string
    elif last_string + first_string in valid_colors:
        color_found = last_string + first_string

    if color_found:
        colors.append(color_found)
    else:
        first_mod = first_string[:-1]
        last_mod = last_string[:-1]

        mid_idx = len(strings) // 2

        if last_mod:
            strings.insert(mid_idx, last_mod)
        if first_mod:
            strings.insert(mid_idx, first_mod)

final_colors = []

for color in colors:
    if color in main_colors:
        final_colors.append(color)
    else:
        required_colors = secondary_map[color]
        if required_colors.issubset(set(colors)):
            final_colors.append(color)

print(final_colors)
