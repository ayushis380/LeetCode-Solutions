# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def dfs(root, maxv):
            nonlocal result
            
            if not root:
                return
            
            dfs(root.left, max(maxv, root.val))
            dfs(root.right, max(maxv, root.val))

            if root.val >= maxv:
                result += 1
        
        dfs(root, float("-inf"))
        return result
