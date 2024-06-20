class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        max_len = 0
        substring = ''
        for i in s:
            if i in substring:
                substring = ''
            substring += i
            if max_len < len(substring):
                max_len = len(substring)
        return max_len


# s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
s = "dvdf"
solution = Solution()
print(solution.length_of_longest_substring(s))

