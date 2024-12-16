class Solution:
    def reverse(self, x: int) -> int:
        reverse = ""
        negative = x < 0

        if negative:
            x = -x
        r = str(x)[::-1]

        for i in r:
            reverse += i
            if len(bin(int(reverse))) - 2 > 31:
                return 0

        if negative:
            return int("-" + reverse)
        return int(reverse)
