class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(prefix[-1] * nums[i])
        for i in range(len(nums) -1, -1, -1):
            if i == len(nums) - 1:
                suffix.append(nums[i])
            else:
                suffix.append(suffix[-1] * nums[i])
        suffix = suffix[::-1]
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(suffix[1])
            elif i == len(nums) - 1:
                res.append(prefix[i-1])
            else:
                res.append(prefix[i-1] * suffix[i+1])
        return res
