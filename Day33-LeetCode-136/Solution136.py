class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        mi = prices[0] if prices else 0
        for p in prices:
            if p > mi:
                mp = max(mp,p - mi)
            else:
                mi = p
        return mp