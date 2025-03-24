class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = defaultdict(list)
        indegree = [0] * (n + 1)

        for prevC, nextC in relations:
            adj[prevC].append(nextC)
            indegree[nextC] += 1
        
        queue = deque()
        for i in range(1, n + 1):
            if indegree[i] == 0:
                queue.append(i)
        
        taken = 0
        semesters = 0

        while queue:
            for _ in range(len(queue)):
                course = queue.popleft()
                taken += 1
                for nei in adj[course]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
            semesters += 1
        
        return semesters if taken == n else -1
