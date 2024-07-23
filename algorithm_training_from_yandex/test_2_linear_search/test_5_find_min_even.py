import pytest


def find_min_even(seq):
    ans = -1
    flag = False
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (not flag or seq[i] < ans):
            ans = seq[i]
            flag = True
    return ans


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ([2, 4, 6], 2),
        ([3, 1], -1),
        ([-1, -2], -2),
        ([0, 2], 0),
        ([], -1),
    ],
)
def test_example(input, expected):
    assert find_min_even(input) == expected
