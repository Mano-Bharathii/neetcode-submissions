from heapq import heapify, heappush, heappop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = [n for n in nums]
        heapify(self.pq)
        self.k = k
        while len(self.pq) > self.k:
            heappop(self.pq)

    def add(self, val: int) -> int:
        heappush(self.pq, val)
        if len(self.pq) > self.k:
            heappop(self.pq)
        return self.pq[0]
