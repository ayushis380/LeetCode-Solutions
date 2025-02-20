# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        flagp, flagq = False, False

        def check(node):
            nonlocal flagp, flagq
            if not node:
                return None
            if node == p:
                flagp = True
            if node == q:
                flagq = True
            
            check(node.left)
            check(node.right)

        def dfs(node):
            if not node:
                return None
            
            if node == p or node == q:
                return node
            
            lefts = dfs(node.left)
            rights = dfs(node.right)

            if not lefts:
                return rights
            elif not rights:
                return lefts
            else:
                return node
        
        check(root)
        return dfs(root) if (flagp == True and flagq == True) else None
            
