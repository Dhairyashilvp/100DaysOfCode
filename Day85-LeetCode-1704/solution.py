class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s)-1
        ans = []
        while i >= 0:
            if s[i] == "#":
                ans.append(chr(int(s[i-2:i]) + ord('a') - 1))
                i -= 3                
            else:
                ans.append(chr(int(s[i]) + ord('a') - 1))
                i -= 1
        return "".join(reversed(ans))