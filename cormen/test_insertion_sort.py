# page 59
from typing import List


class Solution:
    @staticmethod
    def insertion_sort(A: List[int]) -> List[int]:
        for j in range(1, len(A)):
            key = A[j]
            i = j - 1
            while i >= 0 and A[i] > key:
                A[i + 1] = A[i]
                i = i - 1
            A[i + 1] = key
        return A
    
    @staticmethod
    def reverse_insertion_sort(A: List[int]) -> List[int]:
        for j in range(1, len(A)):
            key = A[j]
            i = j - 1
            while i >= 0 and A[i] < key:
                A[i + 1] = A[i]
                i = i - 1
            A[i + 1] = key
        return A


class Tests:
    solution = Solution()
    def test_example_1(self):
        unsorted_nums = [5, 2, 4, 6, 1, 3]
        s = self.solution.insertion_sort(unsorted_nums)
        assert s == [1, 2, 3, 4, 5, 6]

    def test_example_2(self):
        unsorted_nums = [31, 41, 59, 26, 41, 58]
        s = self.solution.insertion_sort(unsorted_nums)
        assert s == [26, 31, 41, 41, 58, 59]

    def test_example_3(self):
        unsorted_nums = [5, 2, 4, 6, 1, 3]
        s = self.solution.reverse_insertion_sort(unsorted_nums)
        assert s == [6, 5, 4, 3, 2, 1]
