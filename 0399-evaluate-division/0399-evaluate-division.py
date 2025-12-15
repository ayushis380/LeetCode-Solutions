class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # N (E + V), N is number of queries - brute force, bfs called fro every query
        # SC = E + V = graph storage

        adj = defaultdict(list) # a -> [(b, a/b)], store all numerators pointing to denominators and their division value; and vice versa

        for i, v in enumerate(equations):
            fv, sv = v[0], v[1] # numerator and denominator

            adj[fv].append((sv, values[i]))
            adj[sv].append((fv, 1/ values[i])) # un directed but with different weights 
        
        # finding a path from src to target and multiplying the weights to get the result 
        # eg a/c can be found if we have a/b and b/c = just multiply them 
        # adj will have all mappings for a and b - use that 
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1 # variables not present
            
            q, visited = deque([(src, 1)]), set()
            visited.add(src)

            while q:
                node, wt = q.popleft()
                if node == target:
                    return wt
                
                for nei, weight in adj[node]:
                    if nei not in visited:
                        q.append((nei, wt * weight)) # all weights get multiplied starting from src where we start with wt = 1
                        visited.add(nei)
            
            return -1
        
        return [bfs(q[0], q[1]) for q in queries]
