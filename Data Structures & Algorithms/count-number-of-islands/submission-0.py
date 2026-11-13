class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if grid[r][c] == "0":
                return
            
            nei = ((r, c+1), (r, c-1), (r+1, c), (r-1, c))

            for nr, nc in nei:
                if (0 <= nr < len(grid) and
                    0 <= nc < len(grid[0]) and
                    (nr, nc) not in visit
                ):
                    visit.add((nr, nc))
                    dfs(nr, nc)
        
        visit = set()
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visit:
                    print(i, j)
                    res += 1
                    dfs(i, j)
                    print(visit)
        
        return res