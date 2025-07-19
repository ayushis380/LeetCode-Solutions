class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        finished = 0
        indegree = [0] * numCourses
        queue = deque()

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        while queue:
            crs = queue.popleft()
            finished += 1

            for nei in adj[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return True if finished == numCourses else False