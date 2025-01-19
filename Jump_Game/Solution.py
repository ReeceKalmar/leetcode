class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums) - 1
        jump = 0
        for i in range(len(nums)):
            num = nums[i]

            if num > jump:
                jump = num

            if jump == 0 and i != length:
                return False
            
            if length - i <= jump:
                return True
            jump -= 1
        return False
