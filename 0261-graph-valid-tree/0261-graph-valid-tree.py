class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = list(range(n))
        rank = [0] * n
        components = n 

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(u, v):
            nonlocal components
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return False
            
            if rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            elif rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            else:
                parent[root_u] = root_v
                rank[root_v] += 1
            
            components -= 1
            return True
         
        for u, v in edges:
            if not union(u, v):
                return False
        
        return components == 1