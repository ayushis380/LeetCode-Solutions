class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = {}

        def dfs(r, c):
            if r >= rows or r < 0 or c >= cols or c < 0 or obstacleGrid[r][c] != 0:
                return 0
            
            if r == rows -1 and c == cols -1:
                return 1
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            visited = obstacleGrid[r][c]
            obstacleGrid[r][c] = "#"
            dp[(r, c)] = 0
            
            for dr, dc in [[1, 0], [0, 1]]:
                nr, nc = r + dr, c + dc
                dp[(r, c)] += dfs(nr, nc)

            obstacleGrid[r][c] = visited
            return dp[(r, c)]

        return dfs(0, 0)
        