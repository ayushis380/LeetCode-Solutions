class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjlist = defaultdict(list)
        heap = [(0, k)] # it can have multiple entries for a node, as we can have multiple paths to reach a node but min heap ensures we take the minimum cost path
        delaytime = 0
        visited = set() # helps check is node is already visited that means the node was already reached with a lower cost

        for u, v, w in times:
            adjlist[u].append((v,w))
        
        while heap:
            time, node = heapq.heappop(heap)
            if node in visited: # already visited means seen with a lower cost
                continue
            
            delaytime = max(delaytime, time) # max seen so far to reach all the nodes
            visited.add(node)
            
            # going from source to the other nodes
            for nei, weight in adjlist[node]:
                if nei not in visited:
                    heapq.heappush(heap, (time + weight, nei))
        
        # not necessarily that we reach all the nodes
        return delaytime if len(visited) == n else -1