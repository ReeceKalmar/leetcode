from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        for i in range(len(digits) - 1, -1, -1):
            if i == 0 and digits[i] == 9:
                digits[i] = 1
                digits.append(0)
                break
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
        return digits
