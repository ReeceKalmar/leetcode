class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        nstr = str(x)
        if len(nstr) == 1:
            return True

        l = 0
        r = len(nstr) - 1

        while l <= r:
            left = nstr[l]
            right = nstr[r]

            if left != right:
                return False
            l += 1
            r -= 1
        return True
