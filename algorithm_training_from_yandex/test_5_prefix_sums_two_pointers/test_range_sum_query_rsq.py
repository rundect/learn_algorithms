import pytest


def make_prefix_sum(nums):
    prefix_sum = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
    return prefix_sum


def rsq(nums, l, r):
    prefix_sum = make_prefix_sum(nums)
    return prefix_sum[r] - prefix_sum[l]


@pytest.mark.parametrize(
    ("input", "input_2", "input_3", "expected"),
    [
        ([5, 3, 8, 1, 4, 6], 2, 5, 13),
    ],
)
def test_example(input, input_2, input_3, expected):
    assert rsq(input, input_2, input_3) == expected
