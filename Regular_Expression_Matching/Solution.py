# INCOMPLETE
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if "*" not in p and "." not in p:
            return s == p

        regex: list[str] = []
        i = 0
        while i < len(p):
            rgx = p[i]
            if rgx == "*":
                regex[len(regex) - 1] += rgx
            else:
                regex.append(rgx)
            i += 1
        
        match: list[str] = []
        regex = regex[::-1]
        rgx = regex.pop()
        i = 0
        while i < len(s) or len(regex) > 0:
            if "*" not in rgx and "." not in rgx:
                if rgx != s[i]:
                    return False
                match.append(s[i])
            elif rgx == ".":
                match.append(s[i])
            elif "*" in rgx and "." not in rgx:
                if rgx[0] != s[i]:
                    return False
                temp = s[i]
                while i < len(s)


            i += 1
            rgx = regex.pop()

        return s == p
