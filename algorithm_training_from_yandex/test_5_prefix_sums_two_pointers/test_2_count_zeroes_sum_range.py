import pytest


def count_prefix_sum(nums):
    prefix_sum_by_value = {0: 1}
    nowsum = 0
    for now in nums:
        nowsum += now
        if nowsum not in prefix_sum_by_value:
            prefix_sum_by_value[nowsum] = 0
        prefix_sum_by_value[nowsum] += 1
    return prefix_sum_by_value


def count_zeroes_sum_range(nums):
    prefix_sum = count_prefix_sum(nums)
    cntranges = 0
    for nowsum in prefix_sum:
        cntsum = prefix_sum[nowsum]
        cntranges += cntsum * (cntsum - 1) // 2
    return cntranges


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ([1, 0, 1, 1, 0, 0, 1], 4),
    ],
)
def test_example(input, expected):
    assert count_zeroes_sum_range(input) == expected
