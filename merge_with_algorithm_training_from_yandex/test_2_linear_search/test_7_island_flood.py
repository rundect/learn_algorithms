
def island_flood(h):
    maxpos = 0
    for i in range(len(h)):
        if h[i] > h[maxpos]:
            maxpos = i
    ans = 0
    nowm = 0
    for i in range(maxpos):
        if h[i] > nowm:
            nowm = h[i]
        ans += nowm - h[i]
    nowm = 0
    for i in range(len(h) - 1, maxpos, -1):
        if h[i] > nowm:
            nowm = h[i]
        ans += nowm - h[i]
    return ans


class Tests:
    def test_example_1(self):
        h = [3, 1, 4, 3, 5, 1, 1, 3, 1]
        s = island_flood(h)
        assert s == 7

    def test_example_2(self):
        h = [1, 0, 1]
        s = island_flood(h)
        assert s == 1

    def test_example_3(self):
        h = [0, 1, 0]
        s = island_flood(h)
        assert s == 0

    def test_example_4(self):
        h = []
        s = island_flood(h)
        assert s == 0
