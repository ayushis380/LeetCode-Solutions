class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        rows, cols = len(grid), len(grid[0])
        total = [[0] * cols for _ in range(rows)]
        empty_land_value = 0
        min_dist = float('inf')

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    min_dist = float('inf')
                    steps = 0
                    q = deque()
                    q.append((row, col))

                    while q:
                        steps += 1
                        for _ in range(len(q)):
                            curr_row, curr_col = q.popleft()

                            for d_row, d_col in dirs:
                                next_row = curr_row + d_row
                                next_col = curr_col + d_col

                                if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == empty_land_value:
                                    grid[next_row][next_col] -= 1
                                    total[next_row][next_col] += steps
                                    q.append((next_row, next_col))
                                    min_dist = min(min_dist, total[next_row][next_col])

                    empty_land_value -= 1

        return -1 if min_dist == float('inf') else min_dist
