import pytest


def find_x(seq, x):
    ans = -1
    for i in range(len(seq)):
        if ans == -1 and seq[i] == x:
            ans = i
    return ans


@pytest.mark.parametrize(
    ("input", "input_2", "expected"),
    [
        ([1, 2, 1, 3, 2], 2, 1),
    ],
)
def test_example(input, input_2, expected):
    assert find_x(input, input_2) == expected
