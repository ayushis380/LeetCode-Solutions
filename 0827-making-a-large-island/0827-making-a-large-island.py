class DSU:
    def __init__(self, n):
        # self.parent = {i: i for i in range(n)}
        # self.rank = {i: 1 for i in range(n)}
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
                self.rank[rootX] += self.rank[rootY]
            else:
                self.parent[rootX] = rootY
                self.rank[rootY] += self.rank[rootY]
    
    def get_size(self, x):
        return self.rank[self.find(x)]
        
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dsu = DSU(n * n)
        directions = [[-1,0], [1,0], [0,1], [0, -1]]

        # union all connected 1s
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    index = r * n + c 
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            dsu.union(index, nr * n + nc) # merge
        
        # find sizes
        island_sizes = {}
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    index = r * n + c
                    root = dsu.find(index)
                    island_sizes[root] = dsu.get_size(root) # only the root node will hold the total island size

        # try flipping 0s

        max_size = max(island_sizes.values(), default = 0)
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    size = 1
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            root = dsu.find(nr * n + nc)
                # important as 0 can be neighbor to 1's which lie in the same connected island, but their root will be same
                            if root not in seen: 
                                size += island_sizes[root]
                                seen.add(root)
                    max_size = max(max_size, size)
        
        return max_size 