import pytest


def merge(nums1, nums2):
    merged = [0] * (len(nums1) + len(nums2))
    first1 = first2 = 0
    for k in range(len(nums1) + len(nums2)):
        if first1 != len(nums1) and (first2 == len(nums2) or nums1[first1] <= nums2[first2]):
            merged[k] = nums1[first1]
            first1 += 1
        else:
            merged[k] = nums2[first2]
            first2 += 1
    return merged


@pytest.mark.parametrize(
    ("input", "input2", "expected"),
    [
        ([1, 2, 5, 7], [3, 4, 4], [1, 2, 3, 4, 4, 5, 7]),
    ],
)
def test_example(input, input2, expected):
    assert merge(input, input2) == expected
