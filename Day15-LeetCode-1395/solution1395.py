class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = []
        for i in range(n-2):
            for j in range(i + 1,n-1):
                for k in range(j + 1,n):
                    if (rating[i] < rating[j] and rating[j] < rating[k]) or (rating[i] > rating[j] and rating[j] > rating[k]) :
                        ans.append((rating[i], rating[j], rating[k]))
        return len(ans)
