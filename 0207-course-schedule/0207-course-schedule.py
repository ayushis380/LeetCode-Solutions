class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        visited = 0

        for course, preReq in prerequisites:
            adj[course].append(preReq)
            indegree[preReq] += 1
        
        queue = deque([course for course in indegree if indegree[course] == 0])

        while queue:
            course = queue.popleft()
            visited += 1
            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return True if visited == numCourses else False