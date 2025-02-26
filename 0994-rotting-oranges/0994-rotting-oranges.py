class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        time = 0
        queue = deque()
        freshCount = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    freshCount += 1
        
        if len(queue):
            time -= 1 # for adding all rotten oranges

        while queue:
            curlen = len(queue)
            time += 1
            for i in range(curlen):
                r, c = queue.popleft()
                for dr, dc in [[-1,0], [1,0], [0,1],[0,-1]]:
                    nr, nc = r +dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        freshCount -= 1

        return time if freshCount == 0 else -1