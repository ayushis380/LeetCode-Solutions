class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}
        maxlen = float("-inf")

        def dfs(r, c, prev):
            if r >= rows or r < 0 or c >= cols or c < 0 or matrix[r][c] <= prev:
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            max_len = 0
            for dr, dc in [(-1,0), (1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                max_len = max(max_len, dfs(nr, nc, matrix[r][c]))
            
            dp[(r, c)] = 1 + max_len
            return dp[(r, c)]

        for r in range(rows):
            for c in range(cols):
                maxlen = max(maxlen, dfs(r, c, -1))
        
        return maxlen