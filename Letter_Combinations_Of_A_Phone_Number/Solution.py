from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []

        def back(combination, digit):
            if not digit:
                result.append(combination)
                return

            for i in digit_to_letters[digit[0]]:
                back(combination + i, digit[1::])

        back("", digits)

        return result
