class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjlist = defaultdict(list)
        heap = []
        heapq.heappush(heap, (0, k)) # start from k
        allReached = 0
        visited = set()

        for u, v, w in times:
            adjlist[u].append((v, w))

        while heap:
            time, node = heapq.heappop(heap)
    # a node can be reached through multiple paths - all possible time values are added to the heap, if its already visited then ignore as this time will impact the final result time
            if node in visited: 
                continue
            
            allReached = max(allReached, time)
            visited.add(node)
            
            for nei, t in adjlist[node]:
                if nei not in visited:
                    heapq.heappush(heap, (time + t, nei))
        
        return allReached if len(visited) == n else -1

