class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Dijkstras - bfs with min heap(priority queue)
        # O(n^2 log n)
        n = len(grid)
        heap = [(grid[0][0], 0, 0)] # to always pick the min t. answer is dictated by max of all these picked minimum ts
        visited = set([(0, 0)])

        while heap:
            t, r, c = heapq.heappop(heap)

            if r == n -1 and c == n-1:
                return t
            
            for dr, dc in [[-1,0], [1,0], [0,-1], [0,1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0<= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))
