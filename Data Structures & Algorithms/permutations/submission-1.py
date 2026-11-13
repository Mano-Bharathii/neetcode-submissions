class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack():
            if len(seq) == len(nums):
                res.append(seq.copy())
                return
            
            for n in nums:
                if n not in used:
                    seq.append(n)
                    used.add(n)
                    backtrack()
                    seq.pop()
                    used.remove(n)

        res = []
        seq = []
        used = set()

        backtrack()
        return res