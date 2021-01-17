class Solution:
    def toGoatLatin(self, S: str) -> str:
        ans = []
        sarr = []
        v = ["a","e","i","o","u","A","E","I","O","U"]
        word = ""
        for c in S:
            if c == " ":
                sarr.append(word)
                word = ""
            else:
                word += c
                
        sarr.append(word)
        for i, w in enumerate(sarr):
            if w[0] in v:
                ans.append(w + "ma" + ("a"*(i+1)))
            else:
                ans.append(w[1:] + w[0] + "ma" + ("a"*(i+1)))
        return " ".join(ans)