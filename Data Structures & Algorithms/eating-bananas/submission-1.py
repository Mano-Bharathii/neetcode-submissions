from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        res = r
        while l <= r:
            k = (l + r) // 2
            cur_h = 0
            for p in piles:
                cur_h += ceil(p / k)
            if cur_h <= h:
                r = k - 1
                res = min(res, k)
            else:
                l = k + 1
        return int(res)






