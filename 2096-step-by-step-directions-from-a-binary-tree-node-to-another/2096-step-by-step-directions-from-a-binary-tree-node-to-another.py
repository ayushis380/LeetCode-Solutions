# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        parentMap = {} # node -> parent
        queue = deque()
        visited = set()

        def dfs(node):
            if not node:
                return
            
            if node.val == startValue:
                queue.append((node, ""))
                visited.add(node)
            
            if node.left:
                parentMap[node.left] = node
                dfs(node.left)
            if node.right:
                parentMap[node.right] = node
                dfs(node.right)
        
        dfs(root)

        while queue:
            for _ in range(len(queue)):
                node, path = queue.popleft()
                if node.val == destValue:
                    return path
                
                if node in parentMap:
                    parent = parentMap[node]
                    if parent not in visited:
                        queue.append((parent, path + "U"))
                        visited.add(parent)
                
                if node.left and node.left not in visited:
                    queue.append((node.left, path + "L"))
                    visited.add(node.left)
                
                if node.right and node.right not in visited:
                    queue.append((node.right, path + "R"))
                    visited.add(node.right)

        return ""
