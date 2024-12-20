from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""

        m = len(strs[0])
        for string in strs:
            if len(string) < m:
                m = len(string)
        if m == 0:
            return longest
        for i in range(m):
            temp = strs[0][i]
            for string in strs:
                if string[i] != temp:
                    return longest
            longest += temp
        return longest
