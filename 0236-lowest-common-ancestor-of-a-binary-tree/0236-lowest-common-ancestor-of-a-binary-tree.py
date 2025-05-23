# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node == p or node == q:
                return node
            if not node:
                return None
            
            left = dfs(node.left)
            right = dfs(node.right)

            if not left:
                return right
            elif not right:
                return left
            else:
                return node
        
        return dfs(root)
