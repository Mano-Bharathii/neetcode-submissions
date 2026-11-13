from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones]
        heapify(stones)
        while len(stones) > 1:
            x, y = heappop(stones), heappop(stones)
            if x != y:
                heappush(stones, x - y)
        return 0 if len(stones) == 0 else -stones[0]