class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # top down
# i for s, j for p, if both i and j are out of bound then they have matched 
# if only j is out of bound, this means there are some chars remaining in s to be matched eg s = aa, p = a, when j = 1 and i = 1
# if i is out of bound, it doenst mean that they don't match, eg s = a, p = a *b * c, when i = 1 and j = 1, whole s is matched 
        dp = {}

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".") # i when in bound and both chars match

            # eg when p = 'a*' - we are looking for * at j + 1
            if (j + 1) < len(p) and p[j + 1] == "*": # first char of p can never be '*' as it matches the preceding char
                dp[(i, j)] = (dfs(i, j + 2) or  # don't use the preceding char eg aab, c*a*b, to match them, c wont be used, i stays same, j jumps +2 
                             (match and dfs(i + 1, j))) # use preceding char only when the values match in s and p, i matched so + 1 but same char in p can be repeated so no increment in j
                return dp[(i, j)]
            
            if match: # if above doesn't satisfy 
                dp[(i, j)] = dfs(i + 1, j + 1) # both char matched, move to next indexes
                return dp[(i, j)]
            
            dp[(i, j)] = False
            return False
        
        return dfs(0, 0)
