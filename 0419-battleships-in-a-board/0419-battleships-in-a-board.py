class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows, cols = len(board), len(board[0])
        count = 0

        def dfs(r, c):
            if r >= rows or r < 0 or c >= cols or c < 0 or board[r][c] == ".":
                return 

            board[r][c] = "."
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            return 1
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    count += dfs(r,c)
        
        return count