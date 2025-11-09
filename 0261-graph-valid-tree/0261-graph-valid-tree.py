class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = list(range(n))
        rank = [0] * n
        components = n

        def find(n):
            if parent[n] != n:
                n = find(parent[n])
            return parent[n]

        def union(u, v):
            nonlocal components

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
            
            components -= 1

            return False 

        for u, v in edges:
            if union(u, v):
                return False
        
        # print(components)
        return True if components == 1 else False