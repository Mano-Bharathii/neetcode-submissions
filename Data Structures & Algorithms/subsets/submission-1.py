class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(index, subset):
            if index == len(nums):
                res.append(subset)
                return
                # print(res)
            # print(index)
            backtrack(index+1, subset)
            backtrack(index+1, subset + [nums[index]])
        
        backtrack(0, [])
        return res
        

            