# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdiam = 0

        def dfs(root):
            nonlocal maxdiam
            if not root:
                return 0
            
            left_sub = dfs(root.left)
            right_sub = dfs(root.right)

            maxdiam = max(maxdiam, left_sub + right_sub)
            return 1 + max(left_sub, right_sub)

        dfs(root)
        return maxdiam