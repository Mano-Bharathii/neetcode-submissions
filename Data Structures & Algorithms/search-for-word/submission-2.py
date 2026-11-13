class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        visit = set()
        
        # BFS But Doesn't work :(
        # def search(row, col):
        #     q = deque([(row, col)])
        #     visit = set()
        #     i = 0
        #     while q:
        #         i += 1
        #         if i >= len(word):
        #             return True
        #         for _ in range(len(q)):
        #             r, c = q.popleft()
        #             visit.add((r, c))
        #             nei = ((r-1, c), (r+1, c), (r, c-1), (r, c+1))
        #             for nr, nc in nei:
        #                 if ((nr, nc) not in visit 
        #                     and 0 <= nr < ROW
        #                     and 0 <= nc < COL
        #                     and board[nr][nc] == word[i]
        #                 ):
        #                     q.append((nr, nc))
        #     return False
                        
        def search(i, r, c):
            if i == len(word):
                return True
            visit.add((r, c))
            nei = ((r-1, c), (r+1, c), (r, c-1), (r, c+1))
            for nr, nc in nei:
                if ((nr, nc) not in visit 
                    and 0 <= nr < ROW
                    and 0 <= nc < COL
                    and board[nr][nc] == word[i]
                    and search(i + 1, nr, nc)
                ):
                    return True
            visit.remove((r, c))
            return False


        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == word[0] and search(1, r, c):
                    return True
        
        return False
                    