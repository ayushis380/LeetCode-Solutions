class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i >= len(word):
                return True
            
            if r >= rows or r < 0 or c >= cols or c < 0 or board[r][c] != word[i]:
                return False
            
            visited = board[r][c]
            board[r][c] = "#"

            res = ( dfs(r+1, c, i+1) or \
            dfs(r-1, c, i+1) or \
            dfs(r, c+1, i+1) or \
            dfs(r, c-1, i+1) )
            
            board[r][c] = visited
            return res
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        
        return False
