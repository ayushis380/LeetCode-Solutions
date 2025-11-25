class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adjlist = defaultdict(list)
        n = len(graph)
        result = []

        for i in range(n):
            for nei in graph[i]:
                adjlist[i].append(nei)
        
        def dfs(node, path):
            if node == n -1:
                path.append(node)
                return True
            
            path.append(node)
            for nei in adjlist[node]:
                if dfs(nei, path):
                    result.append(path.copy())
                
                path.pop()
            
            return False
        
        dfs(0, [])
        # print(result)
        return result