class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n # -1 is uncolored, 0 and 1 colors
        queue = deque()

        for i in range(n): # there can be disconnected components
            if color[i] == -1:
                queue.append(i)
                color[i] = 0
            
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if color[nei] == -1: # neigh is not colored
                        color[nei] = 1 - color[node] # give opposite color as node
                        queue.append(nei)
                    elif color[nei] == color[node]:
                        print("node is: ", node, " nei is: ", nei)
                        return False
        
        return True
