class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        
        return self.parent[node]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return
        else:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            else:
                self.parent[root_u] = root_v
                self.rank[root_v] += 1
            
            self.count -= 1


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
#  If stone A is connected to stone B and stone B is connected to stone C, then all three stones form part of the same group, even if A and C don’t directly share a row or column
# eg (0,1) and (2,2) dont share anything but are connected via (1,2)
# maximum number of stones that can be removed = Max removable stones = Total stones - Number of connected components
        n = len(stones)
        uf = UnionFind(n)
        components = n

        for i in range(n):
            for j in range(i+1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf.union(i, j)
        
        return n - uf.count
