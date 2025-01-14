class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r >= rows or r < 0 or c >= cols or c < 0 or board[r][c] == "X" or board[r][c] == "V":
                return
            
            board[r][c] = "V"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c-1)
            dfs(r, c+1)
            return 

        for c in range(cols):
            dfs(0, c)
            dfs(rows-1, c)
        
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols-1)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "V":
                    board[r][c] = "O"
                