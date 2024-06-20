from typing import List, Tuple, Union


class Solution:
    def two_sum(
            self,
            nums: Union[Tuple[int, int, int, int], Tuple[int, int, int], Tuple[int, int]],
            target: int
    ) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i


nums_dict = {
    (2, 7, 11, 15): 9,
    (3, 2, 4): 6,
    (3, 3): 6
}


for nums, target in nums_dict.items():
    s = Solution()
    print(s.two_sum(nums, target))
