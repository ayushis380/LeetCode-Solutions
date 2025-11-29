class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1
        
        queue = deque([(1, 0, 0)])
        visited = set([(0, 0)])

        while queue:
            dst, r, c = queue.popleft()

            if r == rows - 1 and c == cols - 1:
                return dst

            for dr, dc in [[-1,0], [1,0], [0, 1], [0,-1], [1,1], [1,-1], [-1,-1], [-1,1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((dst + 1, nr, nc))
        
        return -1