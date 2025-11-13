class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [(0, k)]
        adjlist = defaultdict(list)
        visited = set()
        maxtime = 0

        for u, v, w in times:
            adjlist[u].append((v, w))

        while heap:
            t, node = heapq.heappop(heap)
            if node in visited:
                continue
            
            maxtime = max(maxtime, t)
            visited.add(node)
            for nei, time in adjlist[node]:
                if nei not in visited:
                    heapq.heappush(heap, (t + time, nei))

        return maxtime if len(visited) == n else -1