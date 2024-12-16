class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        longest = ""
        t = ""

        # case when theres only length 2 palindrome
        for i in range(len(s)):
            if i < len(s) - 1 and s[i] == s[i + 1]:
                longest = s[i] * 2

        for i in range(1, len(s) - 1):
            if s[i - 1] == s[i + 1]:
                t = s[i - 1 : i + 2]
                left = i - 2
                right = i + 2
                while left >= 0 and right < len(s):
                    if s[left] == s[right]:
                        t = s[left] + s[right]
                    else:
                        break
                if len(t) > len(longest):
                    longest = t

        return longest
