class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        res = float("-inf")

        for i in range(len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
            res = max(res, prefix[i])
        
        for i in range(len(nums)-1):
            for j in range(i + 1, len(nums)):
                res = max(res, prefix[j] - prefix[i])
        
        return res