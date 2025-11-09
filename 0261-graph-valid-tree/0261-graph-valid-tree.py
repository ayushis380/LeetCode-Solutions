class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # using dfs
        adjlist = defaultdict(list)
        visited = set()

        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        
        def dfs(node, prev): # ignore the neighbor from where we came
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adjlist[node]:
                if nei != prev:
                    if not dfs(nei, node):
                        return False

            return True
        
        return dfs(0, -1) and len(visited) == n
