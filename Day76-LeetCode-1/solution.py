class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        buf = {}
        for i, n in enumerate(nums):
            s = target - n
            if s in buf:
                return [buf[s], i]
            else:
                buf[n] = i