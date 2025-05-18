class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minval = float("inf")
        for val in prices:
            minval = min(minval, val)
            res = max(res, val - minval)
        return res