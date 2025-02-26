class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        finished, order = 0, []
        adjlist = defaultdict(list)
        indegree = [0] * numCourses
        queue = deque()

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
                order.append(course)
                finished += 1
                for nei in adjlist[course]:
                    indegree[nei] -= 1
                    if not indegree[nei]:
                        queue.append(nei)
        
        return order[::-1] if finished == numCourses else []