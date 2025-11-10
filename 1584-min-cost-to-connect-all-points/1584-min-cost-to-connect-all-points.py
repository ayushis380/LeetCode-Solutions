class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjlist = defaultdict(list)
        N = len(points)
        heap = [(0, 0)]
        cost = 0
        visited = set()

        for i in range(N):
            for j in range(i + 1, N):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adjlist[i].append((dist, j))
                adjlist[j].append((dist, i))
        

        while len(visited) < N:
            dist, node = heapq.heappop(heap)
            
            if node in visited:
                continue
            
            cost += dist
            visited.add(node)

            for d, nei in adjlist[node]:
                if nei not in visited:
                    heapq.heappush(heap, (d, nei))
        
        return cost
