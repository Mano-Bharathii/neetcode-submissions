class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        subset = []

        def backtrack(i):
            if i == len(nums):
                return

            subset.append(nums[i])
            res.append(subset.copy())
            backtrack(i+1)

            subset.pop()
            cur = nums[i]
            while i < len(nums) and nums[i] == cur:
                i += 1
            backtrack(i)
        
        backtrack(0)

        return res

