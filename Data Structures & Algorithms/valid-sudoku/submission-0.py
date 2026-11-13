class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_set = set()
        square = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if (board[i][j] in hash_set or 
                board[i][j] in square[(i // 3, j // 3)]):
                    print(i,j)
                    return False
                if board[i][j] != '.':
                    hash_set.add(board[i][j])
                    square[(i // 3, j // 3)].add(board[i][j])
            hash_set.clear()
        for i in range(9):
            for j in range(9):
                if board[j][i] in hash_set:
                    print(i,j)
                    return False
                if board[j][i] != '.':
                    hash_set.add(board[j][i])
            hash_set.clear()
        return True


        

        
        
            