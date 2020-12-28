class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ret = 0
        hm = {}
        for n in nums:            
            if n in hm:
                ret += hm[n]
                hm[n] += 1
            else:
                hm[n] = 1
        return ret