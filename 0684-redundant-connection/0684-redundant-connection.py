class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        rank = [1] * (n + 1)

        def find(n):
            if n != parent[n]:
                parent[n] = find(parent[n])
            return parent[n]
        
        def union(u, v):
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return True
            
            if rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
                rank[root_v] += 1
            else:
                parent[root_v] = root_u
                rank[root_u] += 1

            return False            
        
        for u, v in edges:
            if union(u, v):
                return [u, v]
        