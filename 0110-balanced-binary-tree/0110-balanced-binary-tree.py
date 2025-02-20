# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        
        def dfs(node):
            nonlocal balanced

            if not node:
                return 0
            
            leftSub = dfs(node.left)
            rightSub = dfs(node.right)

            if abs(leftSub - rightSub) > 1:
                balanced = False

            return 1 + max(leftSub, rightSub)
        
        dfs(root)
        
        return balanced