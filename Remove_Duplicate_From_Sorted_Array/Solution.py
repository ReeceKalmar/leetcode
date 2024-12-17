from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nset = set()
        left = 0
        for i in range(len(nums)):
            num = nums[i]
            if num not in nset:
                nums[i] = nums[left]
                nums[left] = num
                nset.add(num)
                left += 1
        return len(nset)
