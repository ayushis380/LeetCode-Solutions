class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
# dijkstras: shortest path from a single source node to all other nodes in a graph with edges that have non-negative weights O(N+ElogE)
        adjlist = defaultdict(list)
        MOD = 10**9 + 7

        for u, v, t in roads:
            adjlist[u].append((v, t))
            adjlist[v].append((u, t))
        
        heap = [(0, 0)] # dist, node
        path_count = [0] * n
        path_count[0] = 1 # ways to start from 0
        shortest_time = [float("inf")] * n
        shortest_time[0] = 0

        while heap:
            time, node = heapq.heappop(heap)
            if time > shortest_time[node]: # already saw a shortest path for the node, ignore this
                continue
            
            # see the neighbors of node, as able to reach the node with a shorter distance
            for nei, t in adjlist[node]:
                # # Found a new shortest path → Update shortest time and reset path count
                if time + t < shortest_time[nei]:
                    shortest_time[nei] = time + t
                    path_count[nei] = path_count[node] # path count of nei will be same as node
                    heapq.heappush(heap, (time + t, nei))
                elif time + t == shortest_time[nei]: # found another way with same shortest path
                    path_count[nei] = (path_count[nei] + path_count[node]) % MOD # brute force to find all - so mod
        
        return path_count[n-1]
            

