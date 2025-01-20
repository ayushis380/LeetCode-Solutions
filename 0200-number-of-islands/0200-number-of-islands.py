class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] != "1":
                return 
            
            grid[r][c] = "#"
    
            for dr, dc in [[-1,0], [1,0], [0,1], [0,-1]]:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
            
            return 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += dfs(r, c)
        
        return islands