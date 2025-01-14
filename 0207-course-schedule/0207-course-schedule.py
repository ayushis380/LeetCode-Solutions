class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjlist = [[] for i in range(numCourses)]
        queue = deque()
        finish = 0

        for course, prereq in prerequisites:
            indegree[prereq] += 1
            adjlist[course].append(prereq)
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            finish += 1
            course = queue.popleft()
            for nei in adjlist[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
            
        return finish == numCourses
