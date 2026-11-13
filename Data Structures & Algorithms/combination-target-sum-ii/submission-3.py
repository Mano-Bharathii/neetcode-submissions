class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        total = 0
        candidates.sort()

        def bt(i):
            nonlocal total, target
            if total == target:
                res.append(comb.copy())
                return
            
            if total > target or i == len(candidates):
                return
            
            cur = candidates[i]

            comb.append(cur)
            total += cur
            bt(i + 1)

            
            comb.pop()
            total -= cur
            while i < len(candidates) and cur == candidates[i]:
                i += 1
            bt(i)
            
        bt(0)
        return res