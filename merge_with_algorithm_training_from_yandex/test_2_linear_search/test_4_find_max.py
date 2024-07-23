import pytest


def find_max(seq):
    ans = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[ans]:
            ans = i
    return seq[ans]


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ([2, 1, 3, 2, 1], 6),
    ],
)
def test_example(input, expected):
    assert find_max(input) == expected
