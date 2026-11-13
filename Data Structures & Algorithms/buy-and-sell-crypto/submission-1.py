class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = float("inf")
        r = 0
        res = []
        for p in prices:
            if p < l:
                if r > l:
                    res.append(r - l)
                l = p
                r = p
            else:
                r = max(r, p)
        res.append(r - l)
        return max(res)