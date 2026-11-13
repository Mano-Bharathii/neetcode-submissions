from heapq import heapify, heappop, heappush

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapify(nums)
        for i in range(k-1):
            heappop(nums)
        return -heappop(nums)