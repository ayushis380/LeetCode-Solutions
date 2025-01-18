class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # DFS using memoization
    # order in which strings are joined matter
        if len(s3) != (len(s1) + len(s2)):
            return False

        dp = {}

        def dfs(i, j):
            if (i + j) == len(s3):
                return i == len(s1) and j == len(s2) # if at end, then i and j should be at end
            
            if (i,j) in dp:
                return dp[(i,j)] # already calculated value
            
            res = False

        # comparing with length of each string is required
        # as it can go out of bound but maybe another index is still in bound
        # res can either have a True from dfs(i+1, j) or dfs(i, j+1)

            if i < len(s1) and s1[i] == s3[i+j]: 
                res = dfs(i + 1, j) # match at i in s1
            if not res and j < len(s2) and s2[j] == s3[i+j]: # only compute if res = False, if already True then that means dfs(i+1, j) already got a True
                res = dfs(i, j + 1) # match at j in s2
            
            dp[(i,j)] = res # to refer in future
            return dp[(i,j)]


        return dfs(0,0)