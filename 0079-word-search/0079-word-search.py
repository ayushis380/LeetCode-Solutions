class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i >= len(word):
                return True
            
            if r >= rows or r < 0 or c >= cols or c < 0 or board[r][c] != word[i]:
                return False
            
            value = board[r][c]
            board[r][c] = "#"

            for dr, dc in [[-1,0], [1,0], [0,1], [0,-1]]:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, i+1):
                    return True

            board[r][c] = value
            return False
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        
        return False