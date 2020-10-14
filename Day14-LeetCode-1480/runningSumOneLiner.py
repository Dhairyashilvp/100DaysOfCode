from itertools import accumulate
class Solution: runningSum = staticmethod(accumulate)
fc = Solution()
print(fc.runningSum([1,1,1,1,1]))
