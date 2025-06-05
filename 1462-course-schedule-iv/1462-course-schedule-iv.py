class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        preReq = defaultdict(set) # map which stores all pre reqs of itself + the course 

        for pre, crs in prerequisites:
            adj[crs].append(pre) # course has list of pre reqs 
        
        def dfs(crs):
            if crs not in preReq:
                for pre in adj[crs]:
                    preReq[crs] |= dfs(pre) # union of pre reqs
                
                preReq[crs].add(crs) # adding the crs to its pre req map as it will be returned back to its other pre reqs eg A - > C -> D then D will return D to C and C will return C, D to A
            
            return preReq[crs]
        
        for crs in range(numCourses):
            dfs(crs)
        
        return [u in preReq[v] for u, v in queries]
