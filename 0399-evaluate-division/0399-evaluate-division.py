class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjlist = defaultdict(list)
        for i, equ in enumerate(equations):
            src, dst = equ
            adjlist[src].append((dst, values[i]))
            adjlist[dst].append((src, 1/values[i]))
        
        def bfs(src, dest):
            if src not in adjlist or dest not in adjlist:
                return -1
            
            queue = deque([(src, 1)])
            visited = set([src])

            while queue:
                node, wt = queue.popleft()
                if node == dest:
                    return wt
                
                for nei, cost in adjlist[node]:
                    if nei not in visited:
                        queue.append((nei, wt * cost))
                        visited.add(nei)

            return -1
        
        return [bfs(q[0], q[1]) for q in queries]