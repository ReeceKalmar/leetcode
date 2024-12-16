class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        result = 0
        l = 0

        for r in range(len(s)):
            char = s[r]

            if char in chars and chars[char] >= l:
                l = chars[char] + 1

            chars[char] = r
            length = r - l + 1

            if length > result:
                result = length

        return result

