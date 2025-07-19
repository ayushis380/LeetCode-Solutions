class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        semester = 0
        adj = defaultdict(list)
        indegree = [0] * (n + 1)
        finished = 0

        for prv, crs in relations:
            adj[prv].append(crs)
            indegree[crs] += 1
        
        queue = deque([i for i in range(1, n+1) if indegree[i] == 0])

        while queue:
            for _ in range(len(queue)):
                crs = queue.popleft()
                finished += 1
                for nei in adj[crs]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
            
            semester += 1
        
        return semester if finished == n else -1
            

