class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        counter = 0
        i = 0
        while i < len(s):
            fchar = s[i]
            if i < len(s) - 1:
                schar = s[i + 1]
                if romans[fchar] < romans[schar]:
                    counter += romans[schar] - romans[fchar]
                    i += 2
                    continue
            counter += romans[fchar]
            i += 1
        return counter
