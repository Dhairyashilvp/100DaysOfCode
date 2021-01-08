class Solution:
    def maxDepth(self, s: str) -> int:
        md = 0
        c = 0
        for e in s:
            if e == "(":
                c += 1
            elif e == ")":
                c -= 1
            if c > md:
                md = c
        return md
                