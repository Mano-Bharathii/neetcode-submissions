class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def backtrack(i):
            if i >= len(s):
                res.append(seq.copy())
                return
            
            for j in range(i, len(s)):
                if isPali(i, j):
                    seq.append(s[i: j + 1])
                    backtrack(j+1)
                    seq.pop()        
        
        def isPali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        seq = []
        res = []

        backtrack(0)

        return res