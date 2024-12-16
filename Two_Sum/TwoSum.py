from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        result = []
        for i in range(len(nums)):
            num = nums[i]
            if target - num in numMap:
                result.append(numMap[target - num])
                result.append(i)
                return result
            numMap[num] = i
        return result
