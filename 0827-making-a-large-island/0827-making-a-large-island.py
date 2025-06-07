class DSU:
    def __init__(self, n):
        # Parent array: Each cell is its own parent initially
        self.parent = {i: i for i in range(n)}
        # Rank array: Used for union by size
        self.rank = {i: 1 for i in range(n)}

    def find(self, x):
        """Finds the representative/root of the set containing x."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        """Unites the sets containing x and y."""
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:  # Only merge if different sets
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
                self.rank[rootX] += self.rank[rootY]
            else:
                self.parent[rootX] = rootY
                self.rank[rootY] += self.rank[rootX]

    def get_size(self, x):
        """Returns the size of the island that x belongs to."""
        return self.rank[self.find(x)]

class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        dsu = DSU(n * n)  # Create DSU for all n*n cells
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 1: Union all connected '1's
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    index = r * n + c  # Convert 2D to 1D index
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            dsu.union(index, nr * n + nc)  # Merge islands

        # Step 2: Store island sizes
        island_sizes = {}
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    root = dsu.find(r * n + c)  # Find the root island ID
                    island_sizes[root] = dsu.get_size(root)

        # Step 3: Check for 0s and compute the max island size
        max_size = max(island_sizes.values(), default=0)  # Max existing island size
        print(max_size)
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:  # Try flipping this 0 to 1
                    seen = set()
                    new_size = 1  # Convert this '0' to '1'
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            root = dsu.find(nr * n + nc)
                            if root not in seen:
                                new_size += island_sizes[root]
                                seen.add(root)
                    max_size = max(max_size, new_size)

        return max_size if max_size else n * n  # Edge case: full grid is '1'
