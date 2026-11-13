from heapq import heapify, heappush, heappop

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pq = Counter(tasks)
        pq = [(-v, k) for k, v in pq.items()]
        heapify(pq)
        tick = 0
        wait = {}
        while pq or wait:
            tick += 1
            if tick in wait:
                heappush(pq, wait[tick])
                wait.pop(tick)
            if pq:
                cnt, ch = heappop(pq)
                if cnt < -1:
                    wait[tick + n + 1] = (cnt+1, ch) 
        return tick