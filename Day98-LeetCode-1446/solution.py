class Solution:
    def maxPower(self, s: str) -> int:
        maxpower = 0
        l = 1
        if len(s) > 1:
            for i in range(len(s)):
                if (i+1 < len(s)) and s[i] == s[i+1]:
                    l += 1
                else:
                    l = 1
                if maxpower < l:
                    maxpower = l
            return maxpower
        else:
            return 1