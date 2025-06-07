class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # In 1D, the optimal meeting point (minimizing the sum of distances) is the median of the points.
        # If you pick a point to the left or right of the median, you increase the sum of distances.

        m, n = len(grid), len(grid[0])

        rows, cols = [], []
        houses = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    houses.append((i,j))
                    rows.append(i)
        
        # Notice we iterate column-first to keep cols sorted — important for getting the median.
        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    cols.append(j)
        
#  Get the median row and column (since rows and cols are implicitly sorted due to the way we iterated).
# These are the optimal x and y coordinates of the meeting point and it can be on the house index as well
        median_row = rows[len(rows)//2]
        median_col = cols[len(cols)//2]

        return sum(
            [abs(house[0] - median_row) + abs(house[1] - median_col) for house in houses] 
        )