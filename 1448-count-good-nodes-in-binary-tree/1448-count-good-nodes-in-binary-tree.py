# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        def dfs(root, maxv):
            nonlocal good

            if not root:
                return 
            
            if root.val >= maxv:
                good += 1
            
            dfs(root.left, max(maxv, root.val))
            dfs(root.right, max(maxv, root.val))
        
        dfs(root, float("-inf"))
        return good
