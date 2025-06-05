class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [set() for _ in range(numCourses)]
        preReq = [set() for _ in range(numCourses)]
        indegree = [0] * numCourses

        for pre, crs in prerequisites:
            adj[pre].add(crs)
            indegree[crs] += 1
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        while queue:
            node = queue.popleft() # course with no dependencies are popped first 

            for nei in adj[node]:
                preReq[nei].add(node) # neighbors pre req is node, add that 
                preReq[nei].update(preReq[node]) # add pre req of node, indirect prereq for nei
# update() method is used to modify sets by adding elements from other iterables (like lists, tuples, or other sets)
                
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return [u in preReq[v] for u, v in queries]
