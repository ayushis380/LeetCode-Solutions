class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = defaultdict(list)
        indegree = [0] * (n + 1)
        queue = deque()
        semesters, finished = 0, 0

        for prevC, nextC in relations:
            adj[prevC].append(nextC)
            indegree[nextC] += 1
        
        for i in range(1, n+1):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            for _ in range(len(queue)):
                course = queue.popleft()
                finished += 1
                for nei in adj[course]:
                    indegree[nei] -= 1
                    
                    if indegree[nei] == 0:
                        queue.append(nei)
            
            semesters += 1
        
        return semesters if finished == n else -1

        
