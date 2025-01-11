class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] != "1":
                return
            
            grid[r][c] = "0"

            check = ( dfs(r+1, c) or \
            dfs(r-1, c) or \
            dfs(r, c+1) or \
            dfs(r, c-1) )

            return check
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        
        return islands