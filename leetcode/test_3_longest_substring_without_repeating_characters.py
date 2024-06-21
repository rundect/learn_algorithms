class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        start = max_length = 0
        used_char = {}
        for i in range(len(s)):
            if s[i] in used_char and start <= used_char[s[i]]:
                start = used_char[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used_char[s[i]] = i
        return max_length


class Tests:
    def test_example_1(self):
        string = "abcabcbb"
        solution = Solution()
        s = solution.length_of_longest_substring(string)
        assert s == 3

    def test_example_2(self):
        string = "bbbbb"
        solution = Solution()
        s = solution.length_of_longest_substring(string)
        assert s == 1

    def test_example_3(self):
        string = "pwwkew"
        solution = Solution()
        s = solution.length_of_longest_substring(string)
        assert s == 3

    def test_example_4(self):
        string = "dvdf"
        solution = Solution()
        s = solution.length_of_longest_substring(string)
        assert s == 3

    def test_example_5(self):
        string = " "
        solution = Solution()
        s = solution.length_of_longest_substring(string)
        assert s == 1
