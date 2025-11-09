class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        if not fresh:
            return 0
        
        while queue:
            curlen = len(queue)
            time += 1 # all rotten oranges in queue will convert its fresh o to rotten for this timestamp.

            for _ in range(curlen):
                r, c = queue.popleft()
                for dr, dc in [[-1,0], [1,0], [0,-1],[0,1]]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            
                    if fresh == 0:
                        return time

        return -1

