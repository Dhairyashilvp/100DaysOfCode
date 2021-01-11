class Solution:
    def sortString(self, s: str) -> str:
        s = sorted(list(s))
        d = {}
        ans = ""
        for e in s:
            if e in d.keys() :
                d[e] += 1
            else:
                d[e] = 1
        print(d)
        k = list(d.keys())
        while len(ans) < len(s):
            t = ""
            for i in range(len(d)):
                if d[k[i]] != 0:
                    ans += k[i]
                    d[k[i]] -= 1
            for i in range(len(d)):
                if d[k[~i]] != 0:
                    ans += k[~i]
                    d[k[~i]] -= 1
            print(ans)
        return ans
                    
        
                