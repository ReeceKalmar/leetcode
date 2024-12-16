class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) == 1:
            return s

        strings = ["" for i in range(numRows)]

        row = 0
        increasing = False
        for char in s:
            if row == 0:
                strings[row] += char
                increasing = False
                row += 1
                continue
            if row == numRows - 1:
                strings[row] += char
                increasing = True
                row -= 1
                continue

            strings[row] += char

            if increasing:
                row -= 1
            else:
                row += 1

        return "".join(strings)

