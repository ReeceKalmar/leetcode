from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        count = 0
        for i in range(len(nums)):
            num = nums[i]
            if num != val:
                nums[i] = nums[left]
                nums[left] = num
                count += 1
                left += 1
        return count
