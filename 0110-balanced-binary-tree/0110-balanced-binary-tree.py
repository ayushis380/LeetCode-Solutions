# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def dfs(root):
            nonlocal balanced
            if not root:
                return 0
            
            leftsubtree = dfs(root.left)
            rightsubtree = dfs(root.right)

            if abs(leftsubtree - rightsubtree) > 1:
                balanced = False
            
            return 1 + max(leftsubtree, rightsubtree)
        
        dfs(root)
        return balanced