class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
# For each cell (i, j), find the minimum value in any cell above and to the left, i.e., (r, c) where r < i and c < j
# maxval - minval on (top and left) will give a max result

# Because you can jump directly from (x1, y1) to any (x2, y2) that’s below or to the right, not necessarily adjacent. That means:
# You're not adding intermediate steps' scores.
# The score is only based on the start and end values, i.e., grid[end] - grid[start]; the score is the "elevation gain" if you’re allowed to jump over valleys

        m, n = len(grid), len(grid[0])
        minGrid = [[float("inf")] * n for _ in range(m)]
        maxScore = float("-inf")

        for i in range(m):
            for j in range(n):
            # Only update score if there's at least one cell before (i, j)
                if i > 0:
                    maxScore = max(maxScore, grid[i][j] - minGrid[i-1][j]) # subtract from min value seen so far on top
                if j > 0:
                    maxScore = max(maxScore, grid[i][j] - minGrid[i][j-1]) # subtract from min value seen so far on left
                
                # Build the min_grid
                top = minGrid[i-1][j] if i > 0 else float('inf')
                left = minGrid[i][j-1] if j > 0 else float('inf')

                minGrid[i][j] = min(grid[i][j], top, left) # take the minimum of all, if grid has min then update; its used for future values
        
        return maxScore