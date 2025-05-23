# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance_ = True

        def dfs(node):
            nonlocal balance_

            if not node:
                return 0
            
            left_dep = dfs(node.left)
            right_dep = dfs(node.right)

            if abs(left_dep - right_dep) > 1:
                balance_ = False
            
            return 1 + max(left_dep, right_dep)
        
        dfs(root)
        return balance_