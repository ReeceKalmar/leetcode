from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hmap = {heights[i]: i for i in range(len(heights))}
        heights = sorted(heights, reverse=True)

        return [names[hmap[height]] for height in heights]
