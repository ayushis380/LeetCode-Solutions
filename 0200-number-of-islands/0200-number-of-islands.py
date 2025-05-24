class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        total = 0

        def dfs(r, c):
            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] == "0":
                return 0
            
            grid[r][c] = "0"

            for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
            
            return 1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    total += dfs(i,j)
        
        return total 