class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(needle) - 1, len(haystack)):
            if haystack[i + 1 - len(needle) : i + 1] == needle:
                return i + 1 - len(needle)
        return -1
