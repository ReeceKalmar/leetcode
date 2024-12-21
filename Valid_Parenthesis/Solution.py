class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) & 1:
            return False

        stack = []
        for paren in s:
            if paren == "(" or paren == "[" or paren == "{":
                stack.append(paren)
                continue

            if not stack:
                return False

            if paren == ")":
                if stack[-1] != "(":
                    return False
                stack.pop()
                continue
            elif paren == "]":
                if stack[-1] != "[":
                    return False
                stack.pop()
                continue
            else:
                if stack[-1] != "{":
                    return False
                stack.pop()
                continue
        return len(stack) == 0
