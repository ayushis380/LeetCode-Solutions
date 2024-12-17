# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, maxv, minv):
            if not node:
                return True
            
            if not (minv < node.val < maxv):
                return False
            
            return dfs(node.left, node.val, minv) and dfs(node.right, maxv, node.val)

           
        return dfs(root, float("inf"), float("-inf"))