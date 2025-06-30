class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
# size of the largest square starting at a particular cell (top left cell) is equal to the minimum of the sizes of the largest squares ending at the three adjacent cells plus 1
        rows, cols = len(matrix), len(matrix[0])
        dp = defaultdict(int)

        def dfs(r, c):
            if r >= rows or c >= cols:
                return 0 # see cells on last row and col which have no down, diag and right
            
            if (r, c) not in dp:
                down = dfs(r + 1, c)
                diag = dfs(r + 1, c + 1)
                right = dfs(r, c + 1)
                if matrix[r][c] == "1":
                # min will ensure if any value is 0 then no square formed
                    dp[(r, c)] = 1 + min(down, diag, right) 
            
            return dp[(r, c)]
        
        dfs(0, 0)
        return max(dp.values()) ** 2

