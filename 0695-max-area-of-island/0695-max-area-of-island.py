class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxarea = 0

        def dfs(r, c):
            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] != 1:
                return 0
            
            grid[r][c] = 0
            result = 1
            
            for dr, dc in [[-1,0], [1,0], [0,1], [0,-1]]:
                nr, nc = r + dr, c + dc
                result += dfs(nr, nc)
            
            # return 1 + dfs(r +1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
            return result

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxarea = max(maxarea, dfs(r, c))
            
        return maxarea