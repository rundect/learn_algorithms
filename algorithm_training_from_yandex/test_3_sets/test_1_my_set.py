
set_size = 10
my_set = [[] for _ in range(set_size)]


def add(x):
    my_set[x % set_size].append(x)


def find(x):
    for now in my_set[x % set_size]:
        if now == x:
            return True
    return False


def delete(x):
    xlist = my_set[x % set_size]
    for i in range(len(xlist)):
        if xlist[i] == x:
            xlist[i], xlist[len(xlist) - 1] = xlist[len(xlist) - 1], xlist[i]
            xlist.pop()
            return


def test_example():
    add(17)
    add(7)
    add(17)
    add(27)
    assert find(7) is True
    assert find(37) is False
    delete(17)
    assert my_set == [[], [], [], [], [], [], [], [27, 7, 17], [], []]
