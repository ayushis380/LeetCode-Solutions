class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        size = [1] * n
        components = n

        def find(n):
            if n != parent[n]:
                parent[n] = find(parent[n])
            return parent[n]
        
        def union(u, v):
            nonlocal components
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return 
            
            if size[root_u] < size[root_v]:
                parent[root_u] = root_v
                size[root_v] += size[root_u]
            else:
                parent[root_v] = root_u
                size[root_u] += size[root_v]
            
            components -= 1
        
        for u, v in edges:
            union(u, v)
        
        return components

