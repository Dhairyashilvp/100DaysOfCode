class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
#         for w in words:
#             for cw in words:
#                 if cw != w:
#                     if w in cw:
#                         ans.append(w);
                        
        stri = " ".join(words)
        for w in words:
            if stri.count(w) >= 2:
                ans.append(w)
        return set(ans)