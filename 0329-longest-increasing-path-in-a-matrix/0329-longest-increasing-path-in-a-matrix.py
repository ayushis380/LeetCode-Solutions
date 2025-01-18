class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Memoization decrease TC 
        # TC and SC is O(n * m)
        # if a cell is visited once it wont be visited twice as its result is stored in dp
        rows, cols = len(matrix), len(matrix[0])
        dp = [[-1] * cols for _ in range(rows)]
        pathlen = 0

        def dfs(r, c, prevVal):
            if r >= rows or r < 0 or c >= cols or c < 0 or matrix[r][c] <= prevVal:
                return 0
            
            if dp[r][c] != -1: # return if already calculated
                return dp[r][c]
            
            dp[r][c] = 1 + max( dfs(r+1,c, matrix[r][c]), dfs(r-1, c, matrix[r][c]), \
            dfs(r, c+1,matrix[r][c]), dfs(r, c-1, matrix[r][c]))
            
            return dp[r][c]
        
        for r in range(rows):
            for c in range(cols):
                pathlen = max(pathlen, dfs(r, c, -1))
        
        return pathlen