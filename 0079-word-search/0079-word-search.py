class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i >= len(word):
                return True

            if r >= rows or r < 0 or c >= cols or c < 0 or board[r][c] != word[i] or (r, c) in visited:
                return False

            visited.add((r, c))
            result = False
            for dr, dc in [[-1,0], [1,0], [0,1], [0,-1]]:
                nr, nc = r + dr, c + dc
                result |= dfs(nr, nc, i + 1)
            
            visited.remove((r, c))
            return result

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        
        return False
