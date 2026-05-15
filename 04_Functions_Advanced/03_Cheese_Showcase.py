def sorting_cheeses(**kwargs):
    result = ''
    for name, qtys in sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
        result += f"{name}\n"
        for qty in sorted(qtys, reverse=True):
            result += f"{qty}\n"
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
