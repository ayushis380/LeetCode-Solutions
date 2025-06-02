class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
    # we are traversing the grid from left to right, and from top to bottom, for each land cell we are currently at, we only need to check whether the LEFT and UP cells are land cells with a slight modification on previous approach
        
        rows = len(grid)
        cols = len(grid[0])
        
        result = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    result += 4
                    
                    if r > 0 and grid[r-1][c] == 1: # up
                        result -= 2 # -2 as two boundaries are common here, in old and new cell
                        
                    if c > 0 and grid[r][c-1] == 1: # left
                        result -= 2
        
        return result