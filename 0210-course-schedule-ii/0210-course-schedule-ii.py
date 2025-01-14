class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Kahns Algo 
        indegree = [0] * numCourses
        adjlist = defaultdict(list)
        schedule, finish = [], 0
        queue = deque()

        for course, pre in prerequisites:
            adjlist[course].append(pre)
            indegree[pre] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            schedule.append(course)
            finish += 1
            for nei in adjlist[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        if finish == numCourses: # check if able to finish all the courses
            return schedule[::-1] # reverse as in queue we add courses which dont have an dependencies(indegree of 0)
        else:
            return []