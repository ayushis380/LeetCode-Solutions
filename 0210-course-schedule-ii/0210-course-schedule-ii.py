class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        finished = 0
        indegree = [0] * numCourses
        adj = defaultdict(list)
        queue = deque()
        order = []

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            crs = queue.popleft()
            order.append(crs)
            finished += 1

            for nei in adj[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return order if finished == numCourses else []