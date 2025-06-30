class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}

        def dfs(r, c):
            if r == m-1 and c == n-1:
                return 1
            if r >= m or c >= n:
                return 0
            
            if (r, c) not in dp:
                dp[(r,c)] = dfs(r + 1, c) + dfs(r, c + 1)
            
            return dp[(r, c)]
        
        return dfs(0, 0)