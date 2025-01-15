class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        length = len(edges)
        parent = [i for i in range(length + 1)] # node is starting from 1 and not 0
        rank = [1] * (length + 1)

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2: # already a connection, n1 can be reached by n2 as they have same parent, so adding this will cause cycle
                return 0
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 1
        
        for a, b in edges:
            if union(a, b) == 0:
                return [a, b]