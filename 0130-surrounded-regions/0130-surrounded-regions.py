class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r >= rows or r < 0 or c >= cols or c < 0 or board[r][c] != "O":
                return 
            
            board[r][c] = "T" # all regions from boundaries

            dfs(r +1, c)
            dfs(r -1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"