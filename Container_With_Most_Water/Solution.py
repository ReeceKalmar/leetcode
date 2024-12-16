from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        highest = 0
        while left < right:
            hi = height[left] if height[left] < height[right] else height[right]
            area = (right - left) * hi
            if area > highest:
                highest = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return highest
