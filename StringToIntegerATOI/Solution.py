class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        negative = s[0] == "-"
        if negative or s[0] == "+":
            s = s[1::]
        num = ""
        val = 0

        for char in s:
            if not char.isdigit():
                break

            num += char

        if not num.isnumeric():
            return val

        binary = bin(int(num))
        if len(binary) - 2 > 31:
            binary = "0b10000000000000000000000000000000"
            if not negative:
                val = 2147483647
            else:
                val = int(binary, 2)

        else:
            val = int(num)

        if negative:
            val = -val

        return val
