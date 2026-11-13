class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        fix = 1
        for i in range(1, len(nums)):
            fix *= nums[i-1]
            res[i] *= fix
        fix = 1
        for i in range(len(nums) -2, -1, -1):
            fix *= nums[i+1]
            res[i] *= fix
        return res
