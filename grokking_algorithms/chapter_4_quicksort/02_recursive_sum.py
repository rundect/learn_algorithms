def sum(list):
    if not list:
        return 0
    return list[0] + sum(list[1:])


print(sum([2, 4, 6, 5, 3]))
