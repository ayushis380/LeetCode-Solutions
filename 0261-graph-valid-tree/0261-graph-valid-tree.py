class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adjlist = defaultdict(list)
        visited = set()

        for u,v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adjlist[node]:
                if nei != prev:
                    if not dfs(nei, node):
                        return False # should return from here if not valid tree
            
            return True
        
    # calling from any node works as its a tree and each node can be reached from any of the nodes, but there should be only 1 connected component
        return dfs(0, -1) and len(visited) == n

