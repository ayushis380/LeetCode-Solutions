class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = defaultdict(list) # i = [cost, neighbour]

        # updating adjacency list
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i]) # undirected graph
        
        # prims algo
        totalcost = 0
        visited = set()
        minh = [(0,0)]

        while len(visited) < N: # check until all points are visited
            cost, pt = heapq.heappop(minh) # minimum distance/cost will be popped
            if pt in visited:
                continue
            totalcost += cost
            visited.add(pt) # taken the cost of this point, so add to visited set
            
            for neicost, nei in adj[pt]: # now all enighbors of pt added to heap
                if nei not in visited:
                    heapq.heappush(minh, (neicost, nei))
        
        return totalcost
