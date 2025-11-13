class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # prims
        n = len(points)
        adjlist = defaultdict(list)
        visited = set()
        heap = [(0, 0)]
        cost = 0

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i +1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adjlist[i].append((j, dist))
                adjlist[j].append((i, dist))
        
        while heap:
            dst, pt = heapq.heappop(heap)
            if len(visited) == n:
                return cost
            if pt in visited:
                continue
            
            cost += dst
            visited.add(pt)
            for nei, wt in adjlist[pt]:
                if nei not in visited:
                    heapq.heappush(heap, (wt, nei))
        
        return cost