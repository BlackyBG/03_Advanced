def age_assignment(*args, **kwargs):
    people = {}
    for N, age in kwargs.items():
        for i in range(len(args)):
            if args[i][0] == N:
                people[args[i]] = age
                break
    result = dict(
        sorted(
            people.items(),
            key=lambda item: item[0]
        )
    )
    return '\n'.join(f"{name} is {age} years old." for name, age in result.items())


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
