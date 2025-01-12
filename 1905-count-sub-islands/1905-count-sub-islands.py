class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # check for sub islands in grid2 and see if 1s in sub island is also there in grid1
        rows, cols = len(grid2), len(grid2[0])
        count = 0

        def dfs(r, c):
        # out of bound and getting a 0 is ok for this it doesnt impact count of sub islands
        # its just a break point
            if r >= rows or r < 0 or c >= cols or c < 0 or grid2[r][c] == 0:
                return True
            
            grid2[r][c] = 0 # mark visited
            res = True

            if grid1[r][c] == 0:
                res = False # not a valid island

            # check in all directions, all should be valid
            res &= dfs(r+1, c)
            res &= dfs(r-1, c)
            res &= dfs(r, c-1)
            res &= dfs(r, c+1)

            return res
        
        for r in range(rows):
            for c in range(cols):
                # if both are 1 then start dfs()
                if grid2[r][c] == 1 and grid1[r][c] == 1:
                    count += dfs(r,c)
        
        return count