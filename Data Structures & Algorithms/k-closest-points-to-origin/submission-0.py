from heapq import heapify, heappop, heappush
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = [(sqrt(x*x + y*y), i) for i, [x,y] in enumerate(points)]
        heapify(pq)
        res = []
        for i in range(k):
            res.append(points[heappop(pq)[1]])
        return res