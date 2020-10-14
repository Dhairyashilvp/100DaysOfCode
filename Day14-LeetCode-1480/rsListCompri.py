class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums=[0]
        [sums.append(sums[-1]+i) for i in  nums]
        del sums[0]
    
        return sums