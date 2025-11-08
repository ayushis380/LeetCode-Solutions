class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        result = []

        def dfs(start):
            if start >= len(s):
                result.append(path.copy())
                return
            
            for end in range(start, len(s)): # i is start of string, j is end of string(within i to len(s)) - explore all possible strings
                if self.check(start, end, s):
                    path.append(s[start : end+ 1])
                    dfs(end + 1) # end+1 becomes the start index for the next recursive call.
                    path.pop()
        
        dfs(0)
        return result
    
    def check(self, l, h, s):
        while l < h:
            if s[l] != s[h]:
                return False
            
            l += 1
            h -= 1
        
        return True