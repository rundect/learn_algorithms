import pytest


def func(players):
    best_sum = 0
    return best_sum


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ([1, 1, 3], 4),
    ],
)
def test_example(input, expected):
    assert func(input) == expected
