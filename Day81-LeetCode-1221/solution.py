class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        count = 0
        for c in s:
            if c == "L":
                count += 1
            else:
                count += -1
            if count == 0:
                ans += 1
        return ans