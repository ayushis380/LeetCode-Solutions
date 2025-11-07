# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if root == p or root == q:
                return root
            if not root:
                return None
            
            lefts = dfs(root.left)
            rights = dfs(root.right)

            if not lefts:
                return rights
            elif not rights:
                return lefts
            else:
                return root
        
        return dfs(root)