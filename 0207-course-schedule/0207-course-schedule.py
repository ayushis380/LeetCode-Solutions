class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adjlist[prereq].append(course)
            indegree[course] += 1
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        taken = 0

        while queue:
            taken += 1
            course = queue.popleft()

            for nei in adjlist[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return taken == numCourses