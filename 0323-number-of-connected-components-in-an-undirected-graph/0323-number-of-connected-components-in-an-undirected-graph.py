class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n)) # each node pointing to itself
        rank = [0] * n
        components = n # at start all nodes are considered as not connected

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node]) # path compression
            return parent[node]
        
        def union(u, v):
            nonlocal components
            root_u = find(u)
            root_v = find(v)

            if root_u != root_v: # if roots are not same then decrease the count
                if rank[root_u] < rank[root_v]: # if rank = 2, rank = 1 then attaching them still gives rank = 2, so rank is not updated
                    parent[root_u] = root_v
                elif rank[root_u] > rank[root_v]:
                    parent[root_v] = root_u
                else: # when rank is same then attach and increase rank, shallow tree
                    parent[root_u] = root_v
                    rank[root_u] += 1
                components -= 1

        for u, v in edges:
            union(u, v)
        
        return components
