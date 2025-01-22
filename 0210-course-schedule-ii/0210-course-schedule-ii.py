class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        queue = deque()
        ind = [0] * numCourses
        order = []

        for course, pre in prerequisites:
            adj[course].append(pre)
            ind[pre] += 1
        
        for i in range(numCourses):
            if ind[i] == 0:
                queue.append(i)
        
        while queue:
            curlen = len(queue)
            for i in range(curlen):
                course = queue.popleft()
                order.append(course)

                for nei in adj[course]:
                    ind[nei] -= 1
                    if ind[nei] == 0:
                        queue.append(nei)
        
        return order[::-1] if len(order) == numCourses else []