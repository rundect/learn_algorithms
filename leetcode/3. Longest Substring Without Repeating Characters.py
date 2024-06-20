class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        substring = ''
        for i in s:
            if i not in substring:
                substring += i
        return len(substring)


# s = "abcabcbb"
# solution = Solution()
# print(solution.length_of_longest_substring(s))
#
# s = "bbbbb"
# solution = Solution()
# print(solution.length_of_longest_substring(s))

s = "pwwkew"
solution = Solution()
print(solution.length_of_longest_substring(s))
