import itertools
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        return len([itertools.combinations(rating,3)])
rating = [2,5,3,4,1]
fc = Solution()
print(fc.numTeams(rating))