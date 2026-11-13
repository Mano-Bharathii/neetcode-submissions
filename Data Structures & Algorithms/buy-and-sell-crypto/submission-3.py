class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = float("inf")
        r = 0
        max_profit = 0
        for p in prices:
            if p < l:
                l = p
                r = p
            else:
                r = max(r, p)
            if r - l > max_profit:
                max_profit = r - l

        return max_profit