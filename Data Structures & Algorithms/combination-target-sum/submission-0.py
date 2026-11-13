class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        comb = []
        total = 0

        def bt(i):
            nonlocal target, total
            if total == target:
                res.append(comb.copy())
                return
            if total > target or i == len(nums):
                return
            
            comb.append(nums[i])
            total += nums[i]
            bt(i)
            
            comb.pop()
            total -= nums[i]
            bt(i+1)
        
        bt(0)
        return res