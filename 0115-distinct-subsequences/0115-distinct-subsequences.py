class Solution:
    def numDistinct(self, s: str, t: str) -> int:
    # DFS Top Down
    # Just like LCS with some tweaks in conditions
        dp = {}

        def dfs(i, j):
# reached the end of t, target string to which we are matching the subsequence
            if j == len(t): 
                return 1 # 1 way as reached end of t
            if i == len(s):
                return 0
            
            if (i, j) in dp: # memoization
                return dp[(i,j)]
            
    # when chars match then two ways are possible:
    # both indexes increment by 1, or only index of s increases to see if char matches with char at jth index
    # we are calculating the number of subsequences so we need to check for different combinations of s indexes with t indexes
            if s[i] == t[j]: 
                dp[(i,j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                dp[(i,j)] = dfs(i + 1, j) # if they dont match then check for next index in s and same index in t
            
            return dp[(i,j)]
        
        return dfs(0, 0)