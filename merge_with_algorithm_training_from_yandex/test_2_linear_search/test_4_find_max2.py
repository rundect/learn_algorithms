import pytest


def find_max2(seq):
    max1 = max(seq[0], seq[1])
    max2 = min(seq[0], seq[1])
    for i in range(2, len(seq)):
        if seq[i] > max1:
            max2 = max1
            max1 = seq[i]
        elif seq[i] > max2:
            max2 = seq[i]
    return max1, max2


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ([2, 1, 3, 2, 1], (3, 2)),
    ],
)
def test_example(input, expected):
    assert find_max2(input) == expected
