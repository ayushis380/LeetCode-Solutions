# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(root):
            nonlocal diameter
            if not root:
                return 0
            
            leftval = dfs(root.left)
            rightval = dfs(root.right)
            diameter = max(diameter, leftval + rightval)
            return 1 + max(leftval, rightval)

        dfs(root)
        return diameter