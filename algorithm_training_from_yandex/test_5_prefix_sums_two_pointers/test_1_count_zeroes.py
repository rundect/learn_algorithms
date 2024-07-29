import pytest


def make_prefix_zeroes(nums):
    prefix_zeroes = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        if nums[i - 1] == 0:
            prefix_zeroes[i] = prefix_zeroes[i - 1] + 1
        else:
            prefix_zeroes[i] = prefix_zeroes[i - 1]
    return prefix_zeroes


def count_zeroes(nums, l, r):
    prefix_sum = make_prefix_zeroes(nums)
    return prefix_sum[r] - prefix_sum[l]


@pytest.mark.parametrize(
    ("input", "input_2", "input_3", "expected"),
    [
        ([1, 0, 1, 1, 0, 0, 1], 2, 5, 1),
    ],
)
def test_example(input, input_2, input_3, expected):
    assert count_zeroes(input, input_2, input_3) == expected
