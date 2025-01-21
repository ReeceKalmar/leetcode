class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(nums) - 1
        i = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                i = mid
                break
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        if i == -1:
            return [-1, -1]
        while i > 0 and nums[i - 1] == target:
            i -= 1
        result = []

        result.append(i)
        while i < len(nums) and nums[i] == target:
            i += 1
        result.append(i - 1)
        return result
