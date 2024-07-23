import pytest


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


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ([3, 1, 4, 3, 5, 1, 1, 3, 1], 7),
        ([1, 0, 1], 1),
        ([0, 1, 0], 0),
        ([], 0),
    ],
)
def test_example(input, expected):
    assert island_flood(input) == expected
