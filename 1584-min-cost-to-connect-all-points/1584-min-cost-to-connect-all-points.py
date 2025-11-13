class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prims algo, vertex based, ElogV, for dense graphs
        # start from any node - as tree will be connected 
        adjlist = defaultdict(list)
        minheap, n = [(0,0)], len(points)
        totalCost = 0
        visited = set()

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                val = abs(x1-x2) + abs(y1-y2)
                
                adjlist[i].append((val, j))
                adjlist[j].append((val, i))

        while len(visited) < n:
            cost, node = heapq.heappop(minheap)
            if node in visited: # multiple ways to reach a node, but if already visited then its lowest wt must have been considered
                continue
            
            visited.add(node)
            totalCost += cost
            
            for dist, nei in adjlist[node]:
                if nei not in visited:
                    heapq.heappush(minheap, (dist, nei))
        
        return totalCost



