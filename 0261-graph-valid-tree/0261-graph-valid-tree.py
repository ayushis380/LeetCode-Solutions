class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = list(range(n))
        rank = [1] * n
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
                return True
            
            if rank[root_u] != rank[root_v]:
                if rank[root_u] > rank[root_v]:
                    parent[root_v] = root_u
                elif rank[root_u] < rank[root_v]:
                    parent[root_u] = root_v
            else:
                parent[root_u] = root_v
                rank[root_v] += 1
            
            components -= 1

            return False
        
        for u, v in edges:
            if union(u, v):
                return False
        
        return True if components == 1 else False