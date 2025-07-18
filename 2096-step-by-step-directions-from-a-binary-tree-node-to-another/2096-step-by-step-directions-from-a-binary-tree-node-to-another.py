# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node, path, target):
            if not node:
                return None
            
            if node.val == target:
                return path
            
            path.append("L")
            res = dfs(node.left, path, target)
            if res: return res
            
            path.pop()
            path.append("R")
            res = dfs(node.right, path, target)
            if res: return res
            
            path.pop()
            return None
        
        sarr = dfs(root, [], startValue)
        darr = dfs(root, [], destValue)

        i = 0
        while i < min(len(sarr), len(darr)):
            if sarr[i] != darr[i]:
                break
            i += 1

        res = ["U"] * len(sarr[i:]) + darr[i:]
        return "".join(res)

                