from math import sqrt

import pytest


def find_all_roots(a, b, c):
    if a == 0:
        if b != 0:
            return -c / b
        if b == 0 and c == 0:
            return 'Infinite number of solutions'
    else:
        d = b ** 2 - 4 * a * c
        if d == 0:
            x1 = -b / (2 * a)
            return x1
        elif d > 0:
            x1 = (-b - sqrt(d)) / (2 * a)
            x2 = (-b + sqrt(d)) / (2 * a)
            if x1 < x2:
                return x1, x2
            else:
                return x2, x1


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ([1, -2, 0], (0.0, 2.0)),
        ([1, 2, 1], -1.0),
        ([1, 1, 1], None),
        ([0, 1, 1], -1),
        ([0, 0, 1], None),
        ([0, 0, 0], 'Infinite number of solutions'),
        ([-5, 4, 1], (-0.2, 1.0)),
    ],
)
def test_example(input, expected):
    assert find_all_roots(input[0], input[1], input[2]) == expected
