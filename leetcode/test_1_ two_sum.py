from typing import List, Tuple, Union


class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i


class Tests:
    def test_example_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        solution = Solution()
        s = solution.two_sum(nums, target)
        assert s == [0, 1]

    def test_example_2(self):
        nums = [3, 2, 4]
        target = 6
        solution = Solution()
        s = solution.two_sum(nums, target)
        assert s == [1, 2]

    def test_example_3(self):
        nums = [3, 3]
        target = 6
        solution = Solution()
        s = solution.two_sum(nums, target)
        assert s == [0, 1]
