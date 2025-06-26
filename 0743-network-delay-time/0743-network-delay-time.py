class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        visited = set()
        heap = [(0, k)]
        delaytime = 0

        for u, v, w in times:
            adj[u].append((v, w))

        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            
            delaytime = max(delaytime, time)
            visited.add(node)

            for nei, wt in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap, (time + wt, nei))
        
        return delaytime if len(visited) == n else -1 

