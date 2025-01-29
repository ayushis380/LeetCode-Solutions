class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "*":
                    queue.append((r, c, 0))
                    grid[r][c] == "X"
        
        while queue:
            r, c, path = queue.popleft()

            for dr, dc in [[-1,0], [1,0], [0,-1], [0, 1]]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == "#":
                        return path + 1
                    if grid[nr][nc] == "O":
                        queue.append((nr, nc, path + 1))
                        grid[nr][nc] = "X"

        return -1
        