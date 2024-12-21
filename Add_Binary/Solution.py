class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_i = int(a, 2)
        b_i = int(b, 2)
        return bin(a_i + b_i)[2::]


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        cout = False
        a_i = len(a) - 1
        b_i = len(b) - 1
        while a_i >= 0 and b_i >= 0:
            a_b = int(a[a_i])
            b_b = int(b[b_i])
            if a_b & b_b:
                if cout:
                    result = "1" + result
                else:
                    result = "0" + result
                cout = True
            elif a_b or b_b:
                if cout:
                    result = "0" + result
                else:
                    result = "1" + result
            elif cout:
                result = "1" + result
                cout = False
            else:
                result = "0" + result
            a_i -= 1
            b_i -= 1
        while a_i >= 0:
            a_b = int(a[a_i])
            if a_b:
                if cout:
                    result = "0" + result
                else:
                    result = "1" + result
            else:
                if cout:
                    result = "1" + result
                    cout = False
                else:
                    result = "0" + result
            a_i -= 1
        while b_i >= 0:
            b_b = int(b[b_i])
            if b_b:
                if cout:
                    result = "0" + result
                else:
                    result = "1" + result
            else:
                if cout:
                    result = "1" + result
                    cout = False
                else:
                    result = "0" + result
            b_i -= 1
        if cout:
            result = "1" + result
        return result
