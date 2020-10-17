class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = []
        ob = 0
        cb = 0
        ans = [0] * (len(seq))
        for i in range(len(seq)):
            if seq[i]=='(':
                ans[i] = ob
                ob = ob ^ 1
            else:
                ans[i] = cb
                cb = cb ^ 1
        return ans