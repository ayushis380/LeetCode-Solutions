class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = defaultdict(list)
        indegree = [0] * numCourses
        queue, finished = deque(), 0

        for course, pre in prerequisites:
            adjlist[course].append(pre)
            indegree[pre] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            curlen = len(queue)
            for i in range(curlen):
                course = queue.popleft()
                finished += 1
                for nei in adjlist[course]:
                    indegree[nei] -= 1
                    if not indegree[nei]:
                        queue.append(nei)
        
        return finished == numCourses
