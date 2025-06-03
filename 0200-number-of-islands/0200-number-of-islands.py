class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
#at any point during BFS, the queue never holds more than O(min(M, N)) elements at once, because: The BFS proceeds layer by layer (level-order), and Each cell adds only a few neighbors (up to 4)

# So even if the entire island is one big line, the maximum simultaneous neighbors in the queue will never exceed the length of the shortest side of the grid.

        rows, cols = len(grid), len(grid[0])
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    grid[r][c] = 0
                    neighbors = []
                    neighbors.append((r, c))

                    while neighbors:
                        nr, nc = neighbors.pop(0)
                        
                        if nr -1 >=0 and grid[nr-1][nc] == "1":
                            neighbors.append((nr -1, nc))
                            grid[nr - 1][nc] = "0" # marking visited
                        if nr +1 < rows and grid[nr + 1][nc] == "1":
                            neighbors.append((nr + 1, nc))
                            grid[nr + 1][nc] = "0"
                        if nc -1 >=0 and grid[nr][nc -1] == "1":
                            neighbors.append((nr, nc- 1))
                            grid[nr][nc - 1] = "0"
                        if nc +1 < cols and grid[nr][nc + 1] == "1":
                            neighbors.append((nr, nc +1))
                            grid[nr][nc + 1] = "0"
        
        return islands