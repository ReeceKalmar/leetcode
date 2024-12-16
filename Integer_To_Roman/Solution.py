class Solution:
    def intToRoman(self, num: int) -> str:
        num_map = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        roman = ""
        nums = list(num_map.keys())[::-1]
        for i in nums:
            while i <= num:
                roman += num_map[i]
                num -= i
        return roman
