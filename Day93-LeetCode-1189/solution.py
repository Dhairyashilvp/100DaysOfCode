class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {"b": text.count("b"),"a": text.count("a"),"l": text.count("l"),"l": text.count("l"),"o": text.count("o"),"o": text.count("o"),"n": text.count("n"),}            
        ans = d["b"]
        for e in d.keys():
            if e == "o" or e == "l": 
                ans = min(d[e]/2, ans)
            else:
                ans = min(d[e], ans)
        return int(ans)