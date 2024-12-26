class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        longest = [0, 0]
        for i in range (len(s)):
            l = i
            r = len(s) - 1
            rtemp = r
            temp = []

            while l < r:
                if s[l] != s[r]:
                    l = i
                    temp = []
                    rtemp -= 1
                    r = rtemp
                    continue
                
                if len(temp) == 0:
                    temp = [l, r]
                l += 1
                r -=1
            if len(temp) > 0 and temp[1] - temp[0] > longest[1] - longest[0]:
                longest = temp

        if longest[0] != 0 or longest[1] != 0:
            return s[longest[0] : longest[1] + 1]

        longest = ""
        temp = ""
        previous = s[0]
        for char in s:
            if char == previous:
                temp += char
            else:
                if len(temp) > len(longest):
                    longest = temp
                temp = char
                previous = char
        if len(temp) > len(longest):
            longest = temp
        return longest
