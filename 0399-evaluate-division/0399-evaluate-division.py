class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjlist = defaultdict(list)
        result = []

        for i, eqt in enumerate(equations):
            start, end = eqt
            adjlist[start].append([end, values[i]])
            adjlist[end].append([start, 1/values[i]])

        # print(adjlist)
        def dfs(node, end, visited):
            if node == end:
                return 1
            
            visited.add(node)
            for nei, wt in adjlist[node]:
                if nei not in visited:
                    res = dfs(nei, end, visited)
                    if res != -1:
                        return wt * res

            return -1.0 # no path 
        
        for start, end in queries:
            if start not in adjlist or end not in adjlist:
                result.append(-1.0)
                continue
            
            value = dfs(start, end, set())
            result.append(value)
        
        return result



