def fill_the_box(height, length, width, *args):
    box_volume = height * length * width
    left_over_cubes = 0

    for item in args:
        if item == "Finish":
            break

        if box_volume > 0:
            if item <= box_volume:
                box_volume -= item
            else:
                left_over_cubes += (item - box_volume)
                box_volume = 0
        else:
            left_over_cubes += item

    if box_volume > 0:
        return f"There is free space in the box. You could put {box_volume} more cubes."
    else:
        return f"No more free space! You have {left_over_cubes} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
