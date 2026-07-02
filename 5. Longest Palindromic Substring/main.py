class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1 or s == s[::-1]:
            return s
        longest = ""

        for i in range(n):
            for j in range(i, n):
                substring = s[i:j + 1]

                if len(substring) > len(longest) and substring == substring[::-1]:
                    longest = substring

        return longest
