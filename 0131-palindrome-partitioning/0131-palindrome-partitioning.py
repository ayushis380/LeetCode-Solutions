class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output, path = [], []

        def dfs(i):
            if i >= len(s):
                output.append(path.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                # substring s[i:j+1] has already been included in the current path
                    path.append(s[i:j+1])
            # continues to partition the remainder of the string starting from the index j+1
                    dfs(j+1) 
                    
            # removes the last added substring (s[i:j+1]) from the current path, 
            # allowing the function to backtrack and try other potential partitions.
                    path.pop()
            
        dfs(0)
        return output
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True