class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dirs = path.split("/")

        for i in range(1, len(dirs)):
            if dirs[i] == "..":
                if stack: stack.pop()
            elif dirs[i] and dirs[i] != ".":
                stack.append(dirs[i])
        
        return "/" + "/".join(stack)