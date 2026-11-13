class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        q = deque()
        res = []
        q.append(['(', 1, 0])
        while q:
            i = q.popleft()
            if i[1] < n:
                q.append([i[0] + '(', i[1] + 1, i[2]])
            if i[1] >= i[2] + 1:
                if i[1] == i[2] + 1 == n:
                    res.append(i[0] + ')')
                else:
                    q.append([i[0] + ')', i[1], i[2] + 1])
        return res