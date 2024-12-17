from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordlen = len(words[0])
        totallen = wordlen * len(words)
        result = []
        wmap = Counter(words)

        for i in range(totallen, len(s) + 1):
            slist = [s[j : j + wordlen] for j in range(i - totallen, i, wordlen)]
            tmap = Counter(slist)
            if wmap == tmap:
                result.append(i - totallen)
        return result
