from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
            x = 0
            ans = []
            for i in nums:
                x = x + i
                ans.append(x)
            return ans
fc = Solution()
print(fc.runningSum([1,1,1,1,1]))
print(fc.runningSum([1,2,3,4,5]))