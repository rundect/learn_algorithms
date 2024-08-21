import math

import pytest


class Solution:
    def is_palindrome(self, x: int) -> bool:
        if x == 0:
            return True
        length_of_x = int(math.log10(abs(x))) + 1
        if length_of_x == 1 and x > 0:
            return True
        if length_of_x == 1 and x < 0:
            return False
        mid = length_of_x // 2
        for i in range(mid):
            a = x % (10 ** (i + 1))
            b = x // (10 ** (length_of_x - (i + 1)))
            if a != b:
                return False
        return True


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (1001, True),
        (121, True),
        (-121, False),
        (10, False),
        (-1, False),
        (0, True),
        (1, True),
    ],
)
def test_example(input, expected):
    solution = Solution()
    assert solution.is_palindrome(input) == expected
