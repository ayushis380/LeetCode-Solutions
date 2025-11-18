class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])

        while heap:
            val, r, c = heapq.heappop(heap)

            if r == rows -1 and c == cols -1:
                return val
            
            for dr, dc in [[1,0], [0,1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    heapq.heappush(heap, (val + grid[nr][nc], nr, nc))
                    visited.add((nr, nc))
        
        return cost