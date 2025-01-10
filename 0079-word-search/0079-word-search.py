class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, ind):
            if ind >= len(word):
                return True
            
            if r >= rows or r < 0 or c >= cols or c < 0 or board[r][c] != word[ind] or (r,c) in visited:
                return False
            
            visited.add((r,c))

            check = ( dfs(r+1, c, ind+1) or \
            dfs(r-1, c, ind+1) or \
            dfs(r, c-1, ind+1) or \
            dfs(r, c+1, ind+1) )
            
            visited.remove((r,c))
            return check
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False
