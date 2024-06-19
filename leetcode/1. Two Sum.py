from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9
s = Solution()
print(s.two_sum(nums, target))

nums = [3, 2, 4]
target = 6
s = Solution()
print(s.two_sum(nums, target))

nums = [3, 3]
target = 6
s = Solution()
print(s.two_sum(nums, target))
