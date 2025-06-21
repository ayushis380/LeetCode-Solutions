class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        # Split the path by "/" and iterate over each part
        parts = path.split("/")

        for part in parts:
            if part == "" or part == ".":
                # Ignore empty or current directory parts
                continue
            elif part == "..":
                # Go one level up if possible
                if stack:
                    stack.pop()
            else:
                # Valid directory name
                stack.append(part)

        # Join the cleaned-up stack into a simplified path
        return "/" + "/".join(stack)
        

        # without splitting
        # stack = []
        # i = 1

        # while i < len(path):
        #     ch = path[i]
        #     directory = ch
        #     j = i + 1

        #     while j < len(path) and path[j] != "/":
        #         directory += path[j]
        #         j += 1
            
        #     if directory and directory not in [".", ".."]:
        #         stack.append(directory)
        #     elif directory == "..":
        #         if stack:
        #             stack.pop()
            
        #     i = j + 1
        
        # print(stack)
        # return "/" + "/".join(stack)

