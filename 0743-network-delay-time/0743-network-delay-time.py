class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # bfs using min heap to calculate shortest distance
        adj = defaultdict(list)

        for u,v,w in times:
            adj[u].append((v, w)) # u is source and v is destination

        visited = set()
        minh = [(0, k)] # starting from k
        delaytime = 0

        while minh:
            time, node = heapq.heappop(minh)
            if node in visited:
                continue
            
            visited.add(node)
            delaytime = max(delaytime, time) # max as we are adding the times seen so far

            for neigh, t in adj[node]:
                if neigh not in visited:
                    heapq.heappush(minh, (time + t, neigh)) # time seen so far and new time 
        
       
        return delaytime if len(visited) == n else -1
