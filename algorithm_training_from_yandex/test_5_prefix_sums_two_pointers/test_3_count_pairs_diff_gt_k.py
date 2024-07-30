import pytest


def count_pairs_diff_gt_k(sorted_nums, k):
    cnt_pairs = 0
    last = 0
    len_sorted_nums = len(sorted_nums)
    for first in range(len_sorted_nums):
        while last < len_sorted_nums and sorted_nums[last] - sorted_nums[first] <= k:
            last += 1
        cnt_pairs += len_sorted_nums - last
    return cnt_pairs


@pytest.mark.parametrize(
    ("input", "input_2", "expected"),
    [
        ([1, 3, 5, 7, 8], 4, 3),
    ],
)
def test_example(input, input_2, expected):
    assert count_pairs_diff_gt_k(input, input_2) == expected
