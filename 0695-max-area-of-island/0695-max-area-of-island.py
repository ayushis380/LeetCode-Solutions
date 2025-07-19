class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = 0

        def dfs(r, c):
            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            res = 1

            for dr, dc in [[-1,0], [1,0], [0,1], [0,-1]]:
                nr, nc = r + dr, c + dc
                res += dfs(nr, nc)
            
            return res
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))
        
        return area