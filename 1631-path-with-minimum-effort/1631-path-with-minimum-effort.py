class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
    # each path has a maximum edge weight (effort), and we want to minimize that max across all paths
    # heapq ensures we're processing paths in the order of minimum max effort seen so far — so diff already represents the maximum effort of the best path to that cell

        heap = [(0, 0, 0)]
        rows, cols = len(heights), len(heights[0])
        visited = set()

        while heap:
            diff, r, c = heapq.heappop(heap)

            if (r, c) in visited:
                continue
            
            visited.add((r, c)) # once a cell is visited, add it to set, not before that 
            if r == rows -1 and c == cols -1:
                return diff
            
            for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                nr, nc = r + dr, c + dc
                
                if (nr, nc) not in visited and 0 <= nr < rows and 0 <= nc < cols:
                    maxdiff = max(diff, abs(heights[r][c] - heights[nr][nc]))
                    heapq.heappush(heap, (maxdiff, nr, nc))
        
        return 0
        